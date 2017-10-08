"""
Determines if a number is a prime number
"""

    
def is_prime_func(number):
    """
    Takes a number and determines if it is a prime number
    Args: a number
    Returns:True or False
    """
    is_prime= True
    n= abs(int(number))

    if n<2:
        is_prime = False

    elif n ==2:
        is_prime= True
    elif n%2 == 0:
        is_prime= False
    else:
        for x in range(3,int(n**0.5)+1,2):
            if n%x == 0:
                is_prime= False
    return is_prime


def find_1000_prime():
    """
    Finds the 1000th prime number
    Args: None
    Returns 1000th prime
    """
    current_number = 2
    count = 0
    while True:
        is_prime = is_prime_func(current_number)
        if is_prime:
            count +=1
        if count == 1000:
            return current_number
        else:
            current_number +=1


def find_primes(end_number):
    """
    Finds all prime numbers to and including an end number
    Args: a user entered number to end our loop
    Returns: a list of prime numbers
    """
    primes=[]
    for n in range(2,end_number+1):
        is_prime = is_prime_func(n)
        if is_prime:
            primes.append(n)
    print (primes)

def main():
    print ("Prime number program")
    print ("="*40)
    print("")

    while True:
        user_number = int(input("Enter a number larger than 2: "))
        if user_number <=2:
            print ("Not larger than 2, try again")
            print ("")
        else:
            find_primes(user_number)



    """
    thous_prime = find_1000_prime()

    if thous_prime:
        print ("")
        print ("The 1000th prime number is : ",int(thous_prime))

    else:
        print("Sorry, error occured")
    """


if __name__ == '__main__':
    main()
