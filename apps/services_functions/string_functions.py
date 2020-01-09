
def get_value_or_null_str(value):
    return value if value else ''


def get_val_if_key(_dict, key):
    return _dict[key] if key in _dict else ''
