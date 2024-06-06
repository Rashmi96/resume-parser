import glob
import os
import pandas as pd
from fileParser import fileParser
from tika import parser
import io
import requests

def fileReader(inputPath):
    LIST_OF_FILES_PDF = []
    LIST_OF_FILES_DOC = []
    LIST_OF_FILES_DOCX = []

    os.chdir(inputPath)
    for file in glob.glob('**/*.pdf', recursive=True):
        LIST_OF_FILES_PDF.append(file)
    for file in glob.glob('**/*.doc', recursive=True):
        LIST_OF_FILES_DOC.append(file)
    for file in glob.glob('**/*.docx', recursive=True):
        LIST_OF_FILES_DOCX.append(file)

    LIST_OF_FILES = LIST_OF_FILES_DOC + LIST_OF_FILES_DOCX + LIST_OF_FILES_PDF
    print(LIST_OF_FILES)

    # parsedresume = pd.DataFrame()
    concatenated_dfs = []
    for j,i in enumerate(LIST_OF_FILES):
        Temp = i.split(".")
        if Temp[1] == "pdf" or Temp[1] == "Pdf" or Temp[1] == "PDF":
            try:
                print("This is PDF File" , i)
                parsedSingleResume = fileParser(i)
                parsedSingleResume['fileName'] = i

                concatenated_dfs.append(parsedSingleResume)
            except Exception as e: print(e)

        if Temp[1] == "txt" or Temp[1] == "Txt" or Temp[1] == "TXT":
            print("This is TXT" , i)

            try:
                parsedSingleResume = fileParser(i)
                parsedSingleResume['fileName'] = i

                concatenated_dfs.append(parsedSingleResume)
            except Exception as e: print(e)

        if Temp[1] == "docx" or Temp[1] == "Docx" or Temp[1] == "DOCX":
            print("This is DOCX" , i)

            try:
                parsedSingleResume = fileParser(i)
                parsedSingleResume['fileName'] = i

                concatenated_dfs.append(parsedSingleResume)
            except Exception as e: print(e)

    print(pd.concat(concatenated_dfs))
    return pd.concat(concatenated_dfs)

def process_files():
    try:
        inputPath = '/Users/rashmiranjanswain/Documents/workspace/resume-parser-api/uploads'

        # Implement your processing logic here
        pdf_files = []
        for filename in os.listdir(inputPath):
            file_path = os.path.join(inputPath, filename)
            name = filename
            content_type = filename.split(".")[1]

            # Add file information to the list
            pdf_files.append({
                'name': name,
                'file_path': file_path,
                'content_type': content_type
            })
        data = process_data(pdf_files)
        return data

    except Exception as e: print(e)

def process_data(pdf_files):
    df = pd.DataFrame(pdf_files)
    concatenated_dfs = []

    for index, row in df.iterrows():
        with open(row.get('file_path'), 'rb') as file:
            file_content = file.read()
            text_content = parser.from_buffer(file_content)
        pdf_text = text_content['content']
        df.loc[index,'pdf_text'] = pdf_text

    for index, row in df.iterrows():
        parsed_data = fileParser(row.get('pdf_text'))
        parsed_data['content_type'] = row.get('content_type')
        parsed_data['file_name'] = row.get('name')
        concatenated_dfs.append(parsed_data)
    print (pd.concat(concatenated_dfs))
    return pd.concat(concatenated_dfs)

