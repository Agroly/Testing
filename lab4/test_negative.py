# test_negative.py
import pytest
from order_page import OrderPage

def test_negative(driver):
    page = OrderPage(driver)
    page.visit("file:///C:/Users/slezi/OneDrive/Документы/Учеба/Тестирование/PythonProjects/lab4/test_form.html")  # путь к форме

    # Одно поле пустое
    page.fill_form(["", "2", "3", "4", "5"])
    page.submit_form()

    assert "Спасибо! Форма отправлена." in page.get_success_message()
