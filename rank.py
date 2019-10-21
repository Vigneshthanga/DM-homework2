#!/usr/bin/python
import statistics
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot_2samples

marks = [47, 63, 71, 39, 47, 49, 43, 37, 81, 69, 38, 13, 29, 61, 49, 53, 57, 23, 58, 17, 73, 33, 29]
marks2 = [20, 49, 85, 17, 33, 62, 93, 64, 37, 81, 22, 18, 45, 42, 14, 39, 67, 47, 53, 73, 58, 84, 21]
grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+','C', 'C-', 'D', 'F']
marks.sort()
_sum = 0
print(marks)
for i in range(0, len(marks)):
    _sum += marks[i]
print('sum '+str(_sum))
mean = _sum/len(marks)
print('mean '+str(mean))
sd = statistics.stdev(marks)
print('Standard Deviation '+str(sd))
step = (sd/3)

print('step '+str(step))
mean_index = 5

scores = []

for i in range(len(grade)):
    scores.append(0)

i = mean_index
j = 0
while i < len(grade):
    scores[i] = mean - (step*j)
    j += 1
    i += 1

i = mean_index-1
j = 1
while i >= 0:
    scores[i] = mean + (step*j)
    j += 1
    i -= 1

i = 0
j = 0
idx = 0
flag = False

Z = []
while(i<len(marks)):
    Z.append((marks[i] - mean)/step)
    i+=1
print(Z)

i=0
Z2=[]
marks2.sort()
_sum2=0
for m in marks2:
    _sum2+=m
mean2 = _sum2/len(marks2)
sd2 = statistics.stdev(marks2)
step2 = sd2/3
print('mean '+str(mean)+ ' mean2 '+str(mean2))
print('sd '+str(sd)+'sd2 '+str(sd2))
print('step '+str(step)+'step2 '+str(step2))
while(i<len(marks2)):
    Z2.append((marks2[i]-mean2)/step2)
    i+=1
print(Z2)

plt.figure()
#plt.scatter(Z, Z2)
pp_x = sm.ProbPlot(np.array(marks))
pp_y = sm.ProbPlot(np.array(marks2))
qqplot_2samples(pp_x, pp_y, line='45')
#qqplot(Z, Z2, c='r', alpha=0.5, edgecolor='k')
plt.xlabel('Section-1')
plt.ylabel('Section-2')
#plt.show()


i=0
while (j < len(marks)):
    idx = 0
    flag = False
    i = 0
    while i < len(scores):
        if (marks[j] >= scores[i]):
            flag = True
            if (i != 0):
                print('mark '+ str(marks[j])+' grade '+str(grade[i-1]))
            else:
                print('mark '+ str(marks[j])+' grade '+str(grade[i]))
            break
        else:
            i += 1
    if (not flag):
        i = len(scores)-1
        print('mark '+ str(marks[j])+' grade '+str(grade[i]))
    j += 1
