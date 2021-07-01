from selenium import webdriver

site=input("Enter The company URL ")

site="https://www.google.com/search?q="+site
driver = webdriver.Chrome()
driver.get(site)

name=driver.find_element_by_xpath('.//h2[@class="qrShPb kno-ecr-pt PZPZlf mfMhoc"]').text #company name
url=driver.find_element_by_xpath('.//a[@class="B1uW2d ellip PZPZlf"]').get_attribute('href') #company url
about=driver.find_element_by_xpath('//div[@class="PZPZlf hb8SAc"]').find_element_by_xpath('.//div[@class="kno-rdesc"]').get_attribute('innerText') #company description 
founded= driver.find_element_by_xpath('.//span[@class="Eq0J8 LrzXr kno-fv"]').get_attribute('innerText') #company founding year
revenue= driver.find_element_by_xpath('.//div[@class="zloOqf PZPZlf"]').get_attribute('innerText') #revenue info
headquater=driver.find_element_by_xpath('.//span[@class="Eq0J8 LrzXr kno-fv"]').find_element_by_xpath('.//a[@class="fl"]').get_attribute('innerText') #company headquaters
# Subsidiaries=driver.find_element_by_xpath('.//span[@class="Eq0J8 LrzXr kno-fv"]').find_element_by_xpath('.//a[@class="f1"]').get_attribute('innerText')
# founder=driver.find_element_by_xpath('.//div[@class="rVusze"]').find_element_by_xpath('.//div[@class="rVusze"]').get_attribute('innerText')
print("\n input_company_website_url: "+ url,"\n company_name :"+name,"\n  about_company"+about,"\n Founded :"+founded,"\n Revenue :"+revenue,"\n headquaters "+headquater)
 


