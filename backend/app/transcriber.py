from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path):
    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        language="hi",
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
        word_timestamps=True  # needed for speaker matching
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


def merge_transcript_with_speakers(timed_segments, speaker_segments):
    """
    Match each transcript segment to a speaker based on timestamps
    """
    result = []

    for seg in timed_segments:
        seg_mid = (seg["start"] + seg["end"]) / 2
        speaker = "Unknown"

        for sp in speaker_segments:
            if sp["start"] <= seg_mid <= sp["end"]:
                speaker = sp["speaker"]
                break

        result.append({
            "speaker": speaker,
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"]
        })

    # Merge consecutive same-speaker segments
    merged = []
    for item in result:
        if merged and merged[-1]["speaker"] == item["speaker"]:
            merged[-1]["text"] += " " + item["text"]
            merged[-1]["end"] = item["end"]
        else:
            merged.append(item.copy())

    return merged