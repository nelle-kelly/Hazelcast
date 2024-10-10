from django.shortcuts import render, redirect, get_object_or_404
import time
from django.http import JsonResponse
from .models import Item
import hazelcast

# Creating the Hazelcast client and connecting to the Hazelcast server
client = hazelcast.HazelcastClient(cluster_members=["127.0.0.1:5701"])  # Adjust the address if needed
cache_map = client.get_map("item_cache") #Retrieve the Hazelcast map for caching

def index(request):
    # Retrieves all Item objects from the database
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def calculator(request):
   return render(request, 'calculator.html')

#-----------------------Creation operation-----------------------
def create_item(request):
    #Retrieves data from the submitted form
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']

        #Creates a new item in the database
        item = Item.objects.create(name=name, description=description)

        # Stores the newly created item in Hazelcast cache
        cache_map.put(str(item.id), {"name": item.name, "description": item.description})

       # Redirects to the main page
        return redirect('index')

    return render(request, 'create_item.html')

# READ---------------------------Read operation ----------------------------------------------
def get_item(request, item_id):
    # Checks if the item is already in the Hazelcast cache
    cached_item = cache_map.get(str(item_id)).result()
    
    if cached_item:
        # If the item is found in cache, return it directly
        print("Données récupérées du cache")
        return JsonResponse(cached_item)
    
    # If the item is not in cache, retrieve it from the database
    item = get_object_or_404(Item, id=item_id)

    # Store the retrieved item in the cache for future requests
    cache_map.put(str(item.id), {"name": item.name, "description": item.description})
    print("Données récupérées de la base de données et mises en cache")
    
    return JsonResponse({"name": item.name, "description": item.description})


# UPDATE----------------------------Update operation -----------------------------
def update_item(request, item_id):
    # Retrieves the item to be updated from the database
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()

        # Updates the item data with new values
        cache_map.put(str(item.id), {"name": item.name, "description": item.description})

        return redirect('index')

    return render(request, 'update_item.html', {'item': item})

# DELETE------------------------------ Delete operation------------------------------------
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    if request.method == "POST":
        # Deletes the item from the database
        item.delete()

        # Also removes the item from Hazelcast cache
        cache_map.remove(str(item.id))

        return redirect('index')

    return render(request, 'delete_item.html', {'item': item})
    
 
