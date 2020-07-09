def main():
    ans = 1
    while ans != 0:
        # 入力
        print("-------------------------------------------------")
        print("ようこそ！まずはREADMEを読んでください.\n\n1:小説家になろうから情報を収集する\n2:収集した情報から分析する\n0:終了する\n")
        ans = input()
        try:
            ans = int(ans)
        except:
            print("入力?={}".format(ans))
        # 処理
        if ans == 1:
            print("情報収集")

    print("終了します")


if __name__ == '__main__':
    main()
