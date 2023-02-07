# import numpy as np
right_array=[1,2,3,4,5,6,7]
right_rotate=int(input("enter position to rotate right array elements= "))
print("original array elements before right rotation")
print(right_array)
arr=np.concatenate(right_array[-right_rotate:],right_array[:-right_rotate],axis=0)
print('final array elements after right rotation:')
print(arr)
