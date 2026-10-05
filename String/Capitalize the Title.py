class Solution:
    def capitalizeTitle(self, s: str) -> str:
        arr=s.split()
        for i in range(len(arr)):
            if len(arr[i])>2:
                arr[i]=arr[i].title()
            else:
                arr[i]=arr[i].lower()
        return ' '.join(arr)