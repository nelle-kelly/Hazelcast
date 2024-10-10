from django.test import TestCase
from django.core.cache import cache


class HazelcastCacheTestCase(TestCase):
    # This test checks if the cache correctly sets and retrieves a value
    def test_cache_set_and_get(self):
        cache.set('key', 'value', timeout=30)  # Store the value in the cache for 30 seconds
        self.assertEqual(cache.get('key'), 'value')  # Verify if the value retrieved from the cache is correct

    # This test checks if the cache can successfully delete a key and its value
    def test_cache_delete(self):
        cache.set('key', 'value')  # Store a value in the cache
        cache.delete('key')  # Delete the key from the cache
        self.assertIsNone(cache.get('key'))  # Verify that the key no longer exists in the cache
