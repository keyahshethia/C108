import random
import plotly.figure_factory as ff

dice_result=[]
count=[]

for i in range(0,100):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    dice_result.append(d1+d2)
    count.append(i)

print(count,dice_result)
fig=ff.create_distplot([dice_result],["Result"])
fig.show()