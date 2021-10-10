from typing import Text
from numpy.core.numeric import NaN
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
import re

casas_zapopan = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/zapopan/page-'
    url_part2 = '/v1c1293l14828p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_zapopan.append(property_info)
    print('casa en zapopan sep 21:', len(casas_zapopan)) 
    time.sleep(3)   
dfzap = pd.DataFrame(casas_zapopan)
print(dfzap.head())
dfzap1=dfzap.drop_duplicates(subset='imgslink',keep='first') 
dfzap2=dfzap1
dfzap2.to_csv('casas_zapopan_sep21.csv')
print('df1 sin duplicados:',len(dfzap1))
print('df2 sin NaN:',len(dfzap2))

casas_monterrey = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/monterrey/page-'
    url_part2 = '/v1c1293l10980p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_monterrey.append(property_info)
    print('casa en monterrey sep 21:', len(casas_monterrey)) 
    time.sleep(3)   
dfmty = pd.DataFrame(casas_monterrey)
print(dfmty.head())
dfmty1=dfmty.drop_duplicates(subset='imgslink',keep='first')
dfmty2=dfmty1
dfmty2.to_csv('casas_monterrey_sep21.csv')
print('dfmty1 sin duplicados:',len(dfmty1))
print('dfmty2 sin NaN:',len(dfmty2))

casas_nuevas_monterrey = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/monterrey/fraccionamientos+nuevos/page-'
    url_part2 = '/v1c1293l10980q0p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_nuevas_monterrey.append(property_info)
    print('casa nuevas en monterrey sep 21:', len(casas_nuevas_monterrey)) 
    time.sleep(3)   
dfnmty = pd.DataFrame(casas_nuevas_monterrey)
print(dfnmty.head())
dfnmty1=dfnmty.drop_duplicates(subset='imgslink',keep='first')
dfnmty2=dfnmty1
dfnmty2.to_csv('casas_nuevas_monterrey_sep21.csv')
print('dfnmty1 sin duplicados:',len(dfnmty1))
print('dfnmty2 sin NaN:',len(dfnmty2))

casas_tijuana = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/tijuana/page-'
    url_part2 = '/v1c1293l10015p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tijuana.append(property_info)
    print('casa en tijuana sep 21:', len(casas_tijuana)) 
    time.sleep(3)   
dftj = pd.DataFrame(casas_tijuana)
print(dftj.head())
dftj1=dftj.drop_duplicates(subset='imgslink',keep='first')
dftj2=dftj1
dftj2.to_csv('casas_tijuana_sep21.csv')
print('dftj1 sin duplicados:',len(dftj1))
print('dftj2 sin NaN:',len(dftj2))

casas_mexicali = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/mexicali/page-'
    url_part2 = '/v1c1293l10012p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_mexicali.append(property_info)
    print('casa en mexicali sep 21:', len(casas_mexicali)) 
    time.sleep(3)   
dfmxi = pd.DataFrame(casas_mexicali)
print(dfmxi.head())
dfmxi1=dfmxi.drop_duplicates(subset='imgslink',keep='first')
dfmxi2=dfmxi1
dfmxi2.to_csv('casas_mexicali_sep21.csv')
print('dfmxi1 sin duplicados:',len(dfmxi1))
print('dfmxi2 sin NaN:',len(dfmxi2))

casas_ensenada = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/ensenada/page-'
    url_part2 = '/v1c1293l10011p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_ensenada.append(property_info)
    print('casa en ensenada sep 21:', len(casas_ensenada)) 
    time.sleep(3)   
dfens = pd.DataFrame(casas_ensenada)
print(dfens.head())
dfens1=dfens.drop_duplicates(subset='imgslink',keep='first')
dfens2=dfens1
dfens2.to_csv('casas_ensenada_sep21.csv')
print('dfens1 sin duplicados:',len(dfens1))
print('dfens2 sin NaN:',len(dfens2))

casas_morelia = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/michoacan/page-'
    url_part2 = '/v1c1293l1015p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_morelia.append(property_info)
    print('casa en morelia sep 21:', len(casas_morelia)) 
    time.sleep(3)   
dfmor = pd.DataFrame(casas_morelia)
print(dfmor.head())
dfmor1=dfmor.drop_duplicates(subset='imgslink',keep='first')
dfmor2=dfmor1
dfmor2.to_csv('casas_morelia_sep21.csv')
print('dfmor1 sin duplicados:',len(dfmor1))
print('dfmor2 sin NaN:',len(dfmor2))

casas_uruapan = []
for x in range(1,13):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/uruapan-michoacan/page-'
    url_part2 = '/v1c1293l16484p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_uruapan.append(property_info)
    print('casa en uruapan sep 21:', len(casas_uruapan)) 
    time.sleep(3)   
dfuru = pd.DataFrame(casas_uruapan)
print(dfuru.head())
dfuru1=dfuru.drop_duplicates(subset='imgslink',keep='first')
dfuru2=dfuru1
dfuru2.to_csv('casas_uruapan_sep21.csv')
print('dfuru1 sin duplicados:',len(dfuru1))
print('dfrur2 sin NaN:',len(dfuru2))

casas_zamora = []
for x in range(1,5):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/zamora/page-'
    url_part2 = '/v1c1293l10883p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_zamora.append(property_info)
    print('casa en zamora sep 21:', len(casas_zamora)) 
    time.sleep(3)   
dfzam = pd.DataFrame(casas_zamora)
print(dfzam.head())
dfzam1=dfzam.drop_duplicates(subset='imgslink',keep='first')
dfzam2=dfzam1
dfzam2.to_csv('casas_zamora_sep21.csv')
print('dfzam1 sin duplicados:',len(dfzam1))
print('dfzam2 sin NaN:',len(dfzam2))

casas_los_cabos = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/los-cabos/page-'
    url_part2 = '/v1c1293l10019p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_los_cabos.append(property_info)
    print('casa en los cabos sep 21:', len(casas_los_cabos)) 
    time.sleep(3)   
