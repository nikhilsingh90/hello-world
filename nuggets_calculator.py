"""
Calculates the packs of nuggets required 
"""


def nuggets(number):
    
    """
    Finds a combination of nugget packs (6,9,20) to purchase a given number of nuggets

    Args: limit = the number of nuggets needed
    Returns: a string
    """
    try:
        limit = int(number)
        assert type(limit) == int, "input value is not an integer"
        assert limit>=0, "input value is negative"

        for c in range(int(limit/20)+1):
            for b in range(int(limit/9)+1):
                for a in range(int(limit/6)+1):
                    n=6*a+9*b+20*c
                    if n==limit:
                        return "6 packs = %s, 9 packs = %s, 20 packs = %s" %\
                               (str(a),str(b),str(c))
        return "No soltuion for %s nuggets." % str(limit)
    except:
        return "An error occured, make sure you enter an Integer."

    
def test():
    """
    This is a test for the nuggets function
    """

    input("Testing 55")
    answer = nuggets(55) #test 1
    print (str(answer))

    input("Testing 65")
    answer = nuggets(65) #test 2
    print (str(answer))


    input("Testing 17")
    answer = nuggets(17) #test 3 with no results
    print (str(answer))

    input("Testing 1210")
    answer = nuggets(1210) #test 4 with large number
    print (str(answer))
    
    input("Testing 'h'")
    answer = nuggets('h') #test 4 error due to string
    print (str(answer))
    
    input("Done Testing! Hit enter to exit")

    




def main():
    print ("Nugget Program")
    print ("="*30)
    print ("")

    user_input= str(input("Test or Run"))

    if user_input.lower() == 'test':
        print ("")
        test()

    else:
        while True:
            print ("")
            user_input2= input("How many nuggets do you want for your party? (Type 'q' to exit): ")

            if user_input2.lower() == 'q':
                break

            print("")
            answer = nuggets(user_input2)
            print (str(answer))
            print ("")

if __name__ == "__main__":
    main()
