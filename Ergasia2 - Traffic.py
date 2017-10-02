while True:

  print("Please input the list of traffic between 4-8 pm every 10 minutes. 24 integers are expected.(Do not use brackets.)")
  try:
    traffic_countings = [int(x) for x in input().replace(',' , ' ').split()]
  except ValueError:
    print("Invalid Input")
    continue
	
  if( not len(traffic_countings) == 24 ):
    print("The list should be 24 integers. Please input the correct number of countings.")
    continue
   
  break
   
max_traffic = [0,0,0,0]
for i in range(6):
  if(max_traffic[0] < traffic_countings[i]): max_traffic[0] = traffic_countings[i]
  if(max_traffic[1] < traffic_countings[i+6]): max_traffic[1] = traffic_countings[i+6]
  if(max_traffic[2] < traffic_countings[i+12]): max_traffic[2] = traffic_countings[i+12]
  if(max_traffic[3] < traffic_countings[i+18]): max_traffic[3] = traffic_countings[i+18]
   
print("(4:00pm,",max_traffic[0],"), (5:00pm,",max_traffic[1],"), (6:00pm,",max_traffic[2],"), (7:00pm,",max_traffic[3],")")

##Παράδειγμα:
##23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93
##(4:00pm, 45 ), (5:00pm, 65 ), (6:00pm, 89 ), (7:00pm, 93 )
 
	
	
