from typing import KeysView
from selenium import webdriver
import time 
import datetime
import math

class nobet:
    def __init__(self):
        self.url="https://www.beo.org.tr/nobetci-eczaneler"
        self.browser=webdriver.Chrome("D:\dev\seleniumdene\driver\chromedriver.exe")
    def nob_ecz_bul(self):
        self.browser.get(self.url)
        an=datetime.datetime.now()
        
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[1]/input").send_keys(str(an.day)+"-"+str(an.month)+"-"+str(an.year))
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[2]/select").send_keys("KESTEL")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[3]/input").click()   
        self.nob_olan_ecz=self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[2]/h4").text
        self.nob_olan_ecz_bilgi=(self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[2]/p")).text.split("\n")
        self.nob_olan_ecz_adres=self.nob_olan_ecz_bilgi[0]
        self.nob_olan_ecz_telefon=self.nob_olan_ecz_bilgi[1]
        self.nob_olan_ecz_nobettarihleri=self.nob_olan_ecz_bilgi[3]
        #self.nob_olan_ecz_googlelink=self.browser.find_element_by_css_selector("body > div.wrapper > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div.col-md-10 > p > a:nth-child(7)").get_attribute('href')
        time.sleep(1)
        self.browser.get("https://www.google.com/maps/dir/40.1984181,29.208069")
        self.browser.maximize_window()

        varis_noktasi=self.browser.find_element_by_class_name('tactile-searchbox-input')
        varis_noktasi.clear()
        varis_noktasi.send_keys(self.nob_olan_ecz_adres+" Kestel/Bursa")

        self.browser.find_element_by_xpath("//*[@id='omnibox-directions']/div/div[3]/div[2]/button/div").click()  
        
        baslangic_noktasi=self.browser.find_element_by_class_name('tactile-searchbox-input')
        baslangic_noktasi.clear()
        baslangic_noktasi.send_keys("Ahmet Vefik Paşa Mahallesi, Bursa Caddesi, No:45/2-A, Kestel/Bursa\n")
      

        self.browser.find_element_by_xpath("//*[@id='pane']/div/div[3]/button").click() # Adres tabını kaybet
        time.sleep(30)
        self.browser.save_screenshot("D:\dev\seleniumdene\googlegunluk.jpeg")

wet=nobet()
wet.nob_ecz_bul()
#wet.google()