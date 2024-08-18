from maze.objects import Maze
import unittest


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    
    # def test_open_maze(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     m1._open_maze()
    #     self.assertEqual(
    #         m1._cells[0][0].top_wall, False
    #     )
    #     self.assertEqual(
    #         m1._cells[9][11].bottom_wall, False
    #     )

    # def test_maze_create_cells_2(self):
    #     num_cols = 1
    #     num_rows = 1
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_rows,
    #     )

    # def test_open_maze2(self):
    #     num_cols = 1
    #     num_rows = 1
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     m1._open_maze()
    #     self.assertEqual(
    #         m1._cells[0][0].top_wall, False
    #     )
    #     self.assertEqual(
    #         m1._cells[0][0].bottom_wall, False
    #     )

    # def test_maze_create_cells_3(self):
    #     num_cols = 15
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_rows,
    #     )

    # def test_open_maze3(self):
    #     num_cols = 15
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     m1._open_maze()
    #     self.assertEqual(
    #         m1._cells[0][0].top_wall, False
    #     )
    #     self.assertEqual(
    #         m1._cells[14][9].bottom_wall, False
    #     )

if __name__ == "__main__":
    unittest.main()