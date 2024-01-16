from ctypes import pointer
from typing import Self, Any

import comtypes.automation

from portable_device_api._api.portable_device_api import tag_inner_PROPVARIANT
from portable_device_api._util.date import from_windows_date, to_windows_date

UNSPECIFIED = object()


# noinspection SpellCheckingInspection
class PropVariant:
    def __init__(self, v: tag_inner_PROPVARIANT):
        self._v = v

    @classmethod
    def create(cls, vt: comtypes.automation.VARENUM = comtypes.automation.VT_EMPTY, value: Any = UNSPECIFIED) -> Self:
        prop_variant = cls(tag_inner_PROPVARIANT(vt))

        if value is not UNSPECIFIED:
            prop_variant.value = value

        return prop_variant

    @property
    def v(self) -> tag_inner_PROPVARIANT:
        return self._v

    # VT_* constants from unknown source, possible comtypes.automation (but note
    # that comtypes.automation refers to VARIANT, not PROPVARIANT).
    # Union member types from __MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001:
    @property
    def value(self):
        # elif self.v.vt == comtypes.automation.VT_EMPTY: ...
        # elif self.v.vt == comtypes.automation.VT_NULL: ...
        if   self.v.vt == comtypes.automation.VT_I1:      return self.v.union.cVal     # c_char
        elif self.v.vt == comtypes.automation.VT_UI1:     return self.v.union.bVal     # c_ubyte
        elif self.v.vt == comtypes.automation.VT_I2:      return self.v.union.iVal     # c_short
        elif self.v.vt == comtypes.automation.VT_UI2:     return self.v.union.uiVal    # c_ushort
        elif self.v.vt == comtypes.automation.VT_I4:      return self.v.union.lVal     # c_int
        elif self.v.vt == comtypes.automation.VT_UI4:     return self.v.union.ulVal    # c_ulong
        elif self.v.vt == comtypes.automation.VT_INT:     return self.v.union.intVal   # c_int
        elif self.v.vt == comtypes.automation.VT_UINT:    return self.v.union.uintVal  # c_uint
        elif self.v.vt == comtypes.automation.VT_DECIMAL: return self.v.union.hVal     # _LARGE_INTEGER
        elif self.v.vt == comtypes.automation.VT_I8:      return self.v.union.hVal     # _LARGE_INTEGER
        elif self.v.vt == comtypes.automation.VT_UI8:     return self.v.union.uhVal    # _ULARGE_INTEGER
        elif self.v.vt == comtypes.automation.VT_R4:      return self.v.union.fltVal   # c_float
        elif self.v.vt == comtypes.automation.VT_R8:      return self.v.union.dblVal   # c_double
        elif self.v.vt == comtypes.automation.VT_BOOL:    return self.v.union.boolVal  # VARIANT_BOOL
        elif self.v.vt == comtypes.automation.VT_ERROR:   return self.v.union.scode    # SCODE == LONG
        # elif self.v.vt == comtypes.automation.VT_CY:
        elif self.v.vt == comtypes.automation.VT_DATE:    return from_windows_date(self.v.union.date)  # c_double
        # elif self.v.vt == comtypes.automation.VT_FILETIME: filetime
        elif self.v.vt == comtypes.automation.VT_CLSID:   return self.v.union.puuid.contents
        # elif self.v.vt == comtypes.automation.VT_CF:
        # elif self.v.vt == comtypes.automation.VT_BSTR:
        # elif self.v.vt == comtypes.automation.VT_BLOB:
        # elif self.v.vt == comtypes.automation.VT_BLOB_OBJECT:
        elif self.v.vt == comtypes.automation.VT_LPSTR:   return self.v.union.pszVal
        elif self.v.vt == comtypes.automation.VT_LPWSTR:  return self.v.union.pwszVal
        # elif self.v.vt == comtypes.automation.VT_UNKNOWN:
        # elif self.v.vt == comtypes.automation.VT_DISPATCH:
        # elif self.v.vt == comtypes.automation.VT_STREAM:
        # elif self.v.vt == comtypes.automation.VT_STREAMED_OBJECT:
        # elif self.v.vt == comtypes.automation.VT_STORAGE:
        # elif self.v.vt == comtypes.automation.VT_STORED_OBJECT:
        # elif self.v.vt == comtypes.automation.VT_VERSIONED_STREAM:
        else: raise ValueError(f"Unhandled value type: {self.v.vt}")

    # See value()
    @value.setter
    def value(self, value):
        # elif self.v.vt == comtypes.automation.VT_EMPTY: ...
        # elif self.v.vt == comtypes.automation.VT_NULL: ...
        if   self.v.vt == comtypes.automation.VT_I1:      self.v.union.cVal = value     # c_char
        elif self.v.vt == comtypes.automation.VT_UI1:     self.v.union.bVal = value     # c_ubyte
        elif self.v.vt == comtypes.automation.VT_I2:      self.v.union.iVal = value     # c_short
        elif self.v.vt == comtypes.automation.VT_UI2:     self.v.union.uiVal = value    # c_ushort
        elif self.v.vt == comtypes.automation.VT_I4:      self.v.union.lVal = value     # c_int
        elif self.v.vt == comtypes.automation.VT_UI4:     self.v.union.ulVal = value    # c_ulong
        elif self.v.vt == comtypes.automation.VT_INT:     self.v.union.intVal = value   # c_int
        elif self.v.vt == comtypes.automation.VT_UINT:    self.v.union.uintVal = value  # c_uint
        elif self.v.vt == comtypes.automation.VT_DECIMAL: self.v.union.hVal = value     # _LARGE_INTEGER
        elif self.v.vt == comtypes.automation.VT_I8:      self.v.union.hVal = value     # _LARGE_INTEGER
        elif self.v.vt == comtypes.automation.VT_UI8:     self.v.union.uhVal = value    # _ULARGE_INTEGER
        elif self.v.vt == comtypes.automation.VT_R4:      self.v.union.fltVal = value   # c_float
        elif self.v.vt == comtypes.automation.VT_R8:      self.v.union.dblVal = value   # c_double
        elif self.v.vt == comtypes.automation.VT_BOOL:    self.v.union.boolVal = value  # VARIANT_BOOL
        elif self.v.vt == comtypes.automation.VT_ERROR:   self.v.union.scode = value    # SCODE = LONG
        # elif self.v.vt == comtypes.automation.VT_CY:
        elif self.v.vt == comtypes.automation.VT_DATE:    self.v.union.date = to_windows_date(value)  # float
        # elif self.v.vt == comtypes.automation.VT_FILETIME: filetime
        elif self.v.vt == comtypes.automation.VT_CLSID:   self.v.union.puuid = pointer(value)  # POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)
        # elif self.v.vt == comtypes.automation.VT_CF:
        # elif self.v.vt == comtypes.automation.VT_BSTR:
        # elif self.v.vt == comtypes.automation.VT_BLOB:
        # elif self.v.vt == comtypes.automation.VT_BLOB_OBJECT:
        elif self.v.vt == comtypes.automation.VT_LPSTR:   self.v.union.pszVal = value  # STRING
        elif self.v.vt == comtypes.automation.VT_LPWSTR:  self.v.union.pwszVal = value  # WSTRING
        # elif self.v.vt == comtypes.automation.VT_UNKNOWN:
        # elif self.v.vt == comtypes.automation.VT_DISPATCH:
        # elif self.v.vt == comtypes.automation.VT_STREAM:
        # elif self.v.vt == comtypes.automation.VT_STREAMED_OBJECT:
        # elif self.v.vt == comtypes.automation.VT_STORAGE:
        # elif self.v.vt == comtypes.automation.VT_STORED_OBJECT:
        # elif self.v.vt == comtypes.automation.VT_VERSIONED_STREAM:
        else: raise ValueError(f"Unhandled value type: {self.v.vt}")

    # Unused union members:
    #     ('__OBSOLETE__VARIANT_BOOL', VARIANT_BOOL),
    #     ('cyVal', c_longlong),
    #     ('filetime', _FILETIME),
    #     ('pClipData', POINTER(tagCLIPDATA)),
    #     ('bstrVal', BSTR),
    #     ('bstrblobVal', tagBSTRBLOB),
    #     ('blob', tagBLOB),
    #     ('punkVal', POINTER(IUnknown)),
    #     ('pdispVal', POINTER(IDispatch)),
    #     ('pStream', POINTER(IStream)),
    #     ('pStorage', POINTER(IStorage)),
    #     ('pVersionedStream', POINTER(tagVersionedStream)),
    #     ('parray', wirePSAFEARRAY),
    #     ('cac', tagCAC),
    #     ('caub', tagCAUB),
    #     ('cai', tagCAI),
    #     ('caui', tagCAUI),
    #     ('cal', tagCAL),
    #     ('caul', tagCAUL),
    #     ('cah', tagCAH),
    #     ('cauh', tagCAUH),
    #     ('caflt', tagCAFLT),
    #     ('cadbl', tagCADBL),
    #     ('cabool', tagCABOOL),
    #     ('cascode', tagCASCODE),
    #     ('cacy', tagCACY),
    #     ('cadate', tagCADATE),
    #     ('cafiletime', tagCAFILETIME),
    #     ('cauuid', tagCACLSID),
    #     ('caclipdata', tagCACLIPDATA),
    #     ('cabstr', tagCABSTR),
    #     ('cabstrblob', tagCABSTRBLOB),
    #     ('calpstr', tagCALPSTR),
    #     ('calpwstr', tagCALPWSTR),
    #     ('capropvar', tagCAPROPVARIANT),
    #     ('pcVal', STRING),
    #     ('pbVal', POINTER(c_ubyte)),
    #     ('piVal', POINTER(c_short)),
    #     ('puiVal', POINTER(c_ushort)),
    #     ('plVal', POINTER(c_int)),
    #     ('pulVal', POINTER(c_ulong)),
    #     ('pintVal', POINTER(c_int)),
    #     ('puintVal', POINTER(c_uint)),
    #     ('pfltVal', POINTER(c_float)),
    #     ('pdblVal', POINTER(c_double)),
    #     ('pboolVal', POINTER(VARIANT_BOOL)),
    #     ('pdecVal', POINTER(DECIMAL)),
    #     ('pscode', POINTER(SCODE)),
    #     ('pcyVal', POINTER(c_longlong)),
    #     ('pdate', POINTER(c_double)),
    #     ('pbstrVal', POINTER(BSTR)),
    #     ('ppunkVal', POINTER(POINTER(IUnknown))),
    #     ('ppdispVal', POINTER(POINTER(IDispatch))),
    #     ('pparray', POINTER(wirePSAFEARRAY)),
    #     ('pvarVal', POINTER(tag_inner_PROPVARIANT)),

    # Unused VT_ constants:
    #     VT_VARIANT
    #     VT_VOID
    #     VT_HRESULT
    #     VT_PTR
    #     VT_SAFEARRAY
    #     VT_CARRAY
    #     VT_USERDEFINED
    #     VT_RECORD
    #     VT_INT_PTR
    #     VT_UINT_PTR
    #     VT_BSTR_BLOB
    #     VT_VECTOR
    #     VT_ARRAY
    #     VT_BYREF
