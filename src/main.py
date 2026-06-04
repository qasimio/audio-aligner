from audio_loader import load_audio, duration
from speech_detector import detect_speech
from timeline import build_timeline

URDU_PATH = "data/urdu1.wav"
SINDHI_PATH = "data/sindhi1.wav"

urdu_audio, urdu_sr = load_audio(
    URDU_PATH
)
sindhi_audio, sindhi_sr = load_audio(
    SINDHI_PATH
)

print(
    "\nUrdu Duration:",
    duration(urdu_audio, urdu_sr)
)
print(
    "\nSindhi Duration:",
    duration(sindhi_audio, sindhi_sr)
)

print("\n--- Urdu Speech Segments ---")

segments, sr = detect_speech(URDU_PATH)

for seg in segments:
    start = seg["start"]/sr
    end = seg["end"]/sr
    
    print(f"{start:.2f}s -> {end:.2f}s")


print("\n--- Sindhi Speech Segments ---")

segments, sr = detect_speech(SINDHI_PATH)

for seg in segments:
    start = seg["start"]/sr
    end = seg["end"]/sr
    
    print(f"{start:.2f}s -> {end:.2f}s")

segments, sr = detect_speech(SINDHI_PATH)
timeline = build_timeline(segments, sr)
print("\n--- Sindhi Timeline ---")
for item in timeline:
    print(item)