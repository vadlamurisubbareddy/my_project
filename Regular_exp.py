#    Regular expression

'''
search
match
find all
'''

'''

# modifyres
.  # any charecter match
\d # any digit match
\w # any charecters match
\W # any string does match
\s # space
\t # tab
$  # ending match
^  # stars with match
*  # 0 or more
 

# Character	Description	

[]	A set of characters	
\	Signals a special sequence (can also be used to escape special characters)	
.	Any character (except newline character)	
^	Starts with		
$	Ends with		
*	Zero or more occurrences	
+	One or more occurrences	
?	Zero or one occurrences	
{}	Exactly the specified number of occurrences	
|	Either or		
()	Capture and group	 
'''

# flags
'''
re.M | re.I
'''

import re
'''
 
 
exp='this is module 4,4,5,6,,7 method'
out=re.search(r'\d,\d+',exp)
out1=re.search(r'.+',exp)
print(out1.group())


string= '39801 356, 2102 1111'  # out 80135
out=res=re.search(r'(\d{3}) (\d{2})',string)
print(out.group(1))
print(out.group(2))


line = "cats77 are smarter then dogs"

out=re.match(r'(.*) are (.*?) *(\w+$)',line)
print(out.group(2))
print(out.group(3))

number= '9398159382'
result=re.search(r'\d+',number)
print(result.group())
'''

# Find All

data="""Siva  is 23 years old, Jagan  is 40 years old 
and Venky  is 25  years and Bharath  is 25 
years old his firnds  of sure"""

age =re.findall(r'\d+',data)
names=re.findall(r'[A-Z][a-z]+',data)
print(names)


data='reddysubbu039@gmail.com'
result=re.match(r'\w+@\w+.\w*',data)
print(result.group())
 
# sub

data='iam software engineer'
result=re.sub(r'engineer','testing automation',data)
print(result)

