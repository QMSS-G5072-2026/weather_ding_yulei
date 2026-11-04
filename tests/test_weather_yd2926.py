"""Tests for the weather_yd2926 package (copied from HW6 and adapted)."""

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

import weather_yd2926
from weather_yd2926 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)


def test_version_is_defined():
    assert isinstance(weather_yd2926.__version__, str)


# =============================================================================
# UNIT TESTS
# =============================================================================


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6),
        (-273.15, -459.67),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    """Check valid Celsius values are converted correctly."""
    result = celsius_to_fahrenheit(celsius)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    "bad_input, expected_error",
    [
        ("37", TypeError),
        (None, TypeError),
        (-273.16, ValueError),
        ([37], TypeError),
    ],
)
def test_celsius_to_fahrenheit_invalid(bad_input, expected_error):
    """Check invalid inputs raise the expected exception."""
    with pytest.raises(expected_error):
        celsius_to_fahrenheit(bad_input)


def test_summarize_temperatures():
    """Check summary statistics while ignoring one missing value."""

    # Arrange
    temperatures = [10.0, float("nan"), 20.0]

    # Act
    result = summarize_temperatures(temperatures)

    # Assert
    assert result["mean"] == pytest.approx(15.0)
    assert result["min"] == pytest.approx(10.0)
    assert result["max"] == pytest.approx(20.0)
    assert result["n_missing"] == 1


# =============================================================================
# FIXTURES
# =============================================================================


@pytest.fixture
def raw_readings():
    """Return the raw weather station readings used across tests."""
    return pd.DataFrame({
        "station": ["JFK", "CPK", "JFK", "CPK", "LGA"],
        "date": ["2026-07-02", "2026-07-01", "2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [30.0, 25.0, float("nan"), 999.0, 28.0],
    })


def test_raw_readings_fixture(raw_readings):
    """Check the fixture has the expected structure and missing value."""
    assert list(raw_readings.columns) == ["station", "date", "temp_c"]
    assert len(raw_readings) == 5
    assert raw_readings["temp_c"].isna().sum() == 1


# =============================================================================
# TESTING DATAFRAMES
# =============================================================================


def test_clean_readings(raw_readings):
    """Check that readings are cleaned, sorted, and converted correctly."""

    expected = pd.DataFrame({
        "station": ["CPK", "JFK", "LGA"],
        "date": ["2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [25.0, 30.0, 28.0],
        "temp_f": [77.0, 86.0, 82.4],
    })

    result = clean_readings(raw_readings)

    assert_frame_equal(result, expected)
