from suduko.square import Square
from suduko.group import Group


class Board:

    def __init__(self):
        self._full_set = set(range(1, 10))
        self.all_squares = []
        self.rows = {i: Group(group_type='row') for i in range(1, 10)}
        self.cols = {i: Group(group_type='col') for i in range(1, 10)}
        self.cubes = {i: Group(group_type='cube') for i in range(1, 10)}
        for row in range(1, 10):
            for col in range(1, 10):
                current_square = Square(row, col)
                self.all_squares.append(current_square)
                self.rows[row].add_square(current_square)
                self.cols[col].add_square(current_square)
                self.cubes[current_square.cube].add_square(current_square)

    def solve_groups(self):
        solved_count = 0
        progress_made = True
        while(solved_count < 81):
            if progress_made is False:
                print("Could not solve. Final result is:\n")
                self.display_board()
                break
            self.display_board()
            progress_made = False
            solved_count = 0
            for row in range(1, 10):
                progress_made |= self.rows[row].solve()
            for col in range(1, 10):
                progress_made |= self.cols[col].solve()
            for cube in range(1, 10):
                progress_made |= self.cubes[cube].solve()
            for square in self.all_squares:
                if len(square.potential_values) == 1:
                    solved_count += 1

    def do_changes(self):
        self.all_squares[3].set_value(6)
        self.all_squares[6].set_value(1)
        self.all_squares[8].set_value(7)
        self.all_squares[9].set_value(6)
        self.all_squares[10].set_value(8)
        self.all_squares[12].set_value(9)
        self.all_squares[13].set_value(5)
        self.all_squares[14].set_value(1)
        self.all_squares[15].set_value(3)
        self.all_squares[20].set_value(3)
        self.all_squares[23].set_value(2)
        self.all_squares[24].set_value(5)
        self.all_squares[25].set_value(6)
        self.all_squares[26].set_value(8)
        self.all_squares[28].set_value(4)
        self.all_squares[30].set_value(8)
        self.all_squares[31].set_value(1)
        self.all_squares[34].set_value(2)
        self.all_squares[42].set_value(8)
        self.all_squares[43].set_value(5)
        self.all_squares[46].set_value(9)
        self.all_squares[49].set_value(6)
        self.all_squares[50].set_value(5)
        self.all_squares[52].set_value(7)
        self.all_squares[53].set_value(3)
        self.all_squares[54].set_value(4)
        self.all_squares[56].set_value(9)
        self.all_squares[59].set_value(3)
        self.all_squares[61].set_value(8)
        self.all_squares[62].set_value(5)
        self.all_squares[63].set_value(1)
        self.all_squares[64].set_value(6)
        self.all_squares[65].set_value(2)
        self.all_squares[68].set_value(9)
        self.all_squares[70].set_value(3)
        self.all_squares[72].set_value(5)
        self.all_squares[75].set_value(7)
        self.all_squares[77].set_value(6)

    def set_square(self, index, value):
        self.all_squares[index].set_value(value)

    def clear_square(self, index):
        self.all_squares[index].clear_value()

    def display_board(self):
        board_string = ""
        counter = -1
        for square in self.all_squares:
            counter += 1
            if counter % 9 == 0:
                board_string += '\n'
            if len(square.potential_values) == 1:
                board_string += str(square.potential_values[0])
                board_string += ' '
            else:
                board_string += 'X '
        print(board_string)


if __name__ == '__main__':
    board = Board()
    board.do_changes()
    board.display_board()
    board.solve_groups()
    board.display_board()

