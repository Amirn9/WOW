# Define a function to perform the calculation
def calculate(num1, operator, num2):
  # If the operator is '+', return the sum of the numbers
  if operator == '+':
    return num1 + num2
  # If the operator is '-', return the difference of the numbers
  elif operator == '-':
    return num1 - num2
  # If the operator is '*', return the product of the numbers
  elif operator == '*':
    return num1 * num2
  # If the operator is '/', return the quotient of the numbers
  elif operator == '/':
    # Handle the case where num2 is 0 (division by 0 is undefined)
    if num2 == 0:
      return "Cannot divide by 0!"
    return num1 / num2
  # If the operator is not recognized, return an error message
  else:
    return "Invalid operator!"

# Define a function to check if a number is divisible by 7 or contains the digit 7
def seven_boom(num):
  # Convert the number to a string
  num_str = str(num)
  # Check if the number is divisible by 7 or contains the digit 7
  if num % 7 == 0 or '7' in num_str:
    return "7 BOOM!"
  else:
    return num

# Define the main function
def main():
  # Get the input from the user
  num1 = float(input("Enter the first number: "))
  operator = input("Enter an operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  # Calculate the result
  result = calculate(num1, operator, num2)

  # Check if the result is "7 BOOM!" or a regular number
  result = seven_boom(result)

  # Print the result to the console
  print(result)

# Run the main function
main()
