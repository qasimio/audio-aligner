import numpy as np

def seconds_to_samples(seconds, sr):
    return int(seconds * sr)

def trim_start(audio, seconds, sr):
    samples = seconds_to_samples(seconds, sr)
    return audio[samples:]

def trim_end(audio, seconds, sr):
    samples = seconds_to_samples(seconds, sr)
    if samples <=0:
        return audio
    
    return audio[:-samples]


def pad_start(audio, seconds, sr):

    samples = seconds_to_samples(seconds, sr)

    silence = np.zeros(samples, dtype=audio.dtype)
    return np.concatenate([silence, audio])

def pad_end(audio, seconds, sr):
    samples = seconds_to_samples(seconds, sr)
    if samples <=0:
        return audio
    
    silence = np.zeros(samples, dtype=audio.dtype)
    return np.concatenate([audio, silence])

def apply_alignment(audio, sr, plan):

    leading_shift = (plan["leading_shift"])
    trailing_shift = (plan["trailing_shift"])
    if leading_shift > 0:
        audio = trim_start(audio, leading_shift, sr)
    
    elif leading_shift < 0:
        audio = pad_start(audio, abs(leading_shift), sr)

    if trailing_shift > 0:
        audio = trim_end(audio, trailing_shift, sr)

    elif trailing_shift < 0:
        audio = pad_end(audio, abs(trailing_shift), sr)

    return audio