dfcab = pd.DataFrame(casas_los_cabos)
print(dfcab.head())
dfcab1=dfcab.drop_duplicates(subset='imgslink',keep='first')
dfcab2=dfcab1
dfcab2.to_csv('casas_los_cabos_sep21.csv')
print('dfcab1 sin duplicados:',len(dfcab1))
print('dfcab2 sin NaN:',len(dfcab2))

casas_la_paz = []
for x in range(1,34):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/la-paz-bcs/page-'
    url_part2 = '/v1c1293l10017p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_la_paz.append(property_info)
    print('casa en la paz sep 21:', len(casas_la_paz)) 
    time.sleep(3)   
dfpaz = pd.DataFrame(casas_la_paz)
print(dfpaz.head())
dfpaz1=dfpaz.drop_duplicates(subset='imgslink',keep='first')
dfpaz2=dfpaz1
dfpaz2.to_csv('casas_la_paz_sep21.csv')
print('dfpaz1 sin duplicados:',len(dfpaz1))
print('dfpaz2 sin NaN:',len(dfpaz2))

casas_pachuca = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/pachuca-de-soto/page-'
    url_part2 = '/v1c1293l10488p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_pachuca.append(property_info)
    print('casa en pachuca sep 21:', len(casas_pachuca)) 
    time.sleep(3)   
dfpac = pd.DataFrame(casas_pachuca)
print(dfpac.head())
dfpac1=dfpac.drop_duplicates(subset='imgslink',keep='first')
dfpac2=dfpac1
dfpac2.to_csv('casas_pachuca_sep21.csv')
print('dfpac1 sin duplicados:',len(dfpac1))
print('dfpac2 sin NaN:',len(dfpac2))

casas_mineral_de_la_reforma = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/mineral-de-la-reforma/page-'
    url_part2 = '/v1c1293l10480p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_mineral_de_la_reforma.append(property_info)
    print('casa en mineral de la reforma sep 21:', len(casas_mineral_de_la_reforma)) 
    time.sleep(3)   
dfmin = pd.DataFrame(casas_mineral_de_la_reforma)
print(dfmin.head())
dfmin1=dfmin.drop_duplicates(subset='imgslink',keep='first')
dfmin2=dfmin1
dfmin2.to_csv('casas_mineral_de_la_reforma_sep21.csv')
print('dfmin1 sin duplicados:',len(dfmin1))
print('dfmin2 sin NaN:',len(dfmin2))

casas_ciudad_de_mexico = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/distrito-federal/page-'
    url_part2 = '/v1c1293l1008p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_ciudad_de_mexico.append(property_info)
    print('casa en ciudad de mexico sep 21:', len(casas_ciudad_de_mexico)) 
    time.sleep(3)   
dfcdmx = pd.DataFrame(casas_ciudad_de_mexico)
print(dfcdmx.head())
dfcdmx1=dfcdmx.drop_duplicates(subset='imgslink',keep='first')
dfcdmx2=dfcdmx1
dfcdmx2.to_csv('casas_ciudad_de_mexico_sep21.csv')
print('dfcdmx1 sin duplicados:',len(dfcdmx1))
print('dfcdmx2 sin NaN:',len(dfcdmx2))

casas_campeche = []
for x in range(1,16):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/campeche-campeche/page-'
    url_part2 = '/v1c1293l16970p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_campeche.append(property_info)
    print('casa en campeche sep 21:', len(casas_campeche)) 
    time.sleep(3)   
dfcam = pd.DataFrame(casas_campeche)
print(dfcam.head())
dfcam1=dfcam.drop_duplicates(subset='imgslink',keep='first')
dfcam2=dfcam1
dfcam2.to_csv('casas_campeche_sep21.csv')
print('dfcam1 sin duplicados:',len(dfcam1))
print('dfcam2 sin NaN:',len(dfcam2))

casas_ciudad_del_carmen = []
for x in range(1,28):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/ciudad-del-carmen/page-'
    url_part2 = '/v1c1293l15016p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_ciudad_del_carmen.append(property_info)
    print('casa en ciudad del carmen sep 21:', len(casas_ciudad_del_carmen)) 
    time.sleep(3)   
dfcdc = pd.DataFrame(casas_ciudad_del_carmen)
print(dfcdc.head())
dfcdc1=dfcdc.drop_duplicates(subset='imgslink',keep='first')
dfcdc2=dfcdc1
dfcdc2.to_csv('casas_ciudad_del_carmen_sep21.csv')
print('dfcdc1 sin duplicados:',len(dfcdc1))
print('dfcdc2 sin NaN:',len(dfcdc2))

casas_tuxtla = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/tuxtla-gutierrez-chiapas/page-'
    url_part2 = '/v1c1293l16488p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tuxtla.append(property_info)
    print('casa en tuxtla sep 21:', len(casas_tuxtla)) 
    time.sleep(3)   
dftux = pd.DataFrame(casas_tuxtla)
print(dftux.head())
dftux1=dftux.drop_duplicates(subset='imgslink',keep='first')
dftux2=dftux1
dftux2.to_csv('casas_tuxtla_sep21.csv')
print('dftux1 sin duplicados:',len(dftux1))
print('dftux2 sin NaN:',len(dftux2))

casas_tapachula = []
for x in range(1,9):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/tapachula/page-'
    url_part2 = '/v1c1293l10129p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tapachula.append(property_info)
    print('casa en tapachula sep 21:', len(casas_tapachula)) 
    time.sleep(3)   
dftap = pd.DataFrame(casas_tapachula)
print(dftap.head())
dftap1=dftap.drop_duplicates(subset='imgslink',keep='first')
dftap2=dftap1
dftap2.to_csv('casas_tapachula_sep21.csv')
print('dftap1 sin duplicados:',len(dftap1))
print('dftap2 sin NaN:',len(dftap2))



casas_colima = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/colima-col/page-'
    url_part2 = '/v1c1293l10256p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_colima.append(property_info)
    print('casa en colima sep 21:', len(casas_colima)) 
    time.sleep(3)   
