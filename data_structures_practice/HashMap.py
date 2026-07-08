#key - value pairs
#key1 -> value1 (key is unique)
#key -> |hash| -> index -> value


#O(1) - constant time

#collision handling
    #if collision, jupping till the free index(free spot in the list)
    #to find the position, do the same (jumping till find the good value)

    #if hash give always 1 ( hash -> 1 always)
    # -> worst case : O(n) - linear time

    #if good hash function ( always hash give a different index)
    # -> best case : average case inf O(1)

#Lists of lists
#stocker dans chaque tableau l'ensemble des values qui renvoient le même index avec hash
#SI tous les éléments ont le même hash (pire cas)
# -> hashmap ajout donc simplement comme une linkedlist

class HashMap:
    #capacity pas nécessaire en python car tab dynamique mais oui en C etc
    #capacity = nbr of buckets
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    #O(1) - constant time
    def __len__(self):
        return self.size

    #O(n) - linear time (in worst case)
    #Average : O(1) - constant time
    #Depends of the quality of the hash function
    def __contains__(self, key):
        index = self._hash_functions(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    # O(n) - linear time (in worst case)
    # Average : O(1) - constant time
    # Depends of the quality of the hash function
    def put(self, key, value):
        index = self._hash_functions(key)
        bucket = self.buckets[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k,value)
                break
        else:
            bucket.append((key,value))
            self.size += 1

    # O(n) - linear time (in worst case)
    # Average : O(1) - constant time
    # Depends of the quality of the hash function
    def get(self, key):
        index = self._hash_functions(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError('Key not found')

    # O(n) - linear time (in worst case)
    # Average : O(1) - constant time
    # Depends of the quality of the hash function
    def remove(self, key):
        index = self._hash_functions(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError('Key not found')

    #O(n) - linear time
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n) - linear time
    def values(self):
        return [v for bucket in self.buckets for _ , v in bucket]

    # O(n) - linear time
    def items(self):
        return [(k,v) for bucket in self.buckets for k, v in bucket]

    #O(k) - Linear in key length
    def _hash_functions(self, key):
        key_string = str(key)
        hash_result = 0
        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity  % self.capacity
        return hash_result

if __name__ == '__main__':
    import uuid
    import matplotlib.pyplot as plt

    hash_map = HashMap(100)

    for _ in range(10000):
        hash_map.put(uuid.uuid4(), 'some_value')

    X = []
    Y = []
    for i, bucket in enumerate(hash_map.buckets):
        X.append(i)
        Y.append(len(bucket))
    plt.bar(X, Y)
    plt.show()

#In python
# dict()
#{'key':'value'}