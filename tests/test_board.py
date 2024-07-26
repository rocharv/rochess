from rochess.board import Board


class TestBoard:
    def test_board_constructor(self):
        # Tic-tac-toe board creation
        tic_tac_toe_board = Board(3, 3)
        assert tic_tac_toe_board.number_of_rows == 3
        assert tic_tac_toe_board.number_of_columns == 3
        assert len(tic_tac_toe_board.squares) == 18
        assert tic_tac_toe_board.squares == [
            ".", ".", ".", "-", "-", "-",
            ".", ".", ".", "-", "-", "-",
            ".", ".", ".", "-", "-", "-"
        ]
        # Chess board creation
        chess_board = Board(8, 8)
        assert chess_board.number_of_rows == 8
        assert chess_board.number_of_columns == 8
        assert len(chess_board.squares) == 128
        assert chess_board.squares == [
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
        ]
        # check piece_squares
        assert chess_board.piece_squares == set()


    def test_board_get_algebraic_coodinate(self):
        # Tic-tac-toe get_algebraic_coordinate
        tic_tac_toe_board = Board(3, 3)
        assert tic_tac_toe_board.get_algebraic_coordinate(12) == "a1"
        assert tic_tac_toe_board.get_algebraic_coordinate(14) == "c1"
        assert tic_tac_toe_board.get_algebraic_coordinate(7) == "b2"
        assert tic_tac_toe_board.get_algebraic_coordinate(0) == "a3"
        assert tic_tac_toe_board.get_algebraic_coordinate(2) == "c3"
        # Chess get_algebraic_coordinate
        chess_board = Board(8, 8)
        assert chess_board.get_algebraic_coordinate(112) == "a1"
        assert chess_board.get_algebraic_coordinate(119) == "h1"
        assert chess_board.get_algebraic_coordinate(67) == "d4"
        assert chess_board.get_algebraic_coordinate(0) == "a8"
        assert chess_board.get_algebraic_coordinate(7) == "h8"


    def test_board_get_piece(self):
    	# Tic-tac-toe get_piece and get_piece_alg right after creation
        tic_tac_toe_board = Board(3, 3)
        assert tic_tac_toe_board.get_piece_from_coords(1, 1) == "."
        assert tic_tac_toe_board.get_piece_from_coords(3, 1) == "."
        assert tic_tac_toe_board.get_piece_from_coords(2, 2) == "."
        assert tic_tac_toe_board.get_piece_from_coords(1, 3) == "."
        assert tic_tac_toe_board.get_piece_from_coords(3, 3) == "."
        assert tic_tac_toe_board.get_piece_from_algebraic("a1") == "."
        assert tic_tac_toe_board.get_piece_from_algebraic("c1") == "."
        assert tic_tac_toe_board.get_piece_from_algebraic("b2") == "."
        assert tic_tac_toe_board.get_piece_from_algebraic("a3") == "."
        assert tic_tac_toe_board.get_piece_from_algebraic("c3") == "."
        # Chess get_piece and get_piece_alg right after creation
        chess_board = Board(8, 8)
        assert chess_board.get_piece_from_coords(1, 1) == "."
        assert chess_board.get_piece_from_coords(8, 1) == "."
        assert chess_board.get_piece_from_coords(4, 4) == "."
        assert chess_board.get_piece_from_coords(1, 8) == "."
        assert chess_board.get_piece_from_coords(8, 8) == "."
        assert chess_board.get_piece_from_algebraic("a1") == "."
        assert chess_board.get_piece_from_algebraic("h1") == "."
        assert chess_board.get_piece_from_algebraic("d4") == "."
        assert chess_board.get_piece_from_algebraic("a8") == "."
        assert chess_board.get_piece_from_algebraic("h8") == "."


    def test_board_get_square_from_algebraic(self):
        chess_board = Board(8, 8)
        assert chess_board.get_square_from_algebraic("a1") == 112
        assert chess_board.get_square_from_algebraic("e1") == 116
        assert chess_board.get_square_from_algebraic("h1") == 119
        assert chess_board.get_square_from_algebraic("a4") == 64
        assert chess_board.get_square_from_algebraic("e4") == 68
        assert chess_board.get_square_from_algebraic("h4") == 71
        assert chess_board.get_square_from_algebraic("a8") == 0
        assert chess_board.get_square_from_algebraic("e8") == 4
        assert chess_board.get_square_from_algebraic("h8") == 7


    def test_board_get_square_from_coord(self):
        chess_board = Board(8, 8)
        assert chess_board.get_square_from_coord(1, 1) == 112
        assert chess_board.get_square_from_coord(5, 1) == 116
        assert chess_board.get_square_from_coord(8, 1) == 119
        assert chess_board.get_square_from_coord(1, 4) == 64
        assert chess_board.get_square_from_coord(5, 4) == 68
        assert chess_board.get_square_from_coord(8, 4) == 71
        assert chess_board.get_square_from_coord(1, 8) == 0
        assert chess_board.get_square_from_coord(5, 8) == 4
        assert chess_board.get_square_from_coord(8, 8) == 7


    def test_board_reset_squares(self):
        chess_board = Board(8, 8)
        chess_board.set_piece_from_algebraic("a1", "R")
        chess_board.set_piece_from_algebraic("g1", "K")
        chess_board.set_piece_from_algebraic("h1", "B")
        chess_board.set_piece_from_algebraic("d4", "Q")
        chess_board.set_piece_from_algebraic("a8", "r")
        chess_board.set_piece_from_algebraic("g8", "k")
        chess_board.set_piece_from_algebraic("h8", "b")
        assert chess_board.squares == [
            "r", ".", ".", ".", ".", ".", "k", "b", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", "Q", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            "R", ".", ".", ".", ".", ".", "K", "B", "-", "-", "-", "-", "-", "-", "-", "-",
        ]
        chess_board.reset_squares()
        assert chess_board.squares == [
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
        ]


    def test_board_set_piece_and_get_piece_and_reset(self):
        # Tic-tac-toe set_piece
        tic_tac_toe_board = Board(3, 3)
        tic_tac_toe_board.set_piece_from_coords(1, 1, "O")
        tic_tac_toe_board.set_piece_from_coords(3, 1, "X")
        tic_tac_toe_board.set_piece_from_coords(2, 2, "X")
        tic_tac_toe_board.set_piece_from_coords(1, 3, "X")
        tic_tac_toe_board.set_piece_from_coords(3, 3, "O")
        assert tic_tac_toe_board.squares == [
            "X", ".", "O", "-", "-", "-",
            ".", "X", ".", "-", "-", "-",
            "O", ".", "X", "-", "-", "-"
        ]
        # check piece_squares
        assert tic_tac_toe_board.piece_squares == {0, 2, 7, 12, 14}
        # Tic-tac-toe get_piece after set_piece
        assert tic_tac_toe_board.get_piece_from_coords(1, 1) == "O"
        assert tic_tac_toe_board.get_piece_from_coords(3, 1) == "X"
        assert tic_tac_toe_board.get_piece_from_coords(2, 2) == "X"
        assert tic_tac_toe_board.get_piece_from_coords(1, 3) == "X"
        assert tic_tac_toe_board.get_piece_from_coords(3, 3) == "O"
        # Tic-tac-toe get_piece_alg after set_piece
        assert tic_tac_toe_board.get_piece_from_algebraic("a1") == "O"
        assert tic_tac_toe_board.get_piece_from_algebraic("c1") == "X"
        assert tic_tac_toe_board.get_piece_from_algebraic("b2") == "X"
        assert tic_tac_toe_board.get_piece_from_algebraic("a3") == "X"
        assert tic_tac_toe_board.get_piece_from_algebraic("c3") == "O"
        # Board reset
        tic_tac_toe_board.reset_squares()
        assert tic_tac_toe_board.squares == [
            ".", ".", ".", "-", "-", "-",
            ".", ".", ".", "-", "-", "-",
            ".", ".", ".", "-", "-", "-"
        ]
        # Tic-tac-toe set_piece_alg
        tic_tac_toe_board.set_piece_from_algebraic("a1", "O")
        tic_tac_toe_board.set_piece_from_algebraic("c1", "X")
        tic_tac_toe_board.set_piece_from_algebraic("b2", "X")
        tic_tac_toe_board.set_piece_from_algebraic("a3", "X")
        tic_tac_toe_board.set_piece_from_algebraic("c3", "O")
        assert tic_tac_toe_board.squares == [
            "X", ".", "O", "-", "-", "-",
            ".", "X", ".", "-", "-", "-",
            "O", ".", "X", "-", "-", "-"
        ]
        # check piece_squares
        assert tic_tac_toe_board.piece_squares == {0, 2, 7, 12, 14}
        # Chess set_piece
        chess_board = Board(8, 8)
        chess_board.set_piece_from_coords(1, 1, "R")
        chess_board.set_piece_from_coords(7, 1, "K")
        chess_board.set_piece_from_coords(8, 1, "B")
        chess_board.set_piece_from_coords(4, 4, "Q")
        chess_board.set_piece_from_coords(1, 8, "r")
        chess_board.set_piece_from_coords(7, 8, "k")
        chess_board.set_piece_from_coords(8, 8, "b")
        assert chess_board.squares == [
            "r", ".", ".", ".", ".", ".", "k", "b", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", "Q", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            "R", ".", ".", ".", ".", ".", "K", "B", "-", "-", "-", "-", "-", "-", "-", "-",
        ]
        # check piece_squares
        assert chess_board.piece_squares == {0, 6, 7, 67, 112, 118, 119}
        # Chess get_piece after set_piece
        assert chess_board.get_piece_from_coords(1, 1) == "R"
        assert chess_board.get_piece_from_coords(7, 1) == "K"
        assert chess_board.get_piece_from_coords(8, 1) == "B"
        assert chess_board.get_piece_from_coords(4, 4) == "Q"
        assert chess_board.get_piece_from_coords(1, 8) == "r"
        assert chess_board.get_piece_from_coords(7, 8) == "k"
        assert chess_board.get_piece_from_coords(8, 8) == "b"
        # Chess get_piece_alg after set_piece
        assert chess_board.get_piece_from_algebraic("a1") == "R"
        assert chess_board.get_piece_from_algebraic("g1") == "K"
        assert chess_board.get_piece_from_algebraic("h1") == "B"
        assert chess_board.get_piece_from_algebraic("d4") == "Q"
        assert chess_board.get_piece_from_algebraic("a8") == "r"
        assert chess_board.get_piece_from_algebraic("g8") == "k"
        assert chess_board.get_piece_from_algebraic("h8") == "b"
        # Board reset
        chess_board.reset_squares()
        assert chess_board.squares == [
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
        ]
        # Chess set_piece_alg
        chess_board.set_piece_from_algebraic("a1", "R")
        chess_board.set_piece_from_algebraic("g1", "K")
        chess_board.set_piece_from_algebraic("h1", "B")
        chess_board.set_piece_from_algebraic("d4", "Q")
        chess_board.set_piece_from_algebraic("a8", "r")
        chess_board.set_piece_from_algebraic("g8", "k")
        chess_board.set_piece_from_algebraic("h8", "b")
        assert chess_board.squares == [
            "r", ".", ".", ".", ".", ".", "k", "b", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", "Q", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
            "R", ".", ".", ".", ".", ".", "K", "B", "-", "-", "-", "-", "-", "-", "-", "-",
        ]
        # check piece_squares
        assert chess_board.piece_squares == {0, 6, 7, 67, 112, 118, 119}
