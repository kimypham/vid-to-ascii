"""
The main file to be called which takes in a video and 'plays' it in the
terminal by extracting and converting each frame to ascii art, and printing
them in time with the audio.
"""

__author__ = "Kim Yen Pham"

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # supress the welcome message from pygame
import pygame
import time
import json
from extract_vid import video_to_frames
from convert_to_ascii import frames_to_ascii


def get_num_frames(video: str) -> int:
    """Get the total number of frames extracted from the video.
    
    :param video: a string containing the name of the input mp4 video
    without its .mp4 extension to be converted and played.
    :returns: an integer representing the number of frames in the video."""
    path = video + "_frames"
    files = os.listdir(path) # a list of files

    files_list = []
    for file in files:
        filt = filter(str.isdigit, file) # filters out everything besides numbers
        files_list += [int("".join(filt))] # list contains all frame numbers
    files_list.sort() # sorts in ascending order
    return files_list[-1] # the last frame is also the total number of frames


def setup(video: str) -> list:
    """Take in a video, extract each frame and convert each frame to ascii art.

    1.  Convert video to frames using video_to_frames()
        --> creates (video)_frames folder
    2.  Convert frames to ascii using frames_to_ascii()
        --> creates (video)_ascii_frames.txt
    3.  Load ascii frames from (video)_ascii_frames.txt to a list ready for
        play using player()
    Assumes (video)_ascii_frames.txt only exists if frames_to_ascii has
    successfully run
    Assumes (video)_frames only exists if video_to_frames has successfully run
    
    :param video: a string containing the name of the input mp4 video
    without its .mp4 extension to be converted and played.
    :returns: a list containing strings of ascii characters, with each item
    in the list representing a frame of the original video.
    """
    if not os.path.exists(video + ".mp4"):
        raise Exception("Video file not found")

    # Extracts video frames and saves each frame to a folder
    # If this has already run successfully, a folder named (video)_frames
    # exists and this step can be skipped.
    if not os.path.exists(video + "_frames"):
        print("Extracting video frames...\nThis may take some time, please wait...")
        video_to_frames(video)
        print("All frames extracted successfully!")

    # Converts each frame to ascii art and saves it to a textfile
    # If this has already run successfully, a textfile named 
    # (video)_ascii_frames.txt exists and this step can be skipped.
    if not os.path.exists(video + "_ascii_frames.txt"):
        print("Converting frames to ascii...\nThis may take some time, please wait...")
        num_frames = get_num_frames(video)
        frames_to_ascii(video, num_frames)
        print("All frames converted successfully!")

   # Reads in each frame from (video)_ascii_frames.txt 
    if os.path.exists(video + "_ascii_frames.txt"):
        with open(video + '_ascii_frames.txt', 'r') as filehandle:
            ascii_frames = json.load(filehandle)
    else:
        print("Cannot find find file containing ascii frames.")

    print("All frames loaded and ready to play!")
    return ascii_frames


def player(frame_rate: float) -> None:
    """Print all frames converted to ascii to the screen.

    Iterates through the list of ascii frames created by the function setup(),
    printing each frame to the terminal at the appropriate length of time as
    determined by frame_rate.

    :pre: the input video must be an mp4 file in the same directory.
    
    :param frame_rate: a float containing the frame rate the video should
    play at. An integer can also be used. This value should be adjusted
    accordingly depending on the device. (For example, the playback on
    my device is a bit slow, so instead of frame_rate = 30, which would
    be optimal, frame_rate = 30.875 instead to account for this lag.)
    """
    while True: # keep asking for input until a valid video name is entered
        video = input("Name of video file without its extension: ")
        try:
            ascii_frames = setup(video) # convert video to ascii frames stored in a list
        except Exception:
            print("Video file not found")
        else:
            break # exit loop
    
    play_music(video) # start playing the video's audio

    for frame in ascii_frames:
        start_time = time.time()
        print(frame)
        while time.time() - start_time < 1/frame_rate: # each frame shows for 1/frame_rate of a second
            pass


def play_music(video: str) -> None:
    """Play music in the background.

    :pre: the video's audio file must be in the same directory, must be
    called (video_name).mp3, where video_name is also the same name used
    for the original video input.
    
    :param video: a string containing the name of the input mp4 video
    without its .mp4 extension to be converted and played.
    """
    if not os.path.exists(video + ".mp3"):
        raise Exception("Audio file not found")
    pygame.init()
    pygame.mixer.music.load(video+".mp3")
    pygame.mixer.music.play()


if __name__ == "__main__":
    player(30.3875)
    #ascii_frames = setup("bad_apple")
    #print(ascii_frames[3045])
    
