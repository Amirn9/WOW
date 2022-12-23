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

# Define the main function
def main():
  # Get the input from the user
  num1 = float(input("Enter the first number: "))
  operator = input("Enter an operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  # Calculate the result and print it to the console
  result = calculate(num1, operator, num2)
  print(result)

# Run the main function
main()
