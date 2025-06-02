Plays a mp3 file as long as the damper (from a MIDI input) is pressed.
Each time the damper is pressed, the track is rewinded of half a second.


# Usage

python3 play_on_damper.py path-to-audio-file

Then the script asks which midi input to use.

# Requirements 

python3 with pyglet (for playing mp3) and pygame (for midi input).
pygame can play mp3 but cannot change the current position in a mp3 file.
