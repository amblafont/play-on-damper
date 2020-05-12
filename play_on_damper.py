
# https://github.com/pyglet/pyglet/blob/master/examples/media_player.py

from __future__ import print_function


import os
import sys
import pygame.midi
import pyglet

# length of rewind in seconds at each damper stroke
STEP_S = 0.5



def damper_event(media, switch):
   if switch:
       newtime = media.time - STEP_S
       media.seek(newtime)
       media.play()
   else:
       media.pause()
   print(media.time)


# inspired by 
# https://github.com/bgr/midistuff/blob/master/midis2events.py
CONTROLLER_CHANGE = 3
DAMPER = 64
def call_callback(media, midi_event):
        ((status, note_number, velocity, data3), timestamp) = midi_event

        if status == 0xFF:
            # pygame doesn't seem to get these, so I didn't decode
            command = "META"
            channel = None
        else:
            try:
                command = (status & 0x70) >> 4
            except:
                command = status & 0x70
            channel = status & 0x0F
        if command == CONTROLLER_CHANGE and int(note_number) == DAMPER:
            damper_event(media, int(velocity) >= 64)


filename = sys.argv[1]
print("Playing", filename)
print()


pygame.midi.init()
print("List of midi devices:")
for n in range(pygame.midi.get_count()):
    print (n,pygame.midi.get_device_info(n))
print()
n = int(input("Your choice (MIDI number id): "))

media = pyglet.media.Player()
my_input = pygame.midi.Input(n) 


def check_midi_event(dt):
        while my_input.poll():
            event = my_input.read(1)[0]
            call_callback(media, event)

media.queue(pyglet.media.load(filename))
media.play()

# call check_midi_event every 0.1s
pyglet.clock.schedule_interval(check_midi_event, 0.1)
pyglet.app.run()

