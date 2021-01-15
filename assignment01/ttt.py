import numpy as np

class TicTacToe():
    def __init__(self):
        # create board
        self.board = np.zeros((3,3), dtype=int)
        self.x_turn = True # X will go first
        
        # blank = 0
        # X = 1
        # O = 2

    def print_board(self):
        print("\n")
        for r in self.board:
            for slot in r.tolist():
                if slot == 0:
                    print("_",end=" ")
                elif slot == 1:
                    print("X",end=" ")
                elif slot == 2:
                    print("O",end=" ")
            print("\n")

    def turn(self):
        self.print_board()

        print("X" if self.x_turn else "O","'s turn")
        selected_slot = input("Pick a slot [0-8]: ")

        if selected_slot is "":
            self.turn()
            return
        else: selected_slot = int(selected_slot)

        if selected_slot < 0 or selected_slot > 8:
            print("\n[!] Invalid spot! Please choose again.")
            self.turn()
            return
        
        # idk if there's a better way to do this
        if selected_slot == 0:
            selected_table_slot = (1,1)
        elif selected_slot == 1:
            selected_table_slot = (0,0)
        elif selected_slot == 2:
            selected_table_slot = (0,1)
        elif selected_slot == 3:
            selected_table_slot = (0,2)
        elif selected_slot == 4:
            selected_table_slot = (1,2)
        elif selected_slot == 5:
            selected_table_slot = (2,2)
        elif selected_slot == 6:
            selected_table_slot = (2,1)
        elif selected_slot == 7:
            selected_table_slot = (2,0)
        elif selected_slot == 8:
            selected_table_slot = (1,0)

        if self.board[selected_table_slot] == 0:
            self.board[selected_table_slot] = (1 if self.x_turn else 2)
        else:
            print("\n[!] Space already taken! Please choose again.")
            self.turn()
            return

        self.print_board()
        if not self.check_win():
            self.x_turn = not self.x_turn
            self.turn()

    def check_win(self):
        # Modify your program to recognize wins/losses/draws and end the game accordingly.

        x_won = False
        o_won = False

        # check horizontal
        for r in self.board:
            if np.all((r == 1)):
                x_won = True
            elif np.all((r == 2)):
                o_won = True

        # check vertical
        for c in self.board.T: # transposed
            if np.all((c == 1)):
                x_won = True
            elif np.all((c == 2)):
                o_won = True

        # check diag (thanks numpy)
        # TL -> BR
        if np.all((np.diag(self.board) == 1)):
            x_won = True
        elif np.all((np.diag(self.board) == 2)):
            o_won = True

        # TR -> BL
        if np.all((np.diag(np.fliplr(self.board)) == 1)):
            x_won = True
        elif np.all((np.diag(np.fliplr(self.board)) == 2)):
            o_won = True

        if x_won:
            self.game_outcome(1)
            return True
        elif o_won:
            self.game_outcome(2)
            return True
        elif np.all((self.board != 0)):
            self.game_outcome(0)
            return True

        return False

    def game_outcome(self, outcome):
        print("-"* 10)
        if outcome == 1:
            print("X won the game!")
        elif outcome == 2:
            print("O won the game!")
        else:
            print("Nobody wins!")


    def start(self):
        self.turn()
        pass
