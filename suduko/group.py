class Group:
    """
    squares_list: list of squares
    """
    def __init__(self, squares_list=None, group_type=None):
        if squares_list is None:
            squares_list = list()
        self.squares_list = squares_list
        if group_type is None and group_type != 'col' and group_type != 'row' and group_type != 'cube':
            raise Exception("Type must be col, row, or cube")
        else:
            self.group_type = group_type

    def add_square(self, square):
        self.squares_list.append(square)

    def solve(self):

        progress_made = False
        if len(self.squares_list) != 9:
            raise Exception("Trying to solve a group that does not have 9 squares")
        taken_values = set()
        duos = {}
        trios = {}
        for square in self.squares_list:

            if len(square.potential_values) == 1:
                taken_values.add(square.potential_values[0])
        possible_count = {key: [] for key in range(1, 10)}
        for square_index, square in enumerate(self.squares_list):
            if len(square.potential_values) != 1:
                new_potential_values = list(set(square.potential_values).difference(taken_values))
                if square.potential_values != new_potential_values:
                    progress_made = True
                    square.potential_values = new_potential_values
                for value in square.potential_values:
                    possible_count[value].append(square_index)
                if len(square.potential_values) == 2:
                    duos[square_index] = square.potential_values
                if len(square.potential_values) == 3:
                    trios[square_index] = square.potential_values

        for key, indexes in possible_count.items():
            if len(indexes) == 1:
                self.squares_list[indexes[0]].potential_values = [int(key)]
                progress_made = True
                break






        return progress_made

