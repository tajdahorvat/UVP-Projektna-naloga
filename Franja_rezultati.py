# Projektna naloga pri prdmetu Uvod v programiranje

import requests
import os
import re
import csv

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

def page_to_results(page_content):
    # Poišči vse vrstice tabele (vrstice rezultatov)
    return re.findall(r'<tr[^>]*>(.*?)</tr>', page_content, flags=re.DOTALL)

def clean_html_tags(text):
    """Odstrani HTML oznake iz niza."""
    return re.sub(r'<[^>]+>', '', text).strip()

def get_dict_from_results_block(block):
    # Zajemi vse vrednosti iz <td> v seznam
    tds_raw = re.findall(r'<td[^>]*>(.*?)</td>', block, flags=re.DOTALL)

    # Navigacijska vrstica ima številke strani, ki jih nočemo
    if len(tds_raw) < 10:
        return None

    # Očisti vsebino (odstrani HTML oznake)
    tds = [clean_html_tags(td) for td in tds_raw]

    # Preveri ali je "rezultat" polje videti kot čas (npr. 3:51:47.7)
    if not re.match(r'\d+:\d+:\d+\.\d+', tds[9]):
        return None  # To je verjetno napačna vrstica (npr. "1,2,3,4,5,...")

    return {
        'uvrstitev': tds[0],
        'stevilka': tds[1],
        'oseba': tds[2],
        'država': tds[3],
        'klub': tds[4],
        'rezultat': tds[9]
    }

def results_from_file(filename, directory):
    page_content = read_file_to_string(directory, filename)
    blocks = page_to_results(page_content)
    rezultati = [get_dict_from_results_block(block) for block in blocks]
    return [rezultat for rezultat in rezultati if rezultat != None]
    print(f"Najdeno blokov: {len(blocks)}, Uporabnih rezultatov: {len(rezultati)}")

def write_csv(fieldnames, rows, directory, filename):
    os.makedirs(directory,exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return

def write_franja_rezultati_csv(rezultati, directory, filename):
    assert rezultati and (all(j.keys() == rezultati[0].keys() for j in rezultati))
    fieldnames = list(rezultati[0].keys())
    write_csv(fieldnames, rezultati, directory, filename)

def main(redownload=True, reparse=True):
    if redownload:
        save_frontpage(franja_frontpage_url, results_directory, frontpage_filename)
    if reparse:
        rezultati = results_from_file(frontpage_filename,results_directory)
        write_franja_rezultati_csv(rezultati, results_directory, csv_filename)

if __name__ == '__main__':
    main()