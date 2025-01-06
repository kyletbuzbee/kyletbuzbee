Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... from bs4 import BeautifulSoup
... import csv
... from datetime import datetime
... 
... # Function to extract job listings from a single page
... def extract_jobs(url):
...     try:
...         response = requests.get(url)
...         response.raise_for_status()  # Raise an exception for HTTP errors
...     except requests.exceptions.RequestException as e:
...         print(f"Error fetching data: {e}")
...         return []
... 
...     soup = BeautifulSoup(response.content, 'html.parser')
...     job_listings = soup.find_all('div', class_='job-listing')
...     return job_listings
... 
... # Function to extract job data from job listings
... def extract_job_data(job_listings):
...     jobs = []
...     for job in job_listings:
...         title = job.find('h2', class_='job-title').text.strip()
...         company = job.find('div', class_='company').text.strip()
...         location = job.find('div', class_='location').text.strip()
...         description = job.find('div', class_='description').text.strip()
...         date = datetime.now().strftime('%Y-%m-%d')
...         jobs.append([title, company, location, description, date])
...     return jobs
... 
... # URL of the FlexJobs job search platform for data analyst jobs
... base_url = 'https://www.flexjobs.com/jobs/data-analyst'
... page_number = 1
... all_jobs = []
... 
... # Loop through pages and extract job listings
... while True:
...     url = f"{base_url}?page={page_number}"
...     print(f"Fetching data from page {page_number}...")
...     job_listings = extract_jobs(url)
...     if not job_listings:
...         break
...     all_jobs.extend(extract_job_data(job_listings))
...     page_number += 1
... 
... # Open a CSV file to save the data
... with open('flexjobs_data_analyst_jobs.csv', mode='w', newline='') as file:
...     writer = csv.writer(file)
...     writer.writerow(['Job Title', 'Company', 'Location', 'Description', 'Date'])
...     writer.writerows(all_jobs)

print("Data extraction complete.")
