"""
'/Author': 'Alexis Adrian Ibarra Mora',
 '/Creator': 'PyCharm',
 '/CreationDate': "2021-11",
 '/ModDate': "09/Dec/2021"
 '/ProgrammingLanguage': "Python"
"""
import tabula
import os
from pathlib import Path

os.getcwd()
os.chdir(r'C:\\Users\\aibar\\PycharmProjects\\pythonProject\\PDFs')
my_pdfs = os.getcwd()
print('The Path is:\n', my_pdfs)

print('----------------')
# Read only PDFs documents
print('PDFs documents:\n')


for pdf_paths in Path(r"C:\\Users\\aibar\\PycharmProjects\\pythonProject\\PDFs").glob("*.pdf"):
    bol = False
    dfs = tabula.read_pdf(pdf_paths, pages="all")
    csv_path = str(pdf_paths).replace('.pdf', '')
    with open(f'{csv_path}.csv', 'a') as f:
        for df in dfs:
            if "Definitions" in df.columns:
                bol = True
                print(df)
            if bol:
                df.replace(regex='\n', value=' ', inplace=True)
                df.to_csv(f, index=False)

print('----------------')
# Read only CSVs documents
print('CSVs documents:\n')
from pathlib import Path

for csv_paths in Path(r"C:\\Users\\aibar\\PycharmProjects\\pythonProject\\PDFs").glob("*.csv"):
    print(csv_paths)

path = r"C:\Users\aibar\PycharmProjects\pythonProject\PDFs\ab.pdf"

dfs = tabula.read_pdf(path, pages="all")

