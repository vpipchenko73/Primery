class Bibl():
    def __init__(self,a,b,n):
        self.a=a
        self.b=b
        self.n=n
    def call_v(self):
        a1=self.a
        b1=self.b
        n1=self.n
        self.a=b1*a1
        self.b=a1-n1
        self.n=n1*10
        return self

    def __repr__(self):
        return f'{self.a}, {self.b}, {self.n}'


s=Bibl(2,3,4)

print(s)
s.call_v()
print(s)

