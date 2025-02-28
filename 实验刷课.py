

#不是梅贞鑫写的


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ddddocr import DdddOcr

url = 'http://192.168.16.236/'
ID = input('学号（默认账号密码都是学号）')

# 登录函数
def weblogin(name):
    name.get(url)
    account = name.find_element(By.CSS_SELECTOR, '#txtUserAccount')
    password = name.find_element(By.CSS_SELECTOR, '#txtPassword')
    account.send_keys(ID)
    password.send_keys(ID)
    captcha_img = name.find_element(By.CSS_SELECTOR, '#imgIdentifyingCode')  # 替换为实际的 XPath
    captcha_img.screenshot('captcha.png')
    ocr = DdddOcr()
    with open('captcha.png', 'rb') as f1:
        im = f1.read()
        yzm1 = ocr.classification(im)
    vt = name.find_element(By.CSS_SELECTOR, '#txtIdentifyingCode')
    vt.send_keys(yzm1)
    login_click = name.find_element(By.CSS_SELECTOR, '#btnLogin')
    login_click.click()

def browse_and_login(url, browser_type='Edge'):
    if browser_type == 'Edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Currently only Edge is supported.")

    weblogin(driver)

    driver.get(url)
    time.sleep(1)

    return driver

def refresh_all_pages(drivers, interval=30):
    """ Function to refresh all opened pages every `interval` seconds """
    while True:
        for driver in drivers:
            try:
                driver.refresh()
            except Exception as e:
                print('出错了，重启试试')
        time.sleep(interval)

def main():
    urls = [
        'http://192.168.16.236/Information3.aspx?Id=456F3BF92685646B&NewsType=1FD24FF70D06EF7653FA05E04CCA13C17F23A4FB63A4225A',
        'http://192.168.16.236/PracticeInformation2.aspx?QuestionbankcategoryCode=wl',
        'http://192.168.16.236/Video.aspx?Id=C53AEAD0FE0A23D3&NewsType=67EF6B186F9F5F87630A0FC6AA38D44A',
        'http://192.168.16.236/Information2.aspx?Id=B341E122DBFFDBB3',
        'http://192.168.16.236/PracticeInformation.aspx?QuestionbankcategoryCode=wl'
    ]

    drivers = []

    for url in urls:
        driver = browse_and_login(url)
        drivers.append(driver)

    refresh_all_pages(drivers, interval=30)

if __name__ == "__main__":
    main()