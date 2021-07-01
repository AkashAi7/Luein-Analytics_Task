from selenium import webdriver
site=input("Enter the company")


site="https://www.google.com/search?q="+site
driver = webdriver.Chrome()
driver.get(site)
site=driver.find_element_by_xpath('.//cite[@class="iUh30 Zu0yb tjvcx"]').text  #"company_name":
print("Company site is :- " + site)
