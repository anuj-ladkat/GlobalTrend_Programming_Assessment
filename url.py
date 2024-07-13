import requests
from time import sleep

def download_content(urls, max_retries=3, backoff_factor=0.3):
    """
    Attempts to download content from a list of URLs with retries on error.

    :param urls: List of URLs to download content from.
    :param max_retries: Maximum number of retry attempts on error.
    :param backoff_factor: Factor by which to increase delay between retries.
    :return: Dictionary with URLs as keys and their content or error messages as values.
    """
    results = {}

    for url in urls:
        attempt = 0
        while attempt < max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()
                results[url] = response.text
                break  # Exit the retry loop if the request is successful
            except requests.exceptions.HTTPError as http_err:
                results[url] = f"HTTP error occurred: {http_err}"
                break  # Exit the retry loop on HTTP errors
            except requests.exceptions.ConnectionError as conn_err:
                results[url] = f"Connection error occurred: {conn_err}"
            except requests.exceptions.Timeout as timeout_err:
                results[url] = f"Timeout error occurred: {timeout_err}"
            except requests.exceptions.RequestException as req_err:
                results[url] = f"Request error occurred: {req_err}"
            except Exception as e:
                results[url] = f"An unexpected error occurred: {e}"
                break  # Exit the retry loop on unexpected errors
            attempt += 1
            sleep(backoff_factor * (2 ** attempt))  # Exponential backoff

        if attempt == max_retries:
            results[url] = f"Failed to retrieve content after {max_retries} attempts"

    return results

# Example usage
if __name__ == "__main__":
    urls = [
        "https://in.pinterest.com/",
        "https://https://www.reddit.com/",
        "https://www.wikipedia.org/"
    ]
    results = download_content(urls)
    for url, content in results.items():
        print(f"URL: {url}\nContent: {content}\n")
