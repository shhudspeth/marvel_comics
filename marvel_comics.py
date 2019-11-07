
import random
import get_data


def get_random_id(dictionary_):
    n = len(dictionary_)
    id_ = random.randrange(n)
    return id_

def get_status(id_comic):
    return id_comic['status']

def print_test_lines(id_comic,  get_info, unit='', verb=None):
    print("Comic Marvel {0} {3} {1} {2}".format(id_comic['name'], get_info, unit, verb))

def get_key_from_dict(column, id_comic):
    return id_comic[column]

def get_age (id_comic):
    if id_comic['introduced']:
        age = 2019 - int(id_comic['introduced'])
    else:
        age = "Unknown/TBD"

    return age





def main():
    file = 'input/marvel-comics-character-dataset - marvel-wikia-data.csv'
    mydict = get_data.load_data(file)
    comic_ = get_random_id(mydict)

    orientation = get_key_from_dict('orientation', mydict[comic_])
    year_introduced = get_key_from_dict('introduced', mydict[comic_])
    num_appearances = get_key_from_dict('appearances', mydict[comic_])
    good_evil_no = get_key_from_dict('alignment', mydict[comic_])
    dead_alive = get_key_from_dict('status', mydict[comic_])
    age = get_age(mydict[comic_])

    print_test_lines(mydict[comic_],  age, unit='years old', verb = 'is')
    print_test_lines(mydict[comic_],  year_introduced, verb = 'was created in')
    print_test_lines(mydict[comic_],  num_appearances, unit='times',  verb = 'appeared')
    print_test_lines(mydict[comic_],  good_evil_no, verb= 'is')
    print_test_lines(mydict[comic_],  dead_alive, verb= 'is')

if __name__ == "__main__":
    main()
