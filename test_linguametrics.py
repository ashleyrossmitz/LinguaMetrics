import pytest
from linguametrics import prompt_int_in_range, format_seconds

# ---------- prompt_int_in_range ----------
def test_prompt_int_in_range_returns_value_when_input_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "5")
    assert prompt_int_in_range("Enter:", 1, 10) == 5


def test_prompt_int_in_range_reprompts_when_input_out_of_range(monkeypatch):
    answers = iter(["99", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert prompt_int_in_range("Enter:", 1, 10) == 5


def test_prompt_int_in_range_reprompts_when_input_not_integer(monkeypatch):
    answers = iter(["abc", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert prompt_int_in_range("Enter:", 1, 10) == 7


def test_prompt_int_in_range_returns_value_when_input_lower_bound(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "1")
    assert prompt_int_in_range("Enter:", 1, 10) == 1


def test_prompt_int_in_range_returns_value_when_input_upper_bound(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "10")
    assert prompt_int_in_range("Enter:", 1, 10) == 10


def test_prompt_int_in_range_reprompts_until_valid_when_many_errors(monkeypatch):
    answers = iter(["abc", "0", "100", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert prompt_int_in_range("Enter:", 1, 10) == 5
    
# ---------- format_seconds ----------

def test_format_seconds_returns_zero_when_zero():
    assert format_seconds(0) == "0 seconds"
    
def test_format_seconds_returns_zero_when_negative():
    assert format_seconds(-1) == "0 seconds"
    
def test_format_seconds_returns_only_seconds_when_less_than_minute():
    assert format_seconds(59) == "59 seconds"
    
def test_format_seconds_returns_minutes_and_seconds_when_less_than_hour():
    assert format_seconds(3599) == "59 minutes 59 seconds"
    
def test_format_seconds_returns_hours_minutes_seconds_when_more_than_hour():
    assert format_seconds(4000) == "1 hour(s) 6 minutes 40 seconds"
    
def test_format_seconds_includes_fraction_when_microseconds_present():
    assert format_seconds(15.234) == "15.23 seconds"
    
def test_format_seconds_returns_only_hours_when_exact_hour():
    assert format_seconds(3600) == "1 hour(s)"
    
def test_format_seconds_returns_only_minutes_when_exact_minute():
    assert format_seconds(60) == "1 minutes"