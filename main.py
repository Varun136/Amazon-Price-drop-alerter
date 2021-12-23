import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "https://www.amazon.in/SanDisk-Ultra-SDDDC2-064G-G46-Drives-Silver/dp/B01EZ0X3L8/ref=sr_1_1?dchild=1&m=A14CZOWI0VEHLG&pf_rd_i=1375411031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=ca7b2923-7d14-4607-a217-91ea9515173d&pf_rd_r=7KBGE68YVW1AKZCXNTPD&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1632676198&refinements=p_6%3AA14CZOWI0VEHLG&s=electronics&sr=1-1"
response = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
                                     "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ml;q=0.6,hi;q=0."})
site_html=response.text

soup = BeautifulSoup(site_html,"lxml")
price = soup.find_all(name="span",class_="a-size-medium a-color-price priceBlockBuyingPriceString")[0].text.replace("₹","")
final_price = int(price.split(".")[0])



my_mail = "pythonteam99@gmail.com"
password = "python@1234"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail,password=password)
if final_price < 919:
    connection.sendmail(from_addr=my_mail,to_addrs="varunrajeevandevaragam@gmail.com",msg="Subject:PRICE DROPPED\n\n")
connection.close()



