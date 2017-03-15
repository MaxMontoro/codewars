import re
def is_valid_coordinates(coordinates):
    pattern = re.compile('-?([0-8]{0,1}[0-9]|[9]{1}[0]*)\.?[0-9]*, -?[0-9]{0,3}\.?[0-9]*')
    match = re.search(pattern, coordinates)
    print coordinates
    if match:
        return match.group() == coordinates
    return False