dfcol = pd.DataFrame(casas_colima)
print(dfcol.head())
dfcol1=dfcol.drop_duplicates(subset='imgslink',keep='first')
dfcol2=dfcol1
dfcol2.to_csv('casas_colima_sep21.csv')
print('dfcol1 sin duplicados:',len(dfcol1))
print('dfcol2 sin NaN:',len(dfcol2))

casas_manzanillo = []
for x in range(1,16):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/manzanillo/page-'
    url_part2 = '/v1c1293l10261p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_manzanillo.append(property_info)
    print('casa en manzanillo sep 21:', len(casas_manzanillo)) 
    time.sleep(3)   
dfman = pd.DataFrame(casas_manzanillo)
print(dfman.head())
dfman1=dfman.drop_duplicates(subset='imgslink',keep='first')
dfman2=dfman1
dfman2.to_csv('casas_manzanillo_sep21.csv')
print('dfman1 sin duplicados:',len(dfman1))
print('dfman2 sin NaN:',len(dfman2))

casas_torreon = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/torreon/page-'
    url_part2 = '/v1c1293l10251p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_torreon.append(property_info)
    print('casa en torreon sep 21:', len(casas_torreon)) 
    time.sleep(3)   
dftrc = pd.DataFrame(casas_torreon)
print(dftrc.head())
dftrc1=dftrc.drop_duplicates(subset='imgslink',keep='first')
dftrc2=dftrc1
dftrc2.to_csv('casas_torreon_sep21.csv')
print('dftrc1 sin duplicados:',len(dftrc1))
print('dftrc2 sin NaN:',len(dftrc2))

casas_saltillo = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/saltillo/page-'
    url_part2 = '/v1c1293l10246p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_saltillo.append(property_info)
    print('casa en saltillo sep 21:', len(casas_saltillo)) 
    time.sleep(3)   
dfsal = pd.DataFrame(casas_saltillo)
print(dfsal.head())
dfsal1=dfsal.drop_duplicates(subset='imgslink',keep='first')
dfsal2=dfsal1
dfsal2.to_csv('casas_saltillo_sep21.csv')
print('dfsal1 sin duplicados:',len(dfsal1))
print('dfsal2 sin NaN:',len(dfsal2))

casas_monclova = []
for x in range(1,4):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/monclova/page-'
    url_part2 = '/v1c1293l10234p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_monclova.append(property_info)
    print('casa en monclova sep 21:', len(casas_monclova)) 
    time.sleep(3)   
dfmon = pd.DataFrame(casas_monclova)
print(dfmon.head())
dfmon1=dfmon.drop_duplicates(subset='imgslink',keep='first')
dfmon2=dfmon1
dfmon2.to_csv('casas_monclova_sep21.csv')
print('dfmon1 sin duplicados:',len(dfmon1))
print('dfmon2 sin NaN:',len(dfmon2))

casas_guanajuato = []
for x in range(1,19):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/guanajuato-gto/page-'
    url_part2 = '/v1c1293l10334p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_guanajuato.append(property_info)
    print('casa en guanajuato sep 21:', len(casas_guanajuato)) 
    time.sleep(3)   
dfgua = pd.DataFrame(casas_guanajuato)
print(dfgua.head())
dfgua1=dfgua.drop_duplicates(subset='imgslink',keep='first')
dfgua2=dfgua1
dfgua2.to_csv('casas_guanajuato_sep21.csv')
print('dfgua1 sin duplicados:',len(dfgua1))
print('dfgua2 sin NaN:',len(dfgua2))

casas_leon = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/leon/page-'
    url_part2 = '/v1c1293l10339p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_leon.append(property_info)
    print('casa en leon sep 21:', len(casas_leon)) 
    time.sleep(3)   
dfleo = pd.DataFrame(casas_leon)
print(dfleo.head())
dfleo1=dfleo.drop_duplicates(subset='imgslink',keep='first')
dfleo2=dfleo1
dfleo2.to_csv('casas_leon_sep21.csv')
print('dfleo1 sin duplicados:',len(dfleo1))
print('dfleo2 sin NaN:',len(dfleo2))







casas_acapulco = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/acapulco-de-juarez-guerrero/page-'
    url_part2 = '/v1c1293l17049p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_acapulco.append(property_info)
    print('casa en acapulco sep 21:', len(casas_acapulco)) 
    time.sleep(3)   
dfaca = pd.DataFrame(casas_acapulco)
print(dfaca.head())
dfaca1=dfaca.drop_duplicates(subset='imgslink',keep='first')
dfaca2=dfaca1
dfaca2.to_csv('casas_acapulco_sep21.csv')
print('dfaca1 sin duplicados:',len(dfaca1))
print('dfaca2 sin NaN:',len(dfaca2))

casas_chilpancingo = []
for x in range(1,5):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/acapulco-de-juarez-guerrero/page-'
    url_part2 = '/v1c1293l17049p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_chilpancingo.append(property_info)
    print('casa en chilpancingo sep 21:', len(casas_chilpancingo)) 
    time.sleep(3)   
dfchil = pd.DataFrame(casas_chilpancingo)
print(dfchil.head())
dfchil1=dfchil.drop_duplicates(subset='imgslink',keep='first')
dfchil2=dfchil1
dfchil2.to_csv('casas_chilpancingo_sep21.csv')
print('dfchil1 sin duplicados:',len(dfchil1))
print('dfchil2 sin NaN:',len(dfchil2))

casas_cuernavaca = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/cuernavaca/page-'
    url_part2 = '/v1c1293l10894p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_cuernavaca.append(property_info)
    print('casa en cuernavaca sep 21:', len(casas_cuernavaca)) 
    time.sleep(3)   
dfcue = pd.DataFrame(casas_chilpancingo)
print(dfcue.head())
dfcue1=dfcue.drop_duplicates(subset='imgslink',keep='first')
dfcue2=dfcue1
dfcue2.to_csv('casas_cuernavaca_sep21.csv')
print('dfcue1 sin duplicados:',len(dfcue1))
print('dfcue2 sin NaN:',len(dfcue2))

