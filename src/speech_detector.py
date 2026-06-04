import torch 
import soundfile as sf
import librosa

from silero_vad import (
    load_silero_vad,
    get_speech_timestamps,
)

model = load_silero_vad()

def detect_speech(audio_path):
    audio, sr = sf.read(audio_path)

    if len(audio.shape) > 1:
        audio = audio.mean(axis=1)

    target_sr = 16000

    if sr != target_sr:
        audio = librosa.resample(
            audio,
            orig_sr=sr,
            target_sr=target_sr,
        )
        sr = target_sr

    audio = torch.tensor(
        audio,
        dtype=torch.float32,)

    timestamps = get_speech_timestamps(
        audio,
        model, 
        sampling_rate=sr,
    )

    return timestamps, sr