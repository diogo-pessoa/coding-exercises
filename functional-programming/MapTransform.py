from typing import Tuple, Any

from helpers.TimeItDecorator import timeit_decorator


class MapTransform:
    """
    Studying built-in map() and a use-case I could face in the day-to-day.
    """

    def _reduce_key_to_pattern(self, key):
        return key.split("#")[1]

    def _build_tuple_from_item(self, item: Tuple[str, Any]) -> Tuple[str, Any]:
        return self._reduce_key_to_pattern(item[0]), item[1]

    @timeit_decorator
    def transform_keys(self, string_to_transform: dict[str, Any]) -> list[Tuple[Any, Any]]:
        """
        Given a dictionary, return a a list of tuples with the chars after "#".
        :param string_to_transform: dict
        :return: list[tuple]
        """
        print(type(string_to_transform.items()))
        return list(map(self._build_tuple_from_item, string_to_transform.items()))

    @timeit_decorator
    def transform_keys_with_comprehension(self, string_to_transform: dict[str, Any]) -> list[Tuple[Any, Any]]:
        """
        Given a dictionary, return a a list of tuples with the chars after "#".
        :param string_to_transform: dict
        :return: list[tuple]
        """
        return [(self._reduce_key_to_pattern(item[0]), item[1]) for item in string_to_transform.items()]

    @timeit_decorator
    def transform_keys_with_loop_and_append(self, string_to_transform: dict[str, Any]) -> list[Tuple[Any, Any]]:
        """
        Given a dictionary, return a a list of tuples with the chars after "#".
        :param string_to_transform: dict
        :return: list[tuple]
        """
        result = []
        for item in string_to_transform.items():
            result.append((self._reduce_key_to_pattern(item[0]), item[1]))
        return result
