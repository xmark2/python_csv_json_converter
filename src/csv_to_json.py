import csv
import json
import codecs

def convert_to_json(input_filename, output_filename):
    """ reads csv from input_file and outputs json to output_file """

    with codecs.open(input_filename, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        rows = []
        try:
            for row in readCSV:
                rows.append(row)
        except UnicodeDecodeError:
            pass        
        except UnicodeEncodeError:
            pass        

        headers = rows[0]
        rows = rows[1:]
        rows.sort()


    data_dic = []
    for i, row in enumerate(rows):
        my_dict = {'id':i}
        for j, header in enumerate(headers):
            my_dict[header] = row[j]
        data_dic.append(my_dict)


    out_file = open(output_filename,"w")
    json.dump(data_dic, out_file, indent=4)
    out_file.close()



if __name__ == "__main__":
    input_filename = raw_input('What is the name of your csv file?\n')
    output_filename = input_filename[:-4] + ".json" if input_filename.endswith('.csv') else input_filename + ".json"

    convert_to_json(input_filename, output_filename)
