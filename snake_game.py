import curses
import random

def main(screen):
    # إعداد الشاشة
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # الطعام
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # الثعبان
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # النصوص
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)  # العوائق

    screen_height, screen_width = screen.getmaxyx()
    window = curses.newwin(screen_height, screen_width, 0, 0)
    window.keypad(True)
    window.timeout(100)

    # إعداد الثعبان والطعام
    snk_x = screen_width // 4
    snk_y = screen_height // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2],
    ]

    food = [screen_height // 2, screen_width // 2]
    window.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(1))

    # إعداد العوائق
    num_obstacles = 10  # عدد العوائق
    obstacles = []
    for _ in range(num_obstacles):
        while True:
            obstacle = [
                random.randint(1, screen_height - 2),
                random.randint(1, screen_width - 2)
            ]
            if obstacle not in snake and obstacle != food:
                obstacles.append(obstacle)
                window.addch(obstacle[0], obstacle[1], curses.ACS_VLINE, curses.color_pair(4))
                break

    # الإعدادات الأولية
    key = curses.KEY_RIGHT
    score = 0
    level = 1

    # تعليمات
    window.addstr(0, 2, "Welcome to Snake Game!", curses.color_pair(3))
    window.addstr(1, 2, "Use arrow keys to move. Press 'q' to quit.", curses.color_pair(3))

    while True:
        # عرض النقاط والمستوى
        window.addstr(0, 2, f'Score: {score} Level: {level} ', curses.color_pair(3))

        # الحصول على المفتاح
        next_key = window.getch()
        if next_key == ord('q'):
            break
        key = key if next_key == -1 else next_key

        # التحقق من الاصطدام
        if (snake[0][0] in [0, screen_height] or
                snake[0][1] in [0, screen_width] or
                snake[0] in snake[1:] or
                snake[0] in obstacles):
            curses.endwin()
            print(f"Game Over! Final Score: {score}, Level: {level}")
            quit()

        # تحريك الرأس
        new_head = [snake[0][0], snake[0][1]]
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1

        snake.insert(0, new_head)

        # تناول الطعام
        if snake[0] == food:
            score += 1
            if score % 5 == 0:
                level += 1
                window.timeout(max(10, 100 - (level * 10)))  # زيادة السرعة

            food = None
            while food is None:
                new_food = [
                    random.randint(1, screen_height - 2),
                    random.randint(1, screen_width - 2)
                ]
                if new_food not in snake and new_food not in obstacles:
                    food = new_food
            window.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(1))
        else:
            # إزالة الذيل
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        # رسم الرأس
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD, curses.color_pair(2))

    # رسالة نهاية اللعبة
    curses.endwin()
    print(f"Game Over! Final Score: {score}, Level: {level}")

# تشغيل اللعبة
curses.wrapper(main)
