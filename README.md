# Video to ASCII converter/player
A fun project that takes a video and plays it in the terminal using ASCII
characters!

I loved the 'Bad Apple!!' MV when I was younger and decided to try recreate
it in the terminal. Although this project was optimised for this purpose,
it can be used to convert and play other videos as well.

## Demo
Here's 'Bad Apple!!' playing in terminal:

## How it works
The converter uses the OpenCV library to extract all frames from the input
video, then uses the Pillow library to convert every pixel from each frame to a
value according to its brightness.
The converter then replaces each pixel's value with a corresponding ASCII
character, and saves these converted frames in a textfile, ready for playing and
for future use (so we don't have to convert every frame again on future runs)!
To 'play' the video, the textfile is loaded, and each frame is printed to the
terminal for an specific length of time before the next frame is printed. This
allows for it to be played in time with the music and gives the illusion that
a video is being played!

### Note
Currently, this project only supports mp4 videos as input.
It also is somewhat 'jittery' when printing frames and does fall out of sync
with its audio when playing depending on the CPU usage of the device.

I'm not too sure how to fix the jitteriness of the output.
Perhaps in a future update, the lag could be accounted for by timing and displaying frames at a quicker slower rate so that the video is always in sync with the audio.

## Installation
This project requires some Python modules to run:
- Pygame
- OpenCV (cv2)
- Pillow (PIL)


