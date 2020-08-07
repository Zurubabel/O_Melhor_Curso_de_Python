def func_1(a = "a"):
    print(type(a))
    print(id(a))
    print(a)
    print("#" * 10)
    a = "x"
    print(type(a))
    print(id(a))
    print(a)

def func_2(a = []):
    a.append("1")
    print(type(a))
    print(id(a))
    print(a)

func_2()
func_2()
func_2()

#func_1()
#func_1("b")
#func_1("c")