# Merge Sort Algorithm in Python
# This program sorts an array using the merge sort algorithm
# Merge sort uses a divide-and-conquer approach to sort elements efficiently

def merge_sort(arr):
    
    #Sorts an array in ascending order using the merge sort algorithm.
    
    #Parameters:
    #arr (list): The list of numbers to be sorted
    
    #Returns:
    #None: Sorts the list in-place #
    
    # Base case: If array has more than one element
    if len(arr) > 1:
        # Find the middle point to divide the array
        mid = len(arr)//2
        
        # Divide the array elements into two halves
        L = arr[:mid]
        R = arr[mid:]

        # Recursively sort the first half
        merge_sort(L)
        # Recursively sort the second half
        merge_sort(R)

        # Initialize pointers for L, R and the main array
        i = j = k = 0

        # Merge the sorted halves back into the main array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]  # Place the smaller element from L
                i += 1
            else:
                arr[k] = R[j]  # Place the smaller element from R
                j += 1
            k += 1

        # Copy remaining elements of L, if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R, if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Merge Sorted:", arr)
