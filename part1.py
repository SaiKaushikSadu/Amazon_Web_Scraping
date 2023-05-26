from bs4 import BeautifulSoup
import csv

# List of HTML files representing different pages
html_files = ['page1.html', 'page2.html','page3.html','page4.html','page5.html','page6.html','page7.html','page8.html','page9.html','page10.html']

# List to store extracted data from all pages
data_list = []

# Iterate over each HTML file
for file_name in html_files:
    # Read the HTML file
    with open(file_name, 'r') as file:
        html_data = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find all div elements with the specified class
    div_list = soup.find_all('div', class_='sg-row')

    # Extract information from each div
    for div in div_list:
        # Extract name
        name_element = div.find('span', class_='a-size-medium a-color-base a-text-normal')
        name_data = name_element.text.strip() if name_element else ''

        # Extract rating
        rating_element = div.find('span', class_='a-icon-alt')
        rating_data = rating_element.text.strip() if rating_element else ''

        # Extract number of reviews
        review_element = div.find('span', class_='a-size-base s-underline-text')
        no_of_review_data = review_element.text.strip() if review_element else ''

        # Extract price
        price_element = div.find('span', class_='a-price-whole')
        price_data = price_element.text.strip() if price_element else ''

        # Extract product link
        link_element = div.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        link_data = "https://www.amazon.in/"+link_element['href'] if link_element else ''

        # Add extracted data to the list
        data_list.append([name_data, rating_data, no_of_review_data, price_data, link_data])

# Write data to a CSV file
with open('data_part1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Rating', 'Number of Reviews', 'Price', 'Link'])
    writer.writerows(data_list)

