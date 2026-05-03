from pygame import *
from random import randint


window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')

clock = time.Clock()
FPS = 60
run = True
finish = False

font.init()
my_font = font.SysFont("Arial", 35)
win = my_font.render("Вы победили!", True, (255, 255, 0))

while run:
    for e  in event.get():
        if e.type == QUIT:
            run = False
    window.fill((207, 147, 147))
    if not finish:
        pass
    display.update() 
    clock.tick(60)