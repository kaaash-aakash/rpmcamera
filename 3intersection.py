import math
import json


def circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line=True, tangent_tol=1e-9):

    (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, circle_center
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2)**.5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2

    if discriminant < 0:  # No intersection between circle and line
        return []
    else:  # There may be 0, 1, or 2 intersections with the segment
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
        if not full_line:  # If only considering the segment, filter out intersections that do not fall within the segment
            fraction_along_segment = [
                (xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
            intersections = [pt for pt, frac in zip(
                intersections, fraction_along_segment) if 0 <= frac <= 1]
        # If line is tangent to circle, return just one point (as both intersections have same location)
        if len(intersections) == 2 and abs(discriminant) <= tangent_tol:
            return [intersections[0]]
        else:
            return intersections


def opposite_intersaction_point_delete(int_points, frame_point):
    if (math.dist(int_points[0], frame_point) < math.dist(int_points[1], frame_point)):
        return int_points[0]
    else:
        return int_points[1]


if __name__ == "__main__":
    circle_center = []  # temp
    circle_radius = 0
    with open('circle.json', 'r') as json_file:
        circle_list = json.load(json_file)
        circle_center = circle_list[0]
        circle_radius = (circle_list[1]+circle_list[2])/2

    frame_points = []

    with open('data.json', 'r') as json_file:
        frame_points = json.load(json_file)

    for frame_point in frame_points:
        frame_point_cordinate = (
            frame_point["center_x"], frame_point["center_y"])

        two_intersection_points = circle_line_segment_intersection(
            circle_center, circle_radius, circle_center, frame_point_cordinate)

        one_intersection_point = opposite_intersaction_point_delete(
            two_intersection_points, frame_point_cordinate)

        frame_point['circle_adjusted_point'] = one_intersection_point

    with open("data.json", "w") as json_file:
        json_file.write(json.dumps(frame_points, indent=4))

    print('point adjusted to the cicle and data stored in data.json')
