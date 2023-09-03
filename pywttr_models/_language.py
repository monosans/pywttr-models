from __future__ import annotations

import sys
from enum import Enum
from typing import Union

if sys.version_info < (3, 10):
    from typing_extensions import TypeAlias
else:
    from typing import TypeAlias

if sys.version_info < (3, 11):
    from typing_extensions import Self
else:
    from typing import Self

from . import (
    af,
    am,
    ar,
    be,
    bn,
    ca,
    da,
    de,
    el,
    en,
    et,
    fa,
    fr,
    gl,
    hi,
    hu,
    ia,
    id,
    it,
    lt,
    mg,
    nb,
    nl,
    oc,
    pl,
    pt_br,
    ro,
    ru,
    ta,
    th,
    tr,
    uk,
    vi,
    zh_cn,
    zh_tw,
)

AnyModel: TypeAlias = Union[
    af.Model,
    am.Model,
    ar.Model,
    be.Model,
    bn.Model,
    ca.Model,
    da.Model,
    de.Model,
    el.Model,
    en.Model,
    et.Model,
    fa.Model,
    fr.Model,
    gl.Model,
    hi.Model,
    hu.Model,
    ia.Model,
    id.Model,
    it.Model,
    lt.Model,
    mg.Model,
    nb.Model,
    nl.Model,
    oc.Model,
    pl.Model,
    pt_br.Model,
    ro.Model,
    ru.Model,
    ta.Model,
    th.Model,
    tr.Model,
    uk.Model,
    vi.Model,
    zh_cn.Model,
    zh_tw.Model,
]


class Language(str, Enum):
    """StrEnum of languages supported by wttr.in.

    ```python
    # First option is preferred for typing
    language = Language.zh_cn
    language = Language["zh_cn"]
    language = Language("zh-cn")
    ```
    """

    _model_: AnyModel

    def __new__(cls, value: str, model: AnyModel) -> Self:
        member = str.__new__(cls, value)
        member._value_ = value
        member._model_ = model
        return member

    af = "af", af.Model
    am = "am", am.Model
    ar = "ar", ar.Model
    be = "be", be.Model
    bn = "bn", bn.Model
    ca = "ca", ca.Model
    da = "da", da.Model
    de = "de", de.Model
    el = "el", el.Model
    en = "en", en.Model
    et = "et", et.Model
    fa = "fa", fa.Model
    fr = "fr", fr.Model
    gl = "gl", gl.Model
    hi = "hi", hi.Model
    hu = "hu", hu.Model
    ia = "ia", ia.Model
    id = "id", id.Model
    it = "it", it.Model
    lt = "lt", lt.Model
    mg = "mg", mg.Model
    nb = "nb", nb.Model
    nl = "nl", nl.Model
    oc = "oc", oc.Model
    pl = "pl", pl.Model
    pt_br = "pt-br", pt_br.Model
    ro = "ro", ro.Model
    ru = "ru", ru.Model
    ta = "ta", ta.Model
    th = "th", th.Model
    tr = "tr", tr.Model
    uk = "uk", uk.Model
    vi = "vi", vi.Model
    zh_cn = "zh-cn", zh_cn.Model
    zh_tw = "zh-tw", zh_tw.Model
