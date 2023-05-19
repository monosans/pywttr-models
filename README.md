# pywttr-models

[![CI](https://github.com/monosans/pywttr-models/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/pywttr-models/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/pywttr-models)](https://pepy.tech/project/pywttr-models)

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
