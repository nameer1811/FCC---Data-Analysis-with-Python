import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  listToArray = np.array(list)
  array3d = listToArray.reshape((3,3))

  meanList = [array3d.mean(axis=0).tolist(), array3d.mean(axis = 1).tolist(), array3d.mean()]
  varianceList = [array3d.var(axis=0).tolist(),array3d.var(axis=1).tolist(), array3d.var()]
  standardDevList = [array3d.std(axis=0).tolist(),array3d.std(axis=1).tolist(), array3d.std()]
  maxList = [array3d.max(axis=0).tolist(), array3d.max(axis=1).tolist(), array3d.max()]
  minList = [array3d.min(axis=0).tolist(), array3d.min(axis=1).tolist(), array3d.min()]
  sumList = [array3d.sum(axis=0).tolist(), array3d.sum(axis=1).tolist(), array3d.sum()]


  calculations = {}

  calculations['mean'] = meanList
  calculations['variance'] = varianceList
  calculations['standard deviation'] = standardDevList
  calculations['max'] = maxList
  calculations['min'] = minList
  calculations['sum'] = sumList
    
  return calculations
