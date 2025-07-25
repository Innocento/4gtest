from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def before_all(context):
    context.browser = None  # Initialized only for UI tests


def before_scenario(context, scenario):
    if "UI" in scenario.feature.name.upper():
        chrome_service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(service=chrome_service, options=options)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
