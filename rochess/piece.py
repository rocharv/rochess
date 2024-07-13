unicode_symbol = {
    '.': '·',
    'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘','P': '♙',
    'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝','n': '♞', 'p': '♟︎',
    'o': 'o'
}
black_capturable_pieces = ("q", "r", "b", "n", "p")
black_pieces = ("k", "q", "r", "b", "n", "p")
black_promotable_pieces = ("q", "r", "b", "n")
white_capturable_pieces = ("Q", "R", "B", "N", "P")
white_pieces = ("K", "Q", "R", "B", "N", "P")
white_promotable_pieces = ("Q", "R", "B", "N")
'''
Offsets for a given x position in the board:
    -34 -33 -32 -31 -30 -29
    -18 -17 -16 -15 -14 -13
    -02 -01  x   01  02  03
     14  15  16  17  18  19
     30  31  32  33  34  35
'''
bishop_offsets = (-15, 17, 15, -17)
king_offsets = (-16, -15, 1, 17, 16, 15, -1, -17)
knight_offsets = (-31, -14, 18, 33, 31, 14, -18, -33)
rook_offsets = (-16, 1, 16, -1)
queen_offsets = (-16, -15, 1, 17, 16, 15, -1, -17)
black_pawn_capture_offsets = (17, 15)
black_pawn_single_step_offset = 16
black_pawn_double_step_offset = 32
white_pawn_capture_offsets = (-15, -17)
white_pawn_single_step_offset = -16
white_pawn_double_step_offset = -32