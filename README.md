# pywttr-models

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/pywttr-models/main.svg)](https://results.pre-commit.ci/latest/github/monosans/pywttr-models/main)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pywttr-models?logo=pypi)](https://pypi.org/project/pywttr-models/)

[Pydantic](https://github.com/pydantic/pydantic) models for [pywttr](https://github.com/monosans/pywttr) and [aiopywttr](https://github.com/monosans/aiopywttr).

## Usage for type annotation

```python
import pywttr_models


def do_something(model: pywttr_models.en.Model):
    ...
```

Other languages may also be used instead of `en`. For a complete list of supported languages, follow the code completion in your IDE.

## License

[MIT](https://github.com/monosans/pywttr-models/blob/main/LICENSE)
