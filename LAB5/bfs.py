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

    tree_matrix= bfs(directed_matrix,NUM_VERTICES)
    print_matrix(tree_matrix)
    draw_graph(tree_matrix, True,'red')

    turtle.exitonclick()

def bfs(matrix, num_vert):
    tree_matrix= [[0 for _ in range(num_vert)] for _ in range(num_vert)]
    new_vertnum = [1]
    visit_check = [False for i in range(num_vert)]
    visit_check[0] = True
    q = [0]

    while q:
        active = q.pop(0)

        for visit in range(num_vert):
            if matrix[visit][active] == 1 and not visit_check[visit] :
                tree_matrix[visit][active]=1
                visit_check[visit]=True
                new_vertnum.append(visit+1)
                q.append(visit)

                print('Active=',active,'Visited=',visit,'Queue=',q)
                keyboard.wait('Ctrl')

    return tree_matrix


if __name__ == '__main__':
    main()