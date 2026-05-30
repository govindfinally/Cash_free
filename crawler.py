import requests


def fetch_website(url):
    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        return response.text

    except Exception as e:
        print(f"Error: {e}")
        return None