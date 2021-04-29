import math

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

    # Square of lengths be a2, b2, c2
    a2 = lengthSquare(B, C)
    b2 = lengthSquare(A, C)
    c2 = lengthSquare(A, B)



    # From Cosine law
    alpha = math.acos((b2 + c2 - a2) /
                      (2 * b * c))
    print(alpha)

    # Converting to degree
    alpha = alpha * 180 / math.pi
    print("alpha : %f" % (alpha))

angular_displacement((0,0), (1,0), (0,1))
angular_displacement((0,0), (1,1), (0,2))
angular_displacement((0,0), (1,1), (0,1))
