from pandas import read_hdf
from pandas import HDFStore
import numpy as np

Constellation 		= read_hdf('Input/1_4_configurations.h5','Config')

##########################################################################################

# array([ 0.1 ,  0.21,  0.32,  0.43,  0.54,  0.65,  0.76,  0.87,  0.98,
#         1.09,  1.2 ,  1.31,  1.42,  1.53,  1.64,  1.75,  1.86,  1.97,
#         2.08,  2.19,  2.3 ,  2.41,  2.52,  2.63,  2.74,  2.85,  2.96])

##########################################################################################

z = np.array([ 0.1 ,  0.21,  0.32,  0.43,  0.54,  0.65,  0.76,  0.87,  0.98,
        1.09,  1.2 ,  1.31,  1.42,  1.53,  1.64,  1.75,  1.86,  1.97,
        2.08,  2.19,  2.3 ,  2.41,  2.52,  2.63,  2.74,  2.85,  2.96])

for zpos in z:

	Constellation['Az']	= zpos

	i, d = divmod(zpos, 1)
	i = int(i)
	d = int(round(d,2)*100)


	hdf     =   HDFStore('Input/configurations_zpos_'+str(i)+'_'+str(d)+'.h5')
	hdf.put('Config', Constellation, format='table', data_columns=True)
