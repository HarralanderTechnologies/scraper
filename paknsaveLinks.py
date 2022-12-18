from bs4 import BeautifulSoup
import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get('https://distilnetworks.com')

baseURL = 'https://www.paknsave.co.nz/shop/category/fresh-foods-and-bakery?pg=1',
for url in baseURL:
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find('ul', {'class': 'fs-pagination__items'})
    pageNum = pagination.contents[13]
    pages = (int(pageNum.text)+1)
    pageRange = range(1, pages)
    for eachPage in list(pageRange):
        URLS = ('https://www.paknsave.co.nz/shop/category/fresh-foods-and-bakery?pg='+str(eachPage))
        driver.get(URLS)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        grid = soup.find('section', {'class': 'fs-product-grid'})
        item = grid.find_all('div', {'class': 'fs-product-card'})
        for eachItem in item:
            href = eachItem.find("a").get("href")
            string = "https://www.paknsave.co.nz" + href
            cleanLink = string
            print(cleanLink)
            driver.get(cleanLink)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            title = soup.find('span', {'itemprop': 'offers'})
            price = title.find("meta").get("content")
            name = soup.find('h1', {'class': 'u-color-dark-grey'}).text
            print(price, name)

driver.quit()
