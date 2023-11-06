import pygame as pg
import screen_brightness_control as sbc

# Create the window
window = pg.display.set_mode()
pg.display.set_caption('Лампа')

# Settings
color = (255, 255, 255)
is_shift = False
Clock = pg.time.Clock()
pg.mouse.set_visible(False)
light = 100
game_loop = True

# Main loop
while game_loop:
    window.fill(color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_loop = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if color == (0, 0, 0):
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
            elif event.key in [pg.K_LSHIFT, pg.K_RSHIFT]:
                if color == (0, 0, 0):
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
            elif event.key == pg.K_UP:
                if light <= 95:
                    light += 5
            elif event.key == pg.K_DOWN:
                if light >= 5:
                    light -= 5

            elif event.key in [pg.K_LCTRL, pg.K_RCTRL]:
                pg.mouse.set_visible(True)

        elif event.type == pg.KEYUP:
            if event.key in [pg.K_LSHIFT, pg.K_RSHIFT]:
                if color == (0, 0, 0):
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
                    
            elif event.key in [pg.K_LCTRL, pg.K_RCTRL]:
                pg.mouse.set_visible(False)

    sbc.set_brightness(light)

    pg.display.update()
    Clock.tick(5)

sbc.set_brightness(100)

pg.quit()