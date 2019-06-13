from selenium import webdriver

username = input('Enter your email/ username: ')
password = input('Enter your password: ')

url = 'https://www.facebook.com'

driver = webdriver.Chrome('/Users/collins/Desktop/python_projects/auto_login/chromedriver')

driver.get(url)

def logintourl():
    print('This is just a simple program!')
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()

if __name__ == '__main__':
    logintourl()
