import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Фікстура (fixture) - це функція, яка викликається перед виконанням тесту.
# Це дозволяє виконати певні дії перед виконанням тесту.
# В даному випадку це ініціалізація драйвера браузера.
# Ця fixture використовується в тестовому класі BaseTest.
# Цей файл обов'язково повинен бути в кореневій папці проекту або в папці tests.
# Ім'я файлу повинно бути conftest.py для того, щоб pytest міг автоматично виконати його.
# Цей файл має бути в одній папці з тестами, якщо він використовується в тестах.
@pytest.fixture()
def driver_init():
    # Створюємо екземпляр браузера Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Максимізуємо вікно браузера
    driver.maximize_window()
    # Налаштування часу очікування пошуку всіх елементів на сторінці в секундах
    driver.implicitly_wait(20)
    # Повертаємо драйвер браузера для використання в тестах
    yield driver
    # Закриваємо вікно браузера після виконання тесту
    driver.quit()

