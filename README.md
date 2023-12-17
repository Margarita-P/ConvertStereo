# ConvertStereo
Converting stereo sound to mono

Option1 evaluates that the file has two channels - is stereo (stereo: 2 channels, mono: 1 channel). Uses Numpy module function "mean" to calculate both channel's averages and then puts the averages into the new file.
