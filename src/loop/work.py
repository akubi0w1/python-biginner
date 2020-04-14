# 内包省略
def loop_quiz():

    list = ['avocado', 'cucumber', 'omelette_rice', 'apple', 'green_pepper']

    # todo: 以下の処理を省略記法で書く
    # 処理: 文字数が偶数の要素に対して、先頭の文字のみを大文字にした配列を取得
    # ex) avocado -> Avocado, cucumber -> 含まない
    # 先頭のみ大文字: str.capitalize()
    result = [ x.capitalize() for x in list if len(x) % 2 ]

    return result

if __name__ == '__main__':
    loop_quiz()