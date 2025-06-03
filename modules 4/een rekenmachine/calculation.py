from function import addition, subtraction, multiplication, division

calculations = {
    "add": lambda x, y: addition(x, y),
    "subtract": lambda x, y: subtraction(x, y),
    "multiply": lambda x, y: multiplication(x, y),
    "divide": lambda x, y: division(x, y)
}