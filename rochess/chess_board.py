from rochess.board import Board
from rochess.chess_pieces import ROYAL_PIECES, UNICODE_SYMBOLS


type Piece = str
type Square = int


class ChessBoard(Board):
    """
    A class that represents a chess board. It inherits from the
    `Board` class.

    Attributes
    ----------
    castling_rights : set[str]
        A set of castling rights.
    en_passant_target : int
        The square that an en passant capture can be made on.
        If set to `-1` it means that there is no en passant capture.
    from_chars_list : list[str]
        Create board from a list of characters that represent the board.
    from_fen_string : str
        Create board from a fen string.
    full_move_number : int
        The number of the full moves.
    half_move_clock : int
        The number of half moves.
    is_white_turn : bool
        If it is white's turn to move
    wnite_king_square : Square
        The square of the white king.
    black_king_square : Square
        The square of the black king.
    """
    def __init__(self,
                 castling_rights: set[str] = ROYAL_PIECES,
                 en_passant_target: str = "",
                 from_char_list: list[str] = [],
                 from_fen_string: str = "",
                 full_move_number: int = 1,
                 half_move_clock: int = 0  ,
                 is_white_turn: bool = True):
        super().__init__(8, 8, UNICODE_SYMBOLS)
        self.castling_rights = castling_rights
        self.en_passant_target = en_passant_target
        self.full_move_number = full_move_number
        self.half_move_clock = half_move_clock
        self.is_white_turn = is_white_turn
        self.black_king_square = -1
        self.white_king_square = -1
        # Boarding setup from fen string or chars string
        if from_fen_string:
            self.set_board_from_fen(from_fen_string)
        elif from_char_list:
            self.set_board_from_chars(from_char_list)
        else:
            default_board: str = (
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
            )
            self.set_board_from_fen(default_board)


    def set_board_from_chars(self, chars_list: list[str]) -> None:
        """
        Sets the chess board based from a list of characters.

        Parameters
        ----------
        chars_list : list[str]
            A list of characters representing the chess board.

        Returns
        -------
        None

        Notes
        -----
        This method iterates over the `char_list` and sets the pieces
        on the chess board accordingly.
        The `char_list` should have a length equal to the number of
        cells on the chess board.
        Each character in the `char_list` represents a piece on the
        chess board.

        Examples
        --------
        >>> board = ChessBoard()
        >>> chars = ["R", "N", "B", "Q", "K", "B", "N", "R",
                     "P", "P", "P", "P", "P", "P", "P", "P",
                     " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ",
                     "p", "p", "p", "p", "p", "p", "p", "p",
                     "r", "n", "b", "q", "k", "b", "n", "r"]
        >>> board.set_board_from_chars(chars)
        """
        rank: int = self.number_of_rows
        file: int = 0
        for char in chars_list:
            file += 1
            self.set_piece_from_coords(file, rank, char)
            # update king square
            if char == "K":
                self.white_king_square = self.get_square_from_coord(file, rank)
            elif char == "k":
                self.black_king_square = self.get_square_from_coord(file, rank)
            # update file and rank
            if file == self.number_of_columns:
                file = 0
                rank -= 1


    def set_board_from_fen(self, fen_string):
        """
        Set the chess board state based on the given FEN
        (Forsyth-Edwards Notation) string.

        Parameters
        ----------
        fen_string : str
            The FEN string representing the chess board state.

        Returns
        -------
        None

        Raises
        ------
        None

        Notes
        -----
        - This method parses the FEN string and sets the chess board
        state accordingly.
        - The FEN string should follow the standard Forsyth-Edwards
        Notation format.

        Examples
        --------
        >>> board = ChessBoard()
        >>> fen = "R6R/3Q4/1Q4Q1/4Q3/2Q4Q/Q4Q2/pp1Q4/kBNN1KB1 w - - 0 1"
        >>> board.set_board_from_fen(fen)
        """
        """
        Set the chess board state based on the given FEN
        (Forsyth-Edwards Notation) string.

        Parameters:
            fen_string (str): The FEN string representing the chess
            board state.

        Returns:
            None

        Raises:
            None

        """
        # FEN parts split by spaces
        fen_parts: list[str] = fen_string.split(" ")
        fen_parts_len: int = len(fen_parts)
        if fen_parts_len < 6:
            fen_offset = -1
        else:
            fen_offset = 0
        # FEN position parsing
        fen_position: str = fen_parts[0]
        rank: int = self.number_of_rows
        file: int = 0
        for char in fen_position:
            if char.isnumeric():
                file  += int(char)
            elif char == "/":
                rank -= 1
                file = 0
            else:
                file += 1
                self.set_piece_from_coords(file, rank, char)
                # update king square
                if char == "K":
                    self.white_king_square = self.get_square_from_coord(file, rank)
                elif char == "k":
                    self.black_king_square = self.get_square_from_coord(file, rank)
        # FEN turn parsing
        fen_turn = fen_parts[1]
        if fen_turn == "w":
            self.is_white_turn = True
        else:
            self.is_white_turn = False
        # FEN castling rights parsing
        self.castling_rights = set()
        if fen_offset == 0:
            fen_castling_rights = fen_parts[2]
            for piece in fen_castling_rights:
                if piece in ROYAL_PIECES:
                    self.castling_rights.add(piece)
        # FEN en passant parsing
        fen_en_passant_target = fen_parts[3 + fen_offset]
        if fen_en_passant_target == "-":
            self.en_passant_target = ""
        else:
            self.en_passant_target = fen_en_passant_target
        # FEN position parsing
        fen_half_move_clock = int(fen_parts[4 + fen_offset])
        self.half_move_clock = fen_half_move_clock
        # FEN position parsing
        fen_full_move_number = int(fen_parts[5 + fen_offset])
        self.full_move_number = fen_full_move_number


    def show_info(self) -> None:
            """
            Display information about the current state of the chess
            board.

            Returns:
                None
            """
            # Turn
            if self.is_white_turn:
                print("Turn: white")
            else:
                print("Turn: black")
            # Castling rights
            if self.castling_rights:
                print(f"Castling rights: {self.castling_rights}")
            else:
                print("Castling rights: None")
            # En passant target
            if self.en_passant_target != "":
                print(f"En passant target: {self.en_passant_target}")
            else:
                print("En passant target: None")
            # Half-move clock
            print(f"Half-move clock: {self.half_move_clock}")
            # Full-move number
            print(f"Full-move number: {self.full_move_number}")
            # Piece squares
            piece_set: list[Square] = sorted(list(
                map(self.get_algebraic_coordinate, self.piece_squares)
            ))
            print(f"Piece squares: {piece_set}")
