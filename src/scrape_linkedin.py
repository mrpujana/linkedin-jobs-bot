import requests
from bs4 import BeautifulSoup

class LinkedInScraper:
    def __init__(self,url):
        self.jobs_detail = []
        self.url=url

    def scrape_jobs(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
        
        for job in jobs:
            job_title = job.find('h3', class_='base-search-card__title').text.strip()
            job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
            job_location = job.find('span', class_='job-search-card__location').text.strip()
            job_link = job.find('a', class_='base-card__full-link')['href']
            
            self.jobs_detail.append({
                "Title": job_title,
                "Company": job_company,
                "Location": job_location,
                "Link": job_link
            })

    def get_jobs_detail(self):
        return self.jobs_detail