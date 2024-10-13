# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   8.18.1: LAB: Leet speak
# Date:         12 10 2024
#comment
text = input('Enter some text: ')
hold, changed = text.lower(), {'a': '4', 'e': '3', 'o': '0', 's': '5', 't': '7'}
for letters in changed:
    hold = hold.replace(letters, changed[letters])
print(f'In leet speak, "{text}" is:\n{hold}')