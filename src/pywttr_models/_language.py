from __future__ import annotations

import enum
import functools
import keyword
import operator
from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias

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


class Language(enum.StrEnum):
    """Language of the weather description; values are wttr.in codes.

    Examples:
        Prefer the member: type checkers then know the exact response model.

        ```python
        language = Language.ZH_CN
        language = Language["ZH_CN"]
        language = Language("zh-cn")
        ```
    """

    AF = "af"
    """Afrikaans."""
    AM = "am"
    """Amharic."""
    AR = "ar"
    """Arabic."""
    AZ = "az"
    """Azerbaijani; untranslated descriptions come in English."""
    BA = "ba"
    """Bashkir; untranslated descriptions come in English."""
    BE = "be"
    """Belarusian."""
    BG = "bg"
    """Bulgarian; untranslated descriptions come in English."""
    BN = "bn"
    """Bengali."""
    BS = "bs"
    """Bosnian; untranslated descriptions come in English."""
    BY = "by"
    """Belarusian under the code `by`, translated less than `BE`."""
    CA = "ca"
    """Catalan."""
    CRK = "crk"
    """Plains Cree."""
    CS = "cs"
    """Czech; untranslated descriptions come in English."""
    CY = "cy"
    """Welsh; untranslated descriptions come in English."""
    DA = "da"
    """Danish."""
    DE = "de"
    """German."""
    EL = "el"
    """Greek."""
    EN = "en"
    """English."""
    EO = "eo"
    """Esperanto; untranslated descriptions come in English."""
    ES = "es"
    """Spanish; untranslated descriptions come in English."""
    ET = "et"
    """Estonian."""
    EU = "eu"
    """Basque; untranslated descriptions come in English."""
    FA = "fa"
    """Persian."""
    FI = "fi"
    """Finnish; untranslated descriptions come in English."""
    FR = "fr"
    """French."""
    FY = "fy"
    """Frisian; untranslated descriptions come in English."""
    GA = "ga"
    """Irish; untranslated descriptions come in English."""
    GL = "gl"
    """Galician."""
    HE = "he"
    """Hebrew; untranslated descriptions come in English."""
    HI = "hi"
    """Hindi."""
    HR = "hr"
    """Croatian; untranslated descriptions come in English."""
    HU = "hu"
    """Hungarian."""
    HY = "hy"
    """Armenian; untranslated descriptions come in English."""
    IA = "ia"
    """Interlingua."""
    ID = "id"
    """Indonesian."""
    IS = "is"
    """Icelandic; untranslated descriptions come in English."""
    IT = "it"
    """Italian."""
    JA = "ja"
    """Japanese; untranslated descriptions come in English."""
    JV = "jv"
    """Javanese; untranslated descriptions come in English."""
    KA = "ka"
    """Georgian; untranslated descriptions come in English."""
    KK = "kk"
    """Kazakh; untranslated descriptions come in English."""
    KO = "ko"
    """Korean; untranslated descriptions come in English."""
    KY = "ky"
    """Kyrgyz; untranslated descriptions come in English."""
    LT = "lt"
    """Lithuanian."""
    LV = "lv"
    """Latvian; untranslated descriptions come in English."""
    MG = "mg"
    """Malagasy."""
    MK = "mk"
    """Macedonian; untranslated descriptions come in English."""
    ML = "ml"
    """Malayalam; untranslated descriptions come in English."""
    MR = "mr"
    """Marathi; untranslated descriptions come in English."""
    NB = "nb"
    """Norwegian Bokmål."""
    NL = "nl"
    """Dutch."""
    NN = "nn"
    """Norwegian Nynorsk; untranslated descriptions come in English."""
    OC = "oc"
    """Occitan."""
    PA = "pa"
    """Punjabi."""
    PL = "pl"
    """Polish."""
    PT = "pt"
    """Portuguese; untranslated descriptions come in English."""
    PT_BR = "pt-br"
    """Brazilian Portuguese."""
    RO = "ro"
    """Romanian."""
    RU = "ru"
    """Russian."""
    SK = "sk"
    """Slovak; untranslated descriptions come in English."""
    SL = "sl"
    """Slovenian; untranslated descriptions come in English."""
    SR = "sr"
    """Serbian; untranslated descriptions come in English."""
    SR_LAT = "sr-lat"
    """Serbian (Latin script); untranslated descriptions come in English."""
    SV = "sv"
    """Swedish; untranslated descriptions come in English."""
    SW = "sw"
    """Swahili; untranslated descriptions come in English."""
    TA = "ta"
    """Tamil."""
    TE = "te"
    """Telugu; untranslated descriptions come in English."""
    TH = "th"
    """Thai."""
    TR = "tr"
    """Turkish."""
    TS = "ts"
    """Tsonga; untranslated descriptions come in English."""
    UK = "uk"
    """Ukrainian."""
    VI = "vi"
    """Vietnamese."""
    ZH = "zh"
    """Chinese; untranslated descriptions come in English."""
    ZH_CN = "zh-cn"
    """Simplified Chinese."""
    ZH_TW = "zh-tw"
    """Traditional Chinese."""
    ZU = "zu"
    """Zulu; untranslated descriptions come in English."""

    if TYPE_CHECKING:
        _model_: type[AnyModel]
    else:

        def __getattr__(self, name: str) -> object:
            # A language's module is imported the first time its model is
            # needed, not all 76 of them with the package.
            if name != "_model_":
                msg = f"{type(self).__name__!r} object has no attribute {name!r}"
                raise AttributeError(msg)
            module = self.name.lower()
            if keyword.iskeyword(module):
                module += "_"
            model = import_module(f"pywttr_models.{module}").Model
            self.__dict__["_model_"] = model
            return model


def __getattr__(name: str) -> object:
    if name == "AnyModel":
        # The union of every language's model, so it imports all of them.
        value = functools.reduce(operator.or_, (language._model_ for language in Language))
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)
