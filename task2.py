def typeBasedTransformer(**kwargs):
    transformed = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed[key] = value ** 2
        elif isinstance(value, str):
            transformed[key] = value[::-1]
        elif isinstance(value, bool):
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed[key] = value[::-1]
        elif isinstance(value, dict):
            if len(set(value.values())) == len(value.values()):  # Ensure values are unique
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value  # Do not modify non-unique values
        else:
            transformed[key] = value  # Do not modify unsupported types
    return transformed
print(typeBasedTransformer(name="Chingiz", age=50, active=False, scores=[1, 2, 3], data={"a": 1, "b": 2}))
