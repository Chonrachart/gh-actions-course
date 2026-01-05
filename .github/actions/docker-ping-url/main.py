import os
import requests
from time import sleep

def run():
    website_url = os.getenv("INPUT_URL")
    delay = int(os.getenv("INPUT_DELAY"))
    max_trials = int(os.getenv("INPUT_MAX_TRIALS"))


    website_reachable = ping_url(website_url, delay, max_trials)

    if not website_reachable:
        raise Exception(f"Website {website_url} is unreachable.")
    
    print(f"Website {website_url} is reachable.")


def ping_url(url, delay, max_trails):
    trials = 0

    while trials < max_trails:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Website {url} is reachable.")
                return True
        except requests.ConnectionError:
            print(f"Website {url} is Unreachable. Retrying in {delay} second...")
            time.sleep(delay)
            trials += 1
        except requests.exceptions.MissingSchema:
            print(f"Invalid URL format: {url} Make sure the URL has a valid schema (e.g., http:// or https://)")
            return False
        
    return False

if __name__ == "__main__":
    run()
    
