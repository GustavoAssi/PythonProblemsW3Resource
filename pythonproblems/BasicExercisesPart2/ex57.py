def get_map_matrix() -> list[list[int]]:
    """
    Returns a matrix that represents the island.
    """
    map_matrix = [list(map(int, list(input()))) for _ in range(10)]
    return map_matrix


def display_matrix(matrix: list[list[int]]) -> None:
    """
    Displays a matrix in terminal.
    :param matrix: The matrix map with islands.
    """
    print("\n" * 10)
    print("-" * 20)
    print("ISLAND".center(20))
    print("-" * 20)
    for i in range(10):
        for j in range(10):
            print(f"{matrix[i][j]} ", end="")
        print("")
    print("\n" * 10)


def visit_island(map_matrix: list[list[int]], i: int, j: int) -> None:
    """
    Mark island places with zero recursively.
    :param map_matrix: The matrix map with islands.
    :param i: line index.
    :param j: column index.
    """
    if (0 <= i <= 9) and (0 <= j <= 9) and map_matrix[i][j] == 1:
        map_matrix[i][j] = 0
        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1)]:
            di = i + dx
            dj = j + dy
            visit_island(map_matrix, di, dj)


def count_islands(map_matrix: list[list[int]]) -> int:
    """
    Counts the number of islands in the map matrix.
    :param map_matrix: The matrix map that represents the islands.
    :return: the integer number that represents the total of islands.
    """
    number_of_islands = 0
    for i in range(10):
        for j in range(10):
            if map_matrix[i][j] == 1:
                number_of_islands += 1
                visit_island(map_matrix, i, j)

    return number_of_islands


def island_counter_in_grid() -> None:
    """
    There are 10 vertical and horizontal squares on a plane. 
    Each square is painted blue and green. 
    Blue represents the sea, and green represents the land. 
    When two green squares are in contact with the top and bottom, or right 
    and left, they are said to be ground. 
    The area created by only one green square is called "island".
    This program reads the mass data and find the number of islands.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get from user the matrix.
    print(f">>> Put the island matrix below: \n")
    map_matrix = get_map_matrix()

    # Step 2: Analyse the islands from the matrix and count the number of islands.
    display_matrix(map_matrix)
    number_of_islands = count_islands(map_matrix)
    print(f">>> Number of islands: {number_of_islands}")


def main() -> None:
    island_counter_in_grid()


if __name__ == "__main__":
    main()
