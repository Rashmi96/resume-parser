from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET
import pandas as pd
from tika import parser
import io

from fileParser import fileParser


def process_files(api_endpoint):
    try:
        # Make a GET request to the API endpoint to fetch the list of files
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an error for non-200 status codes
        # Process the JSON data
        print(response.text)
        root = ET.fromstring(response.content)
        print(root)
        # Implement your processing logic here
        pdf_files = []
        for blob in root.findall('.//Blob'):
            name = blob.find('Name').text
            url = blob.find('Url').text
            last_modified = blob.find('LastModified').text
            etag = blob.find('Etag').text
            size = int(blob.find('Size').text)
            content_type = blob.find('ContentType').text

            # Add file information to the list
            pdf_files.append({
                'name': name,
                'url': url,
                'last_modified': last_modified,
                'etag': etag,
                'size': size,
                'content_type': content_type
            })
        data = process_data(pdf_files)
        print(data)
        print('printing data')
        # print(data)
        return data
        # return jsonify({'pdf_files': pdf_files})

    except Exception as e: print(e)

def process_data(pdf_files):
    df = pd.DataFrame(pdf_files)
    concatenated_dfs = []
    # df['pdf_text'] = ''
    # df['content_type'] = ''
    # df['file_name'] = ''

    for index, row in df.iterrows():
        response = requests.get(row.get('url'))
        pdf_file_like_object = io.BytesIO(response.content)
        parsed = parser.from_buffer(pdf_file_like_object)
        pdf_text = parsed['content']
        df.loc[index,'pdf_text'] = pdf_text

    for index, row in df.iterrows():
        parsed_data = fileParser(row.get('pdf_text'))
        parsed_data['content_type'] = row.get('content_type')
        parsed_data['file_name'] = row.get('name')
        concatenated_dfs.append(parsed_data)

    return pd.concat(concatenated_dfs)