# weather_yd2926

[![ci](https://github.com/QMSS-G5072-2026/weather_ding_yulei/actions/workflows/ci.yml/badge.svg)](https://github.com/QMSS-G5072-2026/weather_ding_yulei/actions/workflows/ci.yml)

Weather station utilities for QMSS G5072

## Installation

```bash
$ uv add weather_yd2926
```

or, without uv, `pip install weather_yd2926`.

## Development

```bash
$ uv sync                       # create .venv and install the package with its dev and docs groups
$ uv run pytest                 # run the tests
$ uv run make html -C docs      # build the documentation
$ uv build                      # build the sdist and wheel into dist/
```

## Usage

```python
import pandas as pd
import weather_yd2926

weather_yd2926.celsius_to_fahrenheit(100)  # 212.0
weather_yd2926.summarize_temperatures([10.0, float("nan"), 20.0])

raw = pd.DataFrame({"station": ["JFK"], "date": ["2026-07-01"], "temp_c": [30.0]})
weather_yd2926.clean_readings(raw)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`weather_yd2926` was created by Yulei Ding. It is licensed under the terms of the MIT license.

## Credits

`weather_yd2926` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `qmss-pkgs-cookiecutter` [template](https://github.com/QMSS-G5072-2026/qmss-pkgs-cookiecutter), a uv-based fork of [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter).
