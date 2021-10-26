greeting = "Hello,"
name = input()
question = "how is your day?"
# Hello, Dobry, how is your day?
print(greeting + " " + name + ", " + question)
print("%s %s, %s" % (greeting, name, question))
print("Hello, %s, how is your day?" % name)
print(f"{greeting} {name}, {question}")
