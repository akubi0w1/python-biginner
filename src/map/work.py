# 内包省略
def map_quiz():

    values = ['omelette_rice', 'green_pepper', 'ice_cream']

    # todo: 文字列を'_'から'-'に変換した配列を取得
    # 条件: lambda式、map関数を用いて一行で記述
    result = list(map(lambda x: x.replace('_', '-'), values))

    return result

if __name__ == '__main__':
    map_quiz()