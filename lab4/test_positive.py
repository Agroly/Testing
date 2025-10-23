# test_positive.py
import pytest
from order_page import OrderPage

def test_positive(driver):
    page = OrderPage(driver)
    page.visit("file:///C:/Users/slezi/OneDrive/Документы/Учеба/Тестирование/PythonProjects/lab4/test_form.html")  # путь к форме

    # Валидные данные
    page.fill_form(["1", "2", "3", "4", "5"])
    page.submit_form()

    assert "Спасибо! Форма отправлена." in page.get_success_message()
