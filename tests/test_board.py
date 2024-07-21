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


    def test_board_get_piece(self):
    	# Tic-tac-toe get_piece and get_piece_alg right after creation
        tic_tac_toe_board = Board(3, 3)
        assert tic_tac_toe_board.get_piece(1, 1) == "."
        assert tic_tac_toe_board.get_piece(3, 1) == "."
        assert tic_tac_toe_board.get_piece(2, 2) == "."
        assert tic_tac_toe_board.get_piece(1, 3) == "."
        assert tic_tac_toe_board.get_piece(3, 3) == "."
        assert tic_tac_toe_board.get_piece_alg("a1") == "."
        assert tic_tac_toe_board.get_piece_alg("c1") == "."
        assert tic_tac_toe_board.get_piece_alg("b2") == "."
        assert tic_tac_toe_board.get_piece_alg("a3") == "."
        assert tic_tac_toe_board.get_piece_alg("c3") == "."
        # Chess get_piece and get_piece_alg right after creation
        chess_board = Board(8, 8)
        assert chess_board.get_piece(1, 1) == "."
        assert chess_board.get_piece(8, 1) == "."
        assert chess_board.get_piece(4, 4) == "."
        assert chess_board.get_piece(1, 8) == "."
        assert chess_board.get_piece(8, 8) == "."
        assert chess_board.get_piece_alg("a1") == "."
        assert chess_board.get_piece_alg("h1") == "."
        assert chess_board.get_piece_alg("d4") == "."
        assert chess_board.get_piece_alg("a8") == "."
        assert chess_board.get_piece_alg("h8") == "."


    def test_board_set_piece_and_get_piece_and_reset(self):
        # Tic-tac-toe set_piece
        tic_tac_toe_board = Board(3, 3)
        tic_tac_toe_board.set_piece(1, 1, "O")
        tic_tac_toe_board.set_piece(3, 1, "X")
        tic_tac_toe_board.set_piece(2, 2, "X")
        tic_tac_toe_board.set_piece(1, 3, "X")
        tic_tac_toe_board.set_piece(3, 3, "O")
        assert tic_tac_toe_board.squares == [
            "X", ".", "O", "-", "-", "-",
            ".", "X", ".", "-", "-", "-",
            "O", ".", "X", "-", "-", "-"
        ]
        # check piece_squares
        assert tic_tac_toe_board.piece_squares == {0, 2, 7, 12, 14}
        # Tic-tac-toe get_piece after set_piece
        assert tic_tac_toe_board.get_piece(1, 1) == "O"
        assert tic_tac_toe_board.get_piece(3, 1) == "X"
        assert tic_tac_toe_board.get_piece(2, 2) == "X"
        assert tic_tac_toe_board.get_piece(1, 3) == "X"
        assert tic_tac_toe_board.get_piece(3, 3) == "O"
        # Tic-tac-toe get_piece_alg after set_piece
        assert tic_tac_toe_board.get_piece_alg("a1") == "O"
        assert tic_tac_toe_board.get_piece_alg("c1") == "X"
        assert tic_tac_toe_board.get_piece_alg("b2") == "X"
        assert tic_tac_toe_board.get_piece_alg("a3") == "X"
        assert tic_tac_toe_board.get_piece_alg("c3") == "O"
        # Board reset
        tic_tac_toe_board.reset_squares()
        assert tic_tac_toe_board.squares == [
            ".", ".", ".", "-", "-", "-",
            ".", ".", ".", "-", "-", "-",
            ".", ".", ".", "-", "-", "-"
        ]
        # Tic-tac-toe set_piece_alg
        tic_tac_toe_board.set_piece_alg("a1", "O")
        tic_tac_toe_board.set_piece_alg("c1", "X")
        tic_tac_toe_board.set_piece_alg("b2", "X")
        tic_tac_toe_board.set_piece_alg("a3", "X")
        tic_tac_toe_board.set_piece_alg("c3", "O")
        assert tic_tac_toe_board.squares == [
            "X", ".", "O", "-", "-", "-",
            ".", "X", ".", "-", "-", "-",
            "O", ".", "X", "-", "-", "-"
        ]
        # check piece_squares
        assert tic_tac_toe_board.piece_squares == {0, 2, 7, 12, 14}
        # Chess set_piece
        chess_board = Board(8, 8)
        chess_board.set_piece(1, 1, "R")
        chess_board.set_piece(7, 1, "K")
        chess_board.set_piece(8, 1, "B")
        chess_board.set_piece(4, 4, "Q")
        chess_board.set_piece(1, 8, "r")
        chess_board.set_piece(7, 8, "k")
        chess_board.set_piece(8, 8, "b")
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
        assert chess_board.get_piece(1, 1) == "R"
        assert chess_board.get_piece(7, 1) == "K"
        assert chess_board.get_piece(8, 1) == "B"
        assert chess_board.get_piece(4, 4) == "Q"
        assert chess_board.get_piece(1, 8) == "r"
        assert chess_board.get_piece(7, 8) == "k"
        assert chess_board.get_piece(8, 8) == "b"
        # Chess get_piece_alg after set_piece
        assert chess_board.get_piece_alg("a1") == "R"
        assert chess_board.get_piece_alg("g1") == "K"
        assert chess_board.get_piece_alg("h1") == "B"
        assert chess_board.get_piece_alg("d4") == "Q"
        assert chess_board.get_piece_alg("a8") == "r"
        assert chess_board.get_piece_alg("g8") == "k"
        assert chess_board.get_piece_alg("h8") == "b"
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
        chess_board.set_piece_alg("a1", "R")
        chess_board.set_piece_alg("g1", "K")
        chess_board.set_piece_alg("h1", "B")
        chess_board.set_piece_alg("d4", "Q")
        chess_board.set_piece_alg("a8", "r")
        chess_board.set_piece_alg("g8", "k")
        chess_board.set_piece_alg("h8", "b")
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
