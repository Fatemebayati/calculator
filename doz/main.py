import tkinter as tk
from tkinter import messagebox

class tictoctoeGUI:
    def __init__(self,board_size=3):
        self.board_size=board_size
        self.window=tk.Tk()
        self.window.title("Tic Toc Toe")
        self.board=[[' ' for _ in range (self.board_size)]for _ in range (self.board_size)]
        self.current_player='X'
        self.create_board_buttons()

    # def create_board_buttons(self):
    #     self.buttons=[[tk.Button(self.window,text=' ',width=3,height=1,
    #                              command=lambda row=row , col=col:self.make_move(row,col))for col in range(self.board_size)
    #                              for row in range(self.board_size)]]
    #     for row in range(self.board_size):
    #         for col in range(self.board_size):
    #             self.buttons[row][col].grid(row=row , column=col)

    def create_board_buttons(self):
        self.buttons = []  # ایجاد لیست اصلی دکمه‌ها
        for row in range(self.board_size):
            row_buttons = []
            for col in range(self.board_size):
                button = tk.Button(
                    self.window,
                    text=' ',
                    width=3,
                    height=1,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)


    def make_move(self,row,col):
        if self.board[row][col]==' ':
            self.board[row][col]=self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(self.current_player):
                messagebox.showinfo(f"player{self.current_player}wins!")
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo("its a tie!")
                self.reset_game()
            else:
                self.current_player='O' if self.current_player=='X' else 'X'
        else:
            messagebox.showerror("invalid move,try egain")

    def check_win(self,player):
        for i in range(self.board_size):
            if all(self.board[i][j]==player for j in range(self.board_size) or all(self.board[j][i]==player for j in range(self.board_size))):
                return True
        return all(self.board[i][i]==player for i in range(self.board_size) or all(self.board[i][self.board_size-1 -i]==player for i in range(self.board_size)))

    def is_full(self):
        return all(all(cell !=' ' for cell in row)for row in self.board)

    def reset_game(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.board[row][col]=' '
                self.buttons[row][col].config(text=' ')
        self.current_player='X'

    def run(self):
        self.window.mainloop()
if __name__=='__main__':
    board_size=int(input("enter the size of the board(e.g.,3 for 3x3 ,4 for 4x4,etc):"))
    tic_tac_toe=tictoctoeGUI(board_size)
    tic_tac_toe.run()
