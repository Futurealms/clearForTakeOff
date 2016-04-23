def parse_csv_with_DatesAndIDs(csv_filename):
    with open(csv_filename) as f:
        airport_ids = []
        for line in f:
            source_data = line.split(',')[3].strip('"')
            source_id = line.split(',')[5].strip('"')
            print(source_id,source_data)
            # airport_ids.append(source_id)
    # airport_ids = airport_ids[1:]
    # print(airport_ids)
    return (airport_ids)

# def

if __name__ == '__main__':
    # print(parse_csv_with_DatesAndIDs('subset.csv'))

    pass
