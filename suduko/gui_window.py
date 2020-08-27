import tkinter as tk
from suduko.board import Board


class GuiWindow:
    def __init__(self, master):
        self.solving = False
        self.master = master
        self.master.resizable(0, 0)
        self.largeFrame = tk.Frame(self.master)
        master.title("Suduko Solver")
        self.largeFrame.pack(fill='both', expand=True)
        self.largeFrame.grid_rowconfigure(0, weight=1)
        cell_frame = tk.Frame(self.largeFrame)
        cell_frame.pack(fill='y', expand=True)

        self.board = Board()
        real_row = 0
        self.entry_string_vars = []
        self.svs = []
        for row in range(11):
            if row != 3 and row != 7:
                real_row += 1
            real_col = 0
            for col in range(11):
                if row == 3 or row == 7 or col == 3 or col == 7:
                    tk.Label(cell_frame).grid(row=row, column=col)
                else:
                    real_col += 1
                    cell_num = real_col + (real_row-1)*9-1
                    sv = tk.StringVar(name=str(cell_num))
                    sv.trace('w', self.callback_cell_changed)
                    self.svs.append(sv)
                    entry = tk.Entry(cell_frame,
                                     justify='center',
                                     width=3,
                                     validate='key',
                                     textvariable=sv,
                                     vcmd=(self.master.register(self.validate), '%P'))
                    entry.grid(row=row, column=col)
                    self.entry_string_vars.append(entry)
        self.clear_button = tk.Button(self.largeFrame, text='Clear', command = self.callback_clear_button)
        self.clear_button.pack(side='bottom')
        self.solve_button = tk.Button(self.largeFrame, text='Solve', command=self.callback_solve_button)
        self.solve_button.pack(side='bottom')

    def validate(self, P):
        if not str.isdigit(P):
            if P != '':
                return False
            else:
                return True
        else:
            if int(P) > 9 or int(P) < 0:
                return False
        return True

    def callback_cell_changed(self, *args):
        cell_value = self.entry_string_vars[int(args[0])].get()
        if self.solving:
            return
        elif cell_value != '':
            self.board.set_square(int(args[0]), int(cell_value))
        else:
            self.board.clear_square(int(args[0]))

    def callback_solve_button(self):
        self.solving = True
        self.board.solve_groups()
        self.board.display_board()
        for index, cell in enumerate(self.board.all_squares):
            self.entry_string_vars[index].delete(0, tk.END)
            self.entry_string_vars[index].insert(0, str(cell.potential_values[0]))
        self.board.display_board()
        self.solving = False
        print("Solved")

    def callback_clear_button(self):
        self.board = Board()
        for entry in self.entry_string_vars:
            entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    window = GuiWindow(root)
    root.mainloop()
