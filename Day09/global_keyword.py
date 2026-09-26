count = 10

def change():
    global count
    count = 20

change()

print(count)


# Without global:-
count = 10

def change():
    count = 20

change()

print(count)



# Why global Can Be Dangerous ⚠️
balance = 1000

def withdraw(amount):
    global balance
    balance -= amount



# For small programs it's okay to understand global, but in real projects you should generally prefer:_
# def withdraw(balance, amount):
#     return balance - amount

# Then:-
# balance = 1000
# balance = withdraw(balance, 200)
# print(balance)



