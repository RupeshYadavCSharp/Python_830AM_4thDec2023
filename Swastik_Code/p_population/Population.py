#code for finding illiterate mens and womens in town
tp=80000
print("total population is",tp)                    #tp (total population) = 80000
tm=int(((52/100)*tp))                           #tm (total mens) = (52/100)*80000 = 41600
print("total mens are",tm)
print("total womens are",tp-tm)                    #tw (total womens) = tp-tm = 38400
tl=int(((48/100)*tp))                              #tl (total literacy) = (48/100)*80000 = 38400
print("total literacy is",tl)
lm=int(((35/100)*tp))                              #lm (literate mens) = (35/100)*80000 = 28000
print("literate mens are",lm)
print("literate womens are",tl-lm)                 #lw (literate womens) = tl-lm = 10400
print("illiterate mens are",tm-lm)                 #illiterate mens are = tm-lm = 13600
print("illiterate womens are",((tp-tm)-(tl-lm)))   #illiterate womens are = tw-lw = 28000