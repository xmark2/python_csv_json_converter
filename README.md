# python_csv_json_converter
this python app can convert csv files to json format.

- the converter handle the first row of the csv file as header row
- the converter can detect the number of columns and the columns converted to keys
- the values automatically joined to the keys.


So here you can find a short example how look like the conversion:
  - input:
      csv file:
        header0, header1
        data00, data01
        data10, data11
        data20, data21
   
   -output:
      json file:
        [
        {
          header0 : data00,
          header1 : data01
        },
        {
          header0 : data10,
          header1 : data11
        },
        {
          header0 : data20,
          header1 : data21
        }
        ]
        
 Here you can check if the generated json file valid http://jsonlint.com/
 It should be valid, but please feel free to check the output :)
 
 Thanks,
 Mark
   
