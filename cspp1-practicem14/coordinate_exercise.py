'''Exercise: coordinat'''
class Coordinate(object):
    '''class'''
    def __init__(self, x_input, y_input):
        '''initialize values'''
        self.x_input = x_input
        self.y_input = y_input

    def getx(self):
        ''' Getter method for a Coordinate object's x coordinate.'''
        return self.x_input

    def gety(self):
        '''Getter method for a Coordinate object's y coordinate'''
        return self.y_input
    def __str__(self):
        '''print string'''
        return '<' + str(self.getx()) + ',' + str(self.gety()) + '>'
    def __eq__(self, other):
        '''check equality'''
        if self.getx() == other.getx():
            if self.gety() == other.gety():
                return True
        return False
    def __repr__(self):
        '''representation'''
        return 'Coordinate(' + str(self.getx()) + ',' + str(self.gety()) + ')'
def main():
    '''main'''
    data = input()
    data = data.split(' ')
    data = list(map(int, data))
    print(Coordinate(data[0], data[1]) == Coordinate(data[2], data[3]))
    print(Coordinate(data[4], data[5]).__repr__())

if __name__ == "__main__":
    main()
