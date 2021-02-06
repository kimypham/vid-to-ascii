"""Contains a function to extract and save all frames from a given video."""

__author__ = "Kim Yen Pham"

import os
import cv2

def video_to_frames(video: str) -> None:
    """
    Converts each frame in a mp4 video to PNG images.

    Base code from OpenCV Python documentation.

    :pre: the input video must be an mp4 file in the same directory.
    :post: creates a file named (video)_frames only if all frames are saved.

    :param video: a string containing the name of the input mp4 video
    without its .mp4 extension to be converted and played.
    """ 
    img_path = "frames" # name of folder whilst frames are being saved
    finished_img_path = video + "_frames" # name of folder if all frames are saved

    # if (video_name)_frames folder exists, assumes that all frames have been saved
    if os.path.exists(finished_img_path):
        return # exit program if all frames extracted already

    elif not os.path.exists(img_path): # if temp folder hasn't already been made
        os.makedirs(img_path) # make temporary folder to store extracted frames
         
    cap = cv2.VideoCapture(video + ".mp4")  # takes in name of video

    image_no = 1
    while True:
        success, frame = cap.read() # reads in each frame
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # makes it grayscale

        if success: # if there is a frame that can be read in
            cv2.imwrite(f"frames/frame_{image_no}.png", frame) # saves frame

            print(f"Number of frames saved: {image_no}")
            image_no += 1
        else:
            break # exit if no more frames left

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    os.rename(img_path, finished_img_path) # rename folder containing frames from frames to (video)_frames
    # this is done to keep track of whether all frames have been successfully extracted or not