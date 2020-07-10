import time as t

class Timer():

    def __init__(self):
        self.prompt = 'timer hasnt start yet'
        self.units = ['hour','min','second']
        self.timelasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    #def __add__(self,other):
    #這先不用管，之前沒寫完的
        #prompt = 'totally equals:'
        #result = []
        #for index in range(3,6):
            #result.append(self.timelast,other.timelast)
        
    
    def start(self):
        self.begin = t.localtime()
        self.prompt = 'please stop first'
        print('start')
    
    def stop(self):
        if not self.begin:
            print('please start first')
        else:

            print('stop')
            self.end = t.localtime()
            self._calc()

    def _calc(self):
        self.timelast = []
        self.prompt = "totally"
        self.units = ['hour','min','second']

        for index in range(3,6):
            self.timelast.append(self.end[index] - self.begin[index])
            
        self.prompt += str(self.timelast)

        self.begin = 0
        self.end = 0
                
#t1 = Timer()
t1.start()
#t1.stop()
print(t1.units)
print(t1.timelast)

