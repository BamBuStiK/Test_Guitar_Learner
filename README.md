# Test_Guitar_Learner
Making an app for an easier way to learn guitar
Guitar Chord Detection for Guitar Noobs

1. Extract youtube video and extract frames from it.(o)

Libraries: pytube or youtube_dl => youtube_dlc(updated and working version)
Turns out that this extracts only the video and not the audio. However considering
we only need to identify the neck it may not be much of a problem.
Still when finding what chord a hand shape looks like, we may need to
have a separate folder for collecting the audio as well if we are to use it
as a backup measure to match the chord.

2. Apply object detection using SSD to detect the neck of the guitar.

Libraries:
SSD: You can use SSD implementation from frameworks like TensorFlow or OpenCV.
YOLO: Implementations such as Darknet, YOLOv5, or YOLOv4.

3. Post process the parts of the detected neck of the guitar.

Techniques:
Non-maximum suppression (NMS) to filter overlapping bounding boxes.
Refinement of bounding box coordinates.

4. Within the bounding box of the neck of the guitar, you then track the hand 
and detect what chord the guitarist is playing.

Libraries:
MediaPipe: Offers hand tracking solutions.

5. Once identifying, post process the result like also recognizing the sound and see
if the identified chord sound is the same with what is played in the video.

Libraries:
Chordino: For chord recognition from audio signals.
LibROSA: For audio analysis and feature extraction.

6. Create UI where the app would show the exact or recommended chords on how to
play that certain sound on that certain frame.

Libraries:
Tkinter, PyQt, or Kivy for Python-based GUI development.
