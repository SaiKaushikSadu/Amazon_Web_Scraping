import csv
import requests
from bs4 import BeautifulSoup

column_data = []
data_list=[]

# Fetch additional information from product URL
headers={
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'
}

# Open the CSV file
with open('data_part1.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    # Read each row and append the desired column value to the list
    for row in reader:
        column_data.append(row[4])  # Replace column_index with the desired column index (0-based)

# Print the column data
for url in column_data:
    response = requests.get(url,headers=headers)
    product_soup = BeautifulSoup(response.text, 'html.parser')

    # Extract description
    desc_element = product_soup.find('div', class_='a-section a-spacing-small')
    desc_data = desc_element.text.strip() if desc_element else ''

    # Extract ASIN
    sample=""
    ans=""
    sample+=url
    for i in range(0,len(sample)):
        if (sample[i]=='/' and sample[i+1]=='d' and sample[i+2]=='p' and sample[i+3]=='/'):
            for j in range(i+4,i+14):
                ans+=sample[j]
    asin_data=ans

    # Extract product description
    product_desc_element = product_soup.find('div', class_='a-section a-spacing-small')
    product_desc_data = product_desc_element.text.strip() if product_desc_element else ''

    # Extract manufacturer
    manufacturer_element = product_soup.find('a', class_='a-link-normal')
    manufacturer_data = manufacturer_element.text.strip() if manufacturer_element else ''

    # Add extracted data to the list
    data_list.append([url,desc_data,asin_data,product_desc_data,manufacturer_data])

    # Write data to a CSV file
    with open('data_part2.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Link', 'Description', 'ASIN', 'Product Description', 'Manufacturer'])
        writer.writerows(data_list)

