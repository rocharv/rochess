type Piece = str
type Square = int


class Board:
    """
    A class to represent a rectangular board with pieces.

    Attributes
    ----------
    number_of_rows : int
        The number of rows in the board.
    number_of_columns : int
        The number of columns in the board.
    piece_squares : set[Square]
        The set of squares that contain a piece.
    squares : list[Piece]
        The squares of the board, stored in a one-dimensional list that
        represents a mailbox offset (0x88). Reference:
        https://www.chessprogramming.org/Mailbox
    """
    BLOCKED_SQUARE: Piece = "-"
    COLUMN_NAMES = "abcdefghijklmnopqrstuvwxyz"
    EMPTY_SQUARE: Piece = "."


    def __init__(self,
                 number_of_rows: int,
                 number_of_columns: int,
                 piece_symbols: dict = {}) -> None:
        self.number_of_columns: int = number_of_columns
        self.number_of_rows: int = number_of_rows
        self.piece_squares: set[Square] = set()
        self.piece_symbols = piece_symbols
        self.squares: list[Piece] = []
        self.reset_squares()


    def get_algebraic_coordinate(self, square: Square) -> str:
        """
        Returns the algebraic coordinate of the square.

        Parameters
        ----------
        square : Square
            The square to get the algebraic coordinate from.
        """
        column: int = self.get_column(square)
        row: int = self.get_row(square)
        return f"{self.COLUMN_NAMES[column - 1]}{row}"


    def get_column(self, square: Square) -> int:
        """
        Returns the column of the square.

        Parameters
        ----------
        square : Square
            The square to get the column from.
        """
        return square % (self.number_of_columns * 2) + 1


    def get_piece(self, square: Square) -> Piece:
        """
        Returns the piece at the specified square.

        Parameters
        ----------
        square : Square
            The square to get the piece from.
        """
        return self.squares[square]


    def get_piece_from_coords(self, column: int, row: int) -> Piece:
        """
        Returns the piece at the specified column and row.

        Parameters
        ----------
        column : int
            The column of the piece.
        row : int
            The row of the piece.
        """
        index: int = ((self.number_of_rows - row)
                      * self.number_of_columns * 2 + column - 1)
        return self.squares[index]


    def get_piece_from_algebraic(self, algebraic_coordinate: str) -> Piece:
        """
        Returns the piece at the specified algebraic coordinate.

        Parameters
        ----------
        algebraic_coordinate : str
            The algebraic coordinate of the piece.
        """
        column: int = (
            self.COLUMN_NAMES.index(algebraic_coordinate[0]) + 1
        )
        row: int = int(algebraic_coordinate[1])
        return self.get_piece_from_coords(column, row)


    def get_row(self, square: Square) -> int:
        """
        Returns the row of the square.

        Parameters
        ----------
        square : Square
            The square to get the row from.
        """
        return self.number_of_rows - (square
                                      // (self.number_of_columns * 2))


    def get_square_from_algebraic(self, algebraic_coordinate: str) -> Square:
        """
        Returns the square corresponding to the algebraic coordinate.

        Parameters
        ----------
        algebraic_coordinate : str
            The algebraic coordinate of the square.
        """
        column: int = (
            self.COLUMN_NAMES.index(algebraic_coordinate[0]) + 1
        )
        row: int = int(algebraic_coordinate[1])
        return ((self.number_of_rows - row)
                * self.number_of_columns * 2 + column - 1)


    def get_square_from_coord(self, column: int, row: int) -> Square:
        """
        Returns the square corresponding for the pair column and row.

        Parameters
        ----------
        column : int
            The column of the square.
        row : int
            The row of the square.
        """
        return ((self.number_of_rows - row)
                * self.number_of_columns * 2 + column - 1)


    def reset_squares(self) -> None:
        """
        Resets the squares of the board to empty squares and also clears
        the piece_squares set.
        """
        self.piece_squares.clear()
        self.squares = []
        for _ in range(self.number_of_rows):
            self.squares.extend(
                [self.EMPTY_SQUARE] * self.number_of_columns
            )
            self.squares.extend(
                [self.BLOCKED_SQUARE] * self.number_of_columns
            )


    def set_piece(self, square: Square, piece: Piece) -> None:
        """
        Sets the piece at the specified square.

        Parameters
        ----------
        square : Square
            The square to set the piece.
        piece : Piece
            The piece to set.
        """
        self.squares[square] = piece
        if piece != self.EMPTY_SQUARE:
            self.piece_squares.add(square)
        else:
            self.piece_squares.discard(square)


    def set_piece_from_coords(self,
                              column: int, row: int, piece: Piece) -> None:
        """
        Sets the piece from coordinates, column and row.

        Parameters
        ----------
        column : int
            The column of the piece.
        row : int
            The row of the piece.
        piece : Piece
            The piece to set.
        """
        square: Square = ((self.number_of_rows - row)
                          * self.number_of_columns * 2 + column - 1)
        self.set_piece(square, piece)


    def set_piece_from_algebraic(self,
                      algebraic_coordinate: str,
                      piece: Piece) -> None:
        """
        Sets the piece at the specified algebraic coordinate.

        Parameters
        ----------
        algebraic_coordinate : str
            The algebraic coordinate of the piece.
        piece : Piece
            The piece to set.
        """
        column: int = (
            self.COLUMN_NAMES.index(algebraic_coordinate[0]) + 1
        )
        row: int = int(algebraic_coordinate[1])
        self.set_piece_from_coords(column, row, piece)


    def show(self,
             show_coordinates = True,
             is_symbolic:bool = False) -> None:
        """
        Prints the board to the console.

        Parameters
        ----------
        show_coordinates : bool
            If True, the coordinates will be printed.
        is_symbolic : bool
            If True, the pieces will be printed as symbols.
        """
        files: int = self.number_of_columns
        rank: int = self.number_of_rows
        for square, piece in enumerate(self.squares):
            if square % (self.number_of_columns * 2 - 1) == 0:
                print()
                if show_coordinates and rank > 0:
                    print(f"{rank}", end="| ")
                    rank -= 1
            if (square % (self.number_of_columns * 2)
                < self.number_of_columns):
                if is_symbolic:
                    print(self.piece_symbols[piece], end=" ")
                else:
                    print(piece, end=" ")
        if show_coordinates:
            print(end="  ")
            print("-" * (files*2))
            print(end="   ")
            for file in range(files):
                print(f"{self.COLUMN_NAMES[file]}", end=" ")
            print()
