import pdmixer as pd
from pygame import time

pd.open('bloopy.pd')

# we go into an infinite loop selecting alternate buffers and queueing them up
# to be played each time we run short of a buffer
clock = time.Clock()
while(1):
	pd.iter()
	# cap the framerate
	clock.tick(60)
pd.libpd_release()
