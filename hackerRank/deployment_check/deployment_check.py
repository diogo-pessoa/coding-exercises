#!/bin/python3

import json
import os
import re


#
# Complete the 'evaluate_deployments' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY deployments as parameter.
#


def evaluate_deployments(deployments):
    success_count = 0
    fail_count = 0
    error_count = 0

    for deployment_str in deployments:
        try:
            # Parse the JSON string
            deployment_data = json.loads(deployment_str)

            # Validate the format of deployment_id and status
            if ("deployment_id" in deployment_data and
                    re.match(r"^d-[a-z0-9]{10}$", deployment_data["deployment_id"]) and
                    "status" in deployment_data and
                    deployment_data["status"] in ["Success", "Fail"]):

                # Count successes and failures based on the status
                if deployment_data["status"] == "Success":
                    success_count += 1
                elif deployment_data["status"] == "Fail":
                    fail_count += 1
            else:
                # Increment error count if validation fails
                error_count += 1

        except json.JSONDecodeError:
            # Increment error count if JSON parsing fails
            error_count += 1

    return [success_count, fail_count, error_count]


# Example usage:
deployments_input = [
    '{"deployment_id": "d-123456abcd", "status": "Success"}',
    '{"deployment_id": "d-098765efgh", "status": "Fail"}'
]

result = evaluate_deployments(deployments_input)
print(result)  # Expected output: [1, 1, 0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    deployments_count = int(input().strip())

    deployments = []

    for _ in range(deployments_count):
        deployments_item = input()
        deployments.append(deployments_item)

    result = evaluate_deployments(deployments)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
