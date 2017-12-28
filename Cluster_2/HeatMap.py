import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

labelsize 	= 	12
width  		= 	5
height 		= 	3.09

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=labelsize)
plt.rc('ytick', labelsize=labelsize)
plt.rc('axes', labelsize=labelsize)

TransSeparation     	=       0.11
xpos 					= 		np.arange(0.1, 6, TransSeparation)
ypos 					= 		np.arange(0.1, 4, TransSeparation)

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

#for i in range(0,25):

i = 6

data 	= 	pd.read_csv('Results/Results__Zpos_1_53_Cluster_2.csv')[i*1944:(i+1)*1944]
column 	= 	'Attenuation'
y 		= 	data[column]
W 		= 	36
N 		= 	y.shape[0]
H 		= 	N/W
I 		= 	y.values.reshape((H, W)).T

# print H, W
#I = (I-np.min(I))/(np.max(I)-np.min(I))
# print "Origin Value : ", I[0,0]
# print "End Value    : ", I[-1,-1]

xvalues = data['Ax']
yvalues = data['Ay']

xmax 	= np.amax(xvalues)
ymax 	= np.amax(yvalues)

fig, ax = plt.subplots()
fig.set_size_inches(width, height)

fig.subplots_adjust(left=0.07, bottom=.09, right=1.02, top=0.99)
plt.imshow(I, origin='upper', cmap = 'viridis')

Sx, Sy = data.iloc[1,1:3].values
Rx, Ry = data.iloc[1,4:6].values

Sx = find_nearest(xpos,Sx)
Sy = find_nearest(ypos,Sy)
Rx = find_nearest(xpos,Rx)
Ry = find_nearest(ypos,Ry)

Sxi, = np.where( xpos==Sx )
Syi, = np.where( ypos==Sy )
Rxi, = np.where( xpos==Rx )
Ryi, = np.where( ypos==Ry )

Slabel = 'Noise Source('+str(Sx)+', '+str(Sy)+')'
Rlabel = 'Microphone('+str(Rx)+', '+str(Ry)+')'

plt.plot(Sxi,Syi,'*', color ='r', label =	Slabel)
plt.plot(Rxi,Ryi,'x', color ='k', label =	Rlabel)
plt.legend(loc="lower left", fontsize = labelsize, framealpha=0.08)

# cmap=plt.cm.Blues

plt.xlabel('x position')
plt.ylabel('y position')
plt.colorbar()

# plt.xticks([], [])
# plt.yticks([], [])
# xlabels = [item.get_text() for item in ax.get_xticklabels()]
# ylabels = [item.get_text() for item in ax.get_yticklabels()]

# xticks  = np.round(np.linspace(0, xmax, 7),2)
# yticks  = np.round(np.linspace(0, ymax, 5),2)
# ax.set_xticklabels(xticks)
# ax.set_yticklabels(yticks)
# plt.show()

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
ax.set_xticks([])
ax.set_yticks([])


#plt.show()
plt.savefig('Colorplane_'+str(i)+'.pdf', dpi = 600)
