"""Contains a function to convert frames to ascii art."""

__author__ = "Kim Yen Pham"

import os
import json
import PIL.Image


def frames_to_ascii(video: str, num_frames: int) -> None:
    """Convert a image to ascii art.
    
    Code loosely based off Alex Rowher's Python PIL tutorial: https://www.youtube.com/watch?v=v_raWlX7tZY&ab_channel=Kite

    :param video: a string containing the name of the input mp4 video
    without its .mp4 extension to be converted and played.
    :param num_frames: an integer representing the number of frames in the 
    video.
    """
    ASCII_CHARS = [" ", "-", ":", "!", "?", "S", "9", "8", "$", "&", "@"]
    
    WIDTH = 200 # number of characters to be displayed in a row
    SCALE = 2 # changes the height (eg. 1 makes the output squished)
    # WIDTH and SCALE depends on the font size and width, adjust accordingly.
    # Generally, the bigger width is, the more detailed the output is.
    # These settings were adjusted for Consolas Bold 10 px


    def rescale_img(im: PIL.Image, new_width: int=WIDTH, scale: float=SCALE) -> PIL.Image:
        """Rescale image.
        
        :param im: an Image object from the PIL.Image class that represents a
        single frame.
        :param new_width: an integer representing the number of characters to
        be displayed in a row.
        :param scale: an integer representing the scale of the output.
        :returns: a resized Image object from the PIL.Image class that represents a
        single frame, resized according to the given variable WIDTH.
        """
        width, height = im.size # get current width and height
        new_height = int(height * new_width / width / scale) # find new height, keeping the old ratios
        return im.resize((new_width, new_height)) # return resized frame


    def pixel_to_ascii(im: PIL.Image, new_width: int=WIDTH) -> str:
        """Convert a frame to a string of ascii characters.

        :param im: an Image object from the PIL.Image class that represents a
        single frame.
        :param new_width: an integer representing the number of characters to
        be displayed in a row.
        :returns: a string containing ascii characters representing every pixel
        in a frame.
        """
        im = im.convert("L") # convert frame to grayscale
        pixel_val = im.getdata() # get value of every pixel in frame
        frame = ""
        for i in range(len(pixel_val)): # for every pixel in a frame
            if i % new_width:
                frame += ASCII_CHARS[pixel_val[i]//25] # replace pixel value with respective ascii character
            else:
                frame += "\n" # if on the edge, print a new line
        return frame # return string of ascii characters


    def convert_all(video: str, num_frames: int) -> None:
        """
        Convert all frames of a video to ascii and save them to
        (video)_ascii_frames.txt.
        
        :pre: the input video must be an mp4 file in the same directory.
        :post: creates a file named (video)_ascii_frames.txt only if all frames
        are converted.

        :param video: a string containing the name of the input mp4 video.
        without its .mp4 extension to be converted and played.
        :param num_frames: an integer representing the number of frames in the
        video.
        """
        frame_path = "ascii_frames.txt" # name of file whilst frames are being converted
        finished_frame_path = video + "_ascii_frames.txt" # name of file if all frames are converted

        # For each frame, converts to ascii and saves to list.
        ascii_frames_list = []
        for number in range(1,num_frames): # for every frame
            path = f"{video}_frames/frame_{number}.png" # path for the frame
            try:
                frame = PIL.Image.open(path)
            except Exception:
                return("Unexpected error: Unable to find image")

            rescaled_frame = rescale_img(frame) # rescale the frame
            ascii_frames_list += [pixel_to_ascii(rescaled_frame)] # convert to ascii and add to list
            print("Number of frames converted to ascii: " + str(number))

        # Saves list to 'ascii_frames.txt'.
        # This is done so that the player can check for and load this text file
        # instead of having to convert all frames every time it runs in the
        # future.
        with open(frame_path, "w") as f:
            json.dump(ascii_frames_list, f)
        print("done")

        # Rename textfile containing frames from 'ascii_frames.txt' to
        # '(video)_ascii_frames.txt'.
        # The player only uses this textfile once all frames are converted
        # and saved successfully.
        os.rename(frame_path, finished_frame_path)

    convert_all(video, num_frames)