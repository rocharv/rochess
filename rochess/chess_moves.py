import chess_pieces as pieces
from typing import TypeAlias
from chess_board import ChessBoard


Square: TypeAlias = int
Piece: TypeAlias = str
# Move is a list of two squares and a piece, in the form
# [from_square, to_square, piece]. The piece is the piece that will be
# on the destination square after the move, this is relevant because of
# pawn promotions.
Move: TypeAlias = list[Square|Piece]


class ChessMoves:
    def __init__(self, chess_board: ChessBoard):
        self.board = chess_board


    def get_board_valid_moves(self) -> list[Move]:
        board_valid_moves: list[Move] = []
        for piece_square in self.board.piece_squares:
            board_valid_moves.extend(
                self.get_piece_valid_moves(piece_square)
            )
        return board_valid_moves


    def get_piece_valid_moves(self,
                              piece_square: Square) -> list[Move]:
        valid_moves: list[Move] = []
        move: Move = []
        new_square: Square = 0
        piece: Piece = self.board.squares[piece_square]
        piece_rank: int = self.board.get_row(piece_square)
        white_ally: bool = True

        # if is not piece's color turn
        if ((piece in pieces.WHITE_PIECES and
             not self.board.is_white_turn) or
            ((piece in pieces.BLACK_PIECES and
              self.board.is_white_turn))):
            return []
        match piece:
            case "P":
                # Single step move, no capture
                new_square = (piece_square
                              + pieces.WHITE_PAWN_SINGLE_STEP_OFFSET)
                move = [piece_square, new_square, piece]
                # No promotion move
                if (piece_rank > 1 and piece_rank < 7 and
                    self.board.squares[new_square]
                    == self.board.EMPTY_SQUARE and
                    self.is_king_safe_after_move(move)):
                    valid_moves.append(move)
                    # Double step move
                    new_square = (
                        piece_square +
                        pieces.WHITE_PAWN_DOUBLE_STEP_OFFSET)
                    move = [piece_square, new_square, piece]
                    if (piece_rank == 2 and
                        self.board.squares[new_square]
                        == self.board.EMPTY_SQUARE and
                        self.is_king_safe_after_move(move)):
                        valid_moves.append(move)
                # Promotion move
                elif (piece_rank == 7 and
                      self.board.squares[new_square]
                      == self.board.EMPTY_SQUARE):
                    for new_piece in pieces.WHITE_PROMOTABLE_PIECES:
                        move = [piece_square, new_square, new_piece]
                        if self.is_king_safe_after_move(move):
                            valid_moves.append(move)
                # Capture move
                for offset in pieces.WHITE_PAWN_CAPTURE_OFFSETS:
                    new_square = piece_square + offset
                    move = [piece_square, new_square, piece]
                    if new_square & 0x88:
                        continue
                    if (self.board.squares[new_square]
                        in pieces.BLACK_CAPTURABLE_PIECES):
                        if (piece_rank > 1 and piece_rank < 7 and
                            self.is_king_safe_after_move(move)):
                            valid_moves.append(move)
                        elif piece_rank == 7:
                            # Promotion with capture moves
                            for new_piece in \
                                pieces.WHITE_PROMOTABLE_PIECES:
                                move = ([piece_square,
                                         new_square,
                                         new_piece])
                                if self.is_king_safe_after_move(move):
                                    valid_moves.append(move)
                    # En passant capture move
                    elif new_square == self.board.en_passant_target:
                        if self.is_king_safe_after_move(move):
                            valid_moves.append(move)
            case "p":
                # Single step move, no capture
                new_square = (piece_square
                              + pieces.BLACK_PAWN_SINGLE_STEP_OFFSET)
                move = [piece_square, new_square, piece]
                # No promotion move
                if (piece_rank > 1 and piece_rank < 7 and
                    self.board.squares[new_square]
                    == self.board.EMPTY_SQUARE and
                    self.is_king_safe_after_move(move)):
                    valid_moves.append(move)
                    # Double step move
                    new_square = (
                        piece_square +
                        pieces.BLACK_PAWN_DOUBLE_STEP_OFFSET
                    )
                    move = [piece_square, new_square, piece]
                    if (piece_rank == 7 and
                        self.board.squares[new_square]
                        == self.board.EMPTY_SQUARE and
                        self.is_king_safe_after_move(move)):
                        valid_moves.append(move)
                # Promotion move
                elif (piece_rank == 2 and
                      self.board.squares[new_square]
                      == self.board.EMPTY_SQUARE):
                    for new_piece in pieces.BLACK_PROMOTABLE_PIECES:
                        move = [piece_square, new_square, new_piece]
                        if self.is_king_safe_after_move(move):
                            valid_moves.append(move)
                # Capture move
                for offset in pieces.BLACK_PAWN_CAPTURE_OFFSETS:
                    new_square = piece_square + offset
                    move = [piece_square, new_square, piece]
                    if new_square & 0x88:
                        continue
                    if (self.board.squares[new_square]
                        in pieces.WHITE_CAPTURABLE_PIECES):
                        if (piece_rank > 1 and piece_rank < 7 and
                            self.is_king_safe_after_move(move)):
                            valid_moves.append(move)
                        elif piece_rank == 7:
                            # Promotion with capture moves
                            for new_piece in \
                                pieces.BLACK_PROMOTABLE_PIECES:
                                move = [piece_square,
                                        new_square, new_piece]
                                if self.is_king_safe_after_move(move):
                                    valid_moves.append(move)
                    # En passant capture move
                    elif new_square == self.board.en_passant_target:
                        if self.is_king_safe_after_move(move):
                            valid_moves.append(move)
            case "N" | "n":
                if piece.isupper():
                    enemy_capturable_pieces = (
                        pieces.BLACK_CAPTURABLE_PIECES
                    )
                else:
                    enemy_capturable_pieces = (
                        pieces.WHITE_CAPTURABLE_PIECES
                    )
                for offset in pieces.KNIGHT_OFFSETS:
                    new_square = piece_square + offset
                    move = [piece_square, new_square, piece]
                    if new_square & 0x88:
                        continue
                    if ((self.board.squares[new_square]
                         == self.board.EMPTY_SQUARE or
                        self.board.squares[new_square]
                        in enemy_capturable_pieces) and
                        self.is_king_safe_after_move(move)):
                        valid_moves.append(move)
            case "K" | "k":
                # Castling
                if piece.isupper():
                    white_ally = True
                    enemy_capturable_pieces = (
                        pieces.BLACK_CAPTURABLE_PIECES
                    )
                    K_side_path_is_clear = (self.board.squares[117]
                                            == self.board.EMPTY_SQUARE
                                            and
                                            self.board.squares[118]
                                            == self.board.EMPTY_SQUARE)
                    K_side_path_not_attacked = not (
                        self.is_attacked_square(117, True) or
                        self.is_attacked_square(118, True)
                    )
                    Q_side_path_is_clear = (self.board.squares[113]
                                            == self.board.EMPTY_SQUARE
                                            and
                                            self.board.squares[114]
                                            == self.board.EMPTY_SQUARE
                                            and
                                            self.board.squares[115]
                                            == self.board.EMPTY_SQUARE)
                    Q_side_path_not_attacked = not (
                        self.is_attacked_square(113, True) or
                        self.is_attacked_square(114, True) or
                        self.is_attacked_square(115, True)
                    )
                    k_side_path_is_clear = False
                    q_side_path_is_clear = False
                else:
                    white_ally = False
                    enemy_capturable_pieces = (
                        pieces.WHITE_CAPTURABLE_PIECES
                    )
                    k_side_path_is_clear = (self.board.squares[5]
                                            == self.board.EMPTY_SQUARE
                                            and
                                            self.board.squares[6]
                                             == self.board.EMPTY_SQUARE)
                    k_path_not_attacked = not (
                        self.is_attacked_square(5, False) or
                        self.is_attacked_square(6, False)
                    )
                    q_side_path_is_clear = (self.board.squares[1]
                                            == self.board.EMPTY_SQUARE
                                            and
                                            self.board.squares[2] ==
                                            self.board.EMPTY_SQUARE and
                                            self.board.squares[3] ==
                                            self.board.EMPTY_SQUARE)
                    q_path_not_attacked = not (
                        self.is_attacked_square(1, False) or
                        self.is_attacked_square(2, False) or
                        self.is_attacked_square(3, False)
                    )
                    K_side_path_is_clear = False
                    Q_side_path_is_clear = False
                if (K_side_path_is_clear and
                    K_side_path_not_attacked and
                    "K" in self.board.castling_rights):
                    move = [piece_square, 118, piece]
                    valid_moves.append(move)
                if (Q_side_path_is_clear and
                    Q_side_path_not_attacked and
                    "Q" in self.board.castling_rights):
                    move = [piece_square, 114, piece]
                    valid_moves.append(move)
                if (k_side_path_is_clear and
                    k_path_not_attacked and
                    "k" in self.board.castling_rights):
                    move = [piece_square, 6, piece]
                    valid_moves.append(move)
                if (q_side_path_is_clear and
                    q_path_not_attacked and
                    "q" in self.board.castling_rights):
                    move = [piece_square, 2, piece]
                    valid_moves.append(move)
                # Captures and single moves
                for offset in pieces.KING_OFFSETS:
                    new_square = piece_square + offset
                    move = [piece_square, new_square, piece]
                    if new_square & 0x88:
                        continue
                    if (not self.is_attacked_square(
                            new_square, white_ally) and
                        (self.board.squares[new_square]
                         == self.board.EMPTY_SQUARE or
                        self.board.squares[new_square]
                        in enemy_capturable_pieces)):
                        valid_moves.append(move)
            # Sliding pieces:bishop, rook, queen
            case _:
                if piece.isupper():
                    enemy_capturable_pieces = (
                        pieces.BLACK_CAPTURABLE_PIECES
                    )
                else:
                    enemy_capturable_pieces = (
                        pieces.WHITE_CAPTURABLE_PIECES
                    )
                if piece.upper() == "B":
                    offsets = pieces.BISHOP_OFFSETS
                elif piece.upper() == "R":
                    offsets = pieces.ROCK_OFFSETS
                elif piece.upper() == "Q":
                    offsets = pieces.QUEEN_OFFSETS
                for offset in offsets:
                    new_square = piece_square + offset
                    move = [piece_square, new_square, piece]
                    while new_square & 0x88 == 0:
                        if(self.board.squares[new_square]
                           == self.board.EMPTY_SQUARE):
                            valid_moves.append(move)
                        elif (self.board.squares[new_square]
                              in enemy_capturable_pieces):
                            valid_moves.append(move)
                            break
                        else:
                            break
                        new_square += offset
                        move = [piece_square, new_square, piece]
        return valid_moves


    def is_attacked_square(self,
                           square: Square,
                           is_white_ally: bool) -> bool:
        for piece_square in self.board.piece_squares:
            piece = self.board.squares[piece_square]
            if ((piece.isupper() and is_white_ally) or
                (piece.islower() and not is_white_ally)):
                continue
            elif self.is_piece_attacking_square(piece_square, square):
                return True
        return False


    def is_king_safe_after_move(self, move: Move) -> bool:
        # Save involved squares previous state
        from_square_piece: Square = self.board.squares[move[0]]
        to_square_piece: Square = self.board.squares[move[1]]
        # Consider whose turn it is
        if self.board.is_white_turn:
            king_square = self.board.white_king_square
            is_white_ally = True
        else:
            king_square = self.board.black_king_square
            is_white_ally = False
        # Make move
        self.board.squares[move[0]] = self.board.EMPTY_SQUARE
        self.board.piece_squares.discard(move[0])
        self.board.squares[move[1]] = move[2]
        # Check if king is not in check after move before adding it as
        # a valid move
        is_king_safe: bool = (
            not self.is_attacked_square(king_square, is_white_ally)
            )
        # Undo move
        self.board.squares[move[0]] = from_square_piece
        self.board.piece_squares.add(move[0])
        self.board.squares[move[1]] = to_square_piece
        # Return if king is safe after move
        if is_king_safe:
            return True
        return False

    def is_piece_attacking_square(self,
                                  piece_square: int,
                                  target_square: int) -> bool:
        piece = self.board.squares[piece_square]
        if piece == "P":
            offsets = pieces.WHITE_PAWN_CAPTURE_OFFSETS
            is_sliding_piece = False
        elif piece == "p":
            offsets = pieces.BLACK_PAWN_CAPTURE_OFFSETS
            is_sliding_piece = False
        elif piece.upper() == "N":
            offsets = pieces.KNIGHT_OFFSETS
            is_sliding_piece = False
        elif piece.upper() == "B":
            offsets = pieces.BISHOP_OFFSETS
            is_sliding_piece = True
        elif piece.upper() == "R":
            offsets = pieces.ROCK_OFFSETS
            is_sliding_piece = True
        elif piece.upper() == "Q":
            offsets = pieces.QUEEN_OFFSETS
            is_sliding_piece = True
        elif piece.upper() == "K":
            offsets = pieces.KING_OFFSETS
            is_sliding_piece = False
        if not is_sliding_piece:
            for offset in offsets:
                new_square = piece_square + offset
                if (new_square == target_square or
                    target_square == self.board.en_passant_target):
                    return True
        else:
            for offset in offsets:
                new_square = piece_square + offset
                while new_square & 0x88 == 0:
                    if new_square == target_square:
                        return True
                    if (self.board.squares[new_square]
                        != self.board.EMPTY_SQUARE):
                        break
                    new_square += offset
        return False


    def show_all_valid_moves(self, notation: str = "uci") -> None:
        valid_moves = self.get_board_valid_moves()
        print(f"Valid moves ({len(valid_moves)}):", end=" ")
        for move in valid_moves:
            piece = self.board.squares[move[0]]
            # capture part
            if (self.board.squares[move[1]]
                != self.board.EMPTY_SQUARE and notation != "uci"):
                capture_part = "x"
            else:
                capture_part = ""
            # promotion part
            if piece in ("P", "p") and (move[1] < 16 or move[1] > 111):
                if notation == "uci":
                    promotion_part = move[2].lower()
                elif notation == "algebraic":
                    promotion_part = "=" + move[2]
                elif notation == "symbolic":
                    promotion_part = ("="
                                      + pieces.UNICODE_SYMBOLS[move[2]])
            else:
                promotion_part = ""
            # from and to parts
            if notation == "uci":
                from_part = self.board.get_algebraic_coordinate(move[0])
                to_part = self.board.get_algebraic_coordinate(move[1])
            elif notation == "algebraic" or notation == "symbolic":
                if notation == "algebraic":
                    piece_char = piece
                else:
                    piece_char = pieces.UNICODE_SYMBOLS[piece]
                from_part = (
                    piece_char
                    + self.board.get_algebraic_coordinate(move[0])
                )
                to_part = self.board.get_algebraic_coordinate(move[1])
                # pawn exception
                if piece.upper() == "P":
                    if capture_part and not notation == "uci":
                        from_part = (
                            self.board.get_algebraic_coordinate(
                                move[0])[0]
                            )
                        to_part = self.board.get_algebraic_coordinate(
                            move[1])[0]
                    else:
                        from_part = ""
                        to_part = self.board.get_algebraic_coordinate(
                            move[1])
            print(from_part + capture_part + to_part
                  + promotion_part, end=" ")
        print()
