# ConvertStereo
Converting stereo sound to mono

Option1 evaluates that the file has two channels - is stereo (stereo: 2 channels, mono: 1 channel). Also, checks if one of the channels is emtpy - only 0s, then it would take only one channel. If both are not empty, then it uses Numpy module function "mean" to calculate both channel's averages and then puts the averages into the new file.

Option2 subtracts one stereo channel from the other. When the channels are perfectly identical (like in many stereo recordings), subtracting them results in a mono signal. This method assumes that the stereo channels are phase coherent and will cancel each other out when combined. (Result sounds weird).

Option3 uses weighted mixing method. Assigns different weightage to the left and right channels before summing them up. For instance, you could give 70% weightage to the left channel and 30% to the right channel before adding them together. This technique allows for a customizable balance between the channels. In this code, the stereo_to_mono_weighted_mixing() function takes the stereo audio file as input, and by applying weighted mixing, it generates a mono signal. You can adjust the left_weight and right_weight parameters to assign different weights to the left and right channels before summing them up to create the mono signal. Ensure that the sum of the weights equals 1 to maintain the overall balance of the signal.
