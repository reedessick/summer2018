import numpy as np

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

import sys

#---------

### read in the file from disk
path = sys.argv[1]
data = np.loadtxt(path, skiprows=1)

print len(data)
print data.shape

data = data.transpose()
print data.shape

x, y = data
x = data[0]
y = data[1]

### plot dat data
fig = plt.figure()
ax = fig.gca()

ax.plot(x, y, color='r', linestyle='dashed', label='cool data')

ax.set_xlabel('abscissa')
ax.set_ylabel('ordinate')

ax.grid(True)
ax.legend(loc='best')

figname = 'figure.png'
fig.savefig(figname)
plt.close(fig)

### save modified data
y *= 5

newpath = path[:-4]+'_new.txt'
np.savetxt(newpath, np.array([x,y]).transpose())
