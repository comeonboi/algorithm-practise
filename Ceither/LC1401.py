def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    # def incircle(x,y):
    #     return (x - xCenter) ** 2 + (y - yCenter) <= radius ** 2
    # def inrect(x,y):
    #     return x1 < x < x2 and y1 < y < y2
    # def onborder(x, y):
    #     return x1 <= x <= x2 and (y == y1 or y == y2) or y1 <= y <= y2 and (x == x1 or x == x2)
    # return incircle(x1, y1) or incircle(x1, y2) or incircle(x2, y1) or incircle(x2, y2) or inrect(xCenter, yCenter) or inrect(xCenter-radius, yCenter) or inrect(xCenter+radius, yCenter) or inrect(xCenter, yCenter+radius) or inrect(xCenter, y-radius) or onborder(xCenter, yCenter)
    x_min_dist = 0 if x1 <= xCenter <= x2 else min(abs(xCenter - x1), abs(xCenter - x2))
    y_min_dist = 0 if y1 <= yCenter <= y2 else min(abs(yCenter - y1), abs(yCenter - y2))

    return x_min_dist ** 2 + y_min_dist ** 2 <= radius ** 2