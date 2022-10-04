from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('tr', class_="job")
    for job_section in jobs:
      job_posts = job_section.find_all('td', class_="company")
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[0]
        link = anchor['href']
        for title in anchor:
          job_title = title.find_all('h2')
        location, salary = post.find_all('div', class_="location")
        name = post.find_all('h3')
    summary = name[0].text + job_title[0].text + location[0].text + salary[0].text
    print(summary)
  else:
    print("Can't get jobs.")

extract_jobs("rust")