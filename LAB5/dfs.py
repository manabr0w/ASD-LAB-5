import turtle
import keyboard

from constants import SEED, NUM_VERTICES, K
from matrix_utils import (print_matrix, create_directed_matrix)
from graph import draw_graph


def main():
    directed_matrix = create_directed_matrix(SEED, NUM_VERTICES, K)
    print('Directed matrix:')
    print_matrix(directed_matrix)
    draw_graph(directed_matrix, True)

    tree_matrix = dfs(directed_matrix, NUM_VERTICES)
    print_matrix(tree_matrix)
    draw_graph(tree_matrix, True, 'red')

    turtle.exitonclick()

def dfs(matrix, num_vert):
    global tree_matrix
    tree_matrix= [[0 for _ in range(num_vert)] for _ in range(num_vert)]
    new_vertnum = [1]
    visit_check = [False for i in range(num_vert)]
    visit_check[0] = True

    def dfs_count(matrix,active):
        global tree_matrix

        for visit in range(num_vert):
            if matrix[visit][active] == 1 and not visit_check[visit]:
                tree_matrix[visit][active] = 1
                visit_check[visit] = True
                new_vertnum.append(visit + 1)
                print('Active=', active, 'Visited=', visit)
                keyboard.wait('Ctrl')
                dfs_count(matrix,visit)

    dfs_count(matrix, 0)
    return tree_matrix


if __name__ == '__main__':
    main()