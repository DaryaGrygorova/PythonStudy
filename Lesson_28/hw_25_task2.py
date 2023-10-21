"""Task 2 - Implement in (__contains__) and len (__len__) methods for HashTable"""


class HashTable:
    """Implementation of HastTable"""
    def __init__(self, max_length=0):
        self.max_length = max_length or 100
        self.storage = [[]] * self.max_length
        self.len = 0

    @classmethod
    def _hash(cls, key_str: str, hash_len=100):
        """Returns Hash for key string"""
        hash_value = 17

        for char in key_str:
            hash_value = (hash_value * 31 + ord(char)) % hash_len

        return hash_value

    def _find_item_by_key(self, my_key, ):
        """Returns tuple (index, inner_index, item_key, item_value) if key exists in table
         or returns tuple (index, None, None, None)"""
        index = HashTable._hash(my_key, self.max_length)
        result = self.storage[index]
        for inner_index, (item_key, item_value) in enumerate(result):
            if item_key == my_key:
                return index, inner_index, item_key, item_value
        return index, None, None, None

    def get_by_key(self, my_key):
        """Returns value by key"""
        _, __, item_key, item_value = self._find_item_by_key(my_key)
        if item_key:
            return item_value
        raise KeyError(f"Key '{my_key}' dot exists in table")

    def save_value_by_key(self, my_key, new_value):
        """Add item with key "key" to HashTable"""
        self.len += 1
        self.rehash_and_storage_extend()
        index, inner_index, item_key, _ = self._find_item_by_key(my_key)
        if item_key:
            self.storage[index][inner_index][1] = new_value
            return None
        self.storage[index].append([my_key, new_value])
        return None

    def delete_item_by_key(self, my_key):
        """Delete item from storage by key"""
        index, inner_index, item_key, _ = self._find_item_by_key(my_key)
        if item_key:
            self.storage[index].pop(inner_index)
            self.len -= 1
            return None
        raise KeyError(f"Key '{my_key}' dot exists in table")

    def items(self):
        """Returns list with items"""
        return [[*nested_lists] for nested_lists in self.storage]

    def table_update(self, other_table):
        """Append new items to Table"""
        for item_key, item_value in other_table.items():
            self.save_value_by_key(item_key, item_value)

    def rehash_and_storage_extend(self):
        """Rehash and extend storage"""
        if self.len == self.max_length:
            self.max_length *= 2
            new_table = HashTable(self.max_length)
            for item_key, item_value in self.items():
                new_table.save_value_by_key(item_key, item_value)
            self.storage = new_table.storage
            del new_table

    def __contains__(self, item):
        """Returns True if table contains key that equal item"""
        # value in HashTable() -> __contains__(HashTable(), value)
        _, __, item_key, __ = self._find_item_by_key(item)
        if item_key:
            return True
        return False

    def __len__(self):
        return self.len

    def __getitem__(self, item_key):
        index = HashTable._hash(item_key, self.max_length)
        result = self.storage[index]
        for key, value in result:
            if item_key == key:
                return value
        raise KeyError

    def __setitem__(self, item_key, new_value):
        self.save_value_by_key(item_key, new_value)


my_table = HashTable()
my_table["key"] = "new value"
print(my_table["key"])

my_table["key1"] = "value1"
my_table["key2"] = "value2"
my_table["key4"] = "value3"
my_table["key4"] = "value4"
my_table["key5"] = "value5"
my_table["key6"] = "value6"

print("key1" in my_table)  # True
print("key3" in my_table)  # False

print(len(my_table))  # 7
