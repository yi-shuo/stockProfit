from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 初始化瀏覽器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打開基金的網頁
url = "https://www.anuefund.com/fund/detail/A05143"
driver.get(url)

# 等待頁面加載完成（這裡可以使用顯式等待來確保內容加載）
driver.implicitly_wait(10)

# 找到包含價格的HTML標籤
price_element = driver.find_element(By.CLASS_NAME, "text-1")

# 提取價格數據
price = price_element.text.strip()

# 將價格數據轉換為一位小數
price_float = float(price)
formatted_price = "{:.1f}".format(price_float)

print(f"基金代碼A05143的收盤價格是: {formatted_price}")

# 關閉瀏覽器
driver.quit()




# url = "https://www.anuefund.com/fund/detail/A05143"