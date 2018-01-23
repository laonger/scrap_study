#!/usr/bin/python
# encoding: utf-8


from selenium import webdriver

url = "https://www.portalinmobiliario.com/venta/departamento/centro-historico-de-santiago-santiago-santiago-metropolitana?tp=2&;op=1&ca=3&ts=1&dd=2&dh=4&bd=1&bh=3&or=&mn=2&sf=1&sp=1&pd=2.500&sd=60,00&sh=100,00"
browser = webdriver.PhantomJS()
browser.get(url)

info_block = browser.find_element_by_xpath('//div[@class="col-sm-6"]')

print info_block

