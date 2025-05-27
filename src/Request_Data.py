import requests

# URL of the CSV file
url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv"

# Send a GET request to the URL
response = requests.get(url)

# Save the content as a local file
with open('data/raw/wetter.csv', 'wb') as f:
    f.write(response.content)

print("File downloaded and saved to data/raw/wetter.csv ✅")
