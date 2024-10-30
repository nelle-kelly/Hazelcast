from hazelcast_config import get_hazelcast_client

class Structure_Topic:

    def __init__(self):
        self.client = get_hazelcast_client()
        self.my_topic = self.client.get_topic("patient_topic")

    def message_listener(self, event):
        print("Message reçu sur le topic:", event.message)

    def add_listener_and_publish(self):
        # Ajoute un listener au topic pour écouter les messages
        self.my_topic.add_listener(self.message_listener)

        # Publie des messages
        self.my_topic.publish("Message 1")
        self.my_topic.publish("Message 2")

    def run(self):
        self.add_listener_and_publish()

if __name__ == "__main__":
    topic_example = Structure_Topic()
    topic_example.run()
    topic_example.client.shutdown()
