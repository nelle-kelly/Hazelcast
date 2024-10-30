from hazelcast_config import get_hazelcast_client


class Structure_map:

    def __init__(self):
        # Création du client Hazelcast et de la map 'patients' pour le cache
        self.client = get_hazelcast_client()
        self.my_map = self.client.get_map('patients').blocking()  # Création d'une map pour le cache des patients

    def example_add_item(self):
        # Ajout d'éléments dans la map
        self.my_map.put('1', 'ahmed')
        self.my_map.put('2', 'chaimae')
        self.my_map.put('3', 'jalila')
        self.my_map.put('4', 'othmane')

        # Afficher les différents éléments ajoutés
        print("Éléments ajoutés dans la map:")
        for value in self.my_map.values():
            print(value)

    def example_get_item(self):
        # Récupération d'un élément par sa clé
        item = self.my_map.get('2')
        print("Élément récupéré avec la clé '2':", item)
        return item

    def example_delete_item(self):
        # Suppression d'un élément par sa clé
        self.my_map.remove('1')
        contains_key = self.my_map.contains_key('1')
        print("L'élément avec la clé '1' a été supprimé:", not contains_key)

    def example_get_all_items(self):
        # Récupération de tous les éléments de la map
        print("Tous les éléments dans la map:")
        for key, value in self.my_map.entry_set():
            print(f"Clé: {key}, Valeur: {value}")

    def run_tests_map(self):
        print("--Test : Add Item--")
        self.example_add_item()

        print("\n--Test : Get Item--")
        self.example_get_item()

        print("\n--Test : Delete Item--")
        self.example_delete_item()

        print("\n--Test : Get All Items--")
        self.example_get_all_items()



if __name__ == "__main__":
    # Créer une instance de structure_map
    test_map = Structure_map()

    # Exécuter les tests
    test_map.run_tests_map()

    # Fermer le client Hazelcast
    test_map.client.shutdown()