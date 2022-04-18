# Signal_Processing_on_Dinucleotide_Data

signal_gen.py: I have written and integrated a code for implementing Low-Pass,High Pass and Pass Band Filter on a Dinucleotide data and then convoluted input and the filter to generate the output plot using scipy library in Python using scipy.

enum.py: I have written and integrated a code for implementing Low-Pass,High Pass and Pass Band Filter on a Dinucleotide data and then convoluted input and the filter to generate the output plot using scipy library in Python using scipy, then integrated Power Spectral Density and Peak Counter with it. Then I automated the whole pipeline in which user just have to give a csv file and hw will get the desired results.

![aa0](https://user-images.githubusercontent.com/60814171/163824140-fb9d5e16-0c9b-4263-a6e9-1049a0ceb8bc.png)
![aa_df0 0PSD](https://user-images.githubusercontent.com/60814171/163824235-6501d889-3c98-4078-9069-4a203500ab5f.png)
![aa_df0 0peak_counter_after_bandpass](https://user-images.githubusercontent.com/60814171/163824274-74f5e0b7-61f2-41d2-88b7-4d5b5960b92e.png)

First Image is taking one parameter of a DNA Sequence and convolutr it with the filter.
Second Image is the periodogram of the same parameter.
Third is the peak counter.

And this all helps us in finding the nature of the sequence and location of a promoter.

