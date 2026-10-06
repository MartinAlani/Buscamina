import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image,ImageTk




window = tk.Tk()
window.title("Minesweeper")

original_image = Image.open("bomba.png")
resized_image = original_image.resize((10, 8))

mine_image = ImageTk.PhotoImage(resized_image)

flag_original_image = Image.open("bandera.png")
flag_resized_image = flag_original_image.resize((10, 8))

flag_image = ImageTk.PhotoImage(flag_resized_image)

empty_image = Image.new("RGBA", (10, 8), (0,0,0,0))
empty_image = ImageTk.PhotoImage(empty_image)

rows = 5
columns = 5
number_of_mines = 5
directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

board = []

for row in range(rows):
    new_row = []

    for column in range(columns):
        new_row.append(0)

    board.append(new_row)

revealed = []

for row in range(rows):
    new_row = []
    for column in range(columns):
        new_row.append(False)

    revealed.append(new_row)

flagged = []
for row in range(rows):
    new_row = []

    for column in range(columns):
        new_row.append(False)

    flagged.append(new_row)

game_over = False

mines_placed = 0

while mines_placed < number_of_mines:
    mine_row = random.randint(0, rows - 1)
    mine_column = random.randint(0, columns - 1)

    if board[mine_row][mine_column] == 0:
        board[mine_row][mine_column] = -1
        mines_placed += 1


for row in range(rows):
    for column in range(columns):
        if board[row][column] == -1:
            continue

        nearby_mines = 0

        for column_offset, row_offset in directions:
            neighbor_row = row + row_offset
            neighbor_column = column + column_offset

            if 0 <= neighbor_row < rows and 0 <= neighbor_column < columns:
                if board[neighbor_row][neighbor_column] == -1:
                    nearby_mines += 1

        board[row][column] = nearby_mines


for row in board:
    print(row)

def show_mines():
    for row in range(rows):
        for column in range(columns):
            if board[row][column] == -1:
                buttons[row][column].config(image=mine_image)

def reveal_cell(row, column):
    if board[row][column] == -1:
        return

    revealed[row][column] = True

    number = board[row][column]
    buttons[row][column].config(
        image="",
        text=str(number)
    )
    if number == 0:
        for row_offset, column_offset in directions:
            neighbor_row = row + row_offset
            neighbor_column = column + column_offset
            if 0 <= neighbor_row < rows and 0 <= neighbor_column < columns:
                if not revealed[neighbor_row][neighbor_column]:
                    reveal_cell(neighbor_row, neighbor_column)

def check_win():
    for row in range(rows):
        for column in range(columns):

            if board[row][column] == -1:
                continue

            if not revealed[row][column]:
                return False

    return True

def click_cell(row, column):
    global game_over

    print("clicked cell", row, column)

    if game_over:
        return

    if revealed[row][column]:
        return

    if board[row][column] == -1:
        print("MINE")
        buttons[row][column].config(image=mine_image)
        show_mines()
        game_over = True
        messagebox.showinfo("Minesweeper","YOU LOST")
    else:
        reveal_cell(row, column)

        if check_win():
            game_over = True
            messagebox.showinfo("Minesweeper","YOU WIN")

def flag_cell(row, column):
    if game_over:
        return
    if revealed[row][column]:
        return
    if flagged[row][column]:
        flagged[row][column] = False
        buttons[row][column].config(
            image=empty_image,
            text=""
        )
    else:
        flagged[row][column] = True
        buttons[row][column].config(image=flag_image,text="")


buttons = []

for row in range(rows):
    row_buttons = []

    for column in range(columns):
        button = tk.Button(
            window,
            width=18,
            height=9,
            padx=0,
            pady=0,
            command=lambda r=row, c=column: click_cell(r, c),
        )

        button.bind(
            "<Button-3>",
            lambda event,r=row, c=column: flag_cell(r, c)
        )

        button.grid(row=row, column=column)
        row_buttons.append(button)

    buttons.append(row_buttons)


window.mainloop()