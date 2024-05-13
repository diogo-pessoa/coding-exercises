#!/bin/python3

import os


import re

def ordered_configuration(configuration):
    # Split the configuration string into individual config pairs using '|' as the delimiter
    split_configs = configuration.split('|')

    # Dictionary to store configuration values keyed by their ordinal indices
    config_dict = {}

    # Regular expression to check if the index is valid
    valid_index_regex = re.compile(r"^000[1-9]|00[1-9]\d|0[1-9]\d{2}|[1-9]\d{3}$")

    # Process each configuration pair
    for config in split_configs:
        index = config[:4]
        value = config[4:]

        # Validate the index
        if not valid_index_regex.match(index):
            return ["Invalid configuration"]

        # Validate the length of the configuration value
        if len(value) != 10:
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
    for idx in sorted_indices:
        if int(idx) != expected_index:
            return ["Invalid configuration"]
        expected_index += 1

    # Gather the sorted configuration values based on the sorted indices
    sorted_configs = [config_dict[idx] for idx in sorted_indices]

    return sorted_configs

