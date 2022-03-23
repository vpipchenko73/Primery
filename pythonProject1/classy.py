class Node:
    def __init__(self, cargo=None,next=None,back=None):
        self.cargo=cargo
        self.next=next
        self.back=back

    def __str__(self):
        return (f'{self.cargo}/>{self.next}>/<{self.back}<')

a=Node('wer',34,45)
b=Node('sd',23,67)
c=Node('tt',44,23)
print(a,b,c)
print(type(a))
a.next=b.back
print(a)