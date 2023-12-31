from ruamel.yaml import YAML

def calculate_and_adjust_weights(yaml_file_path):
    # Initialize the YAML object
    yaml = YAML()
    yaml.indent(sequence=4, offset=2)

    # Load the YAML file
    with open(yaml_file_path, 'r') as file:
        yaml_data = yaml.load(file)

    # Initialize a dictionary to accumulate weights for each group
    group_weights = {}

    # Iterate through each entry in the YAML data
    for entry in yaml_data:
        group = entry.get('Group')
        weight = entry.get('Weight')

        # Proceed only if both group and weight are present
        if group and weight:
            # Removing '%' from weight and converting to float
            weight_value = float(weight.rstrip('%'))

            # Accumulate weight for each group
            if group in group_weights:
                group_weights[group] += weight_value
            else:
                group_weights[group] = weight_value

    # Adjust weights if total weight for each group exceeds 100
    for group, total_weight in group_weights.items():
        if total_weight > 100:
            for entry in yaml_data:
                if entry.get('Group') == group:
                    # Adjust the weight proportionally and round to the nearest whole number
                    adjusted_weight = round((float(entry['Weight'].rstrip('%')) / total_weight) * 100)
                    entry['Weight'] = str(adjusted_weight) + '%'

    # Save the adjusted weights back to the YAML file
    with open(yaml_file_path, 'w') as file:
        yaml.dump(yaml_data, file)

    return group_weights

# Example usage
yaml_file_path = 'HJOPA-Scoring-FDA.yml'  # Replace with your actual file path
total_weights = calculate_and_adjust_weights(yaml_file_path)
print(total_weights)
