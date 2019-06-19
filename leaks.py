from selenium import webdriver
import time, re

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
        self.browser.get("https://www.avast.com/hackcheck")
    
        email_field = self.browser.find_element_by_tag_name("input")
        email_field.send_keys(email)
        email_field.submit()

        time.sleep(1.5)

        has_leak = self.browser.find_elements_by_tag_name("h2")[0]
        
        # diz se foi ou nao vazado...
        if has_leak.text[0] == "Y":
            p = re.compile(r'(.* )+')
            num_leak = self.browser.find_elements_by_tag_name("h3")[0]
            num_leak = re.search(p, num_leak.text)[0].strip(" ")
            if num_leak == 'one':
                return 1
            else:
                return num_leak
        else:
            return 0
    
    def write_statics(self):
        with open(self.output_file, "w") as f:
            for email in self.emails_list:
                leak = self.get_leaks(email)
                f.write(f'{email} {leak}\n')
