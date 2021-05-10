#This is program that adds the digits in a 2 digit number. e.g. if the input is 70 the output would be 7 

numbers = input("Type in a two digit number \n")

#because the string is an array you can take the first two elements of it 
#you will have to cast the chars from the string into int for the program to work.
number_one = int(numbers[0])
number_two = int(numbers[1])

#holds the sum of the two numbers
sum = number_one + number_two

#you have to cast the "sum" back into a string for everything to work. 
print("Your sum is " + str(sum) + "\n"
)