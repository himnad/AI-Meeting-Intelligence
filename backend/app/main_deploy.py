from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import shutil
import os

from app.transcriber import transcribe_audio
from app.gemini_utils import generate_meeting_summary
from app.pdf_generator import generate_pdf_report
from app.database import init_db, save_meeting, get_all_meetings, get_meeting_by_id

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

last_result = {}


@app.get("/")
def home():
    return {"message": "AI Meeting Intelligence Backend Running"}


@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Transcribe only (no diarization on cloud)
    result = transcribe_audio(file_path)
    summary = generate_meeting_summary(result["transcript"])

    meeting_id = save_meeting(
        filename=file.filename,
        language=result["language"],
        transcript=result["transcript"],
        meeting_summary=summary
    )

    last_result.update({
        "filename": file.filename,
        "transcript": result["transcript"],
        "language": result["language"],
        "meeting_summary": summary
    })

    return {
        "message": "File uploaded successfully",
        "meeting_id": meeting_id,
        "filename": file.filename,
        "transcript": result["transcript"],
        "language": result["language"],
        "meeting_summary": summary,
        "diarized_segments": []
    }


@app.get("/meetings")
def list_meetings():
    meetings = get_all_meetings()
    return [
        {
            "id": m.id,
            "filename": m.filename,
            "language": m.language,
            "created_at": m.created_at.isoformat(),
            "summary_preview": m.meeting_summary[:150] + "..." if m.meeting_summary else ""
        }
        for m in meetings
    ]


@app.get("/meetings/{meeting_id}")
def get_meeting(meeting_id: int):
    meeting = get_meeting_by_id(meeting_id)
    if not meeting:
        return {"error": "Meeting not found"}
    return {
        "id": meeting.id,
        "filename": meeting.filename,
        "language": meeting.language,
        "transcript": meeting.transcript,
        "meeting_summary": meeting.meeting_summary,
        "created_at": meeting.created_at.isoformat()
    }


@app.get("/download-report")
def download_report():
    if not last_result:
        return {"error": "No report available. Upload audio first."}

    pdf_buffer = generate_pdf_report(
        filename=last_result["filename"],
        transcript=last_result["transcript"],
        language=last_result["language"],
        meeting_summary=last_result["meeting_summary"]
    )

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=meeting_report.pdf"}
    )


@app.get("/download-report/{meeting_id}")
def download_report_by_id(meeting_id: int):
    meeting = get_meeting_by_id(meeting_id)
    if not meeting:
        return {"error": "Meeting not found"}

    pdf_buffer = generate_pdf_report(
        filename=meeting.filename,
        transcript=meeting.transcript,
        language=meeting.language,
        meeting_summary=meeting.meeting_summary
    )

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=meeting_{meeting_id}_report.pdf"}
    )