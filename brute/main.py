### This brute force app is for educational purposes only and should not be used to do anything illegal 
import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'
        
def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'

   


def main():
    print('Searching...')
    password: str = input("enter a password to check: ")

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        for i in range(3, 6):
            if cracked := brute_force(password, length=i, digits=True, symbols=True):
                print(cracked)
                break
            else: 
                print("There was no match....")

    end_time: float = time.perf_counter()
    print(f'Time taken: {round(end_time - start_time, 2)}s')

if __name__ == '__main__':
    main()