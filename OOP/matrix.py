class Matrix:
    def __init__(self, number_string):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in number_string.splitlines()
        ]
        print(self.matrix)




m = Matrix("3 4\n5 6")
m.matrix




