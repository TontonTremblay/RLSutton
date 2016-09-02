"""
Reproduction of the one arm problem from RL Sutton book, page 29. 
author: Jonathan Tremblay
"""


import numpy as np 
import pandas as pd
def AverageReward(a):
	return float(sum(a))/len(a)

def selectAction(d,e=0):
	if np.random.rand() < e:
		return int(np.random.uniform(0,10))
	a = [0]
	ep = 0.001
	for k in d:
		#in the range
		top = 0
		can = 0
		if not d[a[0]]['n'] == 0:
			top = d[a[0]]['sum']/d[a[0]]['n']
		if d[k]['n'] != 0:
			can = d[k]['sum']/d[k]['n']
		if can < top + ep and can > top - ep :
			a.append(k)
		elif can > top:
			a = [k]
	return np.random.choice(a)
		

d = {}	

np.random.seed(1)

d['0']   = {'sum':0, 'n':0, "a":{i:{'sum':0,'n':0} for i in range(10)}, "e":0,   'df':pd.DataFrame(), "avg":[] }
d['01']  = {'sum':0, 'n':0, "a":{i:{'sum':0,'n':0} for i in range(10)}, "e":0.1, 'df':pd.DataFrame(), "avg":[] }
d['001'] = {'sum':0, 'n':0, "a":{i:{'sum':0,'n':0} for i in range(10)}, "e":0.01,'df':pd.DataFrame(), "avg":[] }
d['05'] = {'sum':0, 'n':0, "a":{i:{'sum':0,'n':0} for i in range(10)}, "e":0.5,'df':pd.DataFrame(), "avg":[] }
d['02'] = {'sum':0, 'n':0, "a":{i:{'sum':0,'n':0} for i in range(10)}, "e":0.2,'df':pd.DataFrame(), "avg":[] }

for j in range(100):
	#reset
	s = np.random.randn(10)
	for k in d:
		d[k]['sum'] = 0	
		d[k]['n'] = 0
		d[k]['a'] = {i:{'sum':0,'n':0} for i in range(10)}
		d[k]['avg'] = []
	#one multi-arm game for n rounds
	for i in range(2000):
		for k in d:
			maxkey = selectAction(d[k]["a"],e=d[k]['e'])	
			rg = s[maxkey] + np.random.randn()
			d[k]['a'][maxkey]['sum'] += rg
			d[k]['a'][maxkey]['n'] += 1
			d[k]['sum'] += rg
			d[k]['n'] += 1
			d[k]['avg'].append(d[k]['sum']/d[k]['n'])			

	for k in d:
		d[k]['df'][j] = d[k]['avg']


# print (d['0']['df'])

output = pd.DataFrame()

for k in d:
	output[k] = d[k]['df'].mean(axis=1)

import seaborn as sns
fig= sns.plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)
for k in d:
	output.plot(ax=ax,y=k)
sns.plt.show()

