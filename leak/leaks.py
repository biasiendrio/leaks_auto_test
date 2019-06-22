from selenium import webdriver
import time, re, sys
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

class Leaks:
    def __init__(self, input_file, output_file):
        self.browser = webdriver.Chrome("web_drivers/chromedriver")
        self.emails_list = self.get_emails(input_file)
        self.output_file = output_file

    def run(self):
        self.write_statics()

    def get_emails(self, input_file):
        emails = []
        with open(input_file, "r") as f:
            for email in f.readlines():
                emails.append(email.strip("\n"))
        return emails

    def get_leaks(self, email):
        while True:
            self.browser.get("https://www.avast.com/hackcheck/friends-check")
    
            email_field = self.browser.find_element_by_tag_name("input")
            email_field.send_keys(email)
            email_field.submit()

            time.sleep(1.5)
            try:
                has_leak = self.browser.find_elements_by_tag_name("h2")[0]
                if has_leak.text[0] != "W":
                    page = self.browser.find_element_by_css_selector("a.link-to-detail")
                    self.browser.get(page.text)
                    time.sleep(1.5)
                    
                    p = re.compile(r'(.* )+')
                    num_leak = self.browser.find_elements_by_tag_name("h3")[0]
                    num_leak = re.search(p, num_leak.text)[0].strip(" ")
                    if num_leak == 'one':
                        return 1
                    else:
                        return num_leak
                else:
                    return 0
            except:
                continue
    
    def write_statics(self):
        erro = []
        with open(self.output_file, "w") as f:
            for i, email in zip(tqdm(range(len(self.emails_list))), self.emails_list):
                leak = self.get_leaks(email)
                if leak != None:
                    f.write(f'{email} {leak}\n')
                else:
                    erro.append(f'{email}')

        if erro != []: 
            with open("erro.txt", "a") as e:
                for i in erro:
                    e.write(f'{i}\n')

        self.browser.quit()

