# Projektna naloga pri prdmetu Uvod v programiranje

import requests
import os

franja_frontpage_url = 'https://www.timingljubljana.si/rezultati.aspx?idTekme=6752&tip=B&disc=1M&embed=1'
results_directory = 'podatki'
frontpage_filename = 'rezultati.html'
csv_filename = 'rezultati.csv'

def download_url_to_string(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print (response.status_code)
            return None
        page_content = response.text
        print(page_content)
    except requests.exceptions.RequestException:
        print("Spletna stran ni dosegljiva")
        return None
    return page_content

def save_string_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)

def read_file_to_string(directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as file_in:
        text = file_in.read()
    return text

def save_frontpage(page, directory, filename):
    text = download_url_to_string(page)
    if text is not None:
        save_string_to_file(text, directory, filename)
    return text

def main(redownload=True, reparse=True):
    if redownload:
        save_frontpage(franja_frontpage_url, results_directory, frontpage_filename)

if __name__ == '__main__':
    main()