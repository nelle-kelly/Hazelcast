from hazelcast_config import get_hazelcast_client
import hazelcast
from django.test import TestCase

class structure_map:

    def __init__(self):
        self.client = get_hazelcast_client()
        self.my_map = self.client.get_map('patients').blocking() # creation d'une map pour le cache des patients

    def example_add_item(self) :

        self.my_map.put('1', 'ahmed')
        self.my_map.put('2', 'chaimae')
        self.my_map.put('3', 'jalila')
        self.my_map.put('2', 'othmane')

        


    def axample_get_item(self, key, value):
        self.my_map.put(key, value)

    def delete(self, key):
        self.client.get_map("cache").remove(key)

if __name__ == "__main__":
    # Créer une instance de structure_map
    test_map = structure_map()

    # Exécuter les tests
    test_map.run_tests()

    # Fermer le client Hazelcast
    test_map.client.shutdown()