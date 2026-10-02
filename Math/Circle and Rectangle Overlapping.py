class Solution:
    def checkOverlap(self, radius: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1<=xc<=x2 and y1<=yc<=y2:
            return True
        if x1<=xc<=x2 and (abs(yc-y1)<=radius or abs(yc-y2)<=radius):
            return True
        if y1<=yc<=y2 and (abs(xc-x1)<=radius or abs(xc-x2)<=radius):
            return True
        if abs(xc-x1)<=radius and (abs(yc-y1)<=radius or abs(yc-y2)<=radius):
            return True
        if abs(xc-x2)<=radius and (abs(yc-y2)<=radius or abs(yc-y2)<=radius):
            return True
        
        return False