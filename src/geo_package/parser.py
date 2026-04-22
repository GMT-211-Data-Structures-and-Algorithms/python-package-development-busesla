from .geometry import Point, Line

def read_geometry_file(file_path):
    """Dosyadan geometri verilerini okur."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    geom_type = lines[0].lower()
    count = int(lines[1])
    results = []
    
    if geom_type == 'point':
        for i in range(2, 2 + count):
            parts = lines[i].split(',')
            results.append(Point(parts[0], parts[1], parts[2]))
    
    elif geom_type == 'line':
        current_line = None
        for i in range(2, len(lines)):
            if "," not in lines[i]:
                current_line = Line(lines[i])
                results.append(current_line)
            else:
                coords = lines[i].split(',')
                current_line.add_point(Point(coords[0], coords[1]))
    return results