from moviepy.editor import VideoFileClip
clip = VideoFileClip(r"res/Fan speed-3 1080p 60fps.mp4")
duration = clip.duration  # in secs
print(f"duration: {duration}")
real_fps = (clip.fps)/1.001
print(f"clip.fps: {clip.fps}")
print(f"real_fps: {real_fps}")
tot_frames = real_fps * duration
print(f"tot_frame: {tot_frames}")
def fram_diff(frame1, frame2):
    return((frame1/real_fps)-(frame2/real_fps))



