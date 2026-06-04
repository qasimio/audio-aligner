import soundfile as sf

def save_audio(audio, sr, output_path):
    sf.write(output_path, audio, sr)
