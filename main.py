from adzuna import get_adzuna_jobs
from filters import is_verified
from emailer import send_email

def main():
    print("Script started...")

    jobs = get_adzuna_jobs()
    print(f"Adzuna jobs found: {len(jobs)}")

    verified_jobs = [job for job in jobs if is_verified(job)]
    print(f"Verified jobs after filtering: {len(verified_jobs)}")

    verified_jobs = verified_jobs[:30]

  
    if verified_jobs:
     send_email(verified_jobs)
     print("✅ Email sent successfully")
    
    else:
     send_email([{
        "title": "No verified QA jobs today",
        "company": "System Update",
        "location": "USA",
        "link": "N/A"
    }])
    print("📩 Status email sent (no jobs today)")


if __name__ == "__main__":
    main()

