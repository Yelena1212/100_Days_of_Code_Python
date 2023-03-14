from art_calculator import logo

#Calculator

def add(n1, n2):
  return n1 + n2

def substruct(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": substruct,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))

  for symbol in operations:
      print(symbol)

  flag = True
  while(flag):

    operation_symbol = input("Choose the operation: ")
    num2 = float(input("What's the next number? "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
    if continue_calculating == "y":
      num1 = answer
    else:
      flag = False
      calculator()

calculator()
  # if continue_calculating == 'y':
  #   operation_symbol = input("Pick another operation: ")
  #   num3 = int(input("What's the next number? "))
  #   calculation_function = operations[operation_symbol]
  #   second_answer = calculation_function(answer, num3)
  #
  #   print(f"{answer} {operation_symbol} {num3} = {second_answer}")
  # else:
  #   flag = False


# if operation == "+":
#     answer = add(num1, num2)
#     print(f"{num1} {operation} {num2} = {answer}")
# elif operation == "-":
#     answer = substruct(num1, num2)
#     print(f"{num1} {operation} {num2} = {answer}")
# elif operation == "*" :
#     answer = multiply(num1, num2)
#     print(f"{num1} {operation} {num2} = {answer}")
# elif operation == "/":
#     answer = divide(num1, num2)
#     print(f"{num1} {operation} {num2} = {answer}")
# else:
#     print("Chose the correct operator")
