from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or provide its full path
driver.get("https://results.eci.gov.in/PcResultGenJune2024/index.htm")

# Wait for the page to load and the table to be present
wait = WebDriverWait(driver, 20)
results_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rslt-table table')))

# Extract rows from the table
rows = results_table.find_elements(By.TAG_NAME, 'tr')

# Extract data from rows
data = []
for row in rows[1:-1]:  # Skip header and footer rows
    cols = row.find_elements(By.TAG_NAME, 'td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Close the browser
driver.quit()

# Create a DataFrame
columns = ["Party", "Won", "Leading", "Total"]
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('lok_sabha_election_results_2024.csv', index=False)

print("Data scraped and saved to lok_sabha_election_results_2024.csv")
