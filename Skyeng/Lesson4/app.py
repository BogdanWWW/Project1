


prompt = "Hey what is ur name and famiely name?";
x = input(prompt)
y = x*10

def has_space(message):
    return " " in message

user_input = input("Enter a message: ")

if has_space(user_input):
    print("Thank you for thath information.")
else:
    print("You need to write youre full name!")

counter = 0
for c in "educative":
    counter+=1
print (counter)
