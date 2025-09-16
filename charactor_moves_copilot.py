from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 경로 좌표
rect_points = [
    (50, 90),      # 왼쪽 아래
    (750, 90),     # 오른쪽 아래
    (750, 510),    # 오른쪽 위
    (50, 510)      # 왼쪽 위
]
rect_speed = 5

# 삼각형 경로 좌표
triangle_points = [
    (400, 510),   # 위쪽 꼭짓점
    (100, 90),    # 왼쪽 아래 꼭짓점
    (700, 90)     # 오른쪽 아래 꼭짓점
]
triangle_speed = 5

# 원 경로 정보
circle_center = (400, 300)
circle_radius = 210
circle_speed = 0.02

while True:
    # 1. 사각형 운동
    for i in range(4):
        x1, y1 = rect_points[i]
        x2, y2 = rect_points[(i + 1) % 4]
        dx = x2 - x1
        dy = y2 - y1
        distance = math.hypot(dx, dy)
        steps = int(distance // rect_speed)
        for step in range(steps):
            x = x1 + dx * (step / steps)
            y = y1 + dy * (step / steps)
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            delay(0.01)

    # 2. 삼각형 운동
    for i in range(3):
        x1, y1 = triangle_points[i]
        x2, y2 = triangle_points[(i + 1) % 3]
        dx = x2 - x1
        dy = y2 - y1
        distance = math.hypot(dx, dy)
        steps = int(distance // triangle_speed)
        for step in range(steps):
            x = x1 + dx * (step / steps)
            y = y1 + dy * (step / steps)
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            delay(0.01)

    # 3. 원 운동 (시계 방향)
    for degree in range(0, 360, int(circle_speed * 180 / math.pi * 10)):
        rad = math.radians(-degree)  # 시계 방향
        x = circle_center[0] + circle_radius * math.cos(rad)
        y = circle_center[1] + circle_radius * math.sin(rad)
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)

close_canvas()

