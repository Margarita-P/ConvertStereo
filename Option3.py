from scipy.io import wavfile
import numpy as np

def stereo_to_mono_weighted_mixing(input_file, output_file, left_weight=0.5, right_weight=0.5):
    # Read the stereo audio file
    sample_rate, stereo_data = wavfile.read(input_file)

    # Ensure the data is stereo (2 channels)
    if len(stereo_data.shape) != 2 or stereo_data.shape[1] != 2:
        print("Input file is not stereo.")
        return

    left_channel = stereo_data[:, 0]
    right_channel = stereo_data[:, 1]

    # Weighted mixing to create mono signal
    mono_data = (left_channel * left_weight) + (right_channel * right_weight)

    # Write the mono audio to a WAV file
    wavfile.write(output_file, sample_rate, mono_data.astype(np.int16))

# Usage example
input_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/Stereo_music.wav'  # Replace with your stereo audio file
output_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/output_weighted_mixing.wav'  # Name for the output mono audio file

# Adjust the weights as desired (sum of weights should be 1)
left_weight = 0.7
right_weight = 0.3

# Convert stereo to mono using weighted mixing
stereo_to_mono_weighted_mixing(input_audio, output_audio, left_weight, right_weight)
