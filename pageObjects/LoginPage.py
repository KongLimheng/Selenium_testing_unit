from selenium import webdriver


class Login:
    txtbox_usname_id = 'Email'
    txtbox_pwd_id = 'Password'
    btnLogin_xpath = '//button[@class="button-1 login-button"]'
    link_txt_logout = "Logout"

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')

    def setUserName(self, usname):
        self.driver.find_element_by_id(self.txtbox_usname_id).clear()
        self.driver.find_element_by_id(self.txtbox_usname_id).send_keys(usname)

    def setPassword(self, pwd):
        self.driver.find_element_by_id(self.txtbox_pwd_id).clear()
        self.driver.find_element_by_id(self.txtbox_pwd_id).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.btnLogin_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_txt_logout).click()