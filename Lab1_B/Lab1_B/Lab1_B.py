#cookToCode
#Lab 1_B SE116.51 

#Warning This Program is not perfect and is able to crash | The logic also isn't great FEEL FREE to change and update

#This is a program to determine the selling price of a set 
#cost item and set percent upsale

#   -cost, the cost of an item
#   -margin, the percent of the upcharge
#   -selling_price, the final price for the item


#This is another way to set the variables by asking the user to input the values
#The value given by the user is saved as a string, then, the string is converted to a float data type
#For the variable margin, the string is converted to int

cost = float(input("How much does the item cost "))     #<----This is how you use an imput statement
margin =int(input("What percent do you want to upsale this for "))

justAString = input("This is how you ask the user for an value and then this program will spit it out\nType something\t:")
#The \n = a new line and \t = a tab key | the \ is called an escape key, the letter after the \ tells the computer to do something
print(justAString)

#the math for finding the selling price 
selling_price = (1/(1-margin/100))*cost

#printing out the final "selling_price"
print("The final price will be $",selling_price)

