

def mergeSort(arr1,arr2):
	n1= len(arr1)
	n2 = len(arr2)
	arr3 = [None] * (n1 + n2)
	i = 0
	j = 0
	k = 0
	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
		    arr3[k] = arr1[i]
		    k = k + 1
		    i = i + 1
		else:
		    arr3[k] = arr2[j]
		    k = k + 1
		    j = j + 1
	while i< n1:
		arr3[k] = arr1[i]
		k = k + 1
		i = i + 1
	while j < n2:
		arr3[k] = arr2[j]
		k = k + 1
		j = j + 1

		



 
	print (arr3)



arr= [1,3]
arr1 = [2]
a=mergeSort(arr,arr1)
# print (a)