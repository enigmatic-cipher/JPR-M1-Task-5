"""
Given n as input, print Grade A if n is between 90 and 100, Grade B if it is between 75 and 90, Grade C if it is between 50 and 75 and Grade D otherwise.
"""

n = int(input("Enter Number: "))
if(n>=90 and n<=100):
  print("Grade A")
elif(n>=75 and n<90):
  print("Grade B")
elif(n>=50 and n<75):
  print("Grade C")
else:
  print("Grade D")