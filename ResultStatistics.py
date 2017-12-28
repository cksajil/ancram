import pandas as pd



data0 = pd.read_csv('Cluster_0/Results/Results__Zpos_1_53_Cluster_0.csv')

print data0.describe().iloc[[1,2,3,-1], -4:]

data1 = pd.read_csv('Cluster_1/Results/Results__Zpos_1_53_Cluster_1.csv')

print data1.describe().iloc[[1,2,3,-1], -4:]

data2 = pd.read_csv('Cluster_2/Results/Results__Zpos_1_53_Cluster_2.csv')

print data2.describe().iloc[[1,2,3,-1], -4:]

data3 = pd.read_csv('Cluster_3/Results/Results__Zpos_1_53_Cluster_3.csv')

print data3.describe().iloc[[1,2,3,-1], -4:]

frames = [data0, data1, data2, data3]
result = pd.concat(frames)

print result.shape

print result.describe().iloc[[1,2,3,-1], -4:]
