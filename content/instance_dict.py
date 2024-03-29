from __future__ import division, print_function
import sys


class UserProperty:
    def __init__(self, v0, v1, v2, v3, v4):
        """_summary_

        Args:
            v0 (str): _description_
            v1 (str): _description_
            v2 (str): _description_
            v3 (str): _description_
            v4 (str): _description_
        """
        self.guido = v0
        self.sarah = v1
        self.barry = v2
        self.rachel = v3
        self.tim = v4
    
    def __repr__(self):
        return 'UserProperty(%r, %r, %r, %r, %r)' \
            % (self.guido, self.sarah, self.barry, self.rachel, self.tim)

colors = UserProperty('blueblueblueblue', 'orange', 'green', 'yellow', 'red')
cities = UserProperty('austin', 'dallas', 'tuscon', 'reno', 'portland')
fruits = UserProperty('apple', 'banana', 'orange', 'pear', 'peach')

for user in [colors, cities, fruits]:
    print(vars(user))

print(list(map(sys.getsizeof, map(vars, [colors, cities, fruits]))))
