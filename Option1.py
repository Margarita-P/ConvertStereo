import numpy as np
from scipy.io import wavfile

def is_channel_empty(channel_data):
    return np.all(channel_data == 0)  # Check if all values in the channel are zeros

def stereo_to_mono_non_empty(input_file, output_file):
    # Read the stereo audio file
    sample_rate, stereo_data = wavfile.read(input_file)

    # Ensure the data is stereo (2 channels)
    if len(stereo_data.shape) != 2 or stereo_data.shape[1] != 2:
        print("Input file is not stereo.")
        return

    left_channel = stereo_data[:, 0]
    right_channel = stereo_data[:, 1]

    # Check if either channel is empty (contains only zeros)
    left_empty = is_channel_empty(left_channel)
    right_empty = is_channel_empty(right_channel)

    if left_empty and right_empty:
        print("Both channels are empty.")
        return
    elif left_empty:
        mono_data = right_channel  # Use right channel if left channel is empty
    elif right_empty:
        mono_data = left_channel   # Use left channel if right channel is empty
    else:
        # If both channels have audio, take the average
        mono_data = np.mean(stereo_data, axis=1, dtype=np.int16)

    # Write the mono audio to a WAV file
    wavfile.write(output_file, sample_rate, mono_data)

# Usage example
input_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/Stereo_music.wav'  # Replace with your stereo audio file
output_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/output_mono_audio.wav'  # Name for the output mono audio file

# Convert stereo to mono considering non-empty channel
stereo_to_mono_non_empty(input_audio, output_audio)

