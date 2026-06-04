from audio_loader import load_audio, duration

urdu_audio, urdu_sr = load_audio(
    "data/urdu2.wav"
)
sindhi_audio, sindhi_sr = load_audio(
    "data/sindhi2.wav"
)


print(
    "Urdu:",
    duration(urdu_audio, urdu_sr)
)
print(
    "Sindhi:",
    duration(sindhi_audio, sindhi_sr)
)