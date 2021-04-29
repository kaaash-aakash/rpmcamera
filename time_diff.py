from moviepy.editor import VideoFileClip
clip = VideoFileClip("fs3_60.mp4")
duration = clip.duration  # in secs
real_fps = (clip.fps)/1.001
tot_frames = real_fps * duration
def fram_diff(frame1, frame2):
    return((frame1/real_fps)-(frame2/real_fps))



