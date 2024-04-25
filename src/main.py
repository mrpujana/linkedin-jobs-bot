from scrape_linkedin import LinkedInScraper
import streamlit as st

post=st.text_input('Job Title').replace(' ','-')
location=st.text_input('Job location').replace(' ','-')
url=f"https://www.linkedin.com/jobs/search?keywords={post}&location={location}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
if post !='' and location!='':
    st.write(f"Getting results for {post.upper()} in {location.upper()}")

scraper=LinkedInScraper(url)
scraper.scrape_jobs(url)
jobs_detail = scraper.get_jobs_detail()

# jobs_detail = linkedin_scraper(url)
st.write(jobs_detail)