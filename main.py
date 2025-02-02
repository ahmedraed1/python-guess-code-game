import random


COLORS = ["R" , "G" , "B" , "Y" , "W" , "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code


def guess_code():
    while True:
        guess = input("Enter your guess: ").upper().split(" ")
    
        if len(guess) != CODE_LENGTH:
            print("Invalid guess. Try again.")
            continue
            
    
        for color in guess:
            if color not in COLORS:
                print("Invalid guess. Try again.")
                break
        else:
            break
        
    return guess

def check_code(guess, real_code):
        color_count = {}
        correct_pos = 0
        incorrect_pos = 0
        
        for color in real_code:
            if color not in color_count:
                color_count[color] = 0
            color_count[color] += 1
            
            
        for guess_color , real_color in zip(guess , real_code): 
            if guess_color == real_color:
                correct_pos += 1
                color_count[guess_color] -= 1
                
        for guess_color , real_color in zip(guess , real_code):
            if guess_color in color_count and color_count[guess_color] > 0:
                incorrect_pos += 1
                color_count[guess_color] -= 1
                
        return correct_pos , incorrect_pos 

def game():
    print(f"Welcome to Mastermind. The code has been generated. You have {TRIES} attempts to guess it.")
    print("The Valid colors are:", " ".join(COLORS))
    code = generate_code()
    for attempts in range(1 , TRIES + 1):
        guess = guess_code()
        correct_pos , incorrect_pos = check_code(guess , code)
        
        print(f"{correct_pos} correct position(s) and {incorrect_pos} incorrect position(s).")
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} attempt(s).")
            break
    else:
        print("You ran out of attempts. The code was", " ".join(code))
        
        
if __name__ == "__main__":
    game()