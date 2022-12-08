import pygame as pg
import pdmixer as pd
from os import environ

SCREENSIZE = (640, 480)

environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
screen = pg.display.set_mode(SCREENSIZE)

pd.open('funtest.pd')

rectangles = []
rectcolor = (255, 0, 0)
bg = (255, 255, 255)
rectsize = 200

def updatexy(event):
	pd.libpd_float('x', float(event.pos[1]) / SCREENSIZE[1])
	pd.libpd_float('y', float(event.pos[0]) / SCREENSIZE[0])
	pd.libpd_bang('trigger')
	rectangles.append([event.pos, 0])

# we go into an infinite loop selecting alternate buffers and queueing them up
# to be played each time we run short of a buffer
ms = 0
clock = pg.time.Clock()
quit = False
while not quit:
	pd.iter()

	for event in pg.event.get():
		if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == 27:
			quit = True

		if event.type == pg.MOUSEBUTTONDOWN:
			updatexy(event)

	screen.fill(bg)
	delrects = []
	for r in rectangles:
		dr = pg.Rect(r[0][0], r[0][1], r[1], r[1])
		dr.center = r[0]
		cv = 255 * (rectsize - r[1]) / rectsize
		pg.draw.rect(screen, (255, 255 - cv, 255 - cv), dr, 2)
		r[1] += ms
		if r[1] >= rectsize:
			delrects.append(r)

	for r in delrects:
		rectangles.remove(r)

	pg.display.flip()
	ms = clock.tick(60)

pd.libpd_release()
