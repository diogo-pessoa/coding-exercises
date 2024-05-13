#!/bin/python3

import os


def ordered_configuration(configuration):
    """

    :param configuration:
    :return: list of ordered configurations
    """
    split_configs = configuration.split("|")
    configs_dict = {}

    # Compile a regular expression to check if configuration values are valid (10 alphanumeric characters)
    valid_config_regex = re.compile(r"^[a-zA-Z0-9]{10}$")
    # split_config = [re.findall(r'[A-Za-z0-9_.]', config) for config in split_configs]
    for config in split_configs:
        # In total each split has 14 characters: 4 ordinal index + 10 for the configuration value.
        if len(config) != 14:
            return ["Invalid configuration"]

        # List slicing for the index and config
        index, value = config[:4], config[4:]

        # Validate the index
        if index == "0000" or not index.isdigit() or int(index) == 0:
            return ["Invalid configuration"]

        # Validate the configuration value using the regular expression
        if not valid_config_regex.match(value):
            return ["Invalid configuration"]

        # Check for duplicate indices which are not allowed
        if index in config_dict:
            return ["Invalid configuration"]

    # Sort the dictionary keys to ensure they are in the correct order
    sorted_indices = sorted(config_dict)

    # Verify that indices are continuous and start from '0001'
    expected_index = 1
    for index in sorted_indices:
        if int(index) != expected_index:
            return ["Invalid configuration"]
        expected_index += 1

    # Gather the sorted configuration values based on the sorted indices
    sorted_configs = [config_dict[index] for index in sorted_indices]

    # Return the ordered list of configuration values
    return sorted_configs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    configuration = input()

    result = ordered_configuration(configuration)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

import re


def ordered_configuration(configuration):
    # Split the configuration string into individual config pairs using '|' as the delimiter
    pairs = configuration.split('|')

    # A dictionary to store configuration values keyed by their ordinal indices
    config_dict = {}

    # Compile a regular expression to check if configuration values are valid (10 alphanumeric characters)
    valid_config_regex = re.compile(r"^[a-zA-Z0-9]{10}$")

    # Process each configuration pair
    for pair in pairs:
        # Each pair should have exactly 14 characters: 4 for the index and 10 for the configuration value
        if len(pair) != 14:
            return ["Invalid configuration"]

        # Split the pair into index and value
        index, value = pair[:4], pair[4:]

        # Validate the index: '0000' is invalid, index must be numeric and non-zero
        if index == "0000" or not index.isdigit() or int(index) == 0:
            return ["Invalid configuration"]

        # Validate the configuration value using the regular expression
        if not valid_config_regex.match(value):
            return ["Invalid configuration"]

        # Check for duplicate indices which are not allowed
        if index in config_dict:
            return ["Invalid configuration"]

        # Store the configuration value in the dictionary using its index as the key
        config_dict[index] = value

    # Sort the dictionary keys to ensure they are in the correct order
    sorted_indices = sorted(config_dict)

    # Verify that indices are continuous and start from '0001'
    expected_index = 1
    for index in sorted_indices:
        if int(index) != expected_index:
            return ["Invalid configuration"]
        expected_index += 1

    # Gather the sorted configuration values based on the sorted indices
    sorted_configs = [config_dict[index] for index in sorted_indices]

    # Return the ordered list of configuration values
    return sorted_configs


# Example usage of the function:
valid_configuration = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"
print(ordered_configuration(valid_configuration))  # Output: ['76a3a4d214', 'f7c22e7904', '05d29f4a4b']

invalid_configuration = "0002f7c22e7904|000176a3a4d214|000205d29f4a4b"
print(ordered_configuration(invalid_configuration))  # Output: ['Invalid configuration']
