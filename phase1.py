import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://cs.brown.edu/courses/csci1380/sandbox/3/index.html"
response = requests.get(url, verify=False)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Locate the container div
container = soup.find("div", {"class": "container-fluid page"})  # Look for the div with the class 'container-fluid page'

# Step 4: Extract headers (adjust the logic based on the actual HTML structure)
# Example: If headers are in <h3>, <span>, or other tags, find them accordingly
headers = [header.text.strip() for header in container.find_all("h3")]  # Adjust the tag as per actual headers

# Step 5: Extract rows of data (find rows inside container)
rows = []
for row in container.find_all("div", {"class": "row"}):  # Adjust this based on actual row structure
    cells = [cell.text.strip() for cell in row.find_all("span")]  # Use the tag that contains the actual data
    if cells:
        rows.append(cells)

# Step 6: Create a DataFrame and save to CSV
df = pd.DataFrame(rows, columns=headers)
df.to_csv("scraped_data.csv", index=False)

print("Data scraped and saved to scraped_data.csv!")
