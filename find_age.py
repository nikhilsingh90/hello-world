print ("Hello, what is your name?") 
name=str(input(">> "))
print ("")

print ("Nice!")
print ("")

print ("So %s, I will now guess your age" %name)
print ("")

print ("But I need to ask some questions")
print ("")


print ("What is the first number of your age?")
fn= int(input('>>'))
print ("")

n1=fn*5
print ("Okay %s, I will multiply that by 5= %s" %(str(name),str(n1)))
print ("")


n2=n1+3
print ("Next, I will add 3 to the number=",n2)
print ("")

n3=n2*2
print ("Next, I will double that number=", n3)
print ("")

print ("Now I will need the second number of your age")
sn= int(input(">>"))
print ("")

n4=n3+sn
print ("Thanks! I will add that number to our running total %s + %s = %s" % \
      (str(n3),str(sn),str(n4)))
print ("")
       
age=n4-6
print ("And the last thing I will do is subtract 6[%s -6] = %s" % \
       (str(n4),str(age)))
       
       
print ("So %s your age is = %s" % (str(name),str(age)))
