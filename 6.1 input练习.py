car = input("What kind of car do you want to rent? \n")
print("\nLet me see if I can find you a " + car + ".")

#使用用户输入来填充字典
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which car do you like? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond?(y/n)")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll Result ---")
for name, respond in responses.items():
    print(name.title() + " like " + respond.title() + ".")