import hazelcast

def get_hazelcast_client():
    client = hazelcast.HazelcastClient(
        cluster_members=["127.0.0.1:5701"],  # Serveur Hazelcast local
        cluster_name="dev",  # Nom du cluster, configurable selon mes besoins
    )
    return client
