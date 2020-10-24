from InitKlass import InitKlass


class UpKlass(InitKlass):
    def __init__(self, w, h, quadTemp, topTemp, quadEdge, speed=1):
        super().__init__(w, h, quadTemp, topTemp, quadEdge, speed)

    def fill(self, matrix):
        for i in range(1, self.w - 1):
            for j in range(1, self.h - 1):
                if self.in_square(i, j):
                    continue
                matrix[i][j] = self.speed * (matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] +
                                matrix[i][j + 1]) / 4 + (1 - self.speed) * matrix[i][j]
        return matrix
