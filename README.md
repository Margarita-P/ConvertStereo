# ConvertStereo
Converting stereo sound to mono

Option1 evaluates that the file has two channels - is stereo (stereo: 2 channels, mono: 1 channel). Also, checks if one of the channels is emtpy - only 0s, then it would take only one channel. If both are not empty, then it uses Numpy module function "mean" to calculate both channel's averages and then puts the averages into the new file.
