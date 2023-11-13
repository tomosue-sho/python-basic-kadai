class Human:
    #オブジェクト作成
    def __init__(self):
        self.name = ""
        self.age = "" 

     #if文で条件分岐させる（成人かどうか）   
    def check_adult(self,name,age):
        self.name = name
        self.age = age

        if age >= 20:
            print(self.name+"さんは"+str(self.age)+"歳なので大人です")
        else:
            print(self.name+"さんは"+str(self.age)+"歳なので未成年です")
        

    #クラスと紐づける
honban = Human()

    #辞書用意する
age = {"黒田":50,"新井":48,"森下":26,"大瀬良":19,"林":18}

    #繰り返し処理する
for key, value in age.items():
        honban.check_adult(key,value)