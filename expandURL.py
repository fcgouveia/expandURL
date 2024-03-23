import csv
import requests

# Function to expand a shortened URL
# based on example codes found on StackOverflow
def expand_url(short_url):
    try:
        response = requests.head(short_url, allow_redirects=True)
        #response.encoding = response.apparent_encoding  # Explicitly set the encoding
        return response.url
    except requests.exceptions.RequestException:
        return "Failed to expand"
        
# Input and output file paths
input_file = 'shortened_urls.csv'
output_file = 'expanded_urls.csv'

# Read the list of shortened URLs from the input CSV file
shortened_urls = []
with open(input_file, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if row:
            short_url = row[0]
            expanded_url = expand_url(short_url)
            shortened_urls.append([short_url, expanded_url])
            print(row)
# Write the expanded URLs to the output CSV file
with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in shortened_urls:
        csv_writer.writerow(row)
        print(row)

print(f"Expanded URLs saved to '{output_file}'")

