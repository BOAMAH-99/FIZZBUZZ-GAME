#game_value represent each value in the range from 1-1000

for game_character in range(1,1001):
    if game_character % 15 == 0:
        print("Fizzbuzz")
    elif game_character % 5 == 0:
        print("Buzz")
    elif game_character % 3 == 0:
        print("Fizz")
    else:
        (print(game_character))
