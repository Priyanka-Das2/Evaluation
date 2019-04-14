class CrossWord:
    def CountWords(self, board, size):
        t = 0
        for i in board:
            elements = i.split('X')
            for j in elements:
                if (j.count('.') == size):
                    t += 1
        return t
