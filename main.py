import pygame as pg

pg.init()
pg.display.set_caption("Pygame Game Window")
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True

while running:
    # Check for game events.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Fill the screen with grey color.
    screen.fill((180, 180, 180))

    # Update the screen.
    pg.display.update()

    # Tick rate
    clock.tick(60)

pg.quit()