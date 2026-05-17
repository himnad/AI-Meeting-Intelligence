from faster_whisper import WhisperModel

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path):
    segments, info = model.transcribe(
        audio_path,
        beam_size=1,
        vad_filter=True,
    )

    transcript = ""
    timed_segments = []

    for segment in segments:
        transcript += segment.text + " "
        timed_segments.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": segment.text.strip()
        })

    return {
        "language": info.language,
        "transcript": transcript.strip(),
        "timed_segments": timed_segments
    }