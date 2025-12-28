import requests

APP_ID = "47569c78"
APP_KEY = "ce2b045355381614fca105fd13f3f5c0"

URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"

def get_adzuna_jobs():
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": "entry level qa tester",
        "where": "United States",
        "results_per_page": 30,
        "content-type": "application/json"
    }

    response = requests.get(URL, params=params)
    data = response.json()

    jobs = []
    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "link": job.get("redirect_url")
        })

    return jobs
