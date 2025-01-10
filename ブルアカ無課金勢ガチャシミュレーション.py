# ブルアカ無課金勢ガチャシミュレーション

import random
import matplotlib.pyplot as plt

# PU確率
PU_RATE = 0.007
# 年間ガチャ回数
gacha_per_year = 1000

# 何年シミュレーションするか
year = 100000


# 基本戦略
# PUを引くまでガチャを回す
# PUを引いたらガチャをやめる
# 200連引いたらピックアップと交換する

def gacha() -> bool:
    return random.random() < PU_RATE

def main():
    PU_count = [0] * year
    for i in range(year):
        gacha_count = 0

        for j in range(gacha_per_year):
            gacha_count += 1
            
            if gacha():
                PU_count[i] += 1
                gacha_count = 0
            
            if gacha_count == 200:
                PU_count[i] += 1
                gacha_count = 0
    
    # それぞれの回数が何年分あるかを計算
    year_count =[]
    for i in range(min(PU_count), max(PU_count)+1):
        year_count.append(PU_count.count(i))
    
    # グラフ描画
    plt.xlabel('PU Count')
    plt.ylabel('Year Count')
    plt.xticks(range(min(PU_count), max(PU_count)+1))
    plt.bar(range(min(PU_count), max(PU_count)+1), year_count)

    # 平均値を計算
    average = sum(PU_count) / year
    plt.title(f'PU Count Distribution\nAverage: {average:.2f}')

    # 回数をグラフの上に表示
    for i, count in enumerate(year_count):
        plt.text(min(PU_count)+i, count, str(count), ha='center', va='bottom')

    plt.show()

    


if __name__ == '__main__':
    main()
