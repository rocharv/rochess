from chess_board import ChessBoard
from chess_moves import ChessMoves


def main() -> None:
    board = ChessBoard(
        from_fen_string=(
            "R6R/3Q4/1Q4Q1/4Q3/2Q4Q/Q4Q2/pp1Q4/kBNN1KB1 w - - 0 1"
        )
    )
    board.show()
    board.show_info()
    moves = ChessMoves(board)
    moves.show_all_valid_moves(notation="algebraic")


if __name__ == '__main__':
    main()
