# Analiza podatkov sodelujočih na 44. maratonu Franja
Ta projektna naloga zajema in kasneje tudi obdeluje in analizira podatke o sodelujočih. Cilj je analizirati tekmovalce po rezultatih, državah in klubih. Tekmovalce, države ter klube bomo med seboj primerjali in gledali razlike med njimi.
## Zajem podatkov
V tej projektni nalogi so podatki pridbljeni iz spletne strani www.timingljubljana.si.
## Struktura naloge
Datoteka `zajem_podatkov.py` pridobi podatke iz spletne strani in jih shrani v datoteko `rezultati.csv`. To datoteko najdemo v mapi `podatki`. V zvezku `analiza.ipynb` pa najdemo analizo podatkov.
## Uporabljene knjižnice
Uporabnik mora imeti ob zagonu programa nameščene naslednje knjižnice:
- requests (za zajem podatkov)
- os (za pot do datotek)
- re (za iskanje s pomočjo regularnih izrazov)
- csv (za ustvarjanje csv datotek)
- BeautifulSoup (za pridobivanje podatkov iz html datotek)
- pandas (za analizo podatkov v Jupyter Notebooku)
- matplot.lib.pyplot (za risanje grafikonov)
## Zagon projekta
Za pridobitev podatkov s spleta poženemo datoteko `zajem_podatkov.py`. Ko je datoteka `rezultati.csv` v mapi `podatki` lahko poženemo program `analiza.ipynb`za analizo podatkov.
