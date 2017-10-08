"""
Calculates tip value for a bill
"""

def payments(bill,ppl):
    """
    Determines how much each person pays

    Args:   bill = total bill
            ppl  = number of people

    Returns: The individual payment per person
    """
    try:
        return round((bill/ppl),2)
        
    except:
        print("An error occured while calculating payments")

def tip(bill,perc,ppl):
    """
    Determines the tip to be paid by each person

    Args:   bill = total bill
            perc = percentage of tip to give
            ppl  = number of people
    Returns: The individual payment per person

    """
    try:
        return round((bill*float(perc/100))/ppl,2)
    except:
        print("An error occured while calculating tip")



def main():
    
    print ("How much is the bill?")
    while True:
        try:
            total_bill= float(input(">> Rs."))
            break
        except:
            print ("")
            print ("Must be a number value")
            print ("")

    print ("")

    print ("How many people?")
    while True:
        try:
            num_ppl= int(input(">> "))
            break
        except:
            print ("")
            print ("Must be a integer value")
            print ("")

    print ("")

    print ("What % of tip?")
    while True:
        try:
            perc= float(input(">> %"))
            break
        except:
            print ("")
            print ("Must be a integer value")
            print ("")
            
    print("")
    print("Calculating payment...")

    bill_payment= payments(total_bill,num_ppl)

    tip_payment = tip(total_bill,perc,num_ppl)

    total_payment = float(bill_payment)+float(tip_payment)

    print ("Each person pays $%s for the bill" % \
           str(bill_payment))
    print ("Each person pays $%s for the tip" % \
           str(tip_payment))
    print ("Total payment for each person including the tip = %s" % \
           str(total_payment))


if __name__ == '__main__':
    main()

