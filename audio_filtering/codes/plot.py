import librosa
import numpy as np

def extract_audio_features(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)
    
    # Calculate autocorrelation using librosa
    autocorr = librosa.autocorrelate(y)
    
    # Find the peaks of the autocorrelation function
    peaks = librosa.util.peak_pick(autocorr, pre_max=5, post_max=5, pre_avg=5, post_avg=5, delta=0.0, wait=0)
    
    # Extract r(i), p(i), and k(i)
    r_values = autocorr[peaks]
    p_values = peaks / sr
    k_values = 1 / p_values
    
    return r_values, p_values, k_values

# Example usage
audio_file = "audio.wav"
r_values, p_values, k_values = extract_audio_features(audio_file)

# Print the extracted values
print("r(i) values:", r_values)
print("p(i) values (in seconds):", p_values)
print("k(i) values:", k_values)

