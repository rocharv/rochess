from fen_parser import set_board_from_fen
from move import get_piece_valid_moves, is_piece_attacking_square
from piece import unicode_symbol


class Board:
    def __init__(self,
                 allow_captures: bool = True,
                 castling_rights: set[str] = ('K', 'Q', 'k', 'q'),
                 en_passant_target: int = -1,
                 from_chars_list: list[str] = [],
                 from_fen_string: str = "",
                 full_move_number: int = 1,
                 half_move_clock: int = 0  ,
                 size: tuple[int, int] = (8, 8),
                 white_turn: bool = True):
        # board states
        self.allow_captures = allow_captures
        self.castling_rights = castling_rights
        self.en_passant_target = en_passant_target
        self.full_move_number = full_move_number
        self.half_move_clock = half_move_clock
        self.size = size
        self.white_turn = white_turn
        self.white_king_square = -1
        self.black_king_square = -1
        '''
        `piece_squares` is a set that stores a pieces' square
        `squares` is list that represents a mailbox offset (0x88)
        https://www.chessprogramming.org/Mailbox
        '''
        self.piece_squares: set[int] = set()
        self.squares: list[str] = []
        # Boarding setup from fen string or chars string
        if from_fen_string:
            set_board_from_fen(self, from_fen_string)
        elif from_chars_list:
            self.set_board_from_chars(from_chars_list)
        else:
            default_fen = (
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
            )
            set_board_from_fen(self, default_fen)
        # Update on board pieces' position
        self.update_piece_squares()


    def get_algebric_from_square(self, square: int) -> str:
        rank = 8 - square // 16
        file = (square % 16) + 1
        return f'{chr(file+96)}{rank}'


    def get_all_valid_moves(self) -> list[tuple[int, int]]:
        valid_moves = []
        for piece_square in self.piece_squares:
            valid_moves.extend(get_piece_valid_moves(self, piece_square))

        return valid_moves


    def get_square_from_algebraic(self, algebraic_coordinate: str) -> int:
        file = ord(algebraic_coordinate[0].lower()) - 96
        rank = int(algebraic_coordinate[1])
        return (8-rank) * 16 + (file-1)


    def is_attacked_square(self, square: int, is_white_ally: bool) -> bool:
        for piece_square in self.piece_squares:
            cpiece = self.squares[piece_square]
            if ((cpiece.isupper() and is_white_ally) or
                (cpiece.islower() and not is_white_ally)):
                continue
            elif is_piece_attacking_square(self, piece_square, square):
                return True
        return False


    def set_board_from_chars(self, chars_list: list[str]) -> None:
        index: int = 0
        total_squares: int = self.size[0] * self.size[1] * 2
        for square in range(total_squares):
            if square & 0x88:
                # off board square
                self.squares.append('o')
            else:
                self.squares.append(chars_list[index])
                index += 1


    def show(self,
             show_coordinates = True,
             show_info = False,
             use_symbols:bool = False) -> None:
        rank: int = self.size[0]
        files: int = self.size[1]
        for square, piece in enumerate(self.squares):
            if square % 15 == 0:
                print()
                if show_coordinates and rank > 0:
                    print(f'{rank}', end="| ")
                    rank -= 1

            if not square & 0x88:
                if use_symbols:
                    print(unicode_symbol[piece], end=" ")
                else:
                    print(piece, end=" ")
        if show_coordinates:
            print(end='  ')
            print("-" * (files*2))
            print(end='   ')
            for file in range(files):
                print(f'{chr(file+65)}', end=' ')
            print()
        if show_info:
            # Turn
            if self.white_turn:
                print('Turn: white')
            else:
                print('Turn: black')
            # Castling rights
            if self.castling_rights:
                print(f'Castling rights: {self.castling_rights}')
            else:
                print('Castling rights: None')
            # En passant target
            if self.en_passant_target != -1:
                print(f'En passant target: {self.en_passant_target}')
            else:
                print('En passant target: None')
            # Half-move clock
            print(f'Half-move clock: {self.half_move_clock}')
            # Full-move number
            print(f'Full-move number: {self.full_move_number}')


    def show_all_valid_moves(self, notation: str = "uci") -> None:
        valid_moves = self.get_all_valid_moves()
        print(f"Valid moves ({len(valid_moves)}):", end=" ")
        for move in valid_moves:
            cpiece = self.squares[move[0]]
            # capture or not move
            if self.squares[move[1]] != '.':
                capture_part = "x"
            else:
                capture_part = ""
            # promotion or not move
            if cpiece in ("P", "p") and (move[1] < 16 or move[1] > 111):
                promotion_part = "=" + move[2]
            else:
                promotion_part = ""
            if notation == "uci":
                from_part = self.get_algebric_from_square(move[0])
                capture_part = ""
                to_part = self.get_algebric_from_square(move[1])
                promotion_part = ""
            elif notation == "algebraic":
                from_part = cpiece + self.get_algebric_from_square(move[0])
                to_part = self.get_algebric_from_square(move[1])
            elif notation == "symbolic":
                from_part = (unicode_symbol[cpiece] +
                             self.get_algebric_from_square(move[0]))
                to_part = self.get_algebric_from_square(move[1])
            print(from_part + capture_part + to_part + promotion_part, end=" ")
        print()


    def update_piece_squares(self):
        for square, piece in enumerate(self.squares):
            if piece != '.' and piece != 'o':
                self.piece_squares.add(square)
                if piece == 'K':
                    self.white_king_square = square
                elif piece == 'k':
                    self.black_king_square = square
