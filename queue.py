from hazelcast_config import get_hazelcast_client

class Structure_Queue:

    def __init__(self):
        self.client = get_hazelcast_client()
        self.my_queue = self.client.get_queue("patient_queue").blocking()

    def add_items(self):
        # ajout des elements dans la file
        self.my_queue.offer("ahmed")
        self.my_queue.offer("chaimae")
        self.my_queue.offer("jalila")
        self.my_queue.offer("othmane")

    def get_size(self):
        # connaitre le nombre d'element dans la file
        print("Taille de la queue:", self.my_queue.size())

    def poll_item(self):
        head = self.my_queue.poll() # possibilité de le faire avec .take()
        print("Élément récupéré depuis la queue:", head)
        print("Éléments restants dans la queue:", self.my_queue.size())

    def run(self):
        self.add_items()
        self.get_size()
        self.poll_item()

if __name__ == "__main__":
    queue_example = Structure_Queue()
    queue_example.run()
    queue_example.client.shutdown()
