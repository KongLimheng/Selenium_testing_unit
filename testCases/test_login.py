import time
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********************** Test Login **********************")
        self.logger.info("********************** Verifying Home Page Title **********************")
        self.driver = setup
        self.logger.info("**** Opening URL ****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********************** Home page title passed **********************")
        else:
            self.logger.error("********************** Home page title failed **********************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("********************** Verifying Login test **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        login = Login(self.driver)
        login.setUserName(self.username)
        time.sleep(2)
        login.setPassword(self.password)
        time.sleep(2)
        login.clickLogin()
        time.sleep(2)
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info("********************** Login test is passed **********************")
            self.driver.close()
            assert True
        else:
            self.logger.error("********************** Login test is failed **********************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
