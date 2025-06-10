a= "1"
b= "2"
print (int(a) + int(b))

# explicit typecasting
string="123"
numbers = 7
string_number = int(string)
sum = numbers + string_number
print(" the sum of both numbers is :", sum)



# implicit typecasting
a= 20 #py. converts a to int automatically 
print (type(a))
b= 10.0 #py. converts b to float automatically
print (type(b))
c=a+b 
print (c) #py converts c to float as it is the float addition
print(type(c))