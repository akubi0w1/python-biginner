# dict quiz
def dict_quiz():

    dict = {'google': 'gcp', 'microsoft': 'azure'}

    # todo: add dict {'amazon': 'aws'}
    dict['amazon'] = 'aws'

    # todo: capitalize value to use str.upper()
    # ex) 'google': 'gcp' -> 'google': 'GCP'
    for key, value in dict.items():
        dict[key] = value.upper()

    return dict

if __name__ == '__main__':
    dict_quiz()