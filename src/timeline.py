
def build_timeline(speech_segments, sr,):
    timeline = []
    previous_end = 0
    for seg in speech_segments:
        start=seg["start"] /sr
        end=seg["end"]/sr

        if start > previous_end:
            timeline.append(
                {
                    "type": "gap",
                    "start": previous_end,
                    "end": start,
                    "duration": start - previous_end,
                }
            )
        
        timeline.append(
            {
                "type": "speech",
                "start": start,
                "end": end,
                "duration": end - start
            }
        )

        previous_end = end
    
    return timeline