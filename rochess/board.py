from typing import TypeAlias


Square: TypeAlias = int
Piece: TypeAlias = str


class Board:
    BLOCKED_SQUARE: Piece = '-'
    COLUMN_NAMES = 'abcdefghijklmnopqrstuvwxyz'
    EMPTY_SQUARE: Piece = '.'


    def __init__(self, number_of_rows: int, number_of_columns: int) -> None:
        self.number_of_rows: int = number_of_rows
        self.number_of_columns: int = number_of_columns
        self.squares: list[Square] = []
        self.reset_squares()


    def get_piece(self, column: int, row: int) -> Piece:
        index: int = (self.number_of_rows - row) * self.number_of_columns * 2 + column - 1
        return self.squares[index]


    def get_piece_alg(self, algebraic_coordinate: str) -> Piece:
        column: int = self.COLUMN_NAMES.index(algebraic_coordinate[0]) + 1
        row: int = int(algebraic_coordinate[1])
        return self.get_piece(column, row)


    def reset_squares(self) -> None:
        self.squares = []
        for _ in range(self.number_of_rows):
            self.squares.extend([self.EMPTY_SQUARE] * self.number_of_columns)
            self.squares.extend([self.BLOCKED_SQUARE] * self.number_of_columns)


    def set_piece(self, column: int, row: int, piece: Piece) -> None:
        index: int = (self.number_of_rows - row) * self.number_of_columns * 2 + column - 1
        self.squares[index] = piece


    def set_piece_alg(self, algebraic_coordinate: str, piece: Piece) -> None:
        column: int = self.COLUMN_NAMES.index(algebraic_coordinate[0]) + 1
        row: int = int(algebraic_coordinate[1])
        self.set_piece(column, row, piece)
