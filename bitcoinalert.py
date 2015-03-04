#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
bitcointalert: bitcoinalert is sending an email if the bitcoin price limit is less than x.xx euro.
@author: Robert Tulke, rt@debian.sh
@copyright: GPLv2
@date: 2015-03-04
"""

import urllib2
import json
import smtplib

limit = 200.00     # euro

def send_email(rcptto, subject, data):
    username = 'xx@gmail.com'
    password = 'FooBar99'
    mailfrom = 'xx@gmail.com'

    # Draft the message
    headers = "\r\n".join(["from: " + username,
                           "subject: " + subject,
                           "to: " + rcptto,
                           "mime-version: 1.0",
                           "content-type: text/html"])

    content = headers + '\r\n\r\n' + data

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(mailfrom, rcptto, content)
    server.quit()


response = urllib2.urlopen('https://coinbase.com/api/v1/currencies/exchange_rates')
values = response.read()
dictionary = json.loads(values)
btc = dictionary['btc_to_eur']

fbtc= float(btc)
flimit = float(limit)

if fbtc < flimit :
        #print 'EUR to BTC: ' + dictionary['eur_to_btc']
        #print 'BTC to EUR: ' + dictionary['btc_to_eur']
        data = 'Current price:<br><br>BTC to EUR: ' + dictionary['btc_to_eur'] + '<br>EUR to BTC: ' + dictionary['eur_to_btc']
        send_email('xx@gmail.com', 'Bitcoin alert', data)
