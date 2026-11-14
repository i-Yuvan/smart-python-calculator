
import pytest

from project import (
    calculate,
    square_root,
    calculate_percentage,
    calculate_average,
    save_history,
    clear_history
)


def test_calculate():
    assert calculate(10, "+", 5) == 15
    assert calculate(10, "-", 5) == 5
    assert calculate(10, "*", 5) == 50
    assert calculate(10, "/", 5) == 2
    assert calculate(2, "**", 3) == 8
    assert calculate(10, "%", 3) == 1


def test_calculate_errors():
    with pytest.raises(ValueError):
        calculate(10, "/", 0)

    with pytest.raises(ValueError):
        calculate(10, "%", 0)

    with pytest.raises(ValueError):
        calculate(10, "invalid", 5)


def test_square_root():
    assert square_root(25) == 5
    assert square_root(0) == 0
    assert square_root(9) == 3


def test_square_root_error():
    with pytest.raises(ValueError):
        square_root(-25)


def test_calculate_percentage():
    assert calculate_percentage(200, 10) == 20
    assert calculate_percentage(100, 50) == 50
    assert calculate_percentage(500, 20) == 100


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([5, 5, 5]) == 5
    assert calculate_average([10, 20]) == 15


def test_calculate_average_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_save_history(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    save_history("10 + 5 = 15")

    history_file = tmp_path / "history.txt"

    assert history_file.read_text() == "10 + 5 = 15\n"


def test_clear_history(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    save_history("10 + 5 = 15")
    clear_history()

    history_file = tmp_path / "history.txt"

    assert history_file.read_text() == ""