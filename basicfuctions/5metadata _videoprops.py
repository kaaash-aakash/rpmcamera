from videoprops import get_video_properties

# props = get_video_properties('res/fidget.mp4')
props = get_video_properties(r'res/fan30fpsAniketMobile.mp4')

print(f'''
    Codec: {props['codec_name']}    
    Resolution: {props['width']}×{props['height']}
    Frame rate: {props['avg_frame_rate']}
''')    

# Aspect ratio: {props['display_aspect_ratio']}