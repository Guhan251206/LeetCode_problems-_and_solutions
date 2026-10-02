class Solution:
    def dayOfYear(self, date: str) -> int:
        
        pre=[0,31,59,90,120,151,181,212,243,273,304,334,365]
        y,m,d=map(int,date.split('-'))
        t=pre[m-1]
        t+=d
        if m>2 and ((y%4==0 and y%100!=0) or y%400==0):
            t+=1
        return t