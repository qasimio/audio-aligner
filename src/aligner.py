
from statistics import mean

MAX_COMPRESSION = 1.15
MAX_EXPANSION = 0.85

def calculate_confidence(ratio):

    deviation = abs(1-ratio)
    if deviation <= 0.05:
        return "high"
    if deviation <= 0.15:
        return "medium"
    return "low"

# keep 0.98 to 1.02 as safe
def get_action(ratio):
    if ratio < 0.98:
        return "compress"
    elif ratio > 1.02:
        return "expand"
    return "keep"

def compare_segments(urdu_timeline, sindhi_timeline):
    report = []
    urdu_speech = [
        x for x in urdu_timeline
        if x["type"] == "speech"
    ]
    sindhi_speech = [
        x for x in sindhi_timeline 
        if x["type"] == "speech"
    ]

    count = min(len(urdu_speech), len(sindhi_speech))

    for i in range(count):
        u = urdu_speech[i]
        s = sindhi_speech[i]

        ratio = (
            u["duration"] / s["duration"]
        )
        confidence = calculate_confidence(ratio)
        action = get_action(ratio)
        report.append(
            {
                "segment": i+1,
                "urdu_start": round(u["start"], 3),
                "urdu_end": round(u["end"], 3),
                "urdu_duration": round(u["duration"], 3),

                "sindhi_start": round(s["start"], 3),
                "sindhi_end": round(s["end"], 3),
                "sindhi_duration": round(s["duration"], 3),
                "ratio": round(ratio, 4),
                "action": action,
                "confidence": confidence,
                "within_safe_range":(
                    MAX_EXPANSION <= ratio <= MAX_COMPRESSION
                ),
            }
        )
    return report

def generate_alignment_plan(
    urdu_timeline, sindhi_timeline, report, urdu_duration, sindhi_duration):

    urdu_first_speech = next(
        x for x in urdu_timeline
        if x["type"] == "speech"
    )
    sindhi_first_speech = next(
        x for x in sindhi_timeline
        if x["type"] == "speech"
    )
    urdu_last_speech = [
        x for x in urdu_timeline
        if x["type"] == "speech"
    ][-1]

    sindhi_last_speech = [
        x for x in sindhi_timeline
        if x["type"] == "speech"
    ][-1]

    # leading silence difference

    leading_shift = (
        sindhi_first_speech["start"] - urdu_first_speech["start"]
    )

    # trailing silence difference
    urdu_end_gap = (
        urdu_duration - urdu_last_speech["end"]
    )
    sindhi_end_gap = (
        sindhi_duration - sindhi_last_speech["end"]
    )
    trailing_shift = (sindhi_end_gap - urdu_end_gap)
    
    ratios = [item["ratio"] for item in report]

    avg_ratio = (mean(ratios) if ratios else 1)

    return {
        "leading_shift": round(leading_shift, 3),
        "trailing_shift": round(trailing_shift, 3),
        "avg_ratio": round(avg_ratio, 4),
        "recommended_action": "compress" if avg_ratio < 0.98 else "expand" if avg_ratio > 1.02 else "keep",
        "urdu_end_gap": round(urdu_end_gap, 3),
        "sindhi_end_gap": round(sindhi_end_gap, 3)
    }
