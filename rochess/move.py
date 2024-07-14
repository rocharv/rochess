import piece


def add_valid_move(board,
                   valid_moves: list[list[int|str]],
                   from_square: int, to_square: int,
                   destination_piece: str) -> None:
    # Save involved squares previous state
    from_square_piece = board.squares[from_square]
    to_square_piece = board.squares[to_square]
    # Check king's safety after move
    if board.white_turn:
        king_square = board.white_king_square
        white_ally = True
    else:
        king_square = board.black_king_square
        white_ally = False
    # Make move
    board.squares[from_square] = '.'
    board.piece_squares.remove(from_square)
    board.squares[to_square] = destination_piece
    # Check if king is not in check after move before adding it as a valid move
    if not board.is_attacked_square(king_square, white_ally):
        valid_moves.append([from_square, to_square, destination_piece])
    # Undo move
    board.squares[from_square] = from_square_piece
    board.piece_squares.add(from_square)
    board.squares[to_square] = to_square_piece


def get_piece_valid_moves(board, piece_square: int) -> list[list[int|str]]:
    valid_moves = []
    cpiece = board.squares[piece_square]
    piece_rank = 8 - piece_square // 16
    # if is not piece's color turn
    if ((cpiece in piece.white_pieces and not board.white_turn) or
        ((cpiece in piece.black_pieces and board.white_turn))):
        return []
    match cpiece:
        case "P":
            # Single step move
            new_square = piece_square + piece.white_pawn_single_step_offset
            if (piece_rank > 1 and piece_rank < 7 and
                board.squares[new_square] == '.'):
                add_valid_move(board, valid_moves, piece_square,
                               new_square, cpiece)
                # Double step move
                new_square = piece_square + piece.white_pawn_double_step_offset
                if piece_rank == 2 and board.squares[new_square] == '.':
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, cpiece)
            # Promotion move
            elif piece_rank == 7 and board.squares[new_square] == '.':
                for new_piece in piece.white_promotable_pieces:
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, new_piece)
            # Capture moves
            for offset in piece.white_pawn_capture_offsets:
                new_square = piece_square + offset
                if new_square & 0x88:
                    continue
                if board.squares[new_square] in piece.black_capturable_pieces:
                    if piece_rank > 1 and piece_rank < 7:
                        add_valid_move(board, valid_moves, piece_square,
                                       new_square, cpiece)
                    elif piece_rank == 7:
                        # Promotion capture moves
                        for new_piece in piece.white_promotable_pieces:
                            add_valid_move(board, valid_moves, piece_square,
                                           new_square, new_piece)
                # En passant capture move
                elif new_square == board.en_passant_target:
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, cpiece)
        case "p":
            # Single step move
            new_square = piece_square + piece.black_pawn_single_step_offset
            if (piece_rank > 2 and piece_rank < 8 and
                board.squares[new_square] == '.'):
                add_valid_move(board, valid_moves, piece_square,
                               new_square, cpiece)
                # Double step move
                new_square = piece_square + piece.black_pawn_double_step_offset
                if piece_rank == 7 and board.squares[new_square] == '.':
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, cpiece)
            # Promotion move
            elif piece_rank == 2 and board.squares[new_square] == '.':
                for new_piece in piece.black_promotable_pieces:
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, new_piece)
            # Capture moves
            for offset in piece.black_pawn_capture_offsets:
                new_square = piece_square + offset
                if new_square & 0x88:
                    continue
                if board.squares[new_square] in piece.white_capturable_pieces:
                    if piece_rank > 2 and piece_rank < 8:
                        add_valid_move(board, valid_moves, piece_square,
                                       new_square, cpiece)
                    elif piece_rank == 2:
                        # Promotion capture moves
                        for new_piece in piece.black_promotable_pieces:
                            add_valid_move(board, valid_moves, piece_square,
                                           new_square, new_piece)
                # En passant capture move
                elif new_square == board.en_passant_target:
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, cpiece)
        case "N" | "n":
            if cpiece.isupper():
                enemy_capturable_pieces = piece.black_capturable_pieces
            else:
                enemy_capturable_pieces = piece.white_capturable_pieces
            for offset in piece.knight_offsets:
                new_square = piece_square + offset
                if new_square & 0x88:
                    continue
                if (board.squares[new_square] == "." or
                    board.squares[new_square] in enemy_capturable_pieces):
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, cpiece)
        case 'K' | 'k':
            # Castling
            if cpiece.isupper():
                white_ally = True
                enemy_capturable_pieces = piece.black_capturable_pieces
                K_side_path_is_clear = (board.squares[117] == "." and
                                        board.squares[118] == ".")
                K_side_path_not_attacked = not (
                    board.is_attacked_square(117, True) or
                    board.is_attacked_square(118, True)
                )
                Q_side_path_is_clear = (board.squares[113] == "." and
                                        board.squares[114] == "." and
                                        board.squares[115] == ".")
                Q_side_path_not_attacked = not (
                    board.is_attacked_square(113, True) or
                    board.is_attacked_square(114, True) or
                    board.is_attacked_square(115, True)
                )
                k_side_path_is_clear = False
                q_side_path_is_clear = False
            else:
                white_ally = False
                enemy_capturable_pieces = piece.white_capturable_pieces
                k_side_path_is_clear = (board.squares[5] == "." and
                                        board.squares[6] == ".")
                k_path_not_attacked = not (
                    board.is_attacked_square(5, False) or
                    board.is_attacked_square(6, False)
                )
                q_side_path_is_clear = (board.squares[1] == "." and
                                        board.squares[2] == "." and
                                        board.squares[3] == ".")
                q_path_not_attacked = not (
                    board.is_attacked_square(1, False) or
                    board.is_attacked_square(2, False) or
                    board.is_attacked_square(3, False)
                )
                K_side_path_is_clear = False
                Q_side_path_is_clear = False
            if (K_side_path_is_clear and K_side_path_not_attacked and
                'K' in board.castling_rights):
                add_valid_move(board, valid_moves, piece_square, 118, cpiece)
            if (Q_side_path_is_clear and Q_side_path_not_attacked and
                'Q' in board.castling_rights):
                add_valid_move(board, valid_moves, piece_square, 114, cpiece)
            if (k_side_path_is_clear and k_path_not_attacked and
                'k' in board.castling_rights):
                add_valid_move(board, valid_moves, piece_square, 6, cpiece)
            if (q_side_path_is_clear and q_path_not_attacked and
                'q' in board.castling_rights):
                add_valid_move(board, valid_moves, piece_square, 2, cpiece)
            # Captures and single moves
            for offset in piece.king_offsets:
                new_square = piece_square + offset
                if new_square & 0x88:
                    continue
                if (not board.is_attacked_square(new_square, white_ally) and
                    (board.squares[new_square] == "." or
                     board.squares[new_square] in enemy_capturable_pieces)):
                    add_valid_move(board, valid_moves, piece_square,
                                   new_square, cpiece)
        # Sliding pieces:bishop, rook, queen
        case _:
            if cpiece.isupper():
                enemy_capturable_pieces = piece.black_capturable_pieces
            else:
                enemy_capturable_pieces = piece.white_capturable_pieces
            if cpiece.upper() == "B":
                offsets = piece.bishop_offsets
            elif cpiece.upper() == "R":
                offsets = piece.rook_offsets
            elif cpiece.upper() == "Q":
                offsets = piece.queen_offsets
            for offset in offsets:
                new_square = piece_square + offset
                while new_square & 0x88 == 0:
                    if board.squares[new_square] == ".":
                        add_valid_move(board, valid_moves, piece_square,
                                       new_square, cpiece)
                    elif board.squares[new_square] in enemy_capturable_pieces:
                        add_valid_move(board, valid_moves, piece_square,
                                       new_square, cpiece)
                        break
                    else:
                        break
                    new_square += offset
    return valid_moves


def is_piece_attacking_square(board,
                              piece_square: int,
                              target_square: int) -> bool:
    cpiece = board.squares[piece_square]
    if cpiece == "P":
        offsets = piece.white_pawn_capture_offsets
        sliding_piece = False
    elif cpiece == "p":
        offsets = piece.black_pawn_capture_offsets
        sliding_piece = False
    elif cpiece.upper() == "N":
        offsets = piece.knight_offsets
        sliding_piece = False
    elif cpiece.upper() == "B":
        offsets = piece.bishop_offsets
        sliding_piece = True
    elif cpiece.upper() == "R":
        offsets = piece.rook_offsets
        sliding_piece = True
    elif cpiece.upper() == "Q":
        offsets = piece.queen_offsets
        sliding_piece = True
    elif cpiece.upper() == "K":
        offsets = piece.king_offsets
        sliding_piece = False
    if not sliding_piece:
        for offset in offsets:
            new_square = piece_square + offset
            if (new_square == target_square or
                target_square == board.en_passant_target):
                return True
    else:
        for offset in offsets:
            new_square = piece_square + offset
            while new_square & 0x88 == 0:
                if new_square == target_square:
                    return True
                if board.squares[new_square] != ".":
                    break
                new_square += offset
    return False