casas_jiutepec = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/jiutepec-morelos/page-'
    url_part2 = '/v1c1293l16813p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_jiutepec.append(property_info)
    print('casa en jiutepec sep 21:', len(casas_jiutepec)) 
    time.sleep(3)   
dfjiu = pd.DataFrame(casas_jiutepec)
print(dfjiu.head())
dfjiu1=dfjiu.drop_duplicates(subset='imgslink',keep='first')
dfjiu2=dfjiu1
dfjiu2.to_csv('casas_jiutepec_sep21.csv')
print('dfjiu1 sin duplicados:',len(dfjiu1))
print('dfjiu2 sin NaN:',len(dfjiu2))

casas_tepic = []
for x in range(1,14):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/tepic/page-'
    url_part2 = '/v1c1293l1534p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tepic.append(property_info)
    print('casa en tepic sep 21:', len(casas_tepic)) 
    time.sleep(3)   
dftep = pd.DataFrame(casas_tepic)
print(dftep.head())
dftep1=dftep.drop_duplicates(subset='imgslink',keep='first')
dftep2=dftep1
dftep2.to_csv('casas_tepic_sep21.csv')
print('dftep1 sin duplicados:',len(dftep1))
print('dftep2 sin NaN:',len(dftep2))

casas_benito_juarez = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/benito-juarez-q-roo/page-'
    url_part2 = '/v1c1293l11797p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_benito_juarez.append(property_info)
    print('casa en benito juarez sep 21:', len(casas_benito_juarez)) 
    time.sleep(3)   
dfcan = pd.DataFrame(casas_benito_juarez)
print(dfcan.head())
dfcan1=dfcan.drop_duplicates(subset='imgslink',keep='first')
dfcan2=dfcan1
dfcan2.to_csv('casas_benito_juarez_sep21.csv')
print('dfcan1 sin duplicados:',len(dfcan1))
print('dfcan2 sin NaN:',len(dfcan2))

casas_tulum = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/tulum/page-'
    url_part2 = '/v1c1293l14909p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tulum.append(property_info)
    print('casa en tulum sep 21:', len(casas_tulum)) 
    time.sleep(3)   
dftul = pd.DataFrame(casas_tulum)
print(dftul.head())
dftul1=dftul.drop_duplicates(subset='imgslink',keep='first')
dftul2=dftul1
dftul2.to_csv('casas_tulum_sep21.csv')
print('dftul1 sin duplicados:',len(dftul1))
print('dftul2 sin NaN:',len(dftul2))

casas_isla_mujeres = []
for x in range(1,24):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/isla-mujeres/page-'
    url_part2 = '/v1c1293l11800p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_isla_mujeres.append(property_info)
    print('casa en isla mujeres sep 21:', len(casas_isla_mujeres)) 
    time.sleep(3)   
dfisl = pd.DataFrame(casas_isla_mujeres)
print(dfisl.head())
dfisl1=dfisl.drop_duplicates(subset='imgslink',keep='first')
dfisl2=dfisl1
dfisl2.to_csv('casas_isla_mujeres_sep21.csv')
print('dfisl1 sin duplicados:',len(dfisl1))
print('dfisl2 sin NaN:',len(dfisl2))

casas_cozumel = []
for x in range(1,4):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/cozumel/page-'
    url_part2 = '/v1c1293l11798p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_cozumel.append(property_info)
    print('casa en cozumel sep 21:', len(casas_cozumel)) 
    time.sleep(3)   
dfcoz = pd.DataFrame(casas_cozumel)
print(dfcoz.head())
dfcoz1=dfcoz.drop_duplicates(subset='imgslink',keep='first')
dfcoz2=dfcoz1
dfcoz2.to_csv('casas_cozumel_sep21.csv')
print('dfcoz1 sin duplicados:',len(dfcoz1))
print('dfcoz2 sin NaN:',len(dfcoz2))

casas_solidaridad = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/solidaridad/page-'
    url_part2 = '/v1c1293l11804p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_solidaridad.append(property_info)
    print('casa en solidaridad sep 21:', len(casas_solidaridad)) 
    time.sleep(3)   
dfsol = pd.DataFrame(casas_solidaridad)
print(dfsol.head())
dfsol1=dfsol.drop_duplicates(subset='imgslink',keep='first')
dfsol2=dfsol1
dfsol2.to_csv('casas_solidaridad_sep21.csv')
print('dfsol1 sin duplicados:',len(dfsol1))
print('dfsol2 sin NaN:',len(dfsol2))

casas_puebla = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/puebla-pue/page-'
    url_part2 = '/v1c1293l11677p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_puebla.append(property_info)
    print('casa en puebla sep 21:', len(casas_puebla)) 
    time.sleep(3)   
dfpue = pd.DataFrame(casas_puebla)
print(dfpue.head())
dfpue1=dfpue.drop_duplicates(subset='imgslink',keep='first')
dfpue2=dfpue1
dfpue2.to_csv('casas_puebla_sep21.csv')
print('dfpue1 sin duplicados:',len(dfpue1))
print('dfpue2 sin NaN:',len(dfpue2))

casas_tehuacan = []
for x in range(1,6):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/tehuacan/page-'
    url_part2 = '/v1c1293l11717p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tehuacan.append(property_info)
    print('casa en tehuacan sep 21:', len(casas_tehuacan)) 
    time.sleep(3)   
dfteh = pd.DataFrame(casas_tehuacan)
print(dfteh.head())
dfteh1=dfteh.drop_duplicates(subset='imgslink',keep='first')
dfteh2=dfteh1
dfteh2.to_csv('casas_tehuacan_sep21.csv')
print('dfteh1 sin duplicados:',len(dfteh1))
print('dfteh2 sin NaN:',len(dfteh2))

