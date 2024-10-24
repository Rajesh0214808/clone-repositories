def flatten_dict(d, parent_key=''):
    items = {}
    for k, v in d.items():
        new_key = parent_key + '.' + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.update(flatten_dict(item, f"{new_key}[{i}]"))
        else:
            items[new_key] = v
    return items

# Example usage:
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

print(flatten_dict(nested_dict))
