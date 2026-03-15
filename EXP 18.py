# Name: Nadir Shaikh
# UIN : 251P086
print("Name:Nadir Shaikh,UIN: Nadir Shaikh")

import numbers as  np 


arr1 = np.array([10,20,30,40,50])
print("1D Array:",arr1)

print("first element:",arr1[0])
print("Last Element:",arr1[-1])
print("Elements from index 1 to 3:",arr1[1:4])

arr2 = np.array([[1,2,3],[4,5,6]])
print("\n2D Array:\n",arr2)

print("Element at row 0,colum1:",arr2[0,1])
print("first row:",arr2[0,:])
print("Second column:",arr2[:,1])

arr3= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("\n3D Array: \n",arr3)

print("Element:",arr3[1,0,1])
print("first matrix: \n",arr3[:,0,:])

arr = np.array([1,2,3,4,5,6])
reshaped = arr .reshape(2,3)
print("\nOriginal Array:",arr)
print("Reshaped (2*3):\n",reshaped)