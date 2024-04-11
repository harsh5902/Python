
def printSubsequences(arr, index, subarr): 
	
	if index == len(arr): 
		print(subarr) 
	
	else: 
		printSubsequences(arr, index + 1, subarr+[arr[index]]) 
		printSubsequences(arr, index + 1, subarr) 
	return
		
arr = [1, 2, 3] 

printSubsequences(arr, 0, []) 

