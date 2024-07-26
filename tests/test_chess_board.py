from rochess.chess_board import ChessBoard


class TestChessBoard:
    def test_chess_board_default_constructor(self):
        # Chess default board creation
        chess_board = ChessBoard()
        assert chess_board.black_king_square == 4
        assert chess_board.castling_rights == {"K", "Q", "k", "q"}
        assert chess_board.piece_squares == {
              0,   1,   2,   3,   4,   5,   6,   7,
             16,  17,  18,  19,  20,  21,  22,  23,
             96,  97,  98,  99, 100, 101, 102, 103,
            112, 113, 114, 115, 116, 117, 118, 119,
        }
        assert chess_board.white_king_square == 116
        assert chess_board.en_passant_target == ""
        assert chess_board.full_move_number == 1
        assert chess_board.half_move_clock == 0
        assert chess_board.is_white_turn == True
        assert chess_board.squares == [
           "r", "n", "b", "q", "k", "b", "n", "r", "-", "-", "-", "-", "-", "-", "-", "-",
           "p", "p", "p", "p", "p", "p", "p", "p", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           "P", "P", "P", "P", "P", "P", "P", "P", "-", "-", "-", "-", "-", "-", "-", "-",
           "R", "N", "B", "Q", "K", "B", "N", "R", "-", "-", "-", "-", "-", "-", "-", "-",
        ]
    def test_chess_board_from_char_list(self):
        chess_board = ChessBoard(
            from_char_list = [
                "r", "n", "b", "q", "k", "b", "n", "r",
                "p", "p", "p", "p", "p", "p", "p", "p",
                ".", ".", ".", ".", ".", ".", ".", ".",
                ".", ".", ".", ".", ".", ".", ".", ".",
                ".", ".", ".", ".", ".", ".", ".", ".",
                ".", ".", ".", ".", ".", ".", ".", ".",
                "P", "P", "P", "P", "P", "P", "P", "P",
                "R", "N", "B", "Q", "K", "B", "N", "R",
            ]
        )
        assert chess_board.black_king_square == 4
        assert chess_board.castling_rights == {"K", "Q", "k", "q"}
        assert chess_board.piece_squares == {
              0,   1,   2,   3,   4,   5,   6,   7,
             16,  17,  18,  19,  20,  21,  22,  23,
             96,  97,  98,  99, 100, 101, 102, 103,
            112, 113, 114, 115, 116, 117, 118, 119,
        }
        assert chess_board.white_king_square == 116
        assert chess_board.en_passant_target == ""
        assert chess_board.full_move_number == 1
        assert chess_board.half_move_clock == 0
        assert chess_board.is_white_turn == True
        assert chess_board.squares == [
           "r", "n", "b", "q", "k", "b", "n", "r", "-", "-", "-", "-", "-", "-", "-", "-",
           "p", "p", "p", "p", "p", "p", "p", "p", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           "P", "P", "P", "P", "P", "P", "P", "P", "-", "-", "-", "-", "-", "-", "-", "-",
           "R", "N", "B", "Q", "K", "B", "N", "R", "-", "-", "-", "-", "-", "-", "-", "-",
        ]

    def test_chess_board_from_fen_string(self):
        chess_board = ChessBoard(
            from_fen_string = (
                "8/8/3R1k2/r1p5/4R2P/p7/1r3PP1/6K1 b - - 12 47"
            )
        )
        assert chess_board.black_king_square == 37
        assert chess_board.castling_rights == set()
        assert chess_board.piece_squares == {
             35,  37,  48,  50,  68,  71,  80, 97, 101, 102, 118
        }
        assert chess_board.white_king_square == 118
        assert chess_board.en_passant_target == ""
        assert chess_board.full_move_number == 47
        assert chess_board.half_move_clock == 12
        assert chess_board.is_white_turn == False
        assert chess_board.squares == [
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", "R", ".", "k", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           "r", ".", "p", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", "R", ".", ".", "P", "-", "-", "-", "-", "-", "-", "-", "-",
           "p", ".", ".", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", "r", ".", ".", ".", "P", "P", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", ".", ".", "K", ".", "-", "-", "-", "-", "-", "-", "-", "-",
        ]
        # Castling rights test
        chess_board = ChessBoard(
            from_fen_string = "3rk2r/ppp2ppp/2npqn2/2b1p3/4P3/2PP1N1P/PP1N1PP1/R1BQ1RK1 w k - 2 10"
        )
        assert chess_board.black_king_square == 4
        assert chess_board.castling_rights == {"k"}
        assert chess_board.piece_squares == {
             3, 4, 7, 16, 17, 18, 21, 22, 23, 34, 35, 36, 37, 50, 52,
             68, 82, 83, 85, 87, 96, 97, 99, 101, 102, 112, 114, 115, 117, 118
        }
        assert chess_board.white_king_square == 118
        assert chess_board.en_passant_target == ""
        assert chess_board.full_move_number == 10
        assert chess_board.half_move_clock == 2
        assert chess_board.is_white_turn == True
        print(chess_board.squares)
        assert chess_board.squares == [
           ".", ".", ".", "r", "k", ".", ".", "r", "-", "-", "-", "-", "-", "-", "-", "-",
           "p", "p", "p", ".", ".", "p", "p", "p", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", "n", "p", "q", "n", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", "b", ".", "p", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", ".", ".", "P", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           ".", ".", "P", "P", ".", "N", ".", "P", "-", "-", "-", "-", "-", "-", "-", "-",
           "P", "P", ".", "N", ".", "P", "P", ".", "-", "-", "-", "-", "-", "-", "-", "-",
           "R", ".", "B", "Q", ".", "R", "K", ".", "-", "-", "-", "-", "-", "-", "-", "-",
        ]