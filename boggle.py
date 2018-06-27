from random import choice
import time
import twl
# def get_dictionary(file):
#     dictionary = {}
#     with open(file) as whole_dictionary:
#         lines = whole_dictionary.readlines()
#         del lines[:lines.index("-START-\n")+1]
#         del lines[lines.index("-END-\n"):]
#         for line in lines:
#             line.rstrip()
#             index = line.index(" ")
#             word = line[0:index]
#             definition = line[index:].strip()
#             dictionary[word] = definition
#     print(dictionary)
#     return dictionary

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
        print_board = "   ".join(board[i])
        for i in range(len(print_board)):
            if print_board[i] == "Q":
                print_board = print_board[:i+1] + "u" + print_board[i+2:]
        print(print_board)


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
        elif board[x][y] == word[0] and (x, y) not in used_set:
            if word[0:2] == "QU":
                if len(word) == 2:
                    return True
                else:
                    used_set.add(position)
                    neighbor_list = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), 
                                     (x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]
                    for i in range(len(neighbor_list)):
                        if neighbor_list[i] not in used_set:
                            if check_next(neighbor_list[i], word[2:]) is True:
                                return True
                        i += 1

                    else:
                        used_set.remove(position)
                        return False
            
            elif len(word) == 1:
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
    print()
    print("WELCOME TO BOGGLE SOLITARE!")
    print()
    print("The rules are simple:")
    print("You have limited to type as many words as you can find.")
    print("you can go in any direction, but you can't use the same letter twice.")
    print("3 letter words and shorter are worth 1 point, ",
          "while longer words are worth 1 extra point per letter over 3")
    print("'Qu' can count as Q or QU in words.")
    print()
    length = input("How many seconds do you want for guessing? > " )
    try:
        length = int(length)
    except ValueError:
        print("You failed to enter a valid number, default is 60 seconds")
        length = 60
    else:
        if length < 0:
            print("You failed to enter a valid number, default is 60 seconds")
            length = 60

    user_word_set = set()
    now = time.time()
    end = now + length
    score = 0

    print(f"You have {length} seconds, starting...")
    time.sleep(2)
    print("NOW!")

    board = make_board(5)
    

    while time.time() < end:
        user_word_set.add(input("> ").upper())
    print("STOP")
    time.sleep(1)
    for word in list(user_word_set):
        if twl.check(word.lower()) is False:
            print(f"{word} not in dictionary")
            user_word_set.remove(word)

    
    
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