class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        row=len(image)
        col=len(image[0])
        for i in range(row):
            for j in range(col):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        ans=[]
        for x in image:
            ans.append(x[::-1])
        return ans