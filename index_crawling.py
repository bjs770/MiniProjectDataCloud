import urllib.request
from bs4 import BeautifulSoup
from urllib import parse
from collections import OrderedDict
from datetime import datetime
import pandas as pd

def temp():
	url = "https://finance.naver.com/sise/"
	fp = urllib.request.urlopen(url)
	source = fp.read()
	soup = BeautifulSoup(source, 'html.parser')
	soup = soup.findAll("span",class_="num")

	kospi_value = soup[1].string
	kosdaq_value = soup[2].string
	kospi200_value=soup[3].string

	return kospi_value, kosdaq_value, kospi200_value
