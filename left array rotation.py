import numpy as np
left_array=np.array([1,2,3,4,5,6,7])
left_rotate=int(input("enter position to rotate left array elements= "))
print("original array elements before rotation")
print(left_array)
arr=np.concatenate(left_array[left_rotate:],left_array[:left_rotate],axis=0)
print('final array elements after left rotation:')
print(arr)
