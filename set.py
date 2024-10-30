from hazelcast_config import get_hazelcast_client

class Structure_set:

    def __init__(self):
        self.client = get_hazelcast_client()
        self.my_set = self.client.get_set("patient_set").blocking()

    def add_items(self):
        # ajout des elements avec la methode .add
        self.my_set.add("ahmed")
        self.my_set.add("chaimae")
        self.my_set.add("jalila")
        self.my_set.add("othmane")

    def display_items(self):
        # recuperer tous les elements du cache
        print("Éléments dans le set:")
        for item in self.my_set.get_all():
            print(item)

    def delete_item(self):
        self.my_set.remove("jalila") #supprimer un element
        print(f"Après suppression :", self.my_set.get_all())

    def run(self):
        self.add_items()
        self.display_items()
        self.delete_item()

if __name__ == "__main__":
    set_example = Structure_set()
    set_example.run()
    set_example.client.shutdown()