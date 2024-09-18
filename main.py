from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.common.exceptions import TimeoutException

output_file = r"C:\Users\owery\OneDrive\Masaüstü\Python\zteH3600\logs.txt"

def write_to_file(time_data, uptime, ram_usage, cpu_usage, wip_data, ssid_data2g, channel_data2g, bandwidth_data2g, ssid_data5g, channel_data5g, bandwidth_data5g, download_data, upload_data):
    with open(output_file, 'a', encoding='utf-8') as file:
        # Format the download_data and upload_data with two decimal places
        download_data_formatted = f"{download_data:.2f}MB" if download_data is not None else "0.00"
        upload_data_formatted = f"{upload_data:.2f}MB" if upload_data is not None else "0.00"
        
        file.write(f"{str(time_data).ljust(26)}|{uptime.ljust(35)}|{ram_usage.ljust(12)}|{cpu_usage.ljust(10)}|"
                   f"{wip_data.ljust(14)}|{ssid_data2g.ljust(24)}|{channel_data2g.ljust(16)}|{bandwidth_data2g.ljust(25)}|"
                   f"{ssid_data5g.ljust(24)}|{channel_data5g.ljust(14)}|{bandwidth_data5g.ljust(17)}|"
                   f"{download_data_formatted.ljust(11)}|{upload_data_formatted.ljust(11)}|\n")



    #----------------------------Interface Giris-----------------------------------#
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
    #----------------------------------------------------------------------------------------#

def ADVANCED_SECTION(driver):
    time.sleep(5)
    advanceButton = driver.find_element(By.ID, "mgrAndDiag")
    advanceButton.click()
    time.sleep(5)

    #--------------------------------Yonetim Sayfasi-----------------------------------------#
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
    #----------------------------------------------------------------------------------------#

def LOCAL_NETWORK(driver):
    localNetworkButton = driver.find_element(By.ID, "localnet")
    localNetworkButton.click()
    time.sleep(5)

    #--------------------------------Yerel Ag Sayfasi-----------------------------------------#
    
    #--------------------------------SSID: 2.4 GHZ Verileri----------------------------------#
        #--------------------------(bant genisligi bu sayfada yok)-------------------------------#
def SSID_DATA1(driver):
    ssid1 = driver.find_element(By.ID, "ESSID:0") 
    ssid_data1 = ssid1.text
    print("SSID Data (2.4 GHz) degeri alindi.")
    return ssid_data1

def CH_DATA1(driver):
    ch1 = driver.find_element(By.ID, "ChannelInUsed_0")
    ch1data = ch1.text
    print("Channel (2.4 GHz) degeri alindi.")
    return ch1data

    #----------------------------------------------------------------------------------------#
    #--------------------------------SSID: 5 GHZ Verileri---------------------------------#
    #--------------------------(bant genisligi bu sayfada yok)-------------------------------#
def SSID_DATA2(driver):
    ssid2 = driver.find_element(By.ID, "ESSID:4") 
    ssid_data2 = ssid2.text
    print("SSID Data (5 GHz) degeri alindi.")
    return ssid_data2

def CH_DATA2(driver):
    ch2 = driver.find_element(By.ID, "ChannelInUsed_1")
    ch2data = ch2.text
    print("Channel (5 GHz) degeri alindi.")
    return ch2data
    #----------------------------------------------------------------------------------------#

def WLAN_CONFIG(driver):
    wlansetsButton = driver.find_element(By.ID, "wlanConfig")
    wlansetsButton.click()
    time.sleep(3)
    extendButton = driver.find_element(By.ID, "WlanBasicAdConfBar")
    extendButton.click()
    time.sleep(3)

def BW_DATA1(driver):
    bw1 = driver.find_element(By.ID, "UI_BandWidth:0")
    bw1data = bw1.get_attribute('value')
    print("Bandwidth (2.4 GHz) degeri alindi.")
    return bw1data

def WLAN_CONFIG_5G(driver):
    time.sleep(3)
    wlansetsButton = driver.find_element(By.ID, "wlanConfig")
    wlansetsButton.click()
    time.sleep(3)
    extendButton = driver.find_element(By.ID, "WlanBasicAdConfBar")
    extendButton.click()
    time.sleep(3)
    
