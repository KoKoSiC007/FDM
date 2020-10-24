import copy

from PNGCreator import PNGCreator


class InitKlass:
    def __init__(self, w, h, quadTemp, topTemp, quadEdge, speed=1):
        self.w = w
        self.h = h
        self.quadTemp = quadTemp
        self.topTemp = topTemp
        self.quadEdge = quadEdge
        self.matrix = [[0 for _ in range(self.w)] for _ in range(self.h)]
        self.init()
        self.speed = speed

    def init(self):
        for i in range(self.w):
            self.matrix[0][i] = self.topTemp

        for j in range(self.h // 2, ):
            self.matrix[j][0] = self.matrix[j][self.h - 1] = (self.topTemp / (self.h // 2)) * (self.h // 2 - j)

        for i in range(self.h // 2 - self.quadEdge, self.h // 2 + self.quadEdge + 1):
            self.matrix[self.h // 2 - self.quadEdge][i] = self.matrix[self.h // 2 + self.quadEdge][i] = self.quadTemp
            self.matrix[i][(self.w // 2) - self.quadEdge] = self.matrix[i][self.w // 2 + self.quadEdge] = self.quadTemp

        for i in range(self.w):
            for j in range(self.h):
                if self.in_square(i, j):
                    self.matrix[i][j] = self.quadTemp

    def in_square(self, i, j):
        return (self.w // 2 - self.quadEdge) <= j <= (self.w // 2 + self.quadEdge) \
               and (self.h // 2 - self.quadEdge) <= i <= (self.h // 2 + self.quadEdge)

    def fill(self, matrix):
        pass

    def find(self, quality):
        newMatrix = self.fill(copy.deepcopy(self.matrix))
        maxQuality = abs(newMatrix[1][1] - self.matrix[1][1])

        counter = 0
        while maxQuality >= quality:
            presenter = PNGCreator(self.matrix)
            presenter.save(f'images/{counter}.png')
            counter += 1

            for i in range(self.w):
                for j in range(self.h):
                    if maxQuality <= abs(newMatrix[i][j] - self.matrix[i][j]):
                        maxQuality = abs(newMatrix[i][j] - self.matrix[i][j])

            self.matrix = newMatrix
            newMatrix = self.fill(copy.deepcopy(self.matrix))
            maxQuality = abs(newMatrix[1][1] - self.matrix[1][1])

        print(f"Количество итераций: {counter}")
        return counter