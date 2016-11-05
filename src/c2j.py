import csv
import json
from io import StringIO


def get_json_from_csv(csv_data, delimiter=','):
    
    csv.register_dialect('dialect', delimiter=delimiter)

    with StringIO(csv_data) as csvfile:
        readCSV = csv.reader(csvfile, dialect='dialect')
        rows   = []
        try:
            for row in readCSV:
                rows.append(row)
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
        headers = rows[0]
        rows    = rows[1:]

    json_data = []
    for row in rows:
        d = dict()
        for i, header in enumerate(headers):
            d[header] = row[i]
        json_data.append(d)

    return json_data

