from random import choice
import time
def get_dictionary(file):
    dictionary = {}
    with open(file) as whole_dictionary:
        lines = whole_dictionary.readlines()
        del lines[:lines.index("-START-\n")+1]
        del lines[lines.index("-END-\n"):]
        for line in lines:
            line.rstrip()
            index = line.index(" ")
            word = line[0:index]
            definition = line[index:].strip()
            dictionary[word] = definition
    print(dictionary)
    return dictionary

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
    print("The rules are simple:")
    print("You have 60 seconds to type as many words as you can find")
    print("""3 letter words and shorter are worth 1 point,
        while longer words are worth 1 extra point per letter over 3""")
    width = 5
    board = make_board(width)
    # scrabble_dictionary = get_dictionary("scrabble_dict.txt")
    user_word_set = set()
    now = time.time()
    end = now + 30
    score = 0
    print("The game is about to start")
    time.sleep(2)
    print("You have 60 seconds, starting...")
    time.sleep(1)
    print("NOW!")

    while time.time() < end:
        user_word_set.add(input("> ").upper())
    # for word in user_word_set:
    #     if word not in scrabble_dictionary:
    #         print(f"{word} not in dictionary")
    #         user_word_set.remove(word)

    for word in user_word_set:
        if find(board, word):
            if len(word) <= 3:
                score += 1
            else:
                score += len(word)-3
        else:
            print(f"{word} is not on the board")

    print(f"your score is:{score}")

play_game_singleplayer()