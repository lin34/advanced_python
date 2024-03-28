from bs4 import BeautifulSoup
import requests
import time

response = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=3832889551&distance=25&geoId=104043369&keywords=mechatronics%20engineering&origin=JOBS_HOME_SEARCH_CARDS')
# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.text

    with open('website.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
        print("HTML content saved successfully as 'website.html'")
def find_jobs():
    soup = BeautifulSoup(response.text, 'lxml')#tw-link-column-item
    jobs = soup.find_all('li', class_='job-desc')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamilliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f'More Info: {more_info}\n')
                print(f'file saved {index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)