VERIFIED_DOMAINS = [
    "greenhouse.io",
    "lever.co",
    "workday.com",
    "icims.com"
]

BLACKLIST_COMPANIES = [
    "tek", "solutions", "consult", "staffing", "services"
]

def is_verified(job):
    link = job["link"].lower()
    company = job["company"].lower()

    if not any(domain in link for domain in VERIFIED_DOMAINS):
        return False

    if any(word in company for word in BLACKLIST_COMPANIES):
        return False

    return True
