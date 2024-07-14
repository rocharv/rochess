from board import Board


def main() -> None:
    board = Board(
        #from_fen_string="R6R/3Q4/1Q4Q1/4Q3/2Q4Q/Q4Q2/pp1Q4/kBNN1KB1 w - - 0 1"
        from_fen_string="r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 1"
    )
    board.show(show_info=True, use_symbols=True)
    board.show_all_valid_moves(notation="uci")
    board.show_all_valid_moves(notation="algebraic")
    board.show_all_valid_moves(notation="symbolic")


if __name__ == '__main__':
    main()
