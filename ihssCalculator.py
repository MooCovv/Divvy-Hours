#python 3


print('Hours:')
numHours = input()

print('Days:')
numDays = input()

if int(numHours) > 200:
    numHours = int(numHours) / 2
    print('First half of the Month Detected.\nHours used:     ' + str(int(numHours)) + '\n')

num1 = int(numHours) / int(numDays)
numCheck = int(num1) * int(numDays)
numOf2 = int(numHours) - int(numCheck)   
numOf1 = int(numDays) - int(numOf2)
num2 = int(num1) + 1

print('Days x Hours:\n**  ' + str(numOf1) + ' x ' + str(int(num1)) + '  **')

print('**  ' + str(numOf2) + ' x ' + str(num2) + '  **')


