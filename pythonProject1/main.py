
class Bibl:
    @staticmethod

    def call_v(a1,b1,n1):

        # self.n=n1*10
        a=b1*a1
        b=a1-n1
        n=n1*10
        return a,b,n
    def __repr__(self):
        return f'{self.a}, {self.b}, {self.n}'

a=Bibl.call_v(5,6,3)

print(a[1])
print(type(a))

