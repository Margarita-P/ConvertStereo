import numpy as np
from scipy.io import wavfile

def stereo_to_mono(input_file, output_file):
    # Read the stereo audio file
    sample_rate, stereo_data = wavfile.read(input_file)

    # Ensure the data is stereo (2 channels)
    if len(stereo_data.shape) != 2 or stereo_data.shape[1] != 2:
        print("Input file is not stereo.")
        return

    # Convert stereo to mono by averaging left and right channels
    mono_data = np.mean(stereo_data, axis=1, dtype=np.int16)

    # Write the mono audio to a WAV file
    wavfile.write(output_file, sample_rate, mono_data)

# Usage example
input_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/Stereo_music.wav'  # Replace with your stereo audio file
output_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/output_mono_audio.wav'  # Name for the output mono audio file

# Convert stereo to mono
stereo_to_mono(input_audio, output_audio)
