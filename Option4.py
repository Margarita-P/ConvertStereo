from scipy.io import wavfile
import numpy as np

def stereo_to_mono_energy_based(input_file, output_file):
    # Read the stereo audio file
    sample_rate, stereo_data = wavfile.read(input_file)

    # Ensure the data is stereo (2 channels)
    if len(stereo_data.shape) != 2 or stereo_data.shape[1] != 2:
        print("Input file is not stereo.")
        return

    left_channel = stereo_data[:, 0]
    right_channel = stereo_data[:, 1]

    # Compute energy (RMS) of both channels
    left_energy = np.sqrt(np.mean(np.square(left_channel)))
    right_energy = np.sqrt(np.mean(np.square(right_channel)))

    # Calculate mixing coefficients based on energy levels
    total_energy = left_energy + right_energy

    # Use energy levels to determine mixing coefficients
    left_coefficient = left_energy / total_energy
    right_coefficient = right_energy / total_energy

    # Mix channels based on energy coefficients to create mono signal
    mono_data = (left_channel * left_coefficient) + (right_channel * right_coefficient)

    # Write the mono audio to a WAV file
    wavfile.write(output_file, sample_rate, mono_data.astype(np.int16))

# Usage example
input_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/Stereo_music.wav'  # Replace with your stereo audio file
output_audio = 'C:/Users/scerb/Desktop/uni/Semestras 7/Garso apdorojimas/Python/output_energy_based.wav'  # Name for the output mono audio file

# Convert stereo to mono using energy-based mixing
stereo_to_mono_energy_based(input_audio, output_audio)