def BW_DATA2(driver):
    bw2 = driver.find_element(By.ID, "UI_BandWidth:1")
    bw2data = bw2.get_attribute('value')
    print("Bandwidth (2.4 GHz) degeri alindi.")
    return bw2data
    
    #-------------------------------------------WAN IP---------------------------------------#

def WAN_IP_SECT(driver):
    wanButton = driver.find_element(By.ID, "internet")
    wanButton.click()
    time.sleep(3)
    advwanButton = driver.find_element(By.ID, "EthStateDevBar")
    advwanButton.click()
    time.sleep(10)

def WIP(driver):
    try:
        # Wait for the WAN IP element to be visible, up to 10 seconds
        wanip = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cIPAddress:2"))
        )
        wipdata = wanip.text
        # Extract the part before the '/' character
        wipdata = wipdata.split('/')[0]
        print("WAN IP:", wipdata)
        return wipdata
    except TimeoutException:
        print("Error: WAN IP element not found.")
        return None


def DL_DATA(driver):
    dldata = driver.find_element(By.ID, "cmaxrate:0")
    download_data = dldata.text
    
    # Extract the part after the '/'
    parts = download_data.split('/')
    download_data_after_slash = parts[1] if len(parts) > 1 else '0'
    
    # Convert the extracted value after '/' to an integer
    try:
        download_data_bytes = int(download_data_after_slash)
    except ValueError:
        print("Error: Download data after '/' is not a valid integer.")
        return None
    
    # Convert bytes to megabytes (1 MB = 1,048,576 bytes)
    download_data_mb = download_data_bytes / 1048576
    
    # Print the result
    print(f"Download Data (after '/'): {download_data_mb:.2f} MB")
    return download_data_mb


def UL_DATA(driver):
    uldata = driver.find_element(By.ID, "csend:0")
    upload_data = uldata.text
    
    # Extract the part after the '/'
    parts = upload_data.split('/')
    upload_data_after_slash = parts[1] if len(parts) > 1 else '0'
    
    # Convert the extracted value after '/' to an integer
    try:
        upload_data_bytes = int(upload_data_after_slash)
    except ValueError:
        print("Error: Upload data after '/' is not a valid integer.")
        return None
    
    # Convert bytes to megabytes (1 MB = 1,048,576 bytes)
    upload_data_mb = upload_data_bytes / 1048576
    
    # Print the result
    print(f"Upload Data (after '/'): {upload_data_mb:.2f} MB")
    return upload_data_mb
    #----------------------------------------------------------------------------------------#
def main():
    driver = webdriver.Chrome(service=Service("C:/Program Files (x86)/chromedriver.exe"))
    OPENINTERFACE(driver)
    LOGINPANEL(driver)
    ADVANCED_SECTION(driver)

    uptime = UPTIME(driver)
    ram_usage = RAM_USAGE(driver)
    cpu_usage = CPU_USAGE(driver)

    LOCAL_NETWORK(driver)
    ssid_data2g = SSID_DATA1(driver)
    channel_data2g = CH_DATA1(driver)
    ssid_data5g = SSID_DATA2(driver)
    channel_data5g = CH_DATA2(driver)

    WLAN_CONFIG(driver)
    bandwidth_data2g = BW_DATA1(driver)

    WLAN_CONFIG_5G(driver)
    bandwidth_data5g = BW_DATA2(driver)

    WAN_IP_SECT(driver)
    wip_data = WIP(driver)

    time_data = datetime.now()
    download_data = DL_DATA(driver)
    upload_data = UL_DATA(driver)

    write_to_file(time_data, uptime, ram_usage, cpu_usage, wip_data, ssid_data2g, channel_data2g, bandwidth_data2g, ssid_data5g, channel_data5g, bandwidth_data5g, download_data, upload_data)
    driver.quit()

if __name__ == "__main__":
    for _ in range(50):
        main()
        time.sleep(2)
