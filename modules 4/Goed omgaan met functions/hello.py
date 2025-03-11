def hello_function(x):
    return "\n".join([f"Hello from function town {i}!" for i in range(1, x + 1)])

x = int(input('voer een getal in: '))
print(hello_function(x))
