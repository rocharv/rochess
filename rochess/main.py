from board import Board


def main() -> None:
    board = Board(
        from_fen_string="4k3/4q3/8/8/8/8/4Q3/4K3 w - - 0 1"
    )
    board.show(show_info=True, use_symbols=True)
    board.show_all_valid_moves(notation="algebraic")


if __name__ == '__main__':
    main()
