def _cast_lists_to_string(rows):
    return [[str(value) for value in row] for row in rows if row]


def parse(tableau_object):
    headers = tableau_object.pop(0)
    rows = _cast_lists_to_string(tableau_object)
    return {'data': {'headers': headers, 'rows': rows}}
