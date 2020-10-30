#An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

#Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

#Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

#example
#input=[0,0,2,2]
#      [1,1,3,3]
#output : True

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        A, B, C, D = rec1[0], rec1[1], rec1[2], rec1[3]
        E, F, G, H = rec2[0], rec2[1], rec2[2], rec2[3]
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        if x1 < x2 and y1 < y2:
            return True
        return False
