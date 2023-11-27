total_even_number=0
total_odd_number =0
for number in range(1,101):
	if (number%2==0):
 		total_even_number +=1
	elif(number%2!=0):
		total_odd_number +=1

print("total even number is: ",total_even_number)

print("total odd number is: ",total_odd_number)
