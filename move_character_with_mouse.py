from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
fx, fy = x, y
frame = 0
n = 0
MAX_n = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0
cx = 0
cy = 0
click_coordinateX = []
click_coordinateY = []

def handle_events():
    global running, click_coordinateX, click_coordinateY, MAX_n, x1, x2, y1, y2, n, cx ,cy

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cx = event.x
            cy = TUK_HEIGHT - event.y - 1
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click_coordinateX.append(event.x)
                click_coordinateY.append(TUK_HEIGHT - event.y - 1)
                MAX_n += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_char():
    global TUK_ground, character, arrow, frame, x, y, n, x1, x2, click_coordinateX, click_coordinateY

    clear_canvas()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for j in range(n, MAX_n, 1):
        arrow.draw(click_coordinateX[j], click_coordinateY[j])
    if x1 < x2:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    arrow.draw(cx, cy)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.01)

def character_move():
    global x, y, x1, x2, y1, y2, n, MAX_n, click_coordinateX, click_coordinateY

    if n != MAX_n:
        x1, y1 = x, y
        x2, y2 = int(click_coordinateX[n]), int(click_coordinateY[n])

    for i in range(0, 300+1, 3):
        handle_events()
        t = i / 300
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        draw_char()
    x = click_coordinateX[n]
    y = click_coordinateY[n]
    n += 1


def main():
    hide_cursor()
    global n

    while running:
        if n != MAX_n:
            character_move()
        else:
            handle_events()
            draw_char()
    close_canvas()

if __name__ == "__main__":
    main()



