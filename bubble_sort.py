def bubble_sort(a):
	n = len(a)
	for i in range(0,n-1):
		for j in range(0, n-i-1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
		
a = [6,2,1,7]
bubble_sort(a)
print("Sorted array is:")
for i in range(len(a)):
	print(a[i])

    

 