import re
from bs4 import BeautifulSoup


def extract_signals(html):

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(separator=" ", strip=True)
    title = soup.title.string.strip() if soup.title else "Unknown"

    # Emails
    emails = list(set(
        re.findall(
            r'[\w\.-]+@[\w\.-]+\.\w+',
            text
        )
    ))

    # Phones (basic version)
    phones = list(set(
        re.findall(
            r'\+?\d[\d\s\-]{8,15}\d',
            text
        )
    ))

    # All links
    links = []

    for a in soup.find_all("a", href=True):
        links.append(a["href"])

    # Social links
    social_links = []

    social_domains = [
        "linkedin.com",
        "facebook.com",
        "instagram.com",
        "twitter.com",
        "x.com","github.com","youtube.com","tiktok.com","YCombinator.com"
    ]

    for link in links:
        for domain in social_domains:
            if domain in link:
                social_links.append(link)

    # Privacy Policy
    privacy_policy = (
        "privacy policy" in text.lower()
    )

    # Terms
    terms_conditions = (
        "terms" in text.lower()
        or
        "terms and conditions" in text.lower()
    )

    return {
        "emails": emails,
        "phones": phones,
        "social_links": social_links,
        "privacy_policy": privacy_policy,
        "terms_conditions": terms_conditions,
        "text_content": text,
        "company_name": title
    }