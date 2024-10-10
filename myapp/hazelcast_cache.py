from django.core.cache.backends.base import BaseCache
import hazelcast

class HazelcastCache(BaseCache):
    def __init__(self, location, params):
        super().__init__(params)
        # Configuration du client Hazelcast
        self.client = hazelcast.HazelcastClient(cluster_members=[location])

    def get(self, key, default=None):
        return self.client.get_map("cache").get(key).result() or default

    def set(self, key, value, timeout=None):
        self.client.get_map("cache").put(key, value)

    def delete(self, key):
        self.client.get_map("cache").remove(key)

# Initialisation du client Hazelcast avec l'adresse du serveur 
hazelcast_cache = HazelcastCache(location="127.0.0.1:5701", params={})

# Menu pour permettre à l'utilisateur de saisir des actions
def cache_menu():
    while True:
        print("\n--- Menu Hazelcast Cache ---")
        print("1. Récupérer une donnée")
        print("2. Ajouter une donnée")
        print("3. Supprimer une donnée")
        print("4. Quitter")

        choice = input("Choisissez une option (1-4) : ")

        if choice == '1':
            key = input("Entrez la clé à récupérer : ")
            value = hazelcast_cache.get(key)
            if value:
                print(f"Valeur pour la clé '{key}' : {value}")
            else:
                print(f"Clé '{key}' non trouvée dans le cache.")
        
        elif choice == '2':
            key = input("Entrez la clé à ajouter : ")
            value = input("Entrez la valeur à stocker : ")
            hazelcast_cache.set(key, value)
            print(f"Valeur '{value}' ajoutée pour la clé '{key}'.")
        
        elif choice == '3':
            key = input("Entrez la clé à supprimer : ")
            hazelcast_cache.delete(key)
            print(f"Clé '{key}' supprimée du cache.")
        
        elif choice == '4':
            print("Fermeture du programme.")
            break
        
        else:
            print("Choix invalide. Veuillez choisir une option entre 1 et 4.")

# Exécuter le menu pour interagir avec Hazelcast
cache_menu()
