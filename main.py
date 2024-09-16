from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime

output_file = r"C:\Users\owery\OneDrive\Masaüstü\Python\zteH3600\logs.txt"

def write_to_file(data):
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(data)

def OPENINTERFACE(driver):
    driver.get("http://192.168.1.1/")
    time.sleep(2)
    print("Interface opened.")

def LOGINPANEL(driver):
    userName = "admin"
    userPassword = "admin123"
    userNameInput = driver.find_element(By.ID, "Frm_Username")
    userNameInput.send_keys(userName)
    userPasswordInput = driver.find_element(By.ID, "Frm_Password")
    userPasswordInput.send_keys(userPassword)
    loginButton = driver.find_element(By.ID, "LoginId")
    loginButton.click()
    time.sleep(3)
    print("Login successful.")

def ADVANCED_SECTION(driver):
    time.sleep(10)
    advanceButton = driver.find_element(By.ID, "mgrAndDiag")
    advanceButton.click()
    time.sleep(12)

def UPTIME(driver):
    uptimeValue = driver.find_element(By.ID, "cUpTime")
    uptime = uptimeValue.text
    print("UpTime:", uptime)
    return uptime

def RAM_USAGE(driver):
    ramNotUsingValue = driver.find_element(By.ID, "cMemoryUsage")
    ramNotUsing = ramNotUsingValue.text
    print("RamUsage:", ramNotUsing)
    return ramNotUsing

def CPU_USAGE(driver):
    cpuUsing = driver.find_element(By.ID, "cCPUUsage")
    time.sleep(2)
    cpuUsage = cpuUsing.text
    print("CPU Usage:", cpuUsage)
    return cpuUsage

def LOCAL_NETWORK(driver):
    localNetworkButton = driver.find_element(By.ID, "localnet")
    localNetworkButton.click()
    time.sleep(10)

def SSID_DATA1(driver):
    ssid1 = driver.find_element(By.ID, "_InstID:0")
    ssid_data1 = ssid1.text
    print("SSID 1:", ssid_data1)
    return ssid_data1

def CHANNEL_DATA1(driver):
    channel1 = driver.find_element(By.ID, "ChannelInUsed_0")
    channel_data1 = channel1.text
    print("Channel 1:", channel_data1)
    return channel_data1

def DOWNLOAD_DATA1(driver):
    downloadspeed1 = driver.find_element(By.ID, "TotalBytesCount:0")
    download_data1 = downloadspeed1.text
    print("Download 1:", download_data1)
    return download_data1

def SSID_DATA5(driver):
    ssid5 = driver.find_element(By.ID, "_InstID:4")
    ssid_data5 = ssid5.text
    print("SSID 5:", ssid_data5)
    return ssid_data5

def CHANNEL_DATA5(driver):
    channel5 = driver.find_element(By.ID, "ChannelInUsed_1")
    channel_data5 = channel5.text
    print("Channel 5:", channel_data5)
    return channel_data5

def DOWNLOAD_DATA5(driver):
    downloadspeed5 = driver.find_element(By.ID, "TotalBytesCount:4")
    download_data5 = downloadspeed5.text
    print("Download 5:", download_data5)
    return download_data5

def main():
    driver = webdriver.Chrome(service=Service("C:/Program Files (x86)/chromedriver.exe"))
    
    try:
        OPENINTERFACE(driver)
        LOGINPANEL(driver)
        ADVANCED_SECTION(driver)

        uptime = UPTIME(driver)
        ram_usage = RAM_USAGE(driver)
        cpu_usage = CPU_USAGE(driver)
        
        LOCAL_NETWORK(driver)
        
        ssid1 = SSID_DATA1(driver)
        ch1data = CHANNEL_DATA1(driver)
        download1 = DOWNLOAD_DATA1(driver)
        
        ssid5 = SSID_DATA5(driver)
        ch5data = CHANNEL_DATA5(driver)
        download5 = DOWNLOAD_DATA5(driver)

        time_data = datetime.now()
        write_to_file(f"\n{time_data} | {uptime} | {ram_usage} | {cpu_usage} | {ssid1} | {ch1data}  | {ssid5} |{ch5data} | {download5}    | {download1}")
    
    
    finally:
        driver.quit()

if __name__ == "__main__":
    for _ in range(10):
        main()
        time.sleep(10)
