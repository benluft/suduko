class Square:

    def __init__(self, row, col, actual_value=None):
        if 1 <= row <= 9:
            self.row = row
        else:
            raise BaseException("Row invalid")
        if 1 <= col <= 9:
            self.col = col
        else:
            raise BaseException("Col invalid")
        if actual_value is None:
            self.potential_values = list(range(1, 10))
        elif 1 <= actual_value <= 9:
            self.potential_values = [actual_value]
        else:
            raise BaseException("Actual value invalid")
        self.cube = ((row - 1) // 3) * 3 + ((col - 1) // 3 % 3) + 1

    def set_value(self, value):
        self.potential_values = [value]

    def clear_value(self):
        self.potential_values = list(range(1,10))
