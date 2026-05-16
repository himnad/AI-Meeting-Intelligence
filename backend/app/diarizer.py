import os
from dotenv import load_dotenv
from pyannote.audio import Pipeline
import torch
import soundfile as sf
import subprocess

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
print(f"HF_TOKEN loaded: {HF_TOKEN[:10] if HF_TOKEN else 'NOT FOUND'}")

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    token=HF_TOKEN
)

pipeline.to(torch.device("cpu"))


def convert_to_wav(audio_path):
    """Convert audio to WAV format for reliable processing"""
    wav_path = audio_path.rsplit(".", 1)[0] + "_converted.wav"
    subprocess.run([
        "ffmpeg", "-y", "-i", audio_path,
        "-ar", "16000", "-ac", "1", wav_path
    ], capture_output=True)
    return wav_path


def diarize_audio(audio_path):
    try:
        # Convert to WAV first
        wav_path = convert_to_wav(audio_path)
        waveform, sample_rate = sf.read(wav_path)
    except Exception:
        waveform, sample_rate = sf.read(audio_path)

    waveform = torch.tensor(waveform).float()

    if waveform.dim() == 2:
        waveform = waveform.mean(dim=1)

    waveform = waveform.unsqueeze(0)

    audio_input = {
        "waveform": waveform,
        "sample_rate": sample_rate
    }

    diarization = pipeline(audio_input)

    # Use correct attribute: speaker_diarization
    annotation = diarization.speaker_diarization

    segments = []
    for turn, _, speaker in annotation.itertracks(yield_label=True):
        segments.append({
            "speaker": speaker,
            "start": round(turn.start, 2),
            "end": round(turn.end, 2)
        })

    print(f"Diarization found {len(segments)} segments")
    return segments