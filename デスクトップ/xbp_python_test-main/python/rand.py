import random
a = random.randint(1,6)
print(a)

import random

def main():
    answer = random.randint(1, 30)
    attempts = 0

    print("1から30までの数字を当ててください。")

    while True:
        try:
            guess = int(input("数字を入力してください: "))
            attempts += 1

            if guess == answer:
                print(f"正解！{answer}を当てました。{attempts}回目でクリアしました！")
                break
            else:
                print("不正解です。もう一度試してみてください。")
        except ValueError:
            print("無効な入力です。整数を入力してください。")

if __name__ == "__main__":
    main()
