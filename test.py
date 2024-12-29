import unittest
from snake_game import main  # فرضًا يكون لديك دالة main في ملف snake_game.py

class TestSnakeGame(unittest.TestCase):

    def test_snake_growth(self):
        # فرضًا يمكنك اختبار نمو الثعبان بعد تناول الطعام
        initial_length = len(snake)
        snake_grow()  # دالة مفترضة لزيادة طول الثعبان
        self.assertGreater(len(snake), initial_length)

    def test_collision(self):
        # فرضًا إذا كان الثعبان يصطدم بالجدار أو العائق
        self.assertTrue(check_collision(snake, obstacles))

if __name__ == "__main__":
    unittest.main()