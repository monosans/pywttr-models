from __future__ import annotations

from enum import Enum
from typing import Union

from typing_extensions import Self, TypeAlias

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
    language = Language.ZH_CN
    language = Language["ZH_CN"]
    language = Language("zh-cn")
    ```
    """

    _model_: AnyModel

    def __new__(cls, value: str, model: AnyModel) -> Self:
        member = str.__new__(cls, value)
        member._value_ = value
        member._model_ = model
        return member

    AF = "af", af.Model
    AM = "am", am.Model
    AR = "ar", ar.Model
    BE = "be", be.Model
    BN = "bn", bn.Model
    CA = "ca", ca.Model
    DA = "da", da.Model
    DE = "de", de.Model
    EL = "el", el.Model
    EN = "en", en.Model
    ET = "et", et.Model
    FA = "fa", fa.Model
    FR = "fr", fr.Model
    GL = "gl", gl.Model
    HI = "hi", hi.Model
    HU = "hu", hu.Model
    IA = "ia", ia.Model
    ID = "id", id.Model
    IT = "it", it.Model
    LT = "lt", lt.Model
    MG = "mg", mg.Model
    NB = "nb", nb.Model
    NL = "nl", nl.Model
    OC = "oc", oc.Model
    PL = "pl", pl.Model
    PT_BR = "pt-br", pt_br.Model
    RO = "ro", ro.Model
    RU = "ru", ru.Model
    TA = "ta", ta.Model
    TH = "th", th.Model
    TR = "tr", tr.Model
    UK = "uk", uk.Model
    VI = "vi", vi.Model
    ZH_CN = "zh-cn", zh_cn.Model
    ZH_TW = "zh-tw", zh_tw.Model
