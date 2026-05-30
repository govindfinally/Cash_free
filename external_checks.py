import whois
from urllib.parse import urlparse
from datetime import datetime, timezone
import requests

def get_domain_info(url):

    try:

        domain = urlparse(url).netloc

        domain_info = whois.whois(domain)

        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        registrar = domain_info.registrar

        age_days = None

        if creation_date:

            if creation_date.tzinfo is None:
                creation_date = creation_date.replace(
                    tzinfo=timezone.utc
                )

            age_days = (
                datetime.now(timezone.utc)
                - creation_date
            ).days

        return {
            "domain": domain,
            "registrar": registrar,
            "domain_age_days": age_days
        }

    except Exception as e:

        return {
            "error": str(e)
        }
    def search_company(company_name):

        query = f"{company_name} scam"

        return {
            "search_query": query,
            "scam_mentions": 0
        }