from typing import List, Optional
import copy

class PointUpdateRangeRequest_1:
    def __init__(self, init : List[int]):
        self.start = 1
        self.size = len(init)
        while self.start < self.size:
            self.start *= 2

        treeSize = 2*self.start

        # invariant : tab[i] = tab[2*i] + tab[2*i+1] si i > 0 (et qu'on ne sort pas de la hiérarchie)
        self.tab = [0 for _ in range(treeSize)]
        for k_init in range(self.size):
            self.tab[self.start + k_init] = init[k_init]
        for k in range(self.start-1, 0, -1):
            self.tab[k] = self.tab[2*k] + self.tab[2*k+1]

    def add(self, pos : int, val : int) -> None:
        """ ajoute $val à la position $pos et dans les intervalles correspondants """

        if (pos < 0 or pos >= self.size):
            return
        pos += self.start
        while pos >= 1:
            self.tab[pos] += val
            pos //= 2

    def getSumBefore(self, pos : int) -> int:
        if (pos <= 0 or pos > self.size):
            return 0
        if (pos == self.size):
            return self.tab[1]

        pos += self.start
        actuSum = 0
        while pos > 1:
            if pos % 2 == 0:
                pos //= 2
            else:
                actuSum += self.tab[pos - 1]
                pos //= 2
        return actuSum

    def getInterval(self, start : int, end : int) -> int:
        return self.getSumBefore(end) - self.getSumBefore(start)

    def display(self) -> List[int]:
        accu = [self.getSumBefore(k+1) for k in range(self.size)] + [0]
        normal = [accu[k] - accu[k-1] for k in range(self.size)]
        return normal

class RangeUpdatePointRequest_1:
    def __init__(self, init : List[int]):
        self.size = len(init)
        init = init.copy()
        for k in range(self.size-1,0,-1):
            init[k] -= init[k-1]
        self.diff = PointUpdateRangeRequest_1(init)

    def getValAt(self, pos : int) -> int:
        return self.diff.getSumBefore(pos+1)

    def addInterval(self, start : int, end : int, val : int) -> None:
        self.diff.add(start, val)
        self.diff.add(end, -val)

    def display(self) -> List[int]:
        normal = [self.getValAt(k) for k in range(self.size)]
        return normal

class RangeUpdateRangeRequest_1:
    def __init__(self, init : List[int]):
        self.size = len(init)
        self.const = RangeUpdatePointRequest_1(init)
        self.linear = RangeUpdatePointRequest_1([0]*self.size)

    def getSumBefore(self, pos : int) -> int:
        return self.const.getValAt(pos-1) + (pos-1) * self.linear.getValAt(pos-1)

    def getInterval(self, start : int, end : int) -> int:
        return self.getSumBefore(end) - self.getSumBefore(start)

    def addInterval(self, start : int, end : int, val : int) -> None:
        self.linear.addInterval(start, end, val)
        self.const.addInterval(start, end, (1-start) * val)
        self.const.addInterval(end, self.size, (end-start) * val)

    def display(self) -> List[int]:
        accu = [self.getSumBefore(k+1) for k in range(self.size)] + [0]
        normal = [accu[k] - accu[k-1] for k in range(self.size)]
        return normal

class PURR_2:
    def __init__(self, init : List[List[int]]):
        self.sizeX : int = len(init)
        self.sizeY : int = len(init[0])

        if sum(1 if len(init[k]) != self.sizeY else 0 for k in range(self.sizeX)) != 0:
            raise Exception("Not square matrix")

        self.startX : int = 1
        while self.startX < self.sizeX:
            self.startX *= 2

        treeSize = 2*self.startX

        # invariant : tab[i] = tab[2*i] + tab[2*i+1] si i > 0, mais tab[i] est un arbre binaire...
        self.tab : List[Optional[PointUpdateRangeRequest_1]] = [None for _ in range(treeSize)]
        for k_init in range(self.sizeX):
            self.tab[self.startX + k_init] = PointUpdateRangeRequest_1(init[k_init])
        for k in range(self.startX - 1, 0, -1):
            self.tab[k] = copy.deepcopy(self.tab[2*k])
            if self.tab[2*k + 1] is not None:
                assert self.tab[k] is not None
                for m in range(len(self.tab[k].tab)):
                    self.tab[k].tab[m] += self.tab[2*k+1].tab[m]

    def getSumBefore(self, x : int, y : int) -> int:
        if (x <= 0 or x > self.sizeX):
            return 0
        if (x == self.sizeX):
            return self.tab[1].getSumBefore(y)

        x += self.startX
        actuSum = 0
        while x > 1:
            if x % 2 == 0:
                x //= 2
            else:
                actuSum += self.tab[x - 1].getSumBefore(y)
                x //= 2
        return actuSum

    def getRect(self, startX : int, endX : int, startY : int, endY : int) -> int:
        return self.getSumBefore(endX,endY) - self.getSumBefore(endX,startY) - self.getSumBefore(startX,endY) + self.getSumBefore(startX,startY)

    def add(self, x : int, y : int, val : int) -> None:
        """ ajoute $val à la position (x,y) et dans les rectangles correspondants """

        if (x < 0 or x >= self.sizeX):
            return
        x += self.startX
        while x >= 1:
            self.tab[x].add(y,val)
            x //= 2

    def display(self) -> None:
        cumul : List[List[int]] = [[self.getSumBefore(x+1,y+1) for y in range(self.sizeY)] + [0] for x in range(self.sizeX)] + [[0]*self.sizeY]
        normal : List[List[int]] = [[cumul[x][y] - cumul[x][y-1] - cumul[x-1][y] + cumul[x-1][y-1]  for y in range(self.sizeY)] for x in range(self.sizeX)]
        for x in normal:
            print(x)

