import subprocess
import tempfile
import os
import soundfile as sf

def stretch_audio(audio, sr, ratio):

    if ratio < 0.85:
        ratio = 0.85

    if ratio > 1.15:
        ratio = 1.15

    temp_input = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    temp_output = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    temp_input.close()
    temp_output.close()

    sf.write(
        temp_input.name,
        audio,
        sr
    )

    atempo = 1 / ratio

    command = [
        "ffmpeg",
        "-y",
        "-i",
        temp_input.name,
        "-af",
        f"atempo={atempo}",
        temp_output.name
    ]

    subprocess.run(
        command,
        capture_output=True,
        check=True
    )

    stretched_audio, stretched_sr = sf.read(
        temp_output.name
    )

    os.remove(temp_input.name)
    os.remove(temp_output.name)

    return stretched_audio, stretched_sr
