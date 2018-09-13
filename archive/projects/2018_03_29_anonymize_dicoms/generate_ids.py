import random
import string


def load_ids(file_path):
    ids = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            ids.append(line.strip())
    return ids


def is_unique(i, ids):
    return i not in ids


def get_random_nr(nr=10):
    return ''.join([random.choice(string.digits) for _ in range(nr)])


def run():
    prefix = 'S_'
    random_ids = []
    for i in range(100000):
        random_id = '{}{}'.format(prefix, get_random_nr())
        while not is_unique(random_id, random_ids):
            # If random ID is not unique because it is already in the list, just try again
            print('ID not unique!')
            random_id = '{}{}'.format(prefix, get_random_nr())
        random_ids.append(random_id)
    with open('random_ids.txt', 'w') as f:
        for random_id in random_ids:
            f.write('{}\n'.format(random_id))


if __name__ == '__main__':
    run()
