#ランダム呼ぶ
import random

#整数の範囲決める
var = random.randint(0,100)

#条件式
if var % 15 == 0:
  print("FizzBuzz")

elif var % 3 == 0:
  print("Fizz")

elif var % 5 ==0:
  print("Buzz")

print(var)