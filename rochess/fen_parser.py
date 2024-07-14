def set_board_from_fen(board, fen_string: str) -> None:
    board.squares = []
    # FEN parts split by spaces
    fen_parts = fen_string.split(" ")
    fen_parts_len = len(fen_parts)
    if fen_parts_len < 6:
        fen_offset = -1
    else:
        fen_offset = 0
    # FEN position parsing
    fen_string = fen_parts[0]
    for char in fen_string:
        if char.isnumeric():
            board.squares.extend(["."] * int(char))
        elif char == "/":
            board.squares.extend(["o"] * board.size[1])
        else:
            board.squares.append(char)
    board.squares.extend(["o"] * board.size[1])
    # FEN turn parsing
    fen_turn = fen_parts[1]
    if fen_turn == "w":
        board.white_turn = True
    else:
        board.white_turn = False
    # FEN castling rights parsing
    board.castling_rights = set()
    if fen_offset == 0:
        fen_castling_rights = fen_parts[2]
        for piece in fen_castling_rights:
            if piece in ("K", "Q", "k", "q"):
                board.castling_rights.add(piece)
    # FEN en passant parsing
    fen_en_passant_target = fen_parts[3+fen_offset]
    if fen_en_passant_target == "-":
        board.en_passant_target = -1
    else:
        board.en_passant_target = (
            board.get_square_from_algebraic(fen_en_passant_target)
        )
    # FEN position parsing
    fen_half_move_clock = int(fen_parts[4+fen_offset])
    board.half_move_clock = fen_half_move_clock
    # FEN position parsing
    fen_full_move_number = int(fen_parts[5+fen_offset])
    board.full_move_number = fen_full_move_number
