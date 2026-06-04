import torch 
import soundfile as sf

from silero_vad import (
    load_silero_vad,
    get_speech_timestamps,
)

model = load_silero_vad()

def detect_speech(audio_path):
    audio, sr = sf.read(audio_path)

    if len(audio.shape) > 1:
        audio = audio.mean(axis=1)

    audio = torch.tensor(audio)

    timestamps = get_speech_timestamps(
        audio,
        model,
        sampling_rate=sr,
    )

    return timestamps, sr