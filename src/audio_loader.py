import soundfile as sf

def load_audio(path):
    audio, sr = sf.read(path)
    return audio, sr

def duration(audio, sr):
    return len(audio) / sr