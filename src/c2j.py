import csv
import json
from io import StringIO


def get_json_from_csv(csv_data, delimiter=','):
    """ 
    Use this function to convert csv to json within a program (no reading/writing files)

    Input:  csv formated string
            delimiter - sometimes you will find csv that is formated with alternate delimiters
                        common examples include: | \t ; : 
                        use this optional perameter if you are dealing with csv that is 
                        delimited with anyting other than a comma
    Output: json
    """
    
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

