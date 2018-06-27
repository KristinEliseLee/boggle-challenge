from random import choice
import time

def make_board(width):
    all_letters = "AAABCDEEEFGHIIIJKLMNNOOOPQRSSTTUUUVWXYZ"
    board = []
    letters_needed = width ** 2
    board_letters = ""
    start = 0
    while len(board_letters) < letters_needed:
        board_letters += choice(all_letters)
    for i in range(width):
        board.append([])
        board[i].extend(board_letters[start: start + width])
        start += width
    for i in range(width):
        print(" ".join(board[i]))

    return board


def find(board, word):
    """Can word be found in board?"""
    used_set = set()


    def check_next(position, word):
        """Checks current position for letter, then recursively checks neighbors.
        If on last letter of word, and position is that letter, returns True.
        """
        x, y = position

        if x < 0 or x > (len(board)-1):
            return False
        elif y < 0 or y > (len(board)-1):
            return False
        elif board[x][y] == word[0].upper() and (x, y) not in used_set:
            if len(word) == 1:
                return True
            else:
                used_set.add(position)
                neighbor_list = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), 
                                 (x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]
                for i in range(len(neighbor_list)):
                    if neighbor_list[i] not in used_set:
                        if check_next(neighbor_list[i], word[1:]) is True:
                            return True
                    i += 1

                else:
                    used_set.remove(position)
                    return False

        return False

    for horizonal in range(len(board)):
        for vertical in range(len(board)):
            position = (horizonal, vertical)
            answer = check_next(position, word)
            if answer is True:
                return True

    return False

def play_game_singleplayer():
    while True:
        width = input("How big do you want the board to be? please give 1 number")
        try:
            width = int(width)
            break
        except ValueError:
            print("Please type a number")

    board = make_board(width)
    user_word_set = set()
    now = time.time()
    end = now + 30
    score = 0
    print("You have 60 seconds, time starts now.")
    while time.time() < end:
        user_word_set.add(input("> "))

    for word in user_word_set:
        word = word.upper()
        if find(board, word):
            score += 1
        else:
            print(f"{word} is not on the board")

    print(f"your score is:{score}")

play_game_singleplayer()