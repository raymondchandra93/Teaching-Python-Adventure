import string

# get a list of letters
letters = list(string.ascii_lowercase)

# get letter corresponding to input number
while True:
    answer = input("Enter a number (enter 'stop' to quit): ")
    
    if answer == "stop":
        break
    try:
        index = int(answer) - 1
        print(letters[index])

    except ValueError:
        print("Not a number.")
    except IndexError:
        print("Index out of bounds. (Try numbers 1-26)")