from unittest import TestCase
from .problem_13_4_implement_sbn_cache import Cache


class TestCache(TestCase):
    def testCacheEvictsFILO(self):
        cache = Cache(2)
        cache.insert(1, 1)
        cache.insert(2, 1)
        cache.insert(3, 1)

        self.assertIsNone(cache.get(1))

    def testDelete(self):
        cache = Cache(2)
        cache.insert(1, 1)
        cache.delete(1)
        self.assertIsNone(cache.get(1))

    def testLookupReordersElements(self):
        cache = Cache(3)
        cache.insert(1, 1)
        cache.insert(2, 1)
        cache.insert(3, 1)
        cache.get(3)
        cache.insert(4, 1)
        self.assertIsNone(cache.get(1))
        self.assertEqual((3, 1), cache.get(3))

    def testCacheRetrieve(self):
        cache = Cache(3)
        cache.insert(1, 1)
        cache.insert(2, 1)
        cache.insert(3, 1)
        self.assertEqual((3, 1), cache.get(3))

    def testInsertDoesNotUpdatePrice(self):
        cache = Cache(2)
        cache.insert(1, 1)
        cache.insert(1, 2)
        self.assertEqual((1, 1), cache.get(1))
