from selenium import webdriver
import tldextract

site=input("Enter The company URL ")
print(site)
site1 = tldextract.extract(site)

print(site1.domain)
site1="https://www.google.com/search?q="+site1.domain
driver = webdriver.Chrome()
driver.get(site1)
try:
    name=driver.find_element_by_xpath('.//h2[@class="qrShPb kno-ecr-pt PZPZlf mfMhoc"]').text #company name
except:
    name="None"
try:
    url=driver.find_element_by_xpath('.//a[@class="B1uW2d ellip PZPZlf"]').get_attribute('href') #company url
except:
    url="None"
try:   
    about=driver.find_element_by_xpath('//div[@class="PZPZlf hb8SAc"]').find_element_by_xpath('.//div[@class="kno-rdesc"]').get_attribute('innerText') #company description 
except:
    about="None"
try:   
    founded= driver.find_element_by_xpath('.//span[@class="Eq0J8 LrzXr kno-fv"]').get_attribute('innerText') #company founding year
except:
    founded="None"
try:  
    revenue= driver.find_element_by_xpath('.//div[@class="zloOqf PZPZlf"]').get_attribute('innerText') #revenue info
except:
    revenue="None"
try:  
    headquater=driver.find_element_by_xpath('.//span[@class="Eq0J8 LrzXr kno-fv"]').find_element_by_xpath('.//a[@class="fl"]').get_attribute('innerText') #company headquaters
except:
    headquater="None"
try:
    sub=driver.find_element_by_xpath('.//div[@data-ved="2ahUKEwj6wMGcocbxAhWR_XMBHc2TDhAQkCkwJHoECDAQAA"]').get_attribute('innerText')
except:
    sub="None"
try:
    founder=driver.find_element_by_xpath('.//div[@data-attrid="kc:/business/business_operation:founder"]').find_element_by_xpath('.//div[@class="rVusze"]').get_attribute('innerText')
except:
    founder="None"
print("\n input_company_website_url: "+ url,"\n company_name :"+name,"\n  about_company"+about,"\n Founded :"+founded,"\n Revenue :"+revenue,"\n headquaters "+headquater,"\n Subsidiaries "+sub,"\n Founders "+founder)

    # print("\n input_company_website_url: "+ url,"\n  about_company"+about,"\n Founded :"+founded,"\n Revenue :"+revenue,"\n headquaters "+headquater)



 