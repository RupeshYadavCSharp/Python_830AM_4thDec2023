totalpopulation=80000
totalmen=totalpopulation*52/100
totalwomen=totalpopulation-totalmen
totalliteracy=totalpopulation*48/100
literatemen=totalpopulation*35/100
literatewomen=totalliteracy-literatemen
illiteratemen=totalmen-literatemen
illiteratewomen=totalwomen-literatewomen
print("total population is",totalpopulation)
print("total mens are",totalmen)
print("total womens are",totalwomen)
print("total literacy is",totalliteracy)
print("total literate mens are",literatemen)
print("total literate womens are",literatewomen)
print("total illiterate mens are",illiteratemen)
print("total illiterate womens are",literatewomen)