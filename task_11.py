# Task 11: Concurrent API Processor
# Objective: Fetch API data concurrently and test reliability.

import requests

from threading import Thread

import unittest

from unittest.mock import patch

import logging

logging.basicConfig(level=logging.INFO)

urls = ["https://dummyjson.com/products", "https://dummyjson.com/users", "https://dummyjson.com/car"]

results = {}

def fetch_url(url):
    try:
        response = requests.get(url, timeout=100)
        response.raise_for_status()
        data = response.json()
        results[url] = data
        logging.info(f"Successfully fetched {url}")
    except requests.exceptions.Timeout:
        results[url] = "Server Timeout"
        logging.error(f"Failed to fetch {url}")
    except requests.exceptions.RequestException as e:
        results[url] = "Error"
        logging.error(f"{url} -> {e}")



threads = []

for url in urls:
    threads.append(Thread(target=fetch_url, args=(url,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for url, data in results.items():
    if isinstance(data, dict):  # isinstance() -- It checks whether an object belongs to a particular type.
        key = url.rstrip("/").split("/")[-1]
        first_10 = data.get(key, [])[:10]
        filtered_data = [dict(list(item.items())[:3]) for item in first_10]
        
        print(f"\n{key}: ")
        print(filtered_data)
    else:
        print(f"\n{data}")


class TestAPI(unittest.TestCase):

    @patch("requests.get")
    def test_success_reponse(self, mock_get):
        
        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {"products": [{"id": 1, "title": "Test"}]}
            
        mock_get.return_value = MockResponse()

        fetch_url("https://dummyjson.com/products")
        self.assertIn("https://dummyjson.com/products", results)
        self.assertIsInstance(results["https://dummyjson.com/products"], dict)

    @patch("requests.get")
    def test_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout

        fetch_url("https://dummyjson.com/products")
        self.assertEqual(results["https://dummyjson.com/products"], "Server Timeout")

    @patch("requests.get")
    def test_error_response(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException


        fetch_url("https://dummyjson.com/products")
        self.assertEqual(results["https://dummyjson.com/products"], "Error")


if __name__ == "__main__":
    unittest.main()


# ==========================================================
# TASK 11 - REVISION NOTES (Concurrent API Processor)
# ==========================================================

# -------------------------------
# 1. Threading Concept
# -------------------------------
# - threading.Thread is used to run multiple API calls concurrently.
# - Each thread executes fetch_url(url) independently.
# - This improves performance when waiting for I/O (API calls).

# IMPORTANT FLOW:
# 1. Create Thread objects
# 2. Start all threads (.start())
# 3. Wait for completion (.join())
# 4. Process shared results dictionary

# -------------------------------
# 2. Shared Data (results dictionary)
# -------------------------------
# - 'results' is a global dictionary shared by all threads.
# - Each thread writes:
#     results[url] = response_data OR error_message
# - Threads do NOT return values directly.

# IMPORTANT:
# - Thread return value is always None
# - We use shared variables to collect results

# -------------------------------
# 3. requests.get() + Error Handling
# -------------------------------
# - requests.get(url, timeout=100) makes API call
# - response.raise_for_status() converts HTTP errors (404, 500) into exceptions

# Exception Handling:
# - Timeout → "Server Timeout"
# - RequestException → "Error"
# - Success → JSON response stored in dictionary

# IMPORTANT INSIGHT:
# HTTP 404/500 DOES NOT automatically throw error unless raise_for_status() is used

# -------------------------------
# 4. Logging
# -------------------------------
# - logging.info() → success messages
# - logging.error() → failure messages
# - Helps track execution in real-time systems

# -------------------------------
# 5. Why Invalid URL ("cart" vs "carts") gave empty result?
# -------------------------------
# - API did NOT throw exception
# - It returned a valid HTTP response (e.g., 404 JSON)
# - So code executed normally
# - But expected key was missing → empty list returned

# FIX:
# - Always use response.raise_for_status() to catch HTTP errors properly

# -------------------------------
# 6. Unit Testing (VERY IMPORTANT CONCEPT)
# -------------------------------

# WHY MOCKING IS USED:
# - We do NOT want real API calls in tests
# - Tests should be fast, reliable, offline

# -------------------------------
# 7. @patch("requests.get")
# -------------------------------
# - Replaces real requests.get with a mock object
# - Allows us to control API behavior

# Two ways to control mock:
# 1. return_value → simulate successful response
# 2. side_effect → simulate errors (Timeout, Exception)

# -------------------------------
# 8. MockResponse Class
# -------------------------------
# - Simulates real Response object
# - Must include:
#     - raise_for_status()
#     - json()
# - Used to mimic API success response

# -------------------------------
# 9. Flow of Test Execution
# -------------------------------
# 1. unittest starts test function
# 2. @patch replaces requests.get with mock
# 3. mock behavior is defined (return_value / side_effect)
# 4. fetch_url() runs
# 5. Instead of real API, mock response is used
# 6. results dictionary is updated
# 7. assertions check correctness

# IMPORTANT:
# - NO recursion happens
# - fetch_url does NOT call test function
# - mock only replaces function behavior

# -------------------------------
# 10. unittest Output Meaning
# -------------------------------
# Ran 3 tests → number of test functions executed
# OK → all tests passed successfully
# . → passed test
# F → failed test
# E → error occurred

# -------------------------------
# 11. Common Mistakes I Made
# -------------------------------
# ❌ Treating Thread list like Thread object (threads.start() wrong)
# ❌ Thinking HTTP 404 triggers exception automatically
# ❌ Confusing tuple from results.items()
# ❌ Thinking mock creates recursion (it does NOT)
# ❌ Testing wrong function instead of real fetch_url()

# -------------------------------
# 12. Key Interview Takeaways
# -------------------------------
# - Threading is used for I/O-bound tasks (API calls, file I/O)
# - requests.get is blocking → threads help concurrency
# - Mocking is used to isolate external dependencies
# - unittest checks behavior, not printed output
# - raise_for_status() is required for HTTP error handling

# -------------------------------
# 13. FINAL FLOW SUMMARY
# -------------------------------
# URLs
#   ↓
# Threads created
#   ↓
# Threads start concurrently
#   ↓
# API call (mocked in tests / real in runtime)
#   ↓
# Response stored in global results dictionary
#   ↓
# Threads joined
#   ↓
# Results processed
#   ↓
# Unit tests validate behavior using mocks

# ==========================================================