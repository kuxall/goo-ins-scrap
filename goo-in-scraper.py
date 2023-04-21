import requests
from bs4 import BeautifulSoup
import csv

keyword = input("Enter a keyword to search on Google: ")
number_of_times = input("Enter the number of results that you need: ")
url = f"https://www.google.com/search?q={keyword}&num={number_of_times}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

results = soup.select(".tF2Cxc")

# Create a CSV file and write the headers
with open(f"{keyword}_results_{number_of_times}.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])

    # Loop through the search results and write each title and link to the CSV file if the link is a legitimate Instagram profile URL
    for result in results:
        title = result.select_one(".DKV0Md").text
        link = result.a["href"]
        if link.startswith("https://www.instagram.com/"):
            writer.writerow([title, link])
            print(title)
            print(link)
