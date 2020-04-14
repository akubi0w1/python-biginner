# list quiz
def list_quiz():

    list = ['python', 'java', 'go']

    # todo: add value to list: 'ruby'
    list.append('ruby')

    # todo: add suffix '_lang' to use enumerate
    # ex) python -> python_lang, go -> go_lang, ...
    for i, lang in enumerate(list):
        list[i] = lang + '_lang'
    
    return list

if __name__ == '__main__':
    list_quiz()