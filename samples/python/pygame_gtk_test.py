import pdmixer as pd
from pygame import time
from threading import Thread

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

pd.open('funtest.pd')

# our loop runs in a separate thread to avoid conflict with the GTK window
running = True
def loop():
	clock = time.Clock()
	while running:
		pd.iter()
		clock.tick(60)
	pd.libpd_release()

class MyWindow(Gtk.Window):
	def __init__(self):
		super().__init__(title="Hello World")

		self.set_default_size(250 ,50)
		self.button = Gtk.Button(label="Click Here")
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)

		Thread(target=loop).start()

	def on_button_clicked(self, widget):
		pd.libpd_bang('random')

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

# when window closes
running = False
