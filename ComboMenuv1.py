'''Iteration 1
 Ask the user for a type of sandwich (chicken $5.25, beef $6.25, tofu $5.75).
 Have the program output the user’s sandwich selection to verify that the program is working correctly.'''

print("Chicken is 1, beef is 2, tofu is 3.")
selection = input("What type of sandwich do you want? Chicken ($5.25), beef ($6.25), or tofu ($5.75)? ")
if selection == "1":
    print("You have selected a chicken sandwich.")
elif selection == "2":
    print("You have selected a beef sandwich.")
elif selection == "3":
    print("You have selected a tofu sandwich.")
