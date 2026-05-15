import sys
import random

print("このゲームは、ランダム生成されたn~mまでの数値が何かを当てるゲームです。")
print("生成する乱数の最小値nを入力してください。")
print("n :",end ="")
n = int(input())

print("生成する乱数の最大値mを入力してください。")
print("m :",end ="")
m = int(input())

if n > m:
    print("n > m となっています。ゲームを終了します。")
    exit()

ans = random.randint(n,m)

x = None

while ans != x:
    print("数値を入力してください : ")
    x = int(input())

    if x == ans :
        print("正解です。生成された数字は" + str(ans) + "でした")
        break
    else:
        print("不正解")