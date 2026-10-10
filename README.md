# MeetingMind — AI Meeting Intelligence

A full-stack AI application that converts meeting audio into transcripts, summaries, action items, decisions, and downloadable PDF reports.

## Features

- Audio upload and transcription using Faster-Whisper
- AI-generated meeting summaries and action items using Gemini
- Speaker diarization using Pyannote in the local backend
- PDF report generation using ReportLab
- Meeting history stored using SQLite and SQLAlchemy
- Responsive Next.js frontend

**Deployment note:** The lightweight Render backend does not include Pyannote speaker diarization.

## Tech Stack

| Component | Technologies |
|---|---|
| Frontend | Next.js, React, TypeScript, Tailwind CSS |
| Backend | Python, FastAPI |
| AI | Faster-Whisper, Gemini 2.5 Flash, Pyannote |
| Database | SQLite, SQLAlchemy |
| Reports | ReportLab |
| Deployment | Vercel, Render |

## Architecture

Audio Upload → Transcription → AI Summarization → Database Storage → PDF Report

The local implementation additionally supports speaker diarization.

## Local Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `backend/.env` with the required credentials:

```env
GEMINI_API_KEY=your_api_key
HF_TOKEN=your_huggingface_token
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000

Backend API documentation: http://localhost:8000/docs

## Deployment

- [Live Application](https://ai-meeting-intelligence-nine.vercel.app)
- [Backend API](https://ai-meeting-intelligence-iw1r.onrender.com)

The deployed version uses a lightweight transcription pipeline without local speaker diarization.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).