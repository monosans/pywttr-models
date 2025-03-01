# Changelog

[Semantic Versioning](https://semver.org)

## [2.0.1] - 2024-12-11

- Fix Language docstring.

## [2.0.0] - 2024-11-29

- Switch to pydantic v2.
- Make models immutable and hashable.

## [1.2.4] - 2024-01-29

- Add `diff_rad` and `short_rad` fields.

## [1.2.3] - 2023-12-09

- Use `str.__str__` and `str.__format__` in Language enum.

## [1.2.2] - 2023-09-04

- Fix Language enum type hints.

## [1.2.1] - 2023-09-04

- Fix Language enum type hints.

## [1.2.0] - 2023-09-04

- Raise the minimum required version of Python from 3.7 to 3.8.
- Add enum of supported languages.
- Add AnyModel type.

## [1.1.1] - 2023-07-06

- Compatibility with pydantic v2 via `pydantic.v1`.

## [1.1.0] - 2022-11-26

- Add support for Galician language.

## [1.0.2] - 2022-08-15

- Use relative imports.

## [1.0.1] - 2022-08-14

- Raise minimum required Python version from 3.7 to 3.7.2.
- Add docstring to `__init__.py`.
- Add `from __future__ import annotations` to all modules.

## [1.0.0] - 2022-06-13

- Remove unsupported languages.

## [0.1.6] - 2022-06-05

- Minor cleanup.

## [0.1.5] - 2022-06-03

- Drop Python 3.6 support.
- Update dependencies.

## [0.1.4] - 2022-01-02

- Revert changes from `v0.1.2` and `v0.1.3`

## [0.1.3] - 2022-01-02

- Fix `ValidationError` that occurred in rare cases

## [0.1.2] - 2022-01-02

- Fix `ValidationError` that occurred in rare cases

## [0.1.1] - 2021-12-12

- Initial release