casas_hermosillo = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/hermosillo/page-'
    url_part2 = '/v1c1293l11912p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_hermosillo.append(property_info)
    print('casa en hermosillo sep 21:', len(casas_hermosillo)) 
    time.sleep(3)   
dfher = pd.DataFrame(casas_hermosillo)
print(dfher.head())
dfher1=dfher.drop_duplicates(subset='imgslink',keep='first')
dfher2=dfher1
dfher2.to_csv('casas_hermosillo_sep21.csv')
print('dfher1 sin duplicados:',len(dfher1))
print('dfher2 sin NaN:',len(dfher2))

casas_bahia_de_kino = []
for x in range(1,2):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/bahia-de-kino/page-'
    url_part2 = '/v1c1293l15732p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_bahia_de_kino.append(property_info)
    print('casa en bahia de kino sep 21:', len(casas_bahia_de_kino)) 
    time.sleep(3)   
dfkin = pd.DataFrame(casas_bahia_de_kino)
print(dfkin.head())
dfkin1=dfkin.drop_duplicates(subset='imgslink',keep='first')
dfkin2=dfkin1
dfkin2.to_csv('casas_bahia_de_kino_sep21.csv')
print('dfkin1 sin duplicados:',len(dfkin1))
print('dfkin2 sin NaN:',len(dfkin2))

casas_san_carlos = []
for x in range(1,3):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/san-carlos-son/page-'
    url_part2 = 'v1c1293l16249p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_san_carlos.append(property_info)
    print('casa en san carlos sep 21:', len(casas_san_carlos)) 
    time.sleep(3)   
dfcar = pd.DataFrame(casas_san_carlos)
print(dfcar.head())
dfcar1=dfcar.drop_duplicates(subset='imgslink',keep='first')
dfcar2=dfcar1
dfcar2.to_csv('casas_san_carlos_sep21.csv')
print('dfcar1 sin duplicados:',len(dfcar1))
print('dfcar2 sin NaN:',len(dfcar2))

casas_cajeme = []
for x in range(1,22):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/cajeme/page-'
    url_part2 = '/v1c1293l11900p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_cajeme.append(property_info)
    print('casa en cajeme sep 21:', len(casas_cajeme)) 
    time.sleep(3)   
dfcaj = pd.DataFrame(casas_cajeme)
print(dfcaj.head())
dfcaj1=dfcaj.drop_duplicates(subset='imgslink',keep='first')
dfcaj2=dfcaj1
dfcaj2.to_csv('casas_cajeme_sep21.csv')
print('dfcaj1 sin duplicados:',len(dfcaj1))
print('dfcaj2 sin NaN:',len(dfcaj2))

casas_nogales = []
for x in range(1,4):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/nogales-son/page-'
    url_part2 = '/v1c1293l11927p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_nogales.append(property_info)
    print('casa en nogales sep 21:', len(casas_nogales)) 
    time.sleep(3)   
dfnog = pd.DataFrame(casas_nogales)
print(dfnog.head())
dfnog1=dfnog.drop_duplicates(subset='imgslink',keep='first')
dfnog2=dfnog1
dfnog2.to_csv('casas_nogales_sep21.csv')
print('dfnog1 sin duplicados:',len(dfnog1))
print('dfnog2 sin NaN:',len(dfnog2))

casas_queretaro = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/queretaro-qro/page-'
    url_part2 = '/v1c1293l11792p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_queretaro.append(property_info)
    print('casa en queretaro sep 21:', len(casas_queretaro)) 
    time.sleep(3)   
dfque = pd.DataFrame(casas_queretaro)
print(dfque.head())
dfque1=dfque.drop_duplicates(subset='imgslink',keep='first')
dfque2=dfque1
dfque2.to_csv('casas_queretaro_sep21.csv')
print('dfque1 sin duplicados:',len(dfque1))
print('dfque2 sin NaN:',len(dfque2))

casas_merida = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/merida/page-'
    url_part2 = '/v1c1293l12332p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_merida.append(property_info)
    print('casa en merida sep 21:', len(casas_merida)) 
    time.sleep(3)   
dfmer = pd.DataFrame(casas_merida)
print(dfmer.head())
dfmer1=dfmer.drop_duplicates(subset='imgslink',keep='first')
dfmer2=dfmer1
dfmer2.to_csv('casas_merida_sep21.csv')
print('dfmer1 sin duplicados:',len(dfmer1))
print('dfmer2 sin NaN:',len(dfmer2))

casas_tlaxcala = []
for x in range(1,6):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/tlaxcala-tlax/page-'
    url_part2 = '/v1c1293l12062p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tlaxcala.append(property_info)
    print('casa en tlaxcala sep 21:', len(casas_tlaxcala)) 
    time.sleep(3)   
dftla = pd.DataFrame(casas_tlaxcala)
print(dftla.head())
dftla1=dftla.drop_duplicates(subset='imgslink',keep='first')
dftla2=dftla1
dftla2.to_csv('casas_tlaxcala_sep21.csv')
print('dftla1 sin duplicados:',len(dftla1))
print('dftla2 sin NaN:',len(dftla2))

casas_san_luis_potosi = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/san-luis-potosi-slp/page-'
    url_part2 = '/v1c1293l11834p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_san_luis_potosi.append(property_info)
    print('casa en san luis potosi sep 21:', len(casas_san_luis_potosi)) 
    time.sleep(3)   
dfsan = pd.DataFrame(casas_san_luis_potosi)
print(dfsan.head())
dfsan1=dfsan.drop_duplicates(subset='imgslink',keep='first')
dfsan2=dfsan1
dfsan2.to_csv('casas_san_luis_potosi_sep21.csv')
print('dfsan1 sin duplicados:',len(dfsan1))
print('dfsan2 sin NaN:',len(dfsan2))

casas_mazatlan = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/mazatlan/page-'
    url_part2 = '/v1c1293l11875p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_mazatlan.append(property_info)
    print('casa en mazatlan sep 21:', len(casas_mazatlan)) 
    time.sleep(3)   
