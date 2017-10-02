
sums_of_sheep = []
j=1

while True:

  print("Please input sheep counted this night " , j ," or -1 to stop :")
  try:
    sheep_countings = [int(x) for x in input().replace(',' , ' ').split()]
  except ValueError:
    print("Invalid Input")
    continue;
  
  if(sheep_countings[0] == -1):
    del sheep_countings[:]
    break

  isNegative = False
  i = 0
  
  for x in sheep_countings:
    if(sheep_countings[i] < 0):
      isNegative = True
      print("Invalid Input")
      break
      del sheep_countings[:]
    i+=1

  if(isNegative):
    continue
          
  sum = 0
  i = 0
  
  for x in sheep_countings:	
      sum = sum + sheep_countings[i]
      i+=1
	
  sums_of_sheep.append(sum)
  j+=1
  
i=0

maximum = sums_of_sheep[0]
for x in sums_of_sheep:
  print("Night " , i , " sum = " , sums_of_sheep[i])
  if(maximum < sums_of_sheep[i]):
    maximum = sums_of_sheep[i]
  i+=1
  
  

while True:

  try:
    total_number_of_sheep = int(input("Please enter your total number of sheep:"))
  except ValueError:
    print("Invalid Input")
    continue
  if(total_number_of_sheep < maximum):
    print("Invalid input. Your total number of sheep is at least "+str(maximum)+" which is the biggest number of sheep counted one night.")
    continue

  break

missing_sheep = total_number_of_sheep - sums_of_sheep[j-2]
print("Number of missing sheep the last night is " , missing_sheep)

