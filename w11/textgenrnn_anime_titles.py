from textgenrnn import textgenrnn

textgen = textgenrnn('anime_fantasy_titles_e10.hdf5')
tg = textgen.generate(10, temperature=0.5, return_as_list=True)

#print(tg)
for n in range(len(tg)):
    print(tg[n])
