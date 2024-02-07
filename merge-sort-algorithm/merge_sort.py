# Define a function to perform merge sort on an array
def merge_sort(arr):
    """
    This function implements the merge sort algorithm
    
    :param: arr
    :type: list
    """
    if len(arr) > 1:
        mid = len(arr) // 2    #Find the center of the array
        #Split the array in two halves(L-left and R-right)
        L = arr[:mid]
        R = arr[mid:]

        # Recursively call merge_sort on left and right halves
        merge_sort(L)
        merge_sort(R)
        
        #initialize i,j,k as 0
        i = j = k = 0

        # Merge the sorted left and right halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy any remaining elements from left or right half
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Define a function to perform merge sort on a list of pairs
def merge_sort_pairs(arr):
    """
    This function implements the merge sort algorithm for a list of pairs"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        # Recursively call merge_sort_pairs on left and right halves
        merge_sort_pairs(L)
        merge_sort_pairs(R)

        i = j = k = 0

        # Merge the sorted left and right halves by comparing the latitudes first, if the latitudes are identical compare longitudes
        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            elif L[i][0] > R[j][0]:
                arr[k] = R[j]
                j += 1
            else:
                if L[i][1] < R[j][1]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            k += 1

        # Copy any remaining elements from left or right half
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
