import random
import string
from rappy.network import Node


class RandomIds(Node):
    """
    This node allows developers to retrieve a set of N random IDs of a given length. If the database file
    'db_file' does not exist, it will be created and a default number of IDs generated (e.g. 10000). The
    algorithm will ensure all of these are unique.
    If the database does exist, the node will retrieve N IDs from the database. These IDs will then be removed
    from the database and stored in the 'db_file_used' database. When the user asks 100 IDs but 'db_file' contains
    only 99 IDs, a new set of random IDs must be generated. Of course, these must be unique as well, meaning that
    they cannot be contained in 'db_file_used'.
    """
    def __init__(self):
        super(RandomIds, self).__init__()
        self.add_param(
            'mode',
            data_type='string',
            desc='Mode "create" generates a new set of IDs. Mode "get" returns an existing set from the database')
        self.add_param('id_length', data_type='int', default=10)
        self.add_param('nr_ids', data_type='int')
        self.add_param('prefix', data_type='string', default='S_')
        self.add_param('db_file', data_type='string')
        self.add_param('db_file_used', data_type='string')
        self.add_param('db_file_prev', data_type='string')
        self.add_output('output', data_type='list')

    @staticmethod
    def _generate_random_id(nr_digits):
        return ''.join([random.choice(string.digits) for _ in range(nr_digits)])

    @staticmethod
    def _is_unique(i, ids):
        return i not in ids

    @staticmethod
    def _count_nr_permutations(id_length):
        l = 'x'
        return 1

    def _nr_ids_too_big(self, nr_ids, id_length):
        nr_permutations = self._count_nr_permutations(id_length)
        if nr_ids > 0.75 * nr_permutations:
            return True
        return False

    def execute(self):

        print('RandomIds.execute()')
        nr_ids = self.get_param('nr_ids')
        id_length = self.get_param('id_length')

        # Check that 'nr_ids' does not exceed the max. number of combinations for 'id_length'.
        # Otherwise the algorithm will hang forever. In practice, we require 'nr_ids' to be at
        # least 75% smaller than the max. number of combinations in 'id_length'.
        # If we had nr_ids == nr_perm(id_length) the algorithm might take a very long time before
        # if found all unique numbers.
        if self._nr_ids_too_big(nr_ids, id_length):
            raise RuntimeError('Nr. requested IDs too big for suggested ID length')

        mode = self.get_param('mode')
        prefix = self.get_param('prefix')
        db_file = self.get_param('db_file')  # Mandatory
        db_file_used = self.get_param('db_file_used')  # Optional
        random_ids = []

        for i in range(nr_ids):
            random_id = '{}{}'.format(prefix, self._generate_random_id(id_length))
            while not self._is_unique(random_id, random_ids):
                # If random ID is not unique because it is already in the list, just try again
                random_id = '{}{}'.format(prefix, self._generate_random_id(id_length))
            random_ids.append(random_id)
        with open('random_ids.txt', 'w') as f:
            for random_id in random_ids:
                f.write('{}\n'.format(random_id))

        self.set_output('output', [n for n in range(1000)])
