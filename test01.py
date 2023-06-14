from selenium.webdriver import Chrome

# Adiciona o item
browser = Chrome()
browser.get("https://generic-shop.vercel.app/product/prod_NmSbgfp6OED8Op")
button_xpath = "/html/body/main/section/div[1]/div[2]/div[1]/button"

add_cart = browser.find_element("xpath", button_xpath)
add_cart.click()


# Altera a quantidade de itens
browser.get("https://generic-shop.vercel.app/cart") # revalida o DOM

incres_button_xpath = "/html/body/main/ul/div/div[2]/div/div/button[1]"
decres_button_xpath = "/html/body/main/ul/div/div[2]/div/div/button[2]"

incres_button = browser.find_element("xpath", incres_button_xpath)
decres_button = browser.find_element("xpath", decres_button_xpath)

incres_button.click()
incres_button.click()
incres_button.click()

decres_button.click()
decres_button.click()