dfmza = pd.DataFrame(casas_mazatlan)
print(dfmza.head())
dfmza1=dfmza.drop_duplicates(subset='imgslink',keep='first')
dfmza2=dfmza1
dfmza2.to_csv('casas_mazatlan_sep21.csv')
print('dfmza1 sin duplicados:',len(dfmza1))
print('dfmza2 sin NaN:',len(dfmza2))

casas_culiacan = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/culiacan/page-'
    url_part2 = '/v1c1293l11869p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_culiacan.append(property_info)
    print('casa en culiacan sep 21:', len(casas_culiacan)) 
    time.sleep(3)   
dfcul = pd.DataFrame(casas_culiacan)
print(dfcul.head())
dfcul1=dfcul.drop_duplicates(subset='imgslink',keep='first')
dfcul2=dfcul1
dfcul2.to_csv('casas_culiacan_sep21.csv')
print('dfcul1 sin duplicados:',len(dfcul1))
print('dfcul2 sin NaN:',len(dfcul2))

casas_tabasco = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/centro/page-'
    url_part2 = 'v1c1293l11957p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_tabasco.append(property_info)
    print('casa en tabasco sep 21:', len(casas_tabasco)) 
    time.sleep(3)   
dftab = pd.DataFrame(casas_tabasco)
print(dftab.head())
dftab1=dftab.drop_duplicates(subset='imgslink',keep='first')
dftab2=dftab1
dftab2.to_csv('casas_tabasco_sep21.csv')
print('dftab1 sin duplicados:',len(dftab1))
print('dftab2 sin NaN:',len(dftab2))

casas_matamoros = []
for x in range(1,10):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/matamoros-tamps/page-'
    url_part2 = '/v1c1293l11991p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_matamoros.append(property_info)
    print('casa en matamoros sep 21:', len(casas_matamoros)) 
    time.sleep(3)   
dfmat = pd.DataFrame(casas_matamoros)
print(dfmat.head())
dfmat1=dfmat.drop_duplicates(subset='imgslink',keep='first')
dfmat2=dfmat1
dfmat2.to_csv('casas_matamoros_sep21.csv')
print('dfmat1 sin duplicados:',len(dfmat1))
print('dfmat2 sin NaN:',len(dfmat2))

casas_nuevo_laredo = []
for x in range(1,7):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/nuevo-laredo/page-'
    url_part2 = 'v1c1293l11996p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_nuevo_laredo.append(property_info)
    print('casa en nuevo laredo sep 21:', len(casas_nuevo_laredo)) 
    time.sleep(3)   
dflar = pd.DataFrame(casas_nuevo_laredo)
print(dflar.head())
dflar1=dflar.drop_duplicates(subset='imgslink',keep='first')
dflar2=dflar1
dflar2.to_csv('casas_nuevo_laredo_sep21.csv')
print('dflar1 sin duplicados:',len(dflar1))
print('dflar2 sin NaN:',len(dflar2))

casas_boca_del_rio = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/boca-del-rio/page-'
    url_part2 = 'v1c1293l12097p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_boca_del_rio.append(property_info)
    print('casa en boca del rio sep 21:', len(casas_boca_del_rio)) 
    time.sleep(3)   
dfboc = pd.DataFrame(casas_boca_del_rio)
print(dfboc.head())
dfboc1=dfboc.drop_duplicates(subset='imgslink',keep='first')
dfboc2=dfboc1
dfboc2.to_csv('casas_boca_del_rio_sep21.csv')
print('dfboc1 sin duplicados:',len(dfboc1))
print('dfboc2 sin NaN:',len(dfboc2))

casas_coatzacoalcos = []
for x in range(1,30):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/coatzacoalcos/page-'
    url_part2 = '/v1c1293l12121p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_coatzacoalcos.append(property_info)
    print('casa en coatzacoalcos sep 21:', len(casas_coatzacoalcos)) 
    time.sleep(3)   
dfcoa = pd.DataFrame(casas_coatzacoalcos)
print(dfcoa.head())
dfcoa1=dfcoa.drop_duplicates(subset='imgslink',keep='first')
dfcoa2=dfcoa1
dfcoa2.to_csv('casas_coatzacoalcos_sep21.csv')
print('dfcoa1 sin duplicados:',len(dfcoa1))
print('dfcoa2 sin NaN:',len(dfcoa2))

casas_cordoba = []
for x in range(1,34):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/cordoba-veracruz/page-'
    url_part2 = '/v1c1293l16925p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_cordoba.append(property_info)
    print('casa en cordoba sep 21:', len(casas_cordoba)) 
    time.sleep(3)   
dfcor = pd.DataFrame(casas_cordoba)
print(dfcor.head())
dfcor1=dfcor.drop_duplicates(subset='imgslink',keep='first')
dfcor2=dfcor1
dfcor2.to_csv('casas_cordoba_sep21.csv')
print('dfcor1 sin duplicados:',len(dfcor1))
print('dfcor2 sin NaN:',len(dfcor2))

casas_zacatecas = []
for x in range(1,6):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/zacatecas-zac/page-'
    url_part2 = '/v1c1293l12446p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_zacatecas.append(property_info)
    print('casa en zacatecas sep 21:', len(casas_zacatecas)) 
    time.sleep(3)   
dfzac = pd.DataFrame(casas_zacatecas)
print(dfzac.head())
dfzac1=dfzac.drop_duplicates(subset='imgslink',keep='first')
dfzac2=dfzac1
dfzac2.to_csv('casas_zacatecas_sep21.csv')
print('dfzac1 sin duplicados:',len(dfzac1))
print('dfzac2 sin NaN:',len(dfzac2))

casas_guadalupe_zacatecas = []
for x in range(1,16):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/guadalupe-zac/page-'
    url_part2 = '/v1c1293l12405p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_guadalupe_zacatecas.append(property_info)
    print('casa en guadalupe zacatecas sep 21:', len(casas_guadalupe_zacatecas)) 
    time.sleep(3)   
