# Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit.


temp = int(input("Enter the temperature"))
unit = input("Please Enter C or c for Celsius and F or f for Fahrenheit")
if unit== 'C' or unit =='c':
    print("Temperature in Celsius ", ((5*(temp-32))/9))
else :
    print("Temperature in Fahrenheit ", ((9*temp)/5)+32)
