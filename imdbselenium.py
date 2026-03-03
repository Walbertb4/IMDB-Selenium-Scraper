from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

class IMDB:
    def __init__(self,mail,password):
        self.browser= webdriver.Chrome()
        self.mail=mail
        self.password=password

    def login(self):
        self.browser.get("https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8iLCJsb2dpbkNvbnRleHQiOiI3ZGRhMjRkYi1mZDQwLTQyNTItYjY3NS0zOTdjMjg2YjRiODEifQ&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=imdb_no_account_creation&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.browser.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys(self.mail)
        self.browser.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys(self.password)
        self.browser.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

    def captcha(self):
        if "/ap/cvf/request" in self.browser.current_url:
            input("Captcha detected, please solve it.\n(Press any key to continue.)")

    def gowatchlist(self):
        self.browser.get("https://www.imdb.com/list/watchlist")

    def watchlist(self):
        page_source_html=self.browser.page_source
        return page_source_html

class SHOW:
    def __init__(self):
        self.list= []

    def loadshow(self):
        page_source_html= imdb.watchlist()
        soup= BeautifulSoup(page_source_html, "html.parser")
        shows= soup.find_all("li", {"class":"ipc-metadata-list-summary-item"})
        for show in shows:
            show_title= show.find("h3", {"class":"ipc-title__text"}).text
            show_rating= show.find("span", {"class":"ipc-rating-star--rating"}).text
            fullyshow= f"{show_title} {show_rating}"
            self.list.append(fullyshow)

    def getshow(self):
        for show in self.list:
            print(show)

mail= "example.gmail.com"
password= "example"

imdb= IMDB(mail,password)
imdb.login()
imdb.captcha()
imdb.gowatchlist()

show=SHOW()
show.loadshow()
show.getshow()
