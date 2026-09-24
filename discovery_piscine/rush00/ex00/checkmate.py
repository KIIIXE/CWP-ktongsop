def checkmate(board: str):

    lines = board.split('\n')

    rows = []

    for line in lines:
        line = line.strip()

        if line != "":
            rows.append(line)

    size = len(rows)

    if size == 0:
        return

    for row in rows:
        if len(row) != size:
            print("Error")
            return

    king_x = -1
    king_y = -1
    king_count = 0

    for i in range(size):
        for j in range(size):
            if rows[i][j] == 'K':
                king_x = i
                king_y = j
                king_count = king_count + 1

    if king_count != 1:
        print("Error")
        return

    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (-1, -1), (-1, 1),
        (1, -1), (1, 1)
    ]

    for d in directions:

        move_x = d[0]
        move_y = d[1]

        x = king_x + move_x
        y = king_y + move_y
        distance = 1

        while x >= 0 and x < size and y >= 0 and y < size:

            piece = rows[x][y]

            if piece != '.' and piece != ' ':

                is_straight = (move_x == 0 or move_y == 0)
                is_diagonal = (move_x != 0 and move_y != 0)

                if piece == 'Q':
                    print("Success")
                    return

                elif piece == 'R' and is_straight:
                    print("Success")
                    return

                elif piece == 'B' and is_diagonal:
                    print("Success")
                    return

                elif piece == 'P' and is_diagonal and distance == 1:
                    if move_x == 1:
                        print("Success")
                        return

                break

            x = x + move_x
            y = y + move_y
            distance = distance + 1

    print("Fail")