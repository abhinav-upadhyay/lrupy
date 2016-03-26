from collections import OrderedDict

class LRUCache(object):

    def __init__(self, size=100):
        self.size = size
        self.cache = OrderedDict()

    def add(self, key, value):
        if key in self.cache:
            return

        if len(self.cache) == self.size:
            self._remove_oldest_entry_and_add_new(key, value)
            return

        self._add_new_entry(key, value)

    def get(self, key):
        val = self.cache.get(key, None)
        if val is not None:
            self._update_key_access_time(key)
        return val


    def _remove_oldest_entry_and_add_new(self, key, value):
        self.cache.popitem(last=False)
        self.cache[key] = value

    def _add_new_entry(self, key, value):
        self.cache[key] = value

    def _update_key_access_time(self, key):
        val = self.cache.pop(key)
        self.cache[key] = val






