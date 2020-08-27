from unittest import TestCase
from suduko.square import Square
from suduko.group import Group

class TestGroup(TestCase):

    square_list_1 = [
        Square(1, 1, 1),
        Square(1, 2, 2),
        Square(1, 3, 3),
        Square(1, 4, 4),
        Square(1, 5, 5),
        Square(1, 6, 6),
        Square(1, 7, 7),
        Square(1, 8, 8),
        Square(1, 9),
    ]

    square_list_2 = [
        Square(1, 1, 9),
        Square(1, 2, 8),
        Square(1, 3, 4),
        Square(2, 1, 6),
        Square(2, 2, 1),
        Square(2, 3),
        Square(3, 1, 2),
        Square(3, 2, 5),
        Square(3, 3, 7)

    ]

    group1 = Group(square_list_1)
    group2 = Group(square_list_2)

    def test_solve(self):
        self.group1.solve()
        for square in self.group1.squares_list:
            if square.col == 9:
                assert square.potential_values[0] == 9
        self.group2.solve()
        for square in self.group2.squares_list:
            if square.row == 2 and square.col == 3:
                assert square.potential_values[0] == 3

