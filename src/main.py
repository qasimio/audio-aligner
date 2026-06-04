from audio_loader import load_audio, duration
from speech_detector import detect_speech
from timeline import build_timeline
from aligner import compare_segments, generate_alignment_plan
from audio_editor import apply_alignment
from exporter import save_audio

URDU_PATH = "data/urdu2.wav"
SINDHI_PATH = "data/sindhi2.wav"
ALIGNED_PATH = "data/aligned_sindhi.wav"

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


segments, sr = detect_speech(URDU_PATH)
urdu_timeline = build_timeline(segments, sr)
print("\n--- Urdu Timeline ---")
for item in urdu_timeline:
    print(item)

segments, sr = detect_speech(SINDHI_PATH)
sindhi_timeline = build_timeline(segments, sr)
print("\n--- Sindhi Timeline ---")
for item in sindhi_timeline:
    print(item)

report = compare_segments(
    urdu_timeline, sindhi_timeline,
)
print("\nAlignment Report:")
for item in report:
    print(item)

plan = generate_alignment_plan(
    urdu_timeline, sindhi_timeline, report
)
print("\n--- Global Plan ---")
print(plan)

aligned_audio = apply_alignment(sindhi_audio, sindhi_sr, plan)
save_audio(aligned_audio, sindhi_sr, ALIGNED_PATH)