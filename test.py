import unittest
import random
from io import StringIO
import curses

# فرضًا أنك قمت بتقسيم الكود إلى وظائف بحيث يسهل اختبارها

class TestSnakeGame(unittest.TestCase):
    
    def test_snake_growth(self):
        # فرضًا نتحقق من زيادة طول الثعبان بعد تناول الطعام
        initial_length = len(snake)
        # المحاكاة: تناول الطعام
        snake_grow()  # هنا نفترض أنه يوجد دالة لزيادة طول الثعبان
        self.assertGreater(len(snake), initial_length)
    
    def test_collision(self):
        # فرضًا اختبار الاصطدام بالجدران أو العوائق
        snake = [[5, 5]]
        obstacles = [[5, 6]]
        self.assertTrue(check_collision(snake, obstacles))  # نفترض أن هذه دالة تتحقق من الاصطدام
    
    def test_score_and_level_increase(self):
        # فرضًا نختبر زيادة النقاط والمستوى بعد تناول الطعام
        initial_score = score
        snake_grow()  # محاكاة تناول الطعام
        self.assertGreater(score, initial_score)
        if score % 5 == 0:
            self.assertGreater(level, 1)

    def test_movement(self):
        # محاكاة الحركة باستخدام مفاتيح الأسهم
        current_pos = snake[0]
        key = curses.KEY_RIGHT
        move_snake(key)  # دالة مفترضة لتحريك الثعبان
        new_pos = snake[0]
        self.assertEqual(new_pos[1], current_pos[1] + 1)  # إذا كانت الحركة إلى اليمين

if __name__ == "__main__":
    unittest.main()
