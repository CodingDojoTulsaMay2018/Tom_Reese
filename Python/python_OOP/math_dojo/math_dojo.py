class MathDojo:
    def __init__(self,name):
        self.name = name
        self.total = 0
    def add(self,*args):
        sum = 0
        for i in args:
            sum+=i
        print(sum)
        self.total += sum
        return self
    def subtract(self,*args):
        sum = 0
        for i in args:
            sum-=i
        print(sum)
        self.total += sum
        return self
    def result(self):
        result = self.total
        print(result)
        self.total= 0

md1 = MathDojo("Bob")
md1.add(4,5,6).subtract(4,5,6).subtract(6,7,8,9).subtract(1,2,3).result()
md1.add(9,3,6).add(6,7,-8,-9).add(1,2,3).subtract(4,-5,6).subtract(7,8,9).subtract(1,2,3).result()
