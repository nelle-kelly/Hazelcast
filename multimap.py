from hazelcast_config import get_hazelcast_client

class Structure_MultiMap:

    def __init__(self):
        # Création du client Hazelcast et récupération de la structure MultiMap
        self.client = get_hazelcast_client()
        self.my_multimap = self.client.get_multi_map("patient_multimap").blocking()

    def add_items(self):
        # Ajout de plusieurs valeurs pour une même clé
        self.my_multimap.put("ahmed", "Rendez-vous 1")
        self.my_multimap.put("ahmed", "Rendez-vous 2")
        self.my_multimap.put("chaimae", "Rendez-vous 1")
        self.my_multimap.put("jalila", "Rendez-vous 1")
        self.my_multimap.put("othmane", "Rendez-vous 1")
        self.my_multimap.put("othmane", "Rendez-vous 2")

    def get_items(self, key):
        # Récupération de toutes les valeurs associées à une clé
        items = self.my_multimap.get(key)
        print(f"Éléments associés à '{key}':", items)

    def delete_item(self, key, value):
        # Suppression d'une valeur spécifique associée à une clé
        self.my_multimap.remove(key, value)
        print(f"Après suppression de '{value}' associé à '{key}':", self.my_multimap.get(key))

    def delete_all_items_for_key(self, key):
        # Suppression de toutes les valeurs associées à une clé
        self.my_multimap.remove_all(key)
        print(f"Après suppression de tous les éléments associés à '{key}':", self.my_multimap.get(key))

    def run(self):
        self.add_items()
        self.get_items("ahmed")
        self.delete_item("ahmed", "Rendez-vous 1")
        self.get_items("ahmed")
        self.delete_all_items_for_key("othmane")
        self.get_items("othmane")

if __name__ == "__main__":
    multimap_example = Structure_MultiMap()
    multimap_example.run()
    multimap_example.client.shutdown()
