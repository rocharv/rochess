from rochess.chess_board import ChessBoard
from rochess.chess_moves import ChessMoves


def main() -> None:
    board = ChessBoard(
        # from_fen_string=("r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10")
    )
    board.show()
    board.show_info()
    moves = ChessMoves(board)
    moves.show_all_valid_moves(notation="algebraic")
    print(moves.perft(3))


if __name__ == '__main__':
    main()
