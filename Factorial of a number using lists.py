# Function to multiply the number
def mul(arr, i):
    n = len(arr)
    c = 0 # Initialize carry to zero
    for j in range(n):# Storing the digits in reverse order(123 as       [3,2,1])
        res = (arr[j]*i)+c  # Multiply each digit in the array by i
        if res > 9:
            arr[j] = res%10 # If result is greater than 9
            c = res//10 # then carry is stored in c
        else:
            c = 0           # If carry is not there then change c to 0
            arr[j] = res
    if c != 0:              # if carry is there, then append it at the end
        arr.append(c)
    return arr              # Return the resulting array
            


# Function of factorial
def fact(n):
    arr = [1]               # Initialize the array with value 1
    for i in range(2, n+1): # start from 2 to n
        arr = mul(arr, i)   # pass the list and value to be multiplied 
    return arr              # Return the list


# Driver code
def main():
    n = int(input("Enter a number : ")) # Take the input from the user
    result = fact(n)
    m = len(result)
    print(f"Factorial of {n} is : ", end="")
    for i in range(m-1, -1, -1):        # Our list has the digits of the
        print(result[i], end="")        # number stored in reverse order


# Calling main
if __name__ == "__main__":
    main()
