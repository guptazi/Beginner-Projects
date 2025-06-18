import random


def main():
    target = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    while True:
        guess = input("Guess a number between 1 and 100 (or 'q' to quit): ")
        if guess.lower() == 'q':
            print("Goodbye!")
            break
        try:
            guess_num = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1
        if guess_num < target:
            print("Too low!")
        elif guess_num > target:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


if __name__ == '__main__':
    main()
