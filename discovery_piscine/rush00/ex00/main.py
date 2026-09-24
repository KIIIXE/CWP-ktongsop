from checkmate import checkmate


def run_test(name, board, expected):
    print(f"--- {name} (expected: {expected}) ---")
    checkmate(board)
    print()


def main():
    run_test(
        "Rook check",
        """\
R...
.K..
..P.
....\
""",
        "Success",
    )

    run_test(
        "Bishop check",
        """\
....
.K..
..B.
....\
""",
        "Success",
    )

    run_test(
        "Queen check",
        """\
.K..
....
.Q..
....\
""",
        "Success",
    )

    run_test(
        "Pawn check",
        """\
....
.K..
P...
....\
""",
        "Success",
    )

    run_test(
        "Rook blocked by Pawn",
        """\
R...
.P..
..K.
....\
""",
        "Fail",
    )

    run_test(
        "Bishop blocked",
        """\
...B
..P.
....
K...\
""",
        "Fail",
    )

    run_test(
        "No threat",
        """\
..
.K\
""",
        "Fail",
    )

    run_test(
        "Not square (row too long)",
        """\
R...
.K.....
..P.
....\
""",
        "(nothing printed)",
    )

    run_test(
        "No King on the board",
        """\
R...
....
..P.
....\
""",
        "(nothing printed)",
    )

    run_test(
        "Two Kings on the board",
        """\
K...
....
...K
....\
""",
        "(nothing printed)",
    )

    run_test(
        "Empty board string",
        "",
        "(nothing printed)",
    )

    run_test(
        "Wrong type passed in",
        12345,
        "(nothing printed)",
    )


if __name__ == "__main__":
    main()