class RUPR_2:
    def __init__(self, init : List[List[int]]):
        self.sizeX = len(init)
        self.sizeY = len(init[0])
        init = copy.deepcopy(init)
        for x in range(self.sizeX - 1, 0, -1):
            for y in range(self.sizeY - 1, 0, -1):
                init[x][y] = init[x][y] - init[x][y-1] - init[x-1][y] + init[x-1][y-1]
            init[x][0] = init[x][0] - init[x-1][0]
        for y in range(self.sizeY - 1, 0, -1):
            init[0][y] = init[0][y] - init[0][y-1]
        self.diff = PURR_2(init)

    def getValAt(self, x : int, y : int) -> int:
        return self.diff.getSumBefore(x+1,y+1)

    def addRect(self, startX : int, endX : int, startY : int, endY : int, val : int) -> None:
        self.diff.add(startX, startY,  val)
        self.diff.add(startX,   endY, -val)
        self.diff.add(  endX, startY, -val)
        self.diff.add(  endX,   endY,  val)

    def display(self) -> None:
        normal : List[List[int]] = [[self.getValAt(x,y)  for y in range(self.sizeY)] for x in range(self.sizeX)]
        for x in normal:
            print(x)
        
class RURR_2:
    def __init__(self, init : List[List[int]]):
        self.sizeX = len(init)
        self.sizeY = len(init[0])
        self.const = RUPR_2(init)
        self.linX = RUPR_2([[0]*self.sizeY]*self.sizeX)
        self.linY = RUPR_2([[0]*self.sizeY]*self.sizeX)
        self.bilin = RUPR_2([[0]*self.sizeY]*self.sizeX)

    def getSumBefore(self, x : int, y : int) -> int:
        return self.const.getValAt(x-1,y-1) + x*self.linX.getValAt(x-1,y-1) + y*self.linY.getValAt(x-1,y-1) + x*y*self.bilin.getValAt(x-1,y-1)

    def getRect(self, startX : int, endX : int, startY : int, endY : int) -> int:
        return self.getSumBefore(endX,endY) - self.getSumBefore(endX,startY) - self.getSumBefore(startX,endY) + self.getSumBefore(startX,startY)

    def addRect(self, startX : int, endX : int, startY : int, endY : int, val : int) -> None:
        dX = (endX-startX)
        dY = (endY-startY)

        self.bilin.addRect(startX,endX,startY,endY, val)
        self.linX .addRect(startX,endX,startY,endY, -startY*val)
        self.linY .addRect(startX,endX,startY,endY, -startX*val)
        self.const.addRect(startX,endX,startY,endY, startY*startY*val)
        
        self.linX .addRect(startX,endX,endY,self.sizeY+1, dY*val)
        self.const.addRect(startX,endX,endY,self.sizeY+1, -startX*dY*val)

        self.linY .addRect(endX,self.sizeX+1,startY,endY, dX*val)
        self.const.addRect(endX,self.sizeX+1,startY,endY, -startY*dX*val)

        self.const.addRect(endX, self.sizeX+1, endY, self.sizeY+1, dX*dY*val)

    def display(self) -> None:
        cumul : List[List[int]] = [[self.getSumBefore(x+1,y+1) for y in range(self.sizeY)] + [0] for x in range(self.sizeX)] + [[0]*self.sizeY]
        normal : List[List[int]] = [[cumul[x][y] - cumul[x][y-1] - cumul[x-1][y] + cumul[x-1][y-1]  for y in range(self.sizeY)] for x in range(self.sizeX)]
        for x in normal:
            print(x)
        

