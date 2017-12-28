import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec


width  = 3.5
#height = 2.5
height = width / 1.618
labelsize 	= 10
legendfont 	= 9

for i in range(0,25):


	data = pd.read_csv('Results/Results_Zpos_1_53_Cluster_0.csv')[i*1944:(i+1)*1944]

	column = 'Attenuation'

	y = data[column]
	x = np.sqrt((1-data.iloc[:,7])**2+(3-data.iloc[:,8])**2+(1.5-data.iloc[:,9])**2)


	mu = np.mean(y)
	stdlow  = mu-1.96*np.std(y)
	stdhigh = mu+1.96*np.std(y)

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

	scat.scatter(x, y, alpha=0.8, color='k', s=5, marker='+', linewidth=0.5, label='$A_{dB}$')
	scat.axhline(y = mu, alpha=0.7, linestyle = '-', color='b', linewidth=1, label='$\mu_{A_{dB}}$')
	#plt.plot(x, stdlow, color='r', linewidth='0.6', label='$\mu_{A_{dB}}-2*\sigma_{A_{dB}}$')
	scat.axhline(y = stdhigh, alpha=0.7, linestyle = '--', color='g', linewidth=1, label='$\mu_{A_{dB}}+2*\sigma_{A_{dB}}$')
	#scat.yaxis.tick_right()
	#scat.yaxis.set_label_position("right")

	plt.xlabel('anti-noise source to microphone distance')
	plt.ylabel('Attenuation')
	#plt.xlim((0,3.5))
	#plt.ylim((3.9,5.7))
	#plt.grid(True, which='both', linestyle='--', linewidth='0.3')
	plt.legend(bbox_to_anchor=(1, 0.8),loc='upper right', fontsize = legendfont, framealpha=0.4)


	s = hist.hist(y, bins = 200, orientation='horizontal', normed = True)
	#hist.invert_xaxis()
	hist.axis('off')


	fig.set_size_inches(width, height)
	plt.savefig('Attenuation_'+str(i)+'.pdf', dpi = 600)
