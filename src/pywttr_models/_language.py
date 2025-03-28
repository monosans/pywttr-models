from __future__ import annotations

from typing import TYPE_CHECKING, Final, Union

from typing_extensions import TypeAlias

from pywttr_models import (
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
    id,  # noqa: A004
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
from pywttr_models._strenum import StrEnum

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


class Language(StrEnum):
    """StrEnum of languages supported by wttr.in.

    Examples:
        First option is preferred because of type safety.

        ```python
        language = Language.ZH_CN
        language = Language["ZH_CN"]
        language = Language("zh-cn")
        ```
    """

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

    if TYPE_CHECKING:
        _model_: type[AnyModel]
    else:

        def __init__(self, _: str, model: type[AnyModel], /) -> None:
            self._model_: Final = model
