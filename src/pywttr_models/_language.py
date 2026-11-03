from __future__ import annotations

from typing import TYPE_CHECKING, Final, TypeAlias

from pywttr_models import (
    af,
    am,
    ar,
    az,
    ba,
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
from pywttr_models._strenum import StrEnum

AnyModel: TypeAlias = (
    af.Model
    | am.Model
    | ar.Model
    | az.Model
    | ba.Model
    | be.Model
    | bg.Model
    | bn.Model
    | bs.Model
    | by.Model
    | ca.Model
    | crk.Model
    | cs.Model
    | cy.Model
    | da.Model
    | de.Model
    | el.Model
    | en.Model
    | eo.Model
    | es.Model
    | et.Model
    | eu.Model
    | fa.Model
    | fi.Model
    | fr.Model
    | fy.Model
    | ga.Model
    | gl.Model
    | he.Model
    | hi.Model
    | hr.Model
    | hu.Model
    | hy.Model
    | ia.Model
    | id.Model
    | is_.Model
    | it.Model
    | ja.Model
    | jv.Model
    | ka.Model
    | kk.Model
    | ko.Model
    | ky.Model
    | lt.Model
    | lv.Model
    | mg.Model
    | mk.Model
    | ml.Model
    | mr.Model
    | nb.Model
    | nl.Model
    | nn.Model
    | oc.Model
    | pa.Model
    | pl.Model
    | pt.Model
    | pt_br.Model
    | ro.Model
    | ru.Model
    | sk.Model
    | sl.Model
    | sr.Model
    | sr_lat.Model
    | sv.Model
    | sw.Model
    | ta.Model
    | te.Model
    | th.Model
    | tr.Model
    | ts.Model
    | uk.Model
    | vi.Model
    | zh.Model
    | zh_cn.Model
    | zh_tw.Model
    | zu.Model
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
    AZ = "az", az.Model
    """Azerbaijani; untranslated descriptions come in English."""
    BA = "ba", ba.Model
    """Bashkir; untranslated descriptions come in English."""
    BE = "be", be.Model
    """Belarusian."""
    BG = "bg", bg.Model
    """Bulgarian; untranslated descriptions come in English."""
    BN = "bn", bn.Model
    """Bengali."""
    BS = "bs", bs.Model
    """Bosnian; untranslated descriptions come in English."""
    BY = "by", by.Model
    """Belarusian under the code `by`, translated less than `BE`."""
    CA = "ca", ca.Model
    """Catalan."""
    CRK = "crk", crk.Model
    """Plains Cree."""
    CS = "cs", cs.Model
    """Czech; untranslated descriptions come in English."""
    CY = "cy", cy.Model
    """Welsh; untranslated descriptions come in English."""
    DA = "da", da.Model
    """Danish."""
    DE = "de", de.Model
    """German."""
    EL = "el", el.Model
    """Greek."""
    EN = "en", en.Model
    """English."""
    EO = "eo", eo.Model
    """Esperanto; untranslated descriptions come in English."""
    ES = "es", es.Model
    """Spanish; untranslated descriptions come in English."""
    ET = "et", et.Model
    """Estonian."""
    EU = "eu", eu.Model
    """Basque; untranslated descriptions come in English."""
    FA = "fa", fa.Model
    """Persian."""
    FI = "fi", fi.Model
    """Finnish; untranslated descriptions come in English."""
    FR = "fr", fr.Model
    """French."""
    FY = "fy", fy.Model
    """Frisian; untranslated descriptions come in English."""
    GA = "ga", ga.Model
    """Irish; untranslated descriptions come in English."""
    GL = "gl", gl.Model
    """Galician."""
    HE = "he", he.Model
    """Hebrew; untranslated descriptions come in English."""
    HI = "hi", hi.Model
    """Hindi."""
    HR = "hr", hr.Model
    """Croatian; untranslated descriptions come in English."""
    HU = "hu", hu.Model
    """Hungarian."""
    HY = "hy", hy.Model
    """Armenian; untranslated descriptions come in English."""
    IA = "ia", ia.Model
    """Interlingua."""
    ID = "id", id.Model
    """Indonesian."""
    IS = "is", is_.Model
    """Icelandic; untranslated descriptions come in English."""
    IT = "it", it.Model
    """Italian."""
    JA = "ja", ja.Model
    """Japanese; untranslated descriptions come in English."""
    JV = "jv", jv.Model
    """Javanese; untranslated descriptions come in English."""
    KA = "ka", ka.Model
    """Georgian; untranslated descriptions come in English."""
    KK = "kk", kk.Model
    """Kazakh; untranslated descriptions come in English."""
    KO = "ko", ko.Model
    """Korean; untranslated descriptions come in English."""
    KY = "ky", ky.Model
    """Kyrgyz; untranslated descriptions come in English."""
    LT = "lt", lt.Model
    """Lithuanian."""
    LV = "lv", lv.Model
    """Latvian; untranslated descriptions come in English."""
    MG = "mg", mg.Model
    """Malagasy."""
    MK = "mk", mk.Model
    """Macedonian; untranslated descriptions come in English."""
    ML = "ml", ml.Model
    """Malayalam; untranslated descriptions come in English."""
    MR = "mr", mr.Model
    """Marathi; untranslated descriptions come in English."""
    NB = "nb", nb.Model
    """Norwegian Bokmål."""
    NL = "nl", nl.Model
    """Dutch."""
    NN = "nn", nn.Model
    """Norwegian Nynorsk; untranslated descriptions come in English."""
    OC = "oc", oc.Model
    """Occitan."""
    PA = "pa", pa.Model
    """Punjabi."""
    PL = "pl", pl.Model
    """Polish."""
    PT = "pt", pt.Model
    """Portuguese; untranslated descriptions come in English."""
    PT_BR = "pt-br", pt_br.Model
    """Brazilian Portuguese."""
    RO = "ro", ro.Model
    """Romanian."""
    RU = "ru", ru.Model
    """Russian."""
    SK = "sk", sk.Model
    """Slovak; untranslated descriptions come in English."""
    SL = "sl", sl.Model
    """Slovenian; untranslated descriptions come in English."""
    SR = "sr", sr.Model
    """Serbian; untranslated descriptions come in English."""
    SR_LAT = "sr-lat", sr_lat.Model
    """Serbian (Latin script); untranslated descriptions come in English."""
    SV = "sv", sv.Model
    """Swedish; untranslated descriptions come in English."""
    SW = "sw", sw.Model
    """Swahili; untranslated descriptions come in English."""
    TA = "ta", ta.Model
    """Tamil."""
    TE = "te", te.Model
    """Telugu; untranslated descriptions come in English."""
    TH = "th", th.Model
    """Thai."""
    TR = "tr", tr.Model
    """Turkish."""
    TS = "ts", ts.Model
    """Tsonga; untranslated descriptions come in English."""
    UK = "uk", uk.Model
    """Ukrainian."""
    VI = "vi", vi.Model
    """Vietnamese."""
    ZH = "zh", zh.Model
    """Chinese; untranslated descriptions come in English."""
    ZH_CN = "zh-cn", zh_cn.Model
    """Simplified Chinese."""
    ZH_TW = "zh-tw", zh_tw.Model
    """Traditional Chinese."""
    ZU = "zu", zu.Model
    """Zulu; untranslated descriptions come in English."""

    if TYPE_CHECKING:
        _model_: type[AnyModel]
    else:

        def __init__(self, _: str, model: type[AnyModel], /) -> None:
            self._model_: Final = model
