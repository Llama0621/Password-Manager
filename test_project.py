import pytest
from project import generate_password, load_passwords, save_passwords
import csv

def test_generate_password_length():
    assert len(generate_password()) == 12
    assert len(generate_password(8)) == 8
    assert len(generate_password(15)) == 15

def test_generate_password_chars():
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    password = generate_password()
    for char in password:
        assert char in allowed_chars

def test_load_passwords(tmp_path):
    test_file = tmp_path / "test.csv"
    with open(test_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["example", "password"])
        writer.writerow(["test", "1234"])
    assert load_passwords(test_file) == {"example": "password", "test": "1234"}

def test_save_passwords(tmp_path):
    test_file = tmp_path / "test.csv"
    passwords = {"site": "pass", "another": "word"}
    save_passwords(passwords, test_file)
    with open(test_file, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
    assert rows == [["site", "pass"], ["another", "word"]]

def test_load_passwords_empty(tmp_path):
    test_file = tmp_path / "empty.csv"
    assert load_passwords(test_file) == {}
