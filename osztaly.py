# OOP

class Teglalap:
    szog = 90
    def __init__(self, a_oldal :int = 5, b_oldal :int = 10):
        self.a_old = a_oldal
        self.b_old = b_oldal

    def terulet(self):
        return self.a_old * self.b_old

    def kerulet(self):
        return (self.a_old + self.b_old) *2

class Negyzet(Teglalap):
    def __init__(self, a_oldal :int , b_oldal :int =0 ):
        super().__init__(a_oldal, b_oldal)
        self.a_old = a_oldal
        self.b_old = a_oldal

if __name__ == "__main__":
    t1 = Teglalap()
    print(t1.a_old, t1.b_old)
    print(t1.szog)
    print(t1.kerulet())
    print(t1.terulet())

    t2 = Teglalap(3,8)
    print(t2.a_old, t2.b_old)
    print(t2.szog)
    print(t2.kerulet())
    print(t2.terulet())


    n1 = Negyzet(5)
    print(n1.a_old, n1.b_old)
    print(n1.kerulet())
    print(n1.terulet())
    print(n1.szog)