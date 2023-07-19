import yaml

def extract_roles_from_cloudformation_template(input_file, output_file):
    with open(input_file, 'r') as f:
        template_data = yaml.safe_load(f)

    # Filtrar los roles del template
    roles = []
    resources = template_data.get('Resources', {})
    for resource_name, resource_info in resources.items():
        if resource_info.get('Type') == 'AWS::IAM::Role':
            roles.append({resource_name: resource_info})

    # Escribir los roles en un nuevo archivo YAML
    with open(output_file, 'w') as f:
        yaml.dump(roles, f, default_flow_style=False)

if __name__ == "__main__":
    input_template_file = "original.yaml"
    output_roles_file = "roles.yaml"
    extract_roles_from_cloudformation_template(input_template_file, output_roles_file)