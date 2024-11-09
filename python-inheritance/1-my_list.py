#!/usr/bin/python3
''' No modules imported '''


class MyList(list):
    '''Our base class is list '''

    def print_sorted(self):
        ''' The function to print sorted list in ascending order '''
        print(sorted(self))
