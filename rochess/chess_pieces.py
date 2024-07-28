# Pieces and their symbols
UNICODE_SYMBOLS = {
    ".": "·",
    "K": "♔", "Q": "♕", "R": "♖", "B": "♗", "N": "♘","P": "♙",
    "k": "♚", "q": "♛", "r": "♜", "b": "♝","n": "♞", "p": "♟︎",
    "-": "-"
}
# Group of pieces
BLACK_CAPTURABLE_PIECES = {"q", "r", "b", "n", "p"}
BLACK_PIECES = {"k", "q", "r", "b", "n", "p"}
BLACK_PROMOTABLE_PIECES = {"q", "r", "b", "n"}
ROYAL_PIECES = {"K", "Q", "k", "q"}
WHITE_CAPTURABLE_PIECES = {"Q", "R", "B", "N", "P"}
WHITE_PIECES = {"K", "Q", "R", "B", "N", "P"}
WHITE_PROMOTABLE_PIECES = {"Q", "R", "B", "N"}
"""
Group of offsets for each piece
Offsets for a given x position in the board:
    -34 -33 -32 -31 -30 -29
    -18 -17 -16 -15 -14 -13
    -02 -01  x   01  02  03
     14  15  16  17  18  19
     30  31  32  33  34  35
"""
BISHOP_OFFSETS = (-15, 17, 15, -17)
KING_OFFSETS = (-16, -15, 1, 17, 16, 15, -1, -17)
KNIGHT_OFFSETS = (-31, -14, 18, 33, 31, 14, -18, -33)
ROCK_OFFSETS = (-16, 1, 16, -1)
QUEEN_OFFSETS = (-16, -15, 1, 17, 16, 15, -1, -17)
BLACK_PAWN_CAPTURE_OFFSETS = (17, 15)
BLACK_PAWN_SINGLE_STEP_OFFSET = 16
BLACK_PAWN_DOUBLE_STEP_OFFSET = 32
WHITE_PAWN_CAPTURE_OFFSETS = (-15, -17)
WHITE_PAWN_SINGLE_STEP_OFFSET = -16
WHITE_PAWN_DOUBLE_STEP_OFFSET = -32