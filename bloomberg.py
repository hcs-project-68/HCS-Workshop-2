#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

# We need these to bypass bloomberg's bot detection. If this does not work, replace with cookies in your browser after visiting bloomberg.com
COOKIE = 'bbAbVisits=; bdfpc=004.1612016200.1603790805880; _gcl_au=1.1.1729062557.1603790806; _sp_krux=false; _sp_v1_uid=1:348:fefcd944-de70-40d9-82af-2679a88756c9; _sp_v1_data=2:232240:1603790805:0:1:0:1:0:0:_:-1; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXQGQlksAJ3zQ2mdAAAA; _sp_v1_opt=1:; _sp_v1_csv=null; _sp_v1_lt=1:; consentUUID=1e4154a2-a724-46d5-9b9b-16870727abd9; _pxvid=88711de7-1836-11eb-ad14-0242ac120009; _pxde=a4c5486f243855788772fb250ae4246484cc18d86f0a1e85e9b3408dff02fbdf:eyJ0aW1lc3RhbXAiOjE2MDM3OTA4MDkyNzEsImZfa2IiOjAsImlwY19pZCI6W119; ccpaUUID=047e3427-20b7-4bf2-87f4-9dde0bc3a022; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; bbgconsentstring=req1fun1pad1; _uetsid=885760e0183611eb9ae56f99ac915ba7; _uetvid=885792e0183611eb8d21490a032b5576; _rdt_uuid=1603790807216.25827cf6-e78e-414e-b8b1-f653c18b1c3e; _reg-csrf=s%3AWH2_m_fw5lhU_UOthJi_x8ew.GjHJFWD8NTpfASanCXLSrYX%2BMF2a1V2OraNI7Hje2X4; _reg-csrf-token=OslbH3V8-iBopNM-DfmKt3mXHdTyzu2ytmr4; agent_id=f3f09f4f-5c45-4c4a-8dd0-f8f6ca68eae2; session_id=0a3c461a-0892-484d-8185-696fc9bbbb88; session_key=3354c0261ffd674b76fc7dfd35614d23acb90ac6; _user-status=anonymous; _scid=56da1c41-7bf4-438a-9982-f3229b2a1744; _px2=eyJ1IjoiODg1ZDc5NjAtMTgzNi0xMWViLTkwY2EtOGI0NTk4ZTQ4NzA2IiwidiI6Ijg4NzExZGU3LTE4MzYtMTFlYi1hZDE0LTAyNDJhYzEyMDAwOSIsInQiOjE2MDM3OTExMDc2NTYsImgiOiI1ZGM5NGIxNmQ0NTU4ZTQ2NWFjYmQ4YTFlM2U4ZmZkMmIwNGI4YmM0ODNhMjA2YmY5YjExMmU5MGI0ZjEwOWQ5In0=; _px3=08f0bd0ed3a88ad71e1bd4ea03ac070c3bee7f4683e8f5a20d6b66d3548d2f4d:AQ+mS8fXn5WUr1H0qkmjYuxzdYBlYKNDywL5GA4V/7aCkfT47P9GtQXxIob+8txbWaftWTLDHu8UnatHSe5vpA==:1000:It5D09eQoM4CWJRGFTaVxNgDv0I6+uh7iMF4kscy1qZe2H42wlT4q9FezaGT/OpiLcEUS3+AiC8WE0evvFJuavvQ4lGKlwRVDF8aYoWAW41vxuTVC9IAJCvocZtwG3MaFv5VtG00XU6+3yqtG/UlKoITNY8ec51OP3HSmflwVV4='

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'

def get_quote(sym):
    r = requests.get('https://www.bloomberg.com/quote/' + sym, headers = {'Cookie': COOKIE, 'User-Agent': USER_AGENT})
    data = BeautifulSoup(r.text, 'html.parser')

    def f(c):
        return data.find('span', class_=re.compile(c)).string

    return (f('priceText'), f('changeAbsolute'), f('changePercent'))

def print_quote(sym):
    quote = get_quote(sym)
    print("{} - {} ({}, {})".format(sym, *quote))

print_quote('INDU:IND')
print_quote('SPX:IND')
