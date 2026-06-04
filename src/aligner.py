
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

    count = min(
        len(urdu_speech),
        len(sindhi_speech)
    )

    for i in range(count):
        u = urdu_speech[i]
        s = sindhi_speech[i]

        ratio = (
            u["duration"] / s["duration"]
            ) if s["duration"] > 0 else 0

        report.append(
            {
                "segment": i + 1,
                "urdu_duration": u["duration"],
                "sindhi_duration": s["duration"],
                "ratio": ratio,
            }
        )
    return report
