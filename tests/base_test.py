import pytest


# BaseTest це клас, який містить методи, які можуть бути використані в інших тестових класах.
# Використовує conftest.py (фікстури pytest "driver_init") для ініціалізації драйвера браузера.
class BaseTest:

    @pytest.fixture(scope='function', autouse=True)
    def display_test_name(self, request):
        print(f'\n-------------Running test: {request.node.name}')
        yield
        print(f'\n-------------Test: {request.node.name} finished')
