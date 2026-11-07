"""Response models for pywttr and aiopywttr.

The response type depends on the language: `Language.RU` gives `ru.Model`,
and so on. Each language module adds the weather description in that
language, e.g. `lang_ru`, to `CurrentConditionItem` and `HourlyItem`.
Everything else is in `base`.
"""

from __future__ import annotations

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pywttr_models import (
        af,
        am,
        ar,
        az,
        ba,
        base,
        be,
        bg,
        bn,
        bs,
        by,
        ca,
        crk,
        cs,
        cy,
        da,
        de,
        el,
        en,
        eo,
        es,
        et,
        eu,
        fa,
        fi,
        fr,
        fy,
        ga,
        gl,
        he,
        hi,
        hr,
        hu,
        hy,
        ia,
        id,  # noqa: A004
        is_,
        it,
        ja,
        jv,
        ka,
        kk,
        ko,
        ky,
        lt,
        lv,
        mg,
        mk,
        ml,
        mr,
        nb,
        nl,
        nn,
        oc,
        pa,
        pl,
        pt,
        pt_br,
        ro,
        ru,
        sk,
        sl,
        sr,
        sr_lat,
        sv,
        sw,
        ta,
        te,
        th,
        tr,
        ts,
        uk,
        vi,
        zh,
        zh_cn,
        zh_tw,
        zu,
    )
    from pywttr_models._language import AnyModel

__version__ = "2.1.0"
__all__ = (
    "AnyModel",
    "af",
    "am",
    "ar",
    "az",
    "ba",
    "base",
    "be",
    "bg",
    "bn",
    "bs",
    "by",
    "ca",
    "crk",
    "cs",
    "cy",
    "da",
    "de",
    "el",
    "en",
    "eo",
    "es",
    "et",
    "eu",
    "fa",
    "fi",
    "fr",
    "fy",
    "ga",
    "gl",
    "he",
    "hi",
    "hr",
    "hu",
    "hy",
    "ia",
    "id",
    "is_",
    "it",
    "ja",
    "jv",
    "ka",
    "kk",
    "ko",
    "ky",
    "lt",
    "lv",
    "mg",
    "mk",
    "ml",
    "mr",
    "nb",
    "nl",
    "nn",
    "oc",
    "pa",
    "pl",
    "pt",
    "pt_br",
    "ro",
    "ru",
    "sk",
    "sl",
    "sr",
    "sr_lat",
    "sv",
    "sw",
    "ta",
    "te",
    "th",
    "tr",
    "ts",
    "uk",
    "vi",
    "zh",
    "zh_cn",
    "zh_tw",
    "zu",
)


def __getattr__(name: str) -> object:
    # The modules are imported the first time they are used, so a program
    # that asks for one language loads its models and not all 76.
    if name == "AnyModel":
        from pywttr_models import _language  # noqa: PLC0415

        value = _language.AnyModel
    elif name in __all__:
        value = import_module(f"{__name__}.{name}")
    else:
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted({*globals(), *__all__})
