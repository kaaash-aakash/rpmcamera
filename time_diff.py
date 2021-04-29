from moviepy.editor import VideoFileClip


def fram_diff(frame1, frame2):

    clip = VideoFileClip(r"res/Fan speed-3 1080p 60fps.mp4")
    real_fps = (clip.fps)/1.001
    return((frame1/real_fps)-(frame2/real_fps))
