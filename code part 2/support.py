from csv import reader

def import_csv_layout(path):
    terrain_map = []
    with open(path, "r") as mapFile:
        level = reader(mapFile, delimiter = ",")
        for row in level:
            terrain_map.append(list(row))
    return terrain_map