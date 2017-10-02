# Εχουμε τέσσερις περιπτώσεις n>0,m>0 || n<0,m<0 || n>0,m<0 || n<0,m>0. Παραδείγματα:
# n=2,m=10 sum = 2+4+6+8+10 = 30
# n=-2,m=-10 sum = -2-4-6-8-10 = -30
# n=-2,m=10 sum =-2+0+2+4+6+8+10 = 28
# n=2,m=-10 sum = 2+0-2-4-6-8-10 = -28



print("Please input two integers m,n")

while True:
  try:
    m = int(input("Please enter m: "))
  except ValueError:
    print("Invalid Input")
    continue
  break	
  
while True:
  try:
    n = int(input("Please enter n: "))
  except ValueError:
    print("Invalid Input")
    continue
  break

absolute_n = abs(n)
absolute_m = abs(m)
  
sum = 0
multiple_of_n = absolute_n
i=1

if(n != 0 and m != 0 ):
  while (multiple_of_n <= absolute_m): 
    sum = sum + multiple_of_n
    i+=1
    print(multiple_of_n)
    multiple_of_n = i*absolute_n
elif(n == 0):
  sum = 0
else:
  sum = n


if( n < 0 and m < 0): sum = -sum
if( n > 0 and m < 0): sum = -sum + n
if( n < 0 and m > 0): sum =  sum + n
  

  
  
print("Sum of n's multiples until m = " , sum);
  
