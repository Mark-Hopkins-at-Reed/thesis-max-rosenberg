import unittest
from ozone.taxonomy import BasicTaxonomy, AnimalNet, AnimalWord

class TestBasicTaxonomy(unittest.TestCase):
    
    def setUp(self):
        self.taxonomy = BasicTaxonomy()   

    def test_get_vocab(self):
        expected = {'animal': 0, 'bird': 1, 'mammal': 2, 'finch': 3, 'hummingbird': 4, 'dog': 5, 'cat': 6}
        return self.taxonomy.get_vocab == expected

    def test_get_root_synset(self):
        expected = "animal"
        assert self.taxonomy.get_root_synset() == expected

    def test_random_node(self):
        assert self.taxonomy.random_node(10,14) == 'animal'
        ani = self.taxonomy.random_node(1,3)
        assert ani == 'reptile'

    def test_random_hyponyms(self):
        expected = set(['bulldog', 'poodle'])
        result = set(self.taxonomy.random_hyponyms('dog', 2))
        assert result == expected

        expected1 = set(['finch'])
        expected2 = set(['swallow'])
        result = set(self.taxonomy.random_hyponyms('bird', 1))
        assert result == expected1 or result == expected2

    def test_random_non_hyponyms(self):
        non_birds = {'dog', 'monkey', 'reptile', 'cat', 
                    'animal', 'mammal', 'iguana', 'poodle', 
                    'bulldog', 'giraffe'}
        for _ in range(10):
            non_hyponym = self.taxonomy.random_non_hyponym('bird')
            assert non_hyponym in non_birds

    def test_flatness(self):
        assert self.taxonomy.flatness("dog") == 1
        assert self.taxonomy.flatness("mammal") == 2/3
        assert self.taxonomy.flatness ("animal") == 1/4

    def test_reptitions(self):
        assert self.taxonomy.repititions('animal') == 1
        assert self.taxonomy.repititions('mammal') == 1
        assert self.taxonomy.repititions('dog') == 1
        assert self.taxonomy.repititions('bulldog') == 1

        
if __name__ == "__main__":
	unittest.main()