dfgza = pd.DataFrame(casas_guadalupe_zacatecas)
print(dfgza.head())
dfgza1=dfgza.drop_duplicates(subset='imgslink',keep='first')
dfgza2=dfgza1
dfgza2.to_csv('casas_guadalupe_zacatecas_sep21.csv')
print('dfgza1 sin duplicados:',len(dfgza1))
print('dfgza2 sin NaN:',len(dfgza2))

casas_fresnillo = []
for x in range(1,1):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/fresnillo-zacatecas'
    url_part2 = '/v1c1293l16872p1'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_fresnillo.append(property_info)
    print('casa en fresnillo sep 21:', len(casas_fresnillo)) 
    time.sleep(3)   
dffre = pd.DataFrame(casas_fresnillo)
print(dffre.head())
dffre1=dffre.drop_duplicates(subset='imgslink',keep='first')
dffre2=dffre1
dffre2.to_csv('casas_fresnillo_sep21.csv')
print('dffre1 sin duplicados:',len(dffre1))
print('dffre2 sin NaN:',len(dffre2))


casas_guadalupe = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/guadalupe/page-'
    url_part2 = '/v1c1293l14838p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_guadalupe.append(property_info)
    print('casa en guadalupe sep 21:', len(casas_guadalupe)) 
    time.sleep(3)   
dfgua = pd.DataFrame(casas_guadalupe)
print(dfgua.head())
dfgua1=dfgua.drop_duplicates(subset='imgslink',keep='first')
dfgua2=dfgua1
dfgua2.to_csv('casas_guadalupe_sep21.csv')
print('dfgua1 sin duplicados:',len(dfgua1))
print('dfgua2 sin NaN:',len(dfgua2))

casas_apodaca = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/apodaca/page-'
    url_part2 = '/v1c1293l14832p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_apodaca.append(property_info)
    print('casa en apodaca sep 21:', len(casas_apodaca)) 
    time.sleep(3)   
dfapo = pd.DataFrame(casas_apodaca)
print(dfapo.head())
dfapo1=dfapo.drop_duplicates(subset='imgslink',keep='first')
dfapo2=dfapo1
dfapo2.to_csv('casas_apodaca_sep21.csv')
print('dfapo1 sin duplicados:',len(dfapo1))
print('dfapo2 sin NaN:',len(dfapo2))

casas_san_pedro = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/san-pedro-valle/page-'
    url_part2 = '/v1c1293l14842p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_san_pedro.append(property_info)
    print('casa en san pedro sep 21:', len(casas_san_pedro)) 
    time.sleep(3)   
dfspg = pd.DataFrame(casas_san_pedro)
print(dfspg.head())
dfspg1=dfspg.drop_duplicates(subset='imgslink',keep='first')
dfspg2=dfspg1
dfspg2.to_csv('casas_san_pedro_sep21.csv')
print('dfspg1 sin duplicados:',len(dfspg1))
print('dfspg2 sin NaN:',len(dfspg2))

casas_guadalajara = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/guadalajara/page-'
    url_part2 = '/v1c1293l14822p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_guadalajara.append(property_info)
    print('casa en guadalajara sep 21:', len(casas_guadalajara)) 
    time.sleep(3)   
dfgua = pd.DataFrame(casas_guadalajara)
print(dfgua.head())
dfgua1=dfgua.drop_duplicates(subset='imgslink',keep='first')
dfgua2=dfgua1
dfgua2.to_csv('casas_guadalajara_sep21.csv')
print('dfgua1 sin duplicados:',len(dfgua1))
print('dfgua2 sin NaN:',len(dfgua2))




casas_atizapan = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/atizapan-de-zaragoza/page-'
    url_part2 = '/v1c1293l10663p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_atizapan.append(property_info)
    print('casa en atizapan sep 21:', len(casas_atizapan)) 
    time.sleep(3)   
dfati = pd.DataFrame(casas_atizapan)
print(dfati.head())
dfati1=dfati.drop_duplicates(subset='imgslink',keep='first')
dfati2=dfati1
dfati2.to_csv('casas_atizapan_sep21.csv')
print('dfati1 sin duplicados:',len(dfati1))
print('dfati2 sin NaN:',len(dfati2))

casas_ecatepec = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/ecatepec-de-morelos/page-'
    url_part2 = '/v1c1293l10684p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_ecatepec.append(property_info)
    print('casa en ecatepec sep 21:', len(casas_ecatepec)) 
    time.sleep(3)   
dfeca = pd.DataFrame(casas_ecatepec)
print(dfeca.head())
dfeca1=dfeca.drop_duplicates(subset='imgslink',keep='first')
dfeca2=dfeca1
dfeca2.to_csv('casas_ecatepec_sep21.csv')
print('dfeca1 sin duplicados:',len(dfeca1))
print('dfeca2 sin NaN:',len(dfeca2))

casas_toluca = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/estado-de-mexico/page-'
    url_part2 = '/v1c1293l1014p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_toluca.append(property_info)
    print('casa en toluca sep 21:', len(casas_toluca)) 
    time.sleep(3)   
dftol = pd.DataFrame(casas_toluca)
print(dftol.head())
dftol1=dftol.drop_duplicates(subset='imgslink',keep='first')
dftol2=dftol1
dftol2.to_csv('casas_toluca_sep21.csv')
print('dftol1 sin duplicados:',len(dftol1))
print('dftol2 sin NaN:',len(dftol2))


casas_nezahualcoyotl = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/nezahualcoyotl/page-'
    url_part2 = '/v1c1293l10712p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_nezahualcoyotl.append(property_info)
    print('casa en nezahualcoyotl sep 21:', len(casas_nezahualcoyotl)) 
    time.sleep(3)   
dfnez = pd.DataFrame(casas_nezahualcoyotl)
print(dfnez.head())
dfnez1=dfnez.drop_duplicates(subset='imgslink',keep='first')
dfnez2=dfnez1
dfnez2.to_csv('casas_nezahualcoyotl_sep21.csv')
print('dfnez1 sin duplicados:',len(dfnez1))
print('dfnez2 sin NaN:',len(dfnez2))

