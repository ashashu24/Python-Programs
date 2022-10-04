# Just an example 
def binarySearch(target, List):
    '''This function performs a binary search on a sorted list and returns the position if successful else returns -1'''
    left = 0 
    right = len(List) - 1 
    global iterations
    iterations = 0

    while left <= right: 
        iterations += 1
        mid = (left + right) // 2
        if target == List[mid]:
            return mid
        elif target < List[mid]:
            right =  mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
    target = 2
    ans = binarySearch(target, List)
    if(ans != -1):
        print('Target found at position:',ans,'in',iterations,'iterations')
    else:
        print('Target not found')
