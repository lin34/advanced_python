from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=3832889551&distance=25&geoId=104043369&keywords=mechatronics%20engineering&origin=JOBS_HOME_SEARCH_CARDS')
# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.text

    with open('website.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
        print("HTML content saved successfully as 'website.html'")

soup = BeautifulSoup(response.text, 'lxml')#tw-link-column-item
jobs = soup.find_all('div')
print(jobs)
print(len(jobs))
job_list = []

# for job in jobs:
#     company_name = job.find('a').text.replace(' ', '').replace('\n','').replace('jobs','')
#     location = job.find('li').text#,class_='job-card-container__metadata-item '
#     job_list.append((company_name, location))
# # todo: extract the job name from the listing
# print(job_list)