#Problem 1
#Create a hash table to store students marks using chaining method
#The hash table should have the following methods:
#insert(key, value): Insert a new key-value pair into the hash table.
#get(key): Retrieve the value associated with a given key.
#remove(key): Remove a key-value pair from the hash table.
#display(): Print the entire hash table.
#The hash table should handle collisions using chaining (i.e., each bucket is a list of key-value pairs).
#The hash function should be a simple modulo operation based on the size of the table.
#The hash table should be able to handle a dynamic number of students and their marks.
#Hashing
class Hashtable:
    def __init__(self, size):
        self.size = size # Total number of buckets
        self.table = [[] for _ in range(size)] # Initialize empty list for chaining

    def __hash(self,key):
        # Generate a hash for the given key and map it to an index 
        return hash(key)% self.size

    def insert(self, key, value):
        #insert or update students marks 
        index=self.__hash(key) # Get the index for the key
        # Check if the key already exists in the bucket, if so, update the value
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If the key does not exist, append a new key-value pair to the bucket
        self.table[index].append((key, value))

    def get(self, key):
        # Retrieve the value for the given key
        index = self.__hash(key)
        # Iterate through the bucket to find the key
        for k, v in self.table[index]:
            if k == key:
                return v

        # If the key is not found, return None
        return None
    
    def remove(self, key):
        # Remove the key-value pair from the hashtable
        index = self.__hash(key)
        # Iterate through the bucket to find the key
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # Remove the key-value pair from the bucket
                del self.table[index][i]
                return True
        # If the key is not found, return False
        return False
    def display(self):
        """Print the entire hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
        return self.value == other.value

ht = Hashtable(10)  # Create hash table with 10 buckets

# Insert student names and marks
ht.insert("Alice", 85)
ht.insert("Bob", 90)
ht.insert("Charlie", 78)
ht.insert("Dave", 92)
ht.insert("Eve", 88)

ht.display()  # Display the table

# Retrieve marks
print("Marks of Charlie:", ht.get("Charlie"))  # Output: 78
print("Marks of Eve:", ht.get("Eve"))          # Output: 88
print("Marks of Zoe:", ht.get("Zoe"))          # Output: None (not found)
