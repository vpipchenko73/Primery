import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

r = requests.get('http://anekdotov.net/anekdot/today.html')
doc = lxml.html.fromstring(r.content)
name = doc.xpath('/html/body/center/div/div[1]/div[2]/p')
for p in name:
    print(p.text)

def v_date(a):
   for p in a:
      t=p.text
   return t

spisok={}

r = requests.get('https://cbr.ru/currency_base/daily/')
doc = lxml.html.fromstring(r.content)

for i in range(2,36):
   ticer = doc.xpath(f'/html/body/main/div/div/div/div[3]/div/table/tbody/tr[{i}]/td[2]')
   quantity=doc.xpath(f'/html/body/main/div/div/div/div[3]/div/table/tbody/tr[{i}]/td[3]')
   name=doc.xpath(f'/html/body/main/div/div/div/div[3]/div/table/tbody/tr[{i}]/td[4]')
   price_rub=doc.xpath(f'/html/body/main/div/div/div/div[3]/div/table/tbody/tr[{i}]/td[5]')

   print(f"{i-1}   {v_date(ticer)} --- {v_date(quantity)} --- {v_date(name)} --- {v_date(price_rub)}")
   spisok[v_date(name)]=(v_date(ticer),v_date(quantity),v_date(price_rub))

print(spisok)
print(spisok['Белорусский рубль'])
print(spisok['Белорусский рубль'][0])