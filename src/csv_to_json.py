import csv
import codecs
import json

def convert_to_json(input_file_name, out_file_name):
    with codecs.open(input_file_name, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        header = []
        rows = []

        try:
            for row in readCSV:
                rows.append(row)
        except UnicodeDecodeError:
            pass        

        header = rows[0]

        rows.remove(header)
        rows.sort()

    data_dic = []

    maxRows = len(rows)
    maxHeader = len(header)

    for i in range(0,maxRows):

        my_dict = {'id':i}
        for j in range(0,maxHeader):
            my_dict[header[j]] = rows[i][j]
        data_dic.append(my_dict)

    out_file = open(out_file_name,"w")
    json.dump(data_dic,out_file, indent=4)
    out_file.close()

# input_file_name = 'language_codes.csv'
input_file_name = raw_input('What is the name of your csv file?\n')
out_file_name = 'csv_output.json'

convert_to_json(input_file_name, out_file_name)
