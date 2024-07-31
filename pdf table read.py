import camelot
import os

filepath = input("Enter the file path of your PDF file: ")


# PDF file to extract tables from
file = filepath

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)
print("Total tables extracted:", tables[1])



str1=filepath.split(".")

filename=str1[0].split("\\")[-1] + ".csv"
filenamepath=str1[0].split("\\")[:-1]


finaloutput = '\\'.join(filenamepath)



if tables.n > 0:
    tables[1].to_csv(os.path .join(finaloutput,filename))
    print(f"File generated at {os.path .join(finaloutput,filename)}")