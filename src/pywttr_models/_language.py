from __future__ import annotations

from typing import TYPE_CHECKING, Final, TypeAlias

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

AnyModel: TypeAlias = (
    af.Model
    | am.Model
    | ar.Model
    | be.Model
    | bn.Model
    | ca.Model
    | da.Model
    | de.Model
    | el.Model
    | en.Model
    | et.Model
    | fa.Model
    | fr.Model
    | gl.Model
    | hi.Model
    | hu.Model
    | ia.Model
    | id.Model
    | it.Model
    | lt.Model
    | mg.Model
    | nb.Model
    | nl.Model
    | oc.Model
    | pl.Model
    | pt_br.Model
    | ro.Model
    | ru.Model
    | ta.Model
    | th.Model
    | tr.Model
    | uk.Model
    | vi.Model
    | zh_cn.Model
    | zh_tw.Model
)
"""Response model of any language."""


class Language(StrEnum):
    """Language of the weather description; values are wttr.in codes.

    Examples:
        Prefer the member: type checkers then know the exact response model.

        ```python
        language = Language.ZH_CN
        language = Language["ZH_CN"]
        language = Language("zh-cn")
        ```
    """

    AF = "af", af.Model
    """Afrikaans."""
    AM = "am", am.Model
    """Amharic."""
    AR = "ar", ar.Model
    """Arabic."""
    BE = "be", be.Model
    """Belarusian."""
    BN = "bn", bn.Model
    """Bengali."""
    CA = "ca", ca.Model
    """Catalan."""
    DA = "da", da.Model
    """Danish."""
    DE = "de", de.Model
    """German."""
    EL = "el", el.Model
    """Greek."""
    EN = "en", en.Model
    """English."""
    ET = "et", et.Model
    """Estonian."""
    FA = "fa", fa.Model
    """Persian."""
    FR = "fr", fr.Model
    """French."""
    GL = "gl", gl.Model
    """Galician."""
    HI = "hi", hi.Model
    """Hindi."""
    HU = "hu", hu.Model
    """Hungarian."""
    IA = "ia", ia.Model
    """Interlingua."""
    ID = "id", id.Model
    """Indonesian."""
    IT = "it", it.Model
    """Italian."""
    LT = "lt", lt.Model
    """Lithuanian."""
    MG = "mg", mg.Model
    """Malagasy."""
    NB = "nb", nb.Model
    """Norwegian Bokmål."""
    NL = "nl", nl.Model
    """Dutch."""
    OC = "oc", oc.Model
    """Occitan."""
    PL = "pl", pl.Model
    """Polish."""
    PT_BR = "pt-br", pt_br.Model
    """Brazilian Portuguese."""
    RO = "ro", ro.Model
    """Romanian."""
    RU = "ru", ru.Model
    """Russian."""
    TA = "ta", ta.Model
    """Tamil."""
    TH = "th", th.Model
    """Thai."""
    TR = "tr", tr.Model
    """Turkish."""
    UK = "uk", uk.Model
    """Ukrainian."""
    VI = "vi", vi.Model
    """Vietnamese."""
    ZH_CN = "zh-cn", zh_cn.Model
    """Simplified Chinese."""
    ZH_TW = "zh-tw", zh_tw.Model
    """Traditional Chinese."""

    if TYPE_CHECKING:
        _model_: type[AnyModel]
    else:

        def __init__(self, _: str, model: type[AnyModel], /) -> None:
            self._model_: Final = model
