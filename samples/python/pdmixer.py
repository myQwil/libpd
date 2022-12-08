from numpy import zeros ,int16
from pygame import mixer ,sndarray
from struct import unpack
from pylibpd import *

CHANNELS   = 2
BLOCKSIZE  = libpd_blocksize()
BUFFERSIZE = BLOCKSIZE * 32

mixer.init()
m = PdManager(1, CHANNELS, mixer.get_init()[0], 1)

# this is basically a dummy since we are not actually going to read from the mic
inbuf = array.array('h', range(BLOCKSIZE))

# the pygame channel that we will use to queue up buffers coming from pd
ch = mixer.Channel(0)
# python writeable sound buffers
sounds = [mixer.Sound(zeros((BUFFERSIZE, CHANNELS), int16)) for _ in range(2)]
samples = [sndarray.samples(s) for s in sounds]

block = BLOCKSIZE * CHANNELS
i = block
selector = 0

def open(name):
	patch = libpd_open_patch(name, '.')
	print("$0: ", patch)
	return patch

def iter():
	global selector, i
	# we have run out of things to play, so queue up another buffer of data from Pd
	if not ch.get_queue() or not ch.get_busy():
		# make sure we fill the whole buffer
		for x in range(BUFFERSIZE):
			# let's grab a new block from Pd each time we're out of BLOCKSIZE data
			if i >= block:
				outbuf = m.process(inbuf)
				outbuf = unpack('h' * (len(outbuf) // 2), outbuf)
				i = 0
			# de-interlace the data coming from libpd
			for c in range(CHANNELS):
				samples[selector][x][c] = outbuf[i + c]
			i += CHANNELS
		# queue up the buffer we just filled to be played by pygame
		ch.queue(sounds[selector])
		# next time we'll do the other buffer
		selector = int(not selector)
