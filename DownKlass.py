from InitKlass import InitKlass


class DownKlass(InitKlass):
    def __init__(self, w, h, quadTemp, topTemp, quadEdge, speed=1):
        super().__init__(w, h, quadTemp, topTemp, quadEdge, speed)

    def fill(self, matrix):
        for i in range(self.w - 2, 0, -1):
            for j in range(self.h - 2, 0, -1):
                if self.in_square(i, j):
                    continue
                matrix[i][j] = self.speed * (matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] +
                                matrix[i][j + 1]) / 4 + (1 - self.speed) * matrix[i][j]
        return matrix
