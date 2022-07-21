X = 1

def nester():
    print(X) # Глобальное имя: 1
    class C:
        print(X) # Глобальное имя: 1
        def method(self):
            print(X) # Глобальное имя: 1
        def method2(self):
            X = 3 # Скрывает глобальное имя
            print(X) # Локальное имя: 3

    I = C()
    I.method()
    I.method2()

print(X) # Глобальное имя: 1
nester() # Остаток: 1, 1, 1, 3
print("-"*40)
###
X = 1

def nester():
    X = 2 # Скрывает глобальное имя
    print(X) # Локальное имя: 2
    class C:
        print(X) # В объемлющем def (nester): 2
        def method(self):
            print(X) # В объемлющем def (nester): 2
        def method2(self):
            X = 3 # Скрывает имя из объемлющего def (nester)
            print(X) # Локальное имя: 3

    I = C()
    I.method()
    I.method2()

print(X) # Глобальное имя: 1
nester() # Остаток: 2, 2, 2, 3
print("-"*40)
###
X = 1

def nester():
    X = 2 # Скрывает глобальное имя
    print(X) # Локальное имя: 2
    class C:
        X = 3 # Локальное имя из класса скрывает локальное имя из nester: C.X или I.X
        print(X) # Локальное имя: 3
        def method(self):
            print(X) # В объемлющем def (nester)(НЕ В КЛАССЕ!!!): 2
            print(self.X) # Унаследованное локальное имя класса: 3
        def method2(self):
            X = 4 # Скрывает имя из объемлющей области видимости (nester, не класса!)
            print(X) # Локальное имя: 4
            self.X = 5 # Скрывает имя из класса
            print(self.X) # Находится в экземлпяре: 5

    I = C()
    I.method()
    I.method2()
print(X) # Глобальное имя: 1
nester() # Остаток: 2, 3, 2, 3, 4, 5
print("-"*40)


