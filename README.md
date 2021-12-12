# pywttr-models

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/monosans/pywttr-models/blob/main/LICENSE)

[Pydantic](https://github.com/samuelcolvin/pydantic) models for [pywttr](https://github.com/monosans/pywttr) and [aiopywttr](https://github.com/monosans/aiopywttr).

## Usage for type annotation

```python
import pywttr_models


def do_something(model: pywttr_models.en.Model):
    ...
```

Other languages may also be used instead of `en`. For a complete list of supported languages, see the [file names](https://github.com/monosans/pywttr-models/tree/main/pywttr-models) or follow the code completion in your IDE.

## Documentation

There is no documentation, just follow the code completion from your IDE. I'd recommend [Visual Studio Code](https://code.visualstudio.com) (with [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)) or [PyCharm](https://jetbrains.com/pycharm).
