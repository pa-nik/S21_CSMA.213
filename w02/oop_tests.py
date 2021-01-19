class Point:
    x = 0
    y = 0

def print_point(p):
    print('x: ' + str(p.x) + ', y: ' + str(p.y))

blank = Point()  # create Point object
print(blank)

print('blank Point attribute x:')
print(blank.x)
blank.x = 3.0
blank.y = 4.0
print('blank Point attributes:')
print_point(blank)

class Time:
    def __init__(self, hr=0, min=0, sec=0):
        self.hr = hr
        self.min = min
        self.sec = sec

    def print(self):
        print('%0.2d:%0.2d:%0.2d' % (self.hr, self.min, self.sec) )

def print_time(t):
    print('%0.2d:%0.2d:%0.2d' % (t.hr, t.min, t.sec) )

# create Time object
#start_time = Time()
start_time = Time(min=35)
start_time.hr = 10
#start_time.min = 30
print('start_time using function:')
print_time(start_time)
print('start_time using object method:')
start_time.print()