import pytest
from linguametrics import prompt_int_in_range

# ---------- prompt_int_in_range ----------
def test_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "5")
    assert prompt_int_in_range("Enter:", 1, 10) == 5


def test_out_of_range_then_valid(monkeypatch):
    answers = iter(["99", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert prompt_int_in_range("Enter:", 1, 10) == 5


def test_text_then_valid(monkeypatch):
    answers = iter(["abc", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert prompt_int_in_range("Enter:", 1, 10) == 7


def test_lower_bound(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "1")
    assert prompt_int_in_range("Enter:", 1, 10) == 1


def test_upper_bound(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "10")
    assert prompt_int_in_range("Enter:", 1, 10) == 10


def test_many_errors_then_valid(monkeypatch):
    answers = iter(["abc", "0", "100", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert prompt_int_in_range("Enter:", 1, 10) == 5