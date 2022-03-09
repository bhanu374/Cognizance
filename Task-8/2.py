import numpy as np
x = np.array([1 ,0, 1, 1 ,1, 0])
y = np.array([1 ,0, 0, 1 ,0 ,1])
array_len=len(x)
for i in range(array_len):
    if x[i] == y[i] :       
        result=0
    else :
        result=1
if result==0:
    
    print("Arrays are equal ")
else :
    
    print("Arrays are not equal ")
