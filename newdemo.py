import numpy as np
import scipy.io
from scipy import linalg 
import matplotlib.pyplot as plt
data = scipy.io.loadmat('hw0data.mat')

print (data)
a = data['M']

print ("Dimensions of M", data['M'].shape)
print("Element in Row 4, Col 5" , data['M'][3][4])
print ("Mean of row 5" , data['M'].mean(axis=0)[4])
print("histogram")

M = data['M']
plt.hist(M[3])
plt.show()

mult = np.dot(M.T,M)
p = []
p = np.linalg.eig(mult)
psort = (-np.sort(-p[0]))
print psort[0],psort[1],psort[2]


