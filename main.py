
from bs4 import  BeautifulSoup
import pandas as pd
import requests
def LIDL():
    #Prepare data
    URL = 'https://www.lidl.lt/pasiulymai'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Take all containers
    for container in soup.select("a",{"class":"product__body"}):
        # If container has a price then extract:
        if container.find('span', {"class" : 'pricebox__price'}) is not None:
            #Take name and price from this container
            name = container.find("h3",{"class": "product__title"})
            a.append(name.text.strip())
            price = container.find("span", {"class": "pricebox__price"})
            b.append(price.text.strip())
        else:
            pass
def IKI():
    i = 1
    url = "https://iki.lt/akcijos/savaites-akcijos/page/" + str(i)
    while i<10:
        i = i + 1
        page = requests.get(url)
        if page.status_code != 200:
            break
        URL = "https://iki.lt/akcijos/savaites-akcijos/page/" + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
        for container in soup.select("div",{"class":"akcija__container"}):
            if container.find("span", {"class": "price-cents"}) is not None:
                if container.find('h4', {"class":"akcija__title"}) is not None:
        # If container has a price then extract:
            #Take name and price from this container
                    name = container.find("h4",{"class": "akcija__title"})
                    a.append(name.text.strip())
                    price = container.find("span", {"class": "price-main"}).text.strip()
                    price2=container.find("span", {"class": "price-cents"}).text.strip()
                    price_full=price+ '.' +price2
                    b.append(price_full)
                    Describtion=container.find("div",{"class":"text"})
                    if not Describtion:
                        c.append("")
                    else:
                        c.append(Describtion.text.strip())
                else:
                    pass
            else:
                pass

def maxima():
    URL = 'https://www.maxima.lt/akcijos'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    for container in soup.select("div",{"class":"offer-page-sale-item offer-page-sale-item__actual"}):
        # If container has a price then extract:
        if container.find('span', {"class" : 'value'}) is not None:
            if container.find("div", {"class": "title"}) is not None:

            #Take name and price from this container
                name = container.find("div",{"class": "title"})
                a.append(name.text.strip())
                price = container.find("span", {"class": "value"}).text.strip()
                if container.find("span",{"class": "cents"}) is not None:
                    price_cents = container.find("span", {"class": "cents"}).text.strip()
                else:
                    price_cents = "0"

                if int(price) > 9:
                    price_cents = "% nuolaida"
                    price_total=price + price_cents
                else:
                    price_total=price+"."+price_cents

                b.append(price_total)
            else:
                pass
        else:
            pass
def rimi():
    URL = 'https://www.rimi.lt/akcijos'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    for container in soup.select("div",{"class":"offer-card with-ecom-link"}):
        # If container has a price then extract:
        if container.find('div', {"class" : 'euro'}) is not None:
            #Take name and price from this container
            name = container.find("div",{"class": "offer-card__name"})
            if container.find("div",{"class": "offer-card__name"}) is not None:
                a.append(name.text.strip())
                price = container.find("div", {"class": "euro"})
                price_cents = container.find("div", {"class": "cents"})
                price_total = price.text.strip() + "." + price_cents.text.strip()
                b.append(price_total)
            else:
                pass
        else:
            pass
def printresults():
    print("Maxima kainos")
    print(datamaxima[datamaxima['Maxima Name'].str.contains(word)])
    print("IKI kainos")
    print(dataIKI[dataIKI['IKI Name'].str.contains(word)])
    print("Rimi kainos")
    print(datarimi[datarimi['Name'].str.contains(word)])
    print("Lidl kainos")
    print(dataLIDL[dataLIDL['LIDL Name'].str.contains(word)])
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
dataLIDL = pd.DataFrame({'ID' : ()})
dataIKI = pd.DataFrame({'ID' : ()})
datamaxima = pd.DataFrame({'ID' : ()})
datarimi = pd.DataFrame({'ID' : ()})
word=input("Name:")
a=[]
b=[]
c=[]
rimi()
datarimi.insert(1,'Name', pd.Series(a))
datarimi.insert(2, "Price", pd.Series(b))
a=[]
b=[]
#print(soup.prettify())
LIDL() #Take data from LIDL
dataLIDL.insert(1, 'LIDL Name', pd.Series(a))
dataLIDL.insert(2, "LIDL Price", pd.Series(b))# Add Lidl data to the dataframe
b=[]
a=[]
maxima()
datamaxima.insert(1, 'Maxima Name', pd.Series(a))
datamaxima.insert(2, "Maxima Price", pd.Series(b))
a=[]
b=[]
IKI()
dataIKI.insert(1, 'IKI Name', pd.Series(a))
dataIKI.insert(2, "IKI Price", pd.Series(b))    # Add Lidl data to the dataframe
dataIKI.insert(3, "IKI Describtion", pd.Series(c))
del datarimi['ID']
datarimi.drop_duplicates(inplace=True)
del dataLIDL['ID'] # Delete initial column
del dataIKI['ID']
del datamaxima['ID']
datamaxima.drop_duplicates(inplace=True)
dataIKI.drop_duplicates(inplace=True)
dataLIDL.drop_duplicates(inplace=True)
#print(dataLIDL)
dataLIDL.to_csv (r'C:\Users\Eduard\Desktop\export_dataframeLIDL.csv') #Save data
dataIKI.to_csv (r'C:\Users\Eduard\Desktop\export_dataframeLIKI.csv')
datamaxima.to_csv(r'C:\Users\Eduard\Desktop\export_dataframemaxima.csv')
datarimi.to_csv(r'C:\Users\Eduard\Desktop\export_dataframerimi.csv')
printresults()
try:
    while True:
        word = input("Name:")
        printresults()
except KeyboardInterrupt:
    pass


