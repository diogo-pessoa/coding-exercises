class MapTransform:
    """
    Studying built-in map() and a use-case I could face in the day-to-day.
    """

    def _reduce_key_to_pattern(self, key):
        return key.split("#")[1]

    def transform_keys(self, string_to_transform: dict) -> list[tuple]:
        """
        Given a dictionary, return a a list of tuples with the chars after "#".
        :param string_to_transform: dict
        :return: list[tuple]
        """

        return list(map(lambda x: (self._reduce_key_to_pattern(x[0]), x[1]), string_to_transform.items()))