casas_chihuahua = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/chihuahua-chih/page-'
    url_part2 = '/v1c1293l10163p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_chihuahua.append(property_info)
    print('casa en chihuahua sep 21:', len(casas_chihuahua)) 
    time.sleep(3)   
dfchi = pd.DataFrame(casas_chihuahua)
print(dfchi.head())
dfchi1=dfchi.drop_duplicates(subset='imgslink',keep='first')
dfchi2=dfchi1
dfchi2.to_csv('casas_chihuahua_sep21.csv')
print('dfchi1 sin duplicados:',len(dfchi1))
print('dfchi2 sin NaN:',len(dfchi2))

casas_delicias = []
for x in range(1,4):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/delicias/page-'
    url_part2 = '/v1c1293l10169p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_delicias.append(property_info)
    print('casa en delicias sep 21:', len(casas_delicias)) 
    time.sleep(3)   
dfdel = pd.DataFrame(casas_delicias)
print(dfdel.head())
dfdel1=dfdel.drop_duplicates(subset='imgslink',keep='first')
dfdel2=dfdel1
dfdel2.to_csv('casas_delicias_sep21.csv')
print('dfdel1 sin duplicados:',len(dfdel1))
print('dfdel2 sin NaN:',len(dfdel2))

casas_juarez = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/juarez/page-'
    url_part2 = '/v1c1293l10185p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_juarez.append(property_info)
    print('casa en juarez sep 21:', len(casas_juarez)) 
    time.sleep(3)   
dfjua = pd.DataFrame(casas_juarez)
print(dfjua.head())
dfjua1=dfjua.drop_duplicates(subset='imgslink',keep='first')
dfjua2=dfjua1
dfjua2.to_csv('casas_juarez_sep21.csv')
print('dfjua1 sin duplicados:',len(dfjua1))
print('dfjua2 sin NaN:',len(dfjua2))

casas_durango = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/durango-durango/page-'
    url_part2 = '/v1c1293l16909p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_durango.append(property_info)
    print('casa en durango sep 21:', len(casas_durango)) 
    time.sleep(3)   
dfdur = pd.DataFrame(casas_durango)
print(dfdur.head())
dfdur1=dfdur.drop_duplicates(subset='imgslink',keep='first')
dfdur2=dfdur1
dfdur2.to_csv('casas_durango_sep21.csv')
print('dfdur1 sin duplicados:',len(dfdur1))
print('dfdur2 sin NaN:',len(dfdur2))

casas_gomez_palacio = []
for x in range(1,50):
    url_part1 = 'https://www.vivanuncios.com.mx/s-casas-en-venta/gomez-palacio/page-'
    url_part2 = '/v1c1293l10289p'
    r = requests.get((url_part1+str(x)) + (url_part2+str(x)))
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.title)
    content = soup.find_all('div','source','img', class_= 'tileV2 REAdTileV2 regular mapView')
    #print(content)
       
    for property in content:
        try:
            price = (property.find('span', class_="ad-price").text.replace('\n',''))
            bedroom = (property.find('div', class_="chiplets-inline-block re-bedroom").text.replace('+',''))
            bathrooms = (property.find('div', class_= "chiplets-inline-block re-bathroom").text.replace('+',''))
            cochera= (property.find('div', class_= "chiplets-inline-block car-parking").text.replace('+',''))
            m2_terreno= (property.find('div',class_="chiplets-inline-block surface-area").text.replace('m²',''))
            ubicacion = (property.find('div', class_= "tile-location one-liner").text)
            specs = (property.find('a', class_= "href-link tile-title-text").text)
            image=(property.find('div',class_='bolt-image bolt-image-hoverzoom')) 
            image2=(image.img['data-src'])    
        except:
            #price= 'NaN'
            #bedroom = 'NaN'
            bathrooms = (NaN)
            cochera= (NaN)
            #m2_terreno= 'NaN'
            #ubicacion = 'NaN'
            #image= 'NaN'
            #imagenes= 'NaN'
    
        property_info = {
        'price': price,
        'bedroom': bedroom,
        'bathrooms': bathrooms,
        'cochera': cochera,
        'm2_terreno': m2_terreno,
        'ubicacion': ubicacion,
        'specs': specs,
        'imgslink': image2
        }
        casas_gomez_palacio.append(property_info)
    print('casa en gomez palacio sep 21:', len(casas_gomez_palacio)) 
    time.sleep(3)   
dfgom = pd.DataFrame(casas_gomez_palacio)
print(dfgom.head())
dfgom1=dfgom.drop_duplicates(subset='imgslink',keep='first')
dfgom2=dfgom1
dfgom2.to_csv('casas_gomez_palacio_sep21.csv')
print('dfgom1 sin duplicados:',len(dfgom1))
print('dfgom2 sin NaN:',len(dfgom2))

frames=[dfzap2,dfmty2,dfnmty2,dftj2,dfmxi2,dfens2,dfmor2,dfuru2,dfzam2,dfcab2,dfpaz2,dfpac2,dfmin2,dfcdmx2,dfcam2,dfcdc2,dftux2,dftap2,dfcol2,dfman2,dftrc2,dfsal2,dfmon2,dfgua2,dfleo2,dfaca2,dfchil2,dfcue2,dfjiu2,dftep2,dfcan2,dftul2,dfisl2,dfcoz2,dfsol2,dfpue2,dfteh2,dfher2,dfkin2,dfcar2,dfcaj2,dfnog2,dfque2,dfmer2,dftla2,dfsan2,dfmza2,dfcul2,dftab2,dfmat2,dflar2,dfboc2,dfcoa2,dfcor2,dfzac2,dfgza2,dffre2,dfgua2,dfapo2,dfspg2,dfgua2,dfati2,dfeca2,dftol2,dfnez2,dfchi2,dfdel2,dfjua2,dfdur2,dfgom2]
result= pd.concat(frames)
result.to_csv('casas_mexico_sep21.csv')

