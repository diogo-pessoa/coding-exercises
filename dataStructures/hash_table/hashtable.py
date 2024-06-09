class HashTables:

    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash_func(self, key):
        """
        Adds the ascii value of the character, multiplied
        ny a prime number
        Then, we take the modulo of the length of the hash_table to get the index.
        for dummies: % (modulo) - gives the remainder of the division of the number
        on the left by the number on the right."""
        hash_val = 0
        for l in key:
            hash_val = (hash_val + ord(l) * 11) % len(self.data_map)
        return hash_val

    def set_item(self, key, value):
        # TODO - review how to implement checks for colisions
        """
        Big O(1)
         - why? - by leveraging the hash function, we access the index directly

        hash_table
        :param key:
        :param value:
        :return:
        """
        index = self.__hash_func(key)  # get the index, by passing the key through the
        # hash function
        # Checking for colisions, before initializing the index with empty list
        if not self.data_map[index]:
            self.data_map[index] = []  # Initialize the index with an empty list
        self.data_map[index].append([key, value])  # Append, list within the hash_table.

    def get_item(self, key):
        """
        Big O(1)
        :param key:
        :return:
        """
        index = self.__hash_func(key)  # Get hash from key
        # Check if index is valid and not None
        if index >= len(self.data_map) or self.data_map[index] is None:
            return None  # Return None if index is out of bounds or the list at index
            # is None
        if self.data_map[index]:  # Check if the index is not empty (falsy check)
            # Loop through the list at this index
            for item in range(len(self.data_map[index])):
                # Check for key in the list
                if self.data_map[index][item][0] == key:
                    # Return the value associated with the key
                    return self.data_map[index][item][1]
        return None  # Return None if the key was not found

    def get_keys(self):
        """
        Big O(n) - Linear time complexity - iterates through the hash_table to get
        all keys.

        :return:
        """
        keys = []
        # if hash is empty, return empty list
        if not self.data_map:
            return keys
        for item in self.data_map:
            if item:
                for i in range(len(item)):
                    keys.append(item[i][0])
        return keys

    def __str__(self):
        return str(self.data_map)
