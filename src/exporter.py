import numpy as np
import soundfile as sf

def save_audio(audio, sr, output_path):

    audio = np.asarray(audio)

    sf.write(output_path, audio, sr)
