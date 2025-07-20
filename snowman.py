import random
import sys


def main():
    print("Welcome to Snowman Meltdown!")
    print()

    snowman_list = [
        "      ___",
        "     /___\\ ",
        "     (o o)",
        "     ( : )",
        "     ( : )"
    ]

    word_list = [
        "Apple", "Chair", "Brick", "Plant", "Smile",
        "Water", "Table", "Dress", "Sharp", "Bread",
        "Cloud", "Flash", "Stone", "Light", "Brush"
    ]

    word = word_list[random.randint(0, len(word_list) - 1)]
    word = word.lower()

    guesses = ''
    turns = len(word)
    guess = ''

    while turns > 0:
        failed = len(word)
        for i in range(turns):
            print(snowman_list[i])
        print()

        print("Word: ", end='')
        for char in word:
            if char in guesses:
                print(char, end='')
                failed -= 1
            else:
                print("_", end='')

        if failed == 0:
            print("\nYou Won!")
            sys.exit()

        print()
        old_guess = guess
        print()
        guess = input("Guess a letter: ")
        guess = guess[-1:]
        guesses += guess

        if old_guess != guess:
            if guess not in word:
                turns -= 1
                print("You have " + str(turns) + " guesses left\n")
                if turns == 0:
                    print(f"\nGame Over! The word was: {word}")


if __name__ == '__main__':
    main()