import math
import json
from moviepy.editor import VideoFileClip
from statistics import mean

# find_fps
# def fram_diff(frame1, frame2):
#     # if (flag == 0):
#     #     clip = VideoFileClip(r"res/Fan speed-3 1080p 60fps.mp4")
#     #     flag = (clip.fps)/1.001
#     return((frame1-frame2)/59.94)

def fps(file_path):
    clip = VideoFileClip(file_path)
    real_fps = (clip.fps)/1.001
    return real_fps

def fram_diff(frame1, frame2, real_fps):
    return((frame1/real_fps)-(frame2/real_fps))


def lengthSquare(X, Y):
    xDiff = X[0] - Y[0]
    yDiff = X[1] - Y[1]
    return xDiff * xDiff + yDiff * yDiff


def angular_displacement(A, B, C):
    """ 
    A = center_point: this is a tuple of form (x,y)
    B = pt1: this is point on circle of form (x,y)
    C = pt2: another point on circle of form (x,y)
    return: floating point alpha value at the center of circle
    """
    a = math.dist(B, C)
    b = math.dist(A, C)
    c = math.dist(A, B)
    # print(a)
    # print(b)
    # print(c)
    # Square of lengths be a2, b2, c2
    a2 = lengthSquare(B, C)
    b2 = lengthSquare(A, C)
    c2 = lengthSquare(A, B)

    # From Cosine law
    alpha = math.acos((b2 + c2 - a2) /
                      (2 * b * c))
    # print(alpha)

    # Converting to degree
    alpha = alpha * 180 / math.pi
    # print("alpha : %f" % (alpha))
    return(alpha)

print("processing whole data to get the average rpm (please wait)...")
angular_displacement((0, 0), (1, 0), (0, 1))

data = []
circle_center = [876.403, 563.273]
with open(r'data.json', 'r') as json_file:
    data = json.load(json_file)

rpm = []
file_name = ''
slowmo_flag= input("Enter if the video is slowmo or not (Y/N)")

with open('file_name.json', 'r') as json_file:
    file_name = json.load(json_file)

fps_val = fps(file_name)
for i in range(1, len(data)):
    angular_displacement_value = angular_displacement(
        circle_center, data[i]["circle_adjusted_point"], data[i-1]["circle_adjusted_point"])
    timediff = fram_diff(data[i]['frame_no'], data[i-1]['frame_no'], fps_val)
    print(
        f'frames: {data[i]["frame_no"]}, {data[i-1]["frame_no"]} angular displacement:{angular_displacement_value} time take: {timediff} rpm: {(angular_displacement_value/360)/(timediff/60)}')

    rpm.append((angular_displacement_value/360)/(timediff/60)*2)
if (slowmo_flag == 'Y') or (slowmo_flag == 'y'):
    slowmo_fps = int(input("Enter the slowmo fps: "))
    print(f'The rpm of rotating object is : {(mean(rpm)*(slowmo_fps/fps_val)):.3f}')
else:
    print(f'The rpm of rotating object is : {(mean(rpm)):.3f}')


# print(fram_diff(1,2,fps_val))


# alpha/360 = rotation
# time
# rpm = rotation/time