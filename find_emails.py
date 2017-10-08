"""
Find emails from a string
"""

import re

input("Press a key")
print ("This is the email list - \
        1.random@example.com \
        2.random@example.com \
        3.random@example.com \
        4.random@example.com \
        5.random@example.com")
print ("")
m= re.findall('[\w.-]+@[\w.-]+.com','1.random@example.com \
        2.random@example.com 3.random@example.com 4.random@example.com \
        5.random@example.com')

for email in m:
        print (email)


"""
Output:

1.random@example.com
2.random@example.com
3.random@example.com
4.random@example.com
5.random@example.com
"""
