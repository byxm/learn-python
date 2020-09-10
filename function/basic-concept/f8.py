c = 1

def func1():
    c = 2
    def func2():
        c = 3
        print(c)
    func2()
    

func1()


def globalDeomo():
   global hh
   hh = 10

   globalDeomo()
   print(hh)