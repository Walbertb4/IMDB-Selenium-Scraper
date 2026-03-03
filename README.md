# IMDb Watchlist Scraper

This **Python** project uses the **Selenium** and **BeautifulSoup** libraries to automatically log into IMDb using user-provided credentials, scrapes the titles and ratings from your **Watchlist**, and prints them to the terminal. It also provides an option for manual intervention in case of Captcha verifications.

---

## Features

* **Automated Login:** Automatically logs into the system using the provided email and password.
* **Captcha Detection:** Detects if a Captcha appears during the login process and:
  * Pauses the operation.
  * Waits for manual resolution by the user.
* **Content Scraping:** Scans the watchlist data to extract the following information:
  * Content Title (Movie/Show Name)
  * IMDb Rating
* **Clean Output:** Displays the extracted data as a neat, formatted list in the console.

---

## Installation and Requirements

To run this project, you must have **Python 3.x** and the **Google Chrome** browser installed on your computer. 

You can install the required libraries (`selenium` and `beautifulsoup4`) by opening a terminal in the project directory and running the following command:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Open the downloaded or cloned project folder and open the Python file using a code editor.
2. Enter your own IMDb login credentials into the `mail` and `password` variables located at the bottom of the code:

```python
mail = "example_mail@gmail.com"
password = "yourpassword123"
```

3. Run the Python file via the terminal:

```bash
python imdb_scraper.py
```
