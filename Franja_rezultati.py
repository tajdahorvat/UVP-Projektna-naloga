# Projektna naloga pri prdmetu Uvod v programiranje

import requests
import os

# URL spletne strani, kjer se nahajajo rezultati
franja_frontpage_url = 'https://www.timingljubljana.si/rezultati.aspx?idTekme=6752&tip=B&disc=1M&embed=1'
# Mapa v katero se bodo shranjevali podatki
results_directory = 'podatki'
# Ime datoteke v katero se bo shranil HTML strani
frontpage_filename = 'rezultati.html'
# Ime CSV datoteke v katero se bodo shranili podatki
csv_filename = 'rezultati.csv'

def download_url_to_string(url):
    """Kot argument sprejme niz in poskusi vrniti 
    vsebino te spletne strani kot niz. V primeru,
    da pride do napake vrne None."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print (response.status_code) # izpiše kodo
            return None
        page_content = response.text
        print(page_content)
    except requests.exceptions.RequestException:
        print("Spletna stran ni dosegljiva")
        return None
    return page_content

def save_string_to_file(text, directory, filename):
    """zapiše vrednost parametra "text" v novo ustvarjeno
    datoteko, ali povozi obstoječo."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)

def read_file_to_string(directory, filename):
    """Vrne celotno vsebino datoteke kot niz."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as file_in:
        text = file_in.read()
    return text

def save_frontpage(page, directory, filename):
    """Shrani vsebino spletne strani na naslovu v datoteko"""
    text = download_url_to_string(page)
    if text is not None:
        save_string_to_file(text, directory, filename)
    return text



def main(redownload=True, reparse=True):
    if redownload:
        save_frontpage(franja_frontpage_url, results_directory, frontpage_filename)
    
if __name__ == '__main__':
    main()