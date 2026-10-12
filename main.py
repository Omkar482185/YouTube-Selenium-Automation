
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

SEARCH_QUERY = "Python Selenium Tutorial"
WAIT_SECONDS = 20


def main():
    driver = None

    try:
        # Launch Chrome
        driver = webdriver.Chrome()
        driver.maximize_window()

        wait = WebDriverWait(driver, WAIT_SECONDS)

        # Open YouTube
        print("Opening YouTube...")
        driver.get("https://www.youtube.com")

        # Find the search box
        search_box = wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "search_query")
            )
        )

        # Search for a tutorial
        search_box.send_keys(SEARCH_QUERY)
        search_box.send_keys(Keys.ENTER)
        print(f"Searching for: {SEARCH_QUERY}")

        # Wait for the first video result
        first_video = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "video-title")
            )
        )

        first_video.click()
        print("Opened the first video result.")

        # Wait until the video page loads
        wait.until(
            lambda d: "watch" in d.current_url
        )
        print("Video page loaded.")

        # Open Share dialog
        try:
            share_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//button[contains(@aria-label, "Share")]'
                    )
                )
            )

            share_button.click()
            print("Share dialog opened.")

        except TimeoutException:
            print(
                "Share button not found. "
                "YouTube's interface may have changed."
            )

        print("Automation completed.")
        input("Press Enter to close Chrome...")

    except Exception as error:
        print(f"Automation failed: {error}")

    finally:
        if driver is not None:
            driver.quit()
            print("Chrome closed.")


if __name__ == "__main__":
    main()
