class Human:
    #オブジェクトの生成をする
    def __init__(self):
        self.name = ""
        self.age = ""

    #メソッドを定義する（名前,年齢)    
    def printinfo(self,name,age):
        self.name = name
        self.age = age
        
        print(name)
        print(age)

#これでHUmanクラスに紐付ける
kaitou = Human()

#Humanクラスのメソッドを利用する
kaitou.printinfo("tomosue",33)

