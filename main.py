import tkinter as tk
import random
from PIL import Image,ImageTk

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

window = tk.Tk()
window.title("Minesweeper")

original_image = Image.open("bomba.png")
resized_image = original_image.resize((10, 8))

mine_image = ImageTk.PhotoImage(resized_image)

board = []

for row in range(rows):
    new_row = []

    for column in range(columns):
        new_row.append(0)

    board.append(new_row)


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

def click_cell(row, column):
    print("clicked cell", row, column)
    if board[row][column] == -1:
        print("MINE!")
        buttons[row][column].config(image=mine_image)
    else:
        number=board[row][column]
        buttons[row][column].config(text=str(number))


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

        button.grid(row=row, column=column)
        row_buttons.append(button)

    buttons.append(row_buttons)


window.mainloop()