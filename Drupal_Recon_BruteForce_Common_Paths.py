import requests
import argparse

# Find Drupal Pages via Numerical Bruteforcing Common Drupal URL Paths

# Drupal Docs: https://www.drupal.org/docs/7/understanding-drupal/url-paths

# Define the common drupal paths to be numerically bruteforced
COMMON_PATHS = [
    "?q=node/$n",
    "node/$n",
    "taxonomy/term/$n",
    "user/$n",
]

# Define the range to be bruteforced - modify this logically
BRUTEFORCE_RANGE = range(1, 101)

def make_request(target_url, path):

    url = f"{target_url}/{path}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"[+] Found: {url}")
    return response

if __name__ == "__main__":
    # Define command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Target URL")
    args = parser.parse_args()

    # Check if target URL is provided
    if not args.target:
        print("[-] Please specify a target URL with the -t option.")
        exit()

    # Make requests for each common path with each number in the range
    for path in COMMON_PATHS:
        for n in BRUTEFORCE_RANGE:
            path_with_number = path.replace("$n", str(n))
            make_request(args.target, path_with_number)
