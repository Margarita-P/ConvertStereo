from scipy.io import wavfile
import numpy as np

def stereo_to_mono_phase_cancellation(input_file, output_file):
    # Read the stereo audio file
    sample_rate, stereo_data = wavfile.read(input_file)

    # Ensure the data is stereo (2 channels)
    if len(stereo_data.shape) != 2 or stereo_data.shape[1] != 2:
        print("Input file is not stereo.")
        return

    left_channel = stereo_data[:, 0]
    right_channel = stereo_data[:, 1]

    # Phase cancellation to create mono signal
    mono_data = left_channel - right_channel

    # Write the mono audio to a WAV file
    wavfile.write(output_file, sample_rate, mono_data)

# Usage example
input_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/Stereo_music.wav'  # Replace with your stereo audio file
output_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/output_phase_cancelation.wav'  # Name for the output mono audio file

# Convert stereo to mono using phase cancellation
stereo_to_mono_phase_cancellation(input_audio, output_audio)
