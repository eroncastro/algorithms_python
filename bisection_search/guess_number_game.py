print('Please think of a number between 0 and 100!')

high = 100
low = 0

while True:
    if high == low:
        high = 100
        low = 0

    ans = (high + low) // 2

    print('Is your secret number', ans, '?')
    answer = input("Enter 'h' to indicate the guess is too high. " \
                   "Enter 'l' to indicate the guess is too low. " \
                   "Enter 'c' to indicate I guessed correctly. ")

    if answer == 'c':
        break
    elif answer == 'h':
        high = ans
    elif answer == 'l':
        low = ans
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was:', ans)