import unittest
from maze import *
from cell import *
from graphics import *
from unittest.mock import MagicMock

class MazeTest(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        mock_window = MagicMock()
        mock_window._width = 800
        mock_window._height = 600

        m1 = Maze(0,0,num_rows,num_cols,10,10,mock_window)
        self.assertEqual(len(m1._cells),num_cols)
        self.assertEqual(len(m1._cells[0]),num_rows)

class CellTest(unittest.TestCase):
    def test_cell_initialization(self):
        cell = Cell()
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)

    def test_modify_walls(self):
        cell = Cell()
        cell.has_top_wall = False
        self.assertFalse(cell.has_top_wall)
        cell.has_bottom_wall = False
        self.assertFalse(cell.has_bottom_wall)

class MazeBoundaryTest(unittest.TestCase):
    def test_maze_dimensions_within_window(self):
        window_width = 800
        window_height = 600
        margin = 50
        num_rows = 10
        num_cols = 12
        cell_width = (window_width - 2 * margin) / num_cols
        cell_height = (window_height - 2 * margin) / num_rows

        mock_window = MagicMock()
        mock_window._width = window_width
        mock_window._height = window_height

        maze = Maze(margin, margin, num_rows, num_cols, cell_width, cell_height,mock_window)
        self.assertLessEqual(maze.num_rows * cell_height + margin, window_height)
        self.assertLessEqual(maze.num_cols * cell_width + margin, window_width)

class MazeAnimationTest(unittest.TestCase):
    def test_animate_method(self):

        mock_window = MagicMock()
        mock_window._width = 800
        mock_window._height = 600

        maze = Maze(0, 0, 10, 12, 10, 10,mock_window)
        try:
            maze._animate()
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

class CellMovementTest(unittest.TestCase):
    def test_draw_move(self):
        # Mock the Window object
        mock_window = MagicMock()
        
        # Create two cells with the mocked window
        cell1 = Cell(mock_window)
        cell2 = Cell(mock_window)
        
        # Set dummy coordinates for the cells
        cell1.draw(0, 0, 10, 10)
        cell2.draw(10, 0, 20, 10)
        
        # Call draw_move and ensure no exceptions occur
        try:
            cell1.draw_move(cell2)
            result = True
        except Exception as e:
            print(f"Error during test: {e}")
            result = False

        # Verify that draw_line was called on the mocked window
        mock_window.draw_line.assert_called()
        self.assertTrue(result)



if __name__ == "__main__":
    unittest.main()
