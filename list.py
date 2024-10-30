from hazelcast_config import get_hazelcast_client

class Structure_List:

    def __init__(self):
        self.client = get_hazelcast_client()
        self.my_list = self.client.get_list("patient_list").blocking()

    def add_items(self):
        self.my_list.add("ahmed")
        self.my_list.add("chaimae")
        self.my_list.add("jalila")
        self.my_list.add("othmane")

    def get_item(self, index):
        item = self.my_list.get(index)
        print(f"Élément à l'index {index} dans la liste:", item)

    def delete_item_at_index(self, index):
        self.my_list.remove_at(index)
        print(f"Liste après suppression de l'élément à l'index {index}:", self.my_list.get_all())

    def run(self):
        self.add_items()
        self.get_item(1)
        self.delete_item_at_index(0)

if __name__ == "__main__":
    list_example = ListExample()
    list_example.run()
    list_example.client.shutdown()