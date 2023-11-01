
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
        # Flag to optimize the sorting process
        sorted_flag = True
        for j in range(0, n - i - 1):
            # Comparing adjacent elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                sorted_flag = False

        # If no two elements were swapped in the inner loop, the list is already sorted
        if sorted_flag:
            break

# Exemplu de utilizare:
numere = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numere)
print("Lista sortată:", numere)