from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        M = len(classroom)
        N = len(classroom[0])
        litters = {}
        start = (0,0)
        maxEnergy = energy
        index = 0
        for i in range(M):
            for j in range(N):
                if classroom[i][j] == 'L':
                    litters[(i, j)] = index
                    index += 1
        if len(litters) == 0:
            return 0
        mask = (1 << index) - 1
        numMoves = 0
        for i in range(M):
            for j in range(N):
                if classroom[i][j] == 'S':
                    start = (i, j, mask, energy, numMoves)
       
        visited = [[[ -1 for _ in range(1<<index) ] for _ in range(N)] for _ in range(M)]
        visited[start[0]][start[1]][mask] = energy
        queue = deque([start])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while (queue):
            
            data = queue.popleft()
            sy, sx, mask, energy, numMoves = data[0], data[1], data[2], data[3], data[4]
            if (classroom[sy][sx] == 'R'):
                energy = maxEnergy
            elif (classroom[sy][sx] == 'L'):
                mask = mask & ~(1 << litters[(sy, sx)])
                if mask == 0:
                    return numMoves
            energy2 = energy-1
            for i, j in directions:
                if (sy + i) < 0 or (sy + i) >= M or (sx + j) < 0 or (sx + j) >= N:
                    continue
                else:
                    newy = sy+i
                    newx = sx+j
                    if energy2 < 0 and classroom[newy][newx] != 'R':
                        continue
                    numMoves2 = numMoves + 1
                    if visited[newy][newx][mask] < energy2 and classroom[newy][newx] != 'X':
                        visited[newy][newx][mask]=energy2
                        queue.append((newy, newx, mask, energy2, numMoves2))
        return -1