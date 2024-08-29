"""
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Track if any elements were swapped
        # Last i elements are already sorted
        for j in range(0, n -  - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # If no elements were swapped, the array is already sorted
 """
 
numnum = []
if __name__ == "__main__":
    # Get user input as a string and split into a list of strings
    print("Please enter numbers for me to sort...If you dont want to add another, type 'n'")
    user_input = input("Your number : ")
    while user_input.isdigit() :
        numnum.append(user_input)
        user_input = input("Your number : ")
    print(numnum)
        
