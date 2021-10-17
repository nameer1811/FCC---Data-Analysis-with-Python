#mean_var_std
import numpy as np
a = [2,6,2,8,4,0,1,5,7]

listToArray = np.array(a)
array3d = listToArray.reshape((3,3))

meanList = [array3d.mean(axis=0).tolist(), array3d.mean(axis = 1).tolist(), array3d.mean().tolist()]
varianceList = [array3d.var(axis=0).tolist(),array3d.var(axis=1).tolist(), array3d.var().tolist()]
standardDevList = [array3d.std(axis=0).tolist(),array3d.std(axis=1).tolist(), array3d.std().tolist()]
maxList = [array3d.max(axis=0).tolist(), array3d.max(axis=1).tolist(), array3d.max().tolist()]
minList = [array3d.min(axis=0).tolist(), array3d.min(axis=1).tolist(), array3d.min().tolist()]
sumList = [array3d.sum(axis=0).tolist(), array3d.sum(axis=1).tolist(), array3d.sum().tolist()]


calculations = {}

calculations['mean'] = meanList
calculations['variance'] = varianceList
calculations['standard deviation'] = standardDevList
calculations['max'] = maxList
calculations['min'] = minList
calculations['sum'] = sumList

print(calculations)
