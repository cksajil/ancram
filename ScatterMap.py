import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec


data0 = pd.read_csv('Cluster_0/Results/Results__Zpos_1_53_Cluster_0.csv')
data1 = pd.read_csv('Cluster_1/Results/Results__Zpos_1_53_Cluster_1.csv')
data2 = pd.read_csv('Cluster_2/Results/Results__Zpos_1_53_Cluster_2.csv')
data3 = pd.read_csv('Cluster_3/Results/Results__Zpos_1_53_Cluster_3.csv')
frames = [data0, data1, data2, data3]
result = pd.concat(frames)

print result.shape
print result.describe().iloc[[1,2,3,-1], -4:]


width  = 3.5
#height = 2.5
height = width / 1.618
labelsize 	= 10
legendfont 	= 8

data = result

column = 'Attenuation'

y = data[column]
x = np.sqrt((data.iloc[:,4]-data.iloc[:,7])**2+(data.iloc[:,5]-data.iloc[:,8])**2+(data.iloc[:,6]-data.iloc[:,9])**2)


mu = np.mean(y)
stdlow  = mu-1.96*np.std(y)
stdhigh = mu+1.96*np.std(y)

print stdhigh
plt.rc('pdf', fonttype = 42)
plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=labelsize)
plt.rc('ytick', labelsize=labelsize)
plt.rc('axes', labelsize=labelsize)


fig = plt.figure()
fig.subplots_adjust(left=0.15, bottom=.20, right=.99, top=.97)

gspec 		= 		gridspec.GridSpec(1, 5)
hist 		= 		plt.subplot(gspec[0,4])
scat 		= 		plt.subplot(gspec[0,0:4])

scat.scatter(x, y, alpha=0.3, color='k', s=1, marker='.', linewidth=0.1, label='$A_{dB}$')
scat.axhline(y = mu, alpha=0.8, linestyle = '-', color='b', linewidth=1, label='$\mu_{A_{dB}}$')
#plt.plot(x, stdlow, color='r', linewidth='0.6', label='$\mu_{A_{dB}}-2*\sigma_{A_{dB}}$')
scat.axhline(y = stdhigh, alpha=0.8, linestyle = '--', color='g', linewidth=1, label='$\mu_{A_{dB}}+1.96*\sigma_{A_{dB}}$')
#scat.yaxis.tick_right()
#scat.yaxis.set_label_position("right")

plt.xlabel('Anti-noise source to microphone distance')
plt.ylabel('Attenuation')
#plt.xlim((0,8.5))
#plt.ylim((0,15))
#plt.grid(True, which='both', linestyle='--', linewidth='0.3')
plt.legend(loc='lower right', fontsize = legendfont, framealpha=0.7, borderpad=0.15, labelspacing = 0.1, handlelength=1, handletextpad= 0.1, borderaxespad=0.1,columnspacing=0.1)


s = hist.hist(y, bins = 200, orientation='horizontal', normed = True)
#hist.invert_xaxis()
hist.axis('off')


fig.set_size_inches(width, height)
plt.savefig('Attenuation.png', dpi = 600)
