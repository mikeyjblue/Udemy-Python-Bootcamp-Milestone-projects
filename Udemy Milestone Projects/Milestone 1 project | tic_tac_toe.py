# Milestone project 1 | Tic Tac Toe

import os
# os.system('clear')
from time import gmtime, strftime
curr_time = strftime("%Y-%m-%d %H:%M:%S")



def display_board(board):
    os.system('clear')
    print(f"Here is the current board at {curr_time}: ")
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])




def player_input():
    marker = ''
    marker_dict = {'player1':['',''],'player2':['','']}

    while marker not in ('X','O'):
        marker = input("Player 1: Would you like to be X or O?: ").upper()
    marker_dict['player1'][0] = input("Player 1,what is your name?: ")
    marker_dict['player2'][0] = input("Player 2,what is your name?: ")

    if marker == 'X':
        marker_dict['player1'][1] = 'X'
        marker_dict['player2'][1] = 'O'
        return ('X','O'), marker_dict

        
    else:
        marker_dict['player1'][1] = 'O'
        marker_dict['player2'][1] = 'X'
        return ('O','X'), marker_dict
    
    
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[3]==mark and board[5]==mark and board[7]==mark))

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
   position = 0
   while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
       position = int(input('Choose your next position (1-9):  '))
   return position

def replay():
    play_again = ''
    while play_again not in ('Y','N'):
        play_again = input('Play again? (Y/N): ').upper()
    return play_again == 'Y'

os.system('clear')
print('Welcome to Tic Tac Toe!')
    
while True:
    #reset the board
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_input_output = player_input()
    player1_marker,player2_marker = player_input_output[0]
    players_dict = player_input_output[1]
    turn = choose_first()
    print(players_dict[turn][0] + ' will go first')
    
    play_game = input('Are you ready to play? Enter Y or N: ')

    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
            #Player 1 Turn
            if turn == 'player1':
                display_board(game_board)
                print("It's "+players_dict[turn][0]+"'s turn ...")
                position = player_choice(game_board)
                place_marker(game_board,player1_marker,position)

                if win_check(game_board,player1_marker):
                    display_board(game_board)
                    print('Congratulations '+players_dict[turn][0]+'! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'player2'
            else:
                 # Player2's turn. 
                display_board(game_board)
                print("It's "+players_dict[turn][0]+"'s turn ...")
                position = player_choice(game_board)
                place_marker(game_board,player2_marker,position)

                if win_check(game_board,player2_marker):
                    display_board(game_board)
                    print('Congratulations '+players_dict[turn][0]+'! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'player1'
    if not replay():
        break
                

       
    



    
    
      


