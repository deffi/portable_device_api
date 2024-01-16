# The values in this file are taken from PortableDevice.h from the Windows SDK
# 10.0.22000.0

from enum import IntEnum

from comtypes import GUID

from portable_device_api import PropertyKey as _PropertyKey
from portable_device_api._util import ReverseLookup as _ReverseLookup

#############################################################################
# This section declares WPD guids used in PnP
#############################################################################
GUID_DEVINTERFACE_WPD         = GUID("{6AC27878-A6FA-4155-BA85-F98F491D4F33}")  # This GUID is used to identify devices / drivers that support the WPD DDI.
GUID_DEVINTERFACE_WPD_PRIVATE = GUID("{BA0C718F-4DED-49B7-BDD3-FABE28661211}")  # This GUID is used to identify devices / drivers that can be used only by a specialized WPD client and will not show up in normal WPD enumeration.
GUID_DEVINTERFACE_WPD_SERVICE = GUID("{9EF44F80-3D64-4246-A6AA-206F328D1EDC}")  # This GUID is used to identify services that support the WPD Services DDI.

#############################################################################
# This section declares WPD defines
#############################################################################
# Abridged
WPD_DEVICE_OBJECT_ID = "DEVICE"  # Pre-defined ObjectID for the DEVICE object.


#############################################################################
# This section defines flags used in API arguments
#############################################################################

# noinspection PyPep8Naming
class DELETE_OBJECT_OPTIONS(IntEnum):  # Indicates whether the delete request should recursively delete any children.
    PORTABLE_DEVICE_DELETE_NO_RECURSION = 0
    PORTABLE_DEVICE_DELETE_WITH_RECURSION = 1


# noinspection PyPep8Naming
class WPD_DEVICE_TYPES(IntEnum):  # Possible values for PORTABLE_DEVICE_TYPE registry value.
    WPD_DEVICE_TYPE_GENERIC = 0
    WPD_DEVICE_TYPE_CAMERA = 1
    WPD_DEVICE_TYPE_MEDIA_PLAYER = 2
    WPD_DEVICE_TYPE_PHONE = 3
    WPD_DEVICE_TYPE_VIDEO = 4
    WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER = 5
    WPD_DEVICE_TYPE_AUDIO_RECORDER = 6


class WpdAttributeForm(IntEnum):  # Possible values for WPD_PROPERTY_ATTRIBUTE_FORM
    WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED = 0
    WPD_PROPERTY_ATTRIBUTE_FORM_RANGE = 1
    WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION = 2
    WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION = 3
    WPD_PROPERTY_ATTRIBUTE_FORM_OBJECT_IDENTIFIER = 4


class WpdParameterAttributeForm(IntEnum):  # Possible values for WPD_PARAMETER_ATTRIBUTE_FORM
    WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED = 0
    WPD_PARAMETER_ATTRIBUTE_FORM_RANGE = 1
    WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION = 2
    WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION = 3
    WPD_PARAMETER_ATTRIBUTE_FORM_OBJECT_IDENTIFIER = 4


# noinspection PyPep8Naming
class WPD_DEVICE_TRANSPORTS(IntEnum):  # Possible values for WPD_DEVICE_TRANSPORT property.
    WPD_DEVICE_TRANSPORT_UNSPECIFIED = 0
    WPD_DEVICE_TRANSPORT_USB = 1
    WPD_DEVICE_TRANSPORT_IP = 2
    WPD_DEVICE_TRANSPORT_BLUETOOTH = 3


# noinspection PyPep8Naming
class WPD_STORAGE_TYPE_VALUES(IntEnum):  # Indicates the type of storage.
    WPD_STORAGE_TYPE_UNDEFINED = 0
    WPD_STORAGE_TYPE_FIXED_ROM = 1
    WPD_STORAGE_TYPE_REMOVABLE_ROM = 2
    WPD_STORAGE_TYPE_FIXED_RAM = 3
    WPD_STORAGE_TYPE_REMOVABLE_RAM = 4


# noinspection PyPep8Naming
class WPD_STORAGE_ACCESS_CAPABILITY_VALUES(IntEnum):  # Indicates write-protection that globally affects the storage.
    WPD_STORAGE_ACCESS_CAPABILITY_READWRITE = 0
    WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION = 1
    WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION = 2


# noinspection PyPep8Naming
class WPD_SMS_ENCODING_TYPES(IntEnum):  # Possible values for WPD_SMS_ENCODING
    SMS_ENCODING_7_BIT = 0
    SMS_ENCODING_8_BIT = 1
    SMS_ENCODING_UTF_16 = 2


# noinspection PyPep8Naming
class SMS_MESSAGE_TYPES(IntEnum):  # Possible values for WPD_PROPERTY_SMS_MESSAGE_TYPE
    SMS_TEXT_MESSAGE = 0
    SMS_BINARY_MESSAGE = 1


# noinspection PyPep8Naming
class WPD_POWER_SOURCES(IntEnum):  # Indicates whether the device is on battery power or external power.
    WPD_POWER_SOURCE_BATTERY = 0
    WPD_POWER_SOURCE_EXTERNAL = 1


# noinspection PyPep8Naming
class WPD_WHITE_BALANCE_SETTINGS(IntEnum):  # Indicates the way the device weighs color channels.
    WPD_WHITE_BALANCE_UNDEFINED = 0
    WPD_WHITE_BALANCE_MANUAL = 1
    WPD_WHITE_BALANCE_AUTOMATIC = 2
    WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC = 3
    WPD_WHITE_BALANCE_DAYLIGHT = 4
    WPD_WHITE_BALANCE_FLORESCENT = 5
    WPD_WHITE_BALANCE_TUNGSTEN = 6
    WPD_WHITE_BALANCE_FLASH = 7


# noinspection PyPep8Naming
class WPD_FOCUS_MODES(IntEnum):  # Indicates the focus mode of the device.
    WPD_FOCUS_UNDEFINED = 0
    WPD_FOCUS_MANUAL = 1
    WPD_FOCUS_AUTOMATIC = 2
    WPD_FOCUS_AUTOMATIC_MACRO = 3


# noinspection PyPep8Naming
class WPD_EXPOSURE_METERING_MODES(IntEnum):  # Indicates the metering mode of the device.
    WPD_EXPOSURE_METERING_MODE_UNDEFINED = 0
    WPD_EXPOSURE_METERING_MODE_AVERAGE = 1
    WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE = 2
    WPD_EXPOSURE_METERING_MODE_MULTI_SPOT = 3
    WPD_EXPOSURE_METERING_MODE_CENTER_SPOT = 4


# noinspection PyPep8Naming
class WPD_FLASH_MODES(IntEnum):  # Indicates the flash mode of the device.
    WPD_FLASH_MODE_UNDEFINED = 0
    WPD_FLASH_MODE_AUTO = 1
    WPD_FLASH_MODE_OFF = 2
    WPD_FLASH_MODE_FILL = 3
    WPD_FLASH_MODE_RED_EYE_AUTO = 4
    WPD_FLASH_MODE_RED_EYE_FILL = 5
    WPD_FLASH_MODE_EXTERNAL_SYNC = 6


# noinspection PyPep8Naming
class WPD_EXPOSURE_PROGRAM_MODES(IntEnum):  # Indicates the exposure program mode of the device.
    WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED = 0
    WPD_EXPOSURE_PROGRAM_MODE_MANUAL = 1
    WPD_EXPOSURE_PROGRAM_MODE_AUTO = 2
    WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY = 3
    WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY = 4
    WPD_EXPOSURE_PROGRAM_MODE_CREATIVE = 5
    WPD_EXPOSURE_PROGRAM_MODE_ACTION = 6
    WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT = 7


# noinspection PyPep8Naming
class WPD_CAPTURE_MODES(IntEnum):  # Indicates the capture mode of the device.
    WPD_CAPTURE_MODE_UNDEFINED = 0
    WPD_CAPTURE_MODE_NORMAL = 1
    WPD_CAPTURE_MODE_BURST = 2
    WPD_CAPTURE_MODE_TIMELAPSE = 3


# noinspection PyPep8Naming
class WPD_EFFECT_MODES(IntEnum):  # Indicates the effect mode of the capture device.
    WPD_EFFECT_MODE_UNDEFINED = 0
    WPD_EFFECT_MODE_COLOR = 1
    WPD_EFFECT_MODE_BLACK_AND_WHITE = 2
    WPD_EFFECT_MODE_SEPIA = 3


# noinspection PyPep8Naming
class WPD_FOCUS_METERING_MODES(IntEnum):  # Indicates the metering mode of the capture device.
    WPD_FOCUS_METERING_MODE_UNDEFINED = 0
    WPD_FOCUS_METERING_MODE_CENTER_SPOT = 1
    WPD_FOCUS_METERING_MODE_MULTI_SPOT = 2


# noinspection PyPep8Naming
class WPD_BITRATE_TYPES(IntEnum):  # Indicates the type of bitrate for the audio/video data.
    WPD_BITRATE_TYPE_UNUSED = 0
    WPD_BITRATE_TYPE_DISCRETE = 1
    WPD_BITRATE_TYPE_VARIABLE = 2
    WPD_BITRATE_TYPE_FREE = 3


# noinspection PyPep8Naming
class WPD_META_GENRES(IntEnum):  # Qualifies the object data in a contextual way.
    WPD_META_GENRE_UNUSED = 0x0
    WPD_META_GENRE_GENERIC_MUSIC_AUDIO_FILE = 0x1
    WPD_META_GENRE_GENERIC_NON_MUSIC_AUDIO_FILE = 0x11
    WPD_META_GENRE_SPOKEN_WORD_AUDIO_BOOK_FILES = 0x12
    WPD_META_GENRE_SPOKEN_WORD_FILES_NON_AUDIO_BOOK = 0x13
    WPD_META_GENRE_SPOKEN_WORD_NEWS = 0x14
    WPD_META_GENRE_SPOKEN_WORD_TALK_SHOWS = 0x15
    WPD_META_GENRE_GENERIC_VIDEO_FILE = 0x21
    WPD_META_GENRE_NEWS_VIDEO_FILE = 0x22
    WPD_META_GENRE_MUSIC_VIDEO_FILE = 0x23
    WPD_META_GENRE_HOME_VIDEO_FILE = 0x24
    WPD_META_GENRE_FEATURE_FILM_VIDEO_FILE = 0x25
    WPD_META_GENRE_TELEVISION_VIDEO_FILE = 0x26
    WPD_META_GENRE_TRAINING_EDUCATIONAL_VIDEO_FILE = 0x27
    WPD_META_GENRE_PHOTO_MONTAGE_VIDEO_FILE = 0x28
    WPD_META_GENRE_GENERIC_NON_AUDIO_NON_VIDEO = 0x30
    WPD_META_GENRE_AUDIO_PODCAST = 0x40
    WPD_META_GENRE_VIDEO_PODCAST = 0x41
    WPD_META_GENRE_MIXED_PODCAST = 0x42


# noinspection PyPep8Naming
class WPD_CROPPED_STATUS_VALUES(IntEnum):  # Indicates the cropped status of an image.
    WPD_CROPPED_STATUS_NOT_CROPPED = 0
    WPD_CROPPED_STATUS_CROPPED = 1
    WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED = 2


# noinspection PyPep8Naming
class WPD_COLOR_CORRECTED_STATUS_VALUES(IntEnum):  # Indicates the color corrected status of an image.
    WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED = 0
    WPD_COLOR_CORRECTED_STATUS_CORRECTED = 1
    WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED = 2


# noinspection PyPep8Naming
class WPD_VIDEO_SCAN_TYPES(IntEnum):  # Identifies the video scan-type information.
    WPD_VIDEO_SCAN_TYPE_UNUSED = 0
    WPD_VIDEO_SCAN_TYPE_PROGRESSIVE = 1
    WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST = 2
    WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST = 3
    WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST = 4
    WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST = 5
    WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE = 6
    WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE = 7


# noinspection PyPep8Naming
class WPD_OPERATION_STATES(IntEnum):  # Indicates the current state of the operation in progress.
    WPD_OPERATION_STATE_UNSPECIFIED = 0
    WPD_OPERATION_STATE_STARTED = 1
    WPD_OPERATION_STATE_RUNNING = 2
    WPD_OPERATION_STATE_PAUSED = 3
    WPD_OPERATION_STATE_CANCELLED = 4
    WPD_OPERATION_STATE_FINISHED = 5
    WPD_OPERATION_STATE_ABORTED = 6


# noinspection PyPep8Naming
class WPD_SECTION_DATA_UNITS_VALUES(IntEnum):  # Indicates the units for a referenced section of data.
    WPD_SECTION_DATA_UNITS_BYTES = 0
    WPD_SECTION_DATA_UNITS_MILLISECONDS = 1


# noinspection PyPep8Naming
class WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES(IntEnum):  # Indicates whether the rendering information profile entry corresponds to an Object or a Resource.
    WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT = 0
    WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE = 1


# noinspection PyPep8Naming
class WPD_COMMAND_ACCESS_TYPES(IntEnum):  # Indicates the type of access the command requires.  This is only used internally by the command access lookup table.  There is no need to use these values directly.
    WPD_COMMAND_ACCESS_READ = 1
    WPD_COMMAND_ACCESS_READWRITE = 3
    WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS = 4
    WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS = 8
    WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS = 16


# noinspection PyPep8Naming
class WPD_SERVICE_INHERITANCE_TYPES(IntEnum):  # Indicates the inheritance relationship to query for this service.
    WPD_SERVICE_INHERITANCE_IMPLEMENTATION = 0


# noinspection PyPep8Naming
class WPD_PARAMETER_USAGE_TYPES(IntEnum):  # Indicates the usage of a parameter.
    WPD_PARAMETER_USAGE_RETURN = 0
    WPD_PARAMETER_USAGE_IN = 1
    WPD_PARAMETER_USAGE_OUT = 2
    WPD_PARAMETER_USAGE_INOUT = 3


#############################################################################
# This section declares WPD specific Errors
#############################################################################
# See errors.py

#############################################################################
# This section defines all WPD Events
#############################################################################
WPD_EVENT_NOTIFICATION                = GUID("{2BA2E40A-6B4C-4295-BB43-26322B99AEB2}")  # This GUID is used to identify all WPD driver events to the event sub-system. The driver uses this as the GUID identifier when it queues an event with IWdfDevice::PostEvent(). Applications never use this value.
WPD_EVENT_OBJECT_ADDED                = GUID("{A726DA95-E207-4B02-8D44-BEF2E86CBFFC}")  # This event is sent after a new object is available on the device.
WPD_EVENT_OBJECT_REMOVED              = GUID("{BE82AB88-A52C-4823-96E5-D0272671FC38}")  # This event is sent after a previously existing object has been removed from the device.
WPD_EVENT_OBJECT_UPDATED              = GUID("{1445A759-2E01-485D-9F27-FF07DAE697AB}")  # This event is sent after an object has been updated such that any connected client should refresh its view of that object.
WPD_EVENT_DEVICE_RESET                = GUID("{7755CF53-C1ED-44F3-B5A2-451E2C376B27}")  # This event indicates that the device is about to be reset, and all connected clients should close their connection to the device.
WPD_EVENT_DEVICE_CAPABILITIES_UPDATED = GUID("{36885AA1-CD54-4DAA-B3D0-AFB3E03F5999}")  # This event indicates that the device capabilities have changed. Clients should re-query the device if they have made any decisions based on device capabilities.
WPD_EVENT_STORAGE_FORMAT              = GUID("{3782616B-22BC-4474-A251-3070F8D38857}")  # This event indicates the progress of a format operation on a storage object.
WPD_EVENT_OBJECT_TRANSFER_REQUESTED   = GUID("{8D16A0A1-F2C6-41DA-8F19-5E53721ADBF2}")  # This event is sent to request an application to transfer a particular object from the device.
WPD_EVENT_DEVICE_REMOVED              = GUID("{E4CBCA1B-6918-48B9-85EE-02BE7C850AF9}")  # This event is sent when a driver for a device is being unloaded. This is typically a result of the device being unplugged.
WPD_EVENT_SERVICE_METHOD_COMPLETE     = GUID("{8A33F5F8-0ACC-4D9B-9CC4-112D353B86CA}")  # This event is sent when a driver has completed invoking a service method. This event must be sent even when the method fails.

#############################################################################
# This section defines all WPD content types
#############################################################################
WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT   = GUID("{99ED0160-17FF-4C44-9D98-1D7A6F941921}")  # Indicates this object represents a functional object, not content data on the device.
WPD_CONTENT_TYPE_FOLDER              = GUID("{27E2E392-A111-48E0-AB0C-E17705A05F85}")  # Indicates this object is a folder.
WPD_CONTENT_TYPE_IMAGE               = GUID("{ef2107d5-a52a-4243-a26b-62d4176d7603}")  # Indicates this object represents image data (e.g. a JPEG file)
WPD_CONTENT_TYPE_DOCUMENT            = GUID("{680ADF52-950A-4041-9B41-65E393648155}")  # Indicates this object represents document data (e.g. a MS WORD file, TEXT file, etc.)
WPD_CONTENT_TYPE_CONTACT             = GUID("{EABA8313-4525-4707-9F0E-87C6808E9435}")  # Indicates this object represents contact data (e.g. name/number, or a VCARD file)
WPD_CONTENT_TYPE_CONTACT_GROUP       = GUID("{346B8932-4C36-40D8-9415-1828291F9DE9}")  # Indicates this object represents a group of contacts.
WPD_CONTENT_TYPE_AUDIO               = GUID("{4AD2C85E-5E2D-45E5-8864-4F229E3C6CF0}")  # Indicates this object represents audio data (e.g. a WMA or MP3 file)
WPD_CONTENT_TYPE_VIDEO               = GUID("{9261B03C-3D78-4519-85E3-02C5E1F50BB9}")  # Indicates this object represents video data (e.g. a WMV or AVI file)
WPD_CONTENT_TYPE_TELEVISION          = GUID("{60A169CF-F2AE-4E21-9375-9677F11C1C6E}")  # Indicates this object represents a television recording.
WPD_CONTENT_TYPE_PLAYLIST            = GUID("{1A33F7E4-AF13-48F5-994E-77369DFE04A3}")  # Indicates this object represents a playlist.
WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM = GUID("{00F0C3AC-A593-49AC-9219-24ABCA5A2563}")  # Indicates this object represents an album, which may contain objects of different content types (typically, MUSIC, IMAGE and VIDEO).
WPD_CONTENT_TYPE_AUDIO_ALBUM         = GUID("{AA18737E-5009-48FA-AE21-85F24383B4E6}")  # Indicates this object represents an audio album.
WPD_CONTENT_TYPE_IMAGE_ALBUM         = GUID("{75793148-15F5-4A30-A813-54ED8A37E226}")  # Indicates this object represents an image album.
WPD_CONTENT_TYPE_VIDEO_ALBUM         = GUID("{012B0DB7-D4C1-45D6-B081-94B87779614F}")  # Indicates this object represents a video album.
WPD_CONTENT_TYPE_MEMO                = GUID("{9CD20ECF-3B50-414F-A641-E473FFE45751}")  # Indicates this object represents memo data
WPD_CONTENT_TYPE_EMAIL               = GUID("{8038044A-7E51-4F8F-883D-1D0623D14533}")  # Indicates this object represents e-mail data
WPD_CONTENT_TYPE_APPOINTMENT         = GUID("{0FED060E-8793-4B1E-90C9-48AC389AC631}")  # Indicates this object represents an appointment in a calendar
WPD_CONTENT_TYPE_TASK                = GUID("{63252F2C-887F-4CB6-B1AC-D29855DCEF6C}")  # Indicates this object represents a task for tracking (e.g. a TO-DO list)
WPD_CONTENT_TYPE_PROGRAM             = GUID("{D269F96A-247C-4BFF-98FB-97F3C49220E6}")  # Indicates this object represents a file that can be run. This could be a script, executable and so on.
WPD_CONTENT_TYPE_GENERIC_FILE        = GUID("{0085E0A6-8D34-45D7-BC5C-447E59C73D48}")  # Indicates this object represents a file that does not fall into any of the other predefined WPD types for files.
WPD_CONTENT_TYPE_CALENDAR            = GUID("{A1FD5967-6023-49A0-9DF1-F8060BE751B0}")  # Indicates this object represents a calender
WPD_CONTENT_TYPE_GENERIC_MESSAGE     = GUID("{E80EAAF8-B2DB-4133-B67E-1BEF4B4A6E5F}")  # Indicates this object represents a message (e.g. SMS message, E-Mail message, etc.)
WPD_CONTENT_TYPE_NETWORK_ASSOCIATION = GUID("{031DA7EE-18C8-4205-847E-89A11261D0F3}")  # Indicates this object represents an association between a host and a device.
WPD_CONTENT_TYPE_CERTIFICATE         = GUID("{DC3876E8-A948-4060-9050-CBD77E8A3D87}")  # Indicates this object represents certificate used for authentication.
WPD_CONTENT_TYPE_WIRELESS_PROFILE    = GUID("{0BAC070A-9F5F-4DA4-A8F6-3DE44D68FD6C}")  # Indicates this object represents wireless network access information.
WPD_CONTENT_TYPE_MEDIA_CAST          = GUID("{5E88B3CC-3E65-4E62-BFFF-229495253AB0}")  # Indicates this object represents a media cast. A media cast object can be though of as a container object that groups related content, similar to how a playlist groups songs to play. Often, a media cast object is used to group media content originally published online.
WPD_CONTENT_TYPE_SECTION             = GUID("{821089F5-1D91-4DC9-BE3C-BBB1B35B18CE}")  # Indicates this object describes a section of data contained in another object. The WPD_OBJECT_REFERENCES property indicates which object contains the actual data.
WPD_CONTENT_TYPE_UNSPECIFIED         = GUID("{28D8D31E-249C-454E-AABC-34883168E634}")  # Indicates this object doesn't fall into the predefined WPD content types
WPD_CONTENT_TYPE_ALL                 = GUID("{80E170D2-1055-4A3E-B952-82CC4F8A8689}")  # This content type is only valid as a parameter to API functions and driver commands. It should not be reported as a supported content type by the driver.

#############################################################################
# This section defines all WPD Functional Categories
#############################################################################
WPD_FUNCTIONAL_CATEGORY_DEVICE                = GUID("{08EA466B-E3A4-4336-A1F3-A44D2B5C438C}")  # Used for the device object, which is always the top-most object of the device. 
WPD_FUNCTIONAL_CATEGORY_STORAGE               = GUID("{23F05BBC-15DE-4C2A-A55B-A9AF5CE412EF}")  # Indicates this object encapsulates storage functionality on the device (e.g. memory cards, internal memory) 
WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE   = GUID("{613CA327-AB93-4900-B4FA-895BB5874B79}")  # Indicates this object encapsulates still image capture functionality on the device (e.g. camera or camera attachment) 
WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE         = GUID("{3F2A1919-C7C2-4A00-855D-F57CF06DEBBB}")  # Indicates this object encapsulates audio capture functionality on the device (e.g. voice recorder or other audio recording component) 
WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE         = GUID("{E23E5F6B-7243-43AA-8DF1-0EB3D968A918}")  # Indicates this object encapsulates video capture functionality on the device (e.g. video recorder or video recording component) 
WPD_FUNCTIONAL_CATEGORY_SMS                   = GUID("{0044A0B1-C1E9-4AFD-B358-A62C6117C9CF}")  # Indicates this object encapsulates SMS sending functionality on the device (not the receiving or saved SMS messages since those are represented as content objects on the device) 
WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION = GUID("{08600BA4-A7BA-4A01-AB0E-0065D0A356D3}")  # Indicates this object provides information about the rendering characteristics of the device. 
WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION = GUID("{48F4DB72-7C6A-4AB0-9E1A-470E3CDBF26A}")  # Indicates this object encapsulates network configuration functionality on the device (e.g. WiFi Profiles, Partnerships). 
WPD_FUNCTIONAL_CATEGORY_ALL                   = GUID("{2D8A6512-A74C-448E-BA8A-F4AC07C49399}")  # This functional category is only valid as a parameter to API functions and driver commands. It should not be reported as a supported functional category by the driver. 

#############################################################################
# This section defines all WPD Formats
#############################################################################
WPD_OBJECT_FORMAT_ICON                = GUID("{077232ED-102C-4638-9C22-83F142BFC822}")  # Standard Windows ICON format 
WPD_OBJECT_FORMAT_M4A                 = GUID("{30ABA7AC-6FFD-4C23-A359-3E9B52F3F1C8}")  # Audio file format 
WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION = GUID("{B1020000-AE6C-4804-98BA-C57B46965FE7}")  # Network Association file format. 
WPD_OBJECT_FORMAT_X509V3CERTIFICATE   = GUID("{B1030000-AE6C-4804-98BA-C57B46965FE7}")  # X.509 V3 Certificate file format. 
WPD_OBJECT_FORMAT_MICROSOFT_WFC       = GUID("{B1040000-AE6C-4804-98BA-C57B46965FE7}")  # Windows Connect Now file format. 
WPD_OBJECT_FORMAT_3GPA                = GUID("{E5172730-F971-41EF-A10B-2271A0019D7A}")  # Audio file format 
WPD_OBJECT_FORMAT_3G2A                = GUID("{1A11202D-8759-4E34-BA5E-B1211087EEE4}")  # Audio file format 
WPD_OBJECT_FORMAT_ALL                 = GUID("{C1F62EB2-4BB3-479C-9CFA-05B5F3A57B22}")  # This format is only valid as a parameter to API functions and driver commands. It should not be reported as a supported format by the driver. 

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_NULL 
#
# This category is used exclusively for the NULL property key define.
#############################################################################
WPD_CATEGORY_NULL = GUID("{00000000-0000-0000-0000-000000000000}")
WPD_PROPERTY_NULL = _PropertyKey.create(GUID("{00000000-0000-0000-0000-000000000000}"), 0)  # [ VT_EMPTY ] A NULL property key.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_OBJECT_PROPERTIES_V1 
#
# This category is for all common object properties.
#############################################################################
WPD_OBJECT_PROPERTIES_V1 = GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}")
WPD_OBJECT_CONTENT_TYPE                     = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1,  7)  # [ VT_CLSID ] The abstract type for the object content, indicating the kinds of properties and data that may be supported on the object.
WPD_OBJECT_REFERENCES                       = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 14)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR indicating a list of ObjectIDs.
WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID   = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 23)  # [ VT_LPWSTR ] Indicates the Object ID of the closest functional object ancestor. For example, objects that represent files/folders under a Storage functional object, will have this property set to the object ID of the storage functional object.
WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 24)  # [ VT_BOOL ] Indicates whether the thumbnail for this object should be generated from the default resource.
WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME       = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 25)  # [ VT_LPWSTR ] If this object appears as a hint location, this property indicates the hint-specific name to display instead of the object name.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_OBJECT_PROPERTIES_V2 
#
# This category is for all common object properties.
#############################################################################
WPD_OBJECT_PROPERTIES_V2 = GUID("{0373CD3D-4A46-40D7-B4D8-73E8DA74E775}")
WPD_OBJECT_SUPPORTED_UNITS = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V2, 2)  # [ VT_UI4 ] Indicates the units supported on this object.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all functional objects.
#############################################################################
WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1 = GUID("{8F052D93-ABCA-4FC5-A5AC-B01DF4DBE598}")
WPD_FUNCTIONAL_OBJECT_CATEGORY = _PropertyKey.create(WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1, 2)  # [ VT_CLSID ] Indicates the object's functional category.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_STORAGE_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all objects whose functional category is WPD_FUNCTIONAL_CATEGORY_STORAGE.
#############################################################################
WPD_STORAGE_OBJECT_PROPERTIES_V1 = GUID("{01A3057A-74D6-4E80-BEA7-DC4C212CE50A}")
WPD_STORAGE_TYPE                  = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  2)  # [ VT_UI4 ] Indicates the type of storage e.g. fixed, removable etc.
WPD_STORAGE_FILE_SYSTEM_TYPE      = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  3)  # [ VT_LPWSTR ] Indicates the file system type e.g. "FAT32" or "NTFS" or "My Special File System"
WPD_STORAGE_CAPACITY              = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  4)  # [ VT_UI8 ] Indicates the total storage capacity in bytes.
WPD_STORAGE_FREE_SPACE_IN_BYTES   = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  5)  # [ VT_UI8 ] Indicates the available space in bytes.
WPD_STORAGE_FREE_SPACE_IN_OBJECTS = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  6)  # [ VT_UI8 ] Indicates the available space in objects e.g. available slots on a SIM card.
WPD_STORAGE_DESCRIPTION           = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  7)  # [ VT_LPWSTR ] Contains a description of the storage.
WPD_STORAGE_SERIAL_NUMBER         = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  8)  # [ VT_LPWSTR ] Contains the serial number of the storage.
WPD_STORAGE_MAX_OBJECT_SIZE       = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1,  9)  # [ VT_UI8 ] Specifies the maximum size of a single object (in bytes) that can be placed on this storage.
WPD_STORAGE_CAPACITY_IN_OBJECTS   = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1, 10)  # [ VT_UI8 ] Indicates the total storage capacity in objects e.g. available slots on a SIM card.
WPD_STORAGE_ACCESS_CAPABILITY     = _PropertyKey.create(WPD_STORAGE_OBJECT_PROPERTIES_V1, 11)  # [ VT_UI4 ] This property identifies any write-protection that globally affects this storage. This takes precedence over access specified on individual objects.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_NETWORK_ASSOCIATION_PROPERTIES_V1 
#
# This category is for properties common to all network association objects.
#############################################################################
WPD_NETWORK_ASSOCIATION_PROPERTIES_V1 = GUID("{E4C93C1F-B203-43F1-A100-5A07D11B0274}")
WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS = _PropertyKey.create(WPD_NETWORK_ASSOCIATION_PROPERTIES_V1, 2)  # [ VT_VECTOR | VT_UI1 ] The list of EUI-64 host identifiers valid for this association.
WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE           = _PropertyKey.create(WPD_NETWORK_ASSOCIATION_PROPERTIES_V1, 3)  # [ VT_VECTOR | VT_UI1 ] The sequence of X.509 v3 certificates to be provided for TLS server authentication.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all objects whose functional category is WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE
#############################################################################
WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1 = GUID("{58C571EC-1BCB-42A7-8AC5-BB291573A260}")
WPD_STILL_IMAGE_CAPTURE_RESOLUTION         = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Controls the size of the image dimensions to capture in pixel width and height.
WPD_STILL_IMAGE_CAPTURE_FORMAT             = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  3)  # [ VT_CLSID ] Controls the format of the image to capture.
WPD_STILL_IMAGE_COMPRESSION_SETTING        = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  4)  # [ VT_UI8 ] Controls the device-specific quality setting.
WPD_STILL_IMAGE_WHITE_BALANCE              = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  5)  # [ VT_UI4 ] Controls how the device weights color channels.
WPD_STILL_IMAGE_RGB_GAIN                   = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  6)  # [ VT_LPWSTR ] Controls the RGB gain.
WPD_STILL_IMAGE_FNUMBER                    = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  7)  # [ VT_UI4 ] Controls the aperture of the lens.
WPD_STILL_IMAGE_FOCAL_LENGTH               = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  8)  # [ VT_UI4 ] Controls the 35mm equivalent focal length.
WPD_STILL_IMAGE_FOCUS_DISTANCE             = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1,  9)  # [ VT_UI4 ] This property corresponds to the focus distance in millimeters
WPD_STILL_IMAGE_FOCUS_MODE                 = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 10)  # [ VT_UI4 ] Identifies the focusing mode used by the device for image capture.
WPD_STILL_IMAGE_EXPOSURE_METERING_MODE     = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 11)  # [ VT_UI4 ] Identifies the exposure metering mode used by the device for image capture.
WPD_STILL_IMAGE_FLASH_MODE                 = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 12)  # [ VT_UI4 ]
WPD_STILL_IMAGE_EXPOSURE_TIME              = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 13)  # [ VT_UI4 ] Controls the shutter speed of the device.
WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE      = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 14)  # [ VT_UI4 ] Controls the exposure program mode of the device.
WPD_STILL_IMAGE_EXPOSURE_INDEX             = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 15)  # [ VT_UI4 ] Controls the emulation of film speed settings.
WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 16)  # [ VT_I4 ] Controls the adjustment of the auto exposure control.
WPD_STILL_IMAGE_CAPTURE_DELAY              = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 17)  # [ VT_UI4 ] Controls the amount of time delay between the capture trigger and the actual data capture (in milliseconds).
WPD_STILL_IMAGE_CAPTURE_MODE               = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 18)  # [ VT_UI4 ] Controls the type of still image capture.
WPD_STILL_IMAGE_CONTRAST                   = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 19)  # [ VT_UI4 ] Controls the perceived contrast of captured images.
WPD_STILL_IMAGE_SHARPNESS                  = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 20)  # [ VT_UI4 ] Controls the perceived sharpness of the captured image.
WPD_STILL_IMAGE_DIGITAL_ZOOM               = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 21)  # [ VT_UI4 ] Controls the effective zoom ratio of a digital camera's acquired image scaled by a factor of 10.
WPD_STILL_IMAGE_EFFECT_MODE                = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 22)  # [ VT_UI4 ] Controls the special effect mode of the capture.
WPD_STILL_IMAGE_BURST_NUMBER               = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 23)  # [ VT_UI4 ] Controls the number of images that the device will attempt to capture upon initiation of a burst operation.
WPD_STILL_IMAGE_BURST_INTERVAL             = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 24)  # [ VT_UI4 ] Controls the time delay between captures upon initiation of a burst operation.
WPD_STILL_IMAGE_TIMELAPSE_NUMBER           = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 25)  # [ VT_UI4 ] Controls the number of images that the device will attempt to capture upon initiation of a time-lapse capture.
WPD_STILL_IMAGE_TIMELAPSE_INTERVAL         = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 26)  # [ VT_UI4 ] Controls the time delay between captures upon initiation of a time-lapse operation.
WPD_STILL_IMAGE_FOCUS_METERING_MODE        = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 27)  # [ VT_UI4 ] Controls which automatic focus mechanism is used by the device.
WPD_STILL_IMAGE_UPLOAD_URL                 = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 28)  # [ VT_LPWSTR ] Used to describe the URL that the device may use to upload images upon capture.
WPD_STILL_IMAGE_ARTIST                     = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 29)  # [ VT_LPWSTR ] Contains the owner/user of the device, which may be inserted as meta-data into any images that are captured.
WPD_STILL_IMAGE_CAMERA_MODEL               = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 30)  # [ VT_LPWSTR ] Contains the model of the device
WPD_STILL_IMAGE_CAMERA_MANUFACTURER        = _PropertyKey.create(WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1, 31)  # [ VT_LPWSTR ] Contains the manufacturer of the device

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all objects whose functional category is WPD_FUNCTIONAL_CATEGORY_AUDIO_RENDERING_INFORMATION
#############################################################################
WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1 = GUID("{C53D039F-EE23-4A31-8590-7639879870B4}")
WPD_RENDERING_INFORMATION_PROFILES                          = _PropertyKey.create(WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1, 2)  # [ VT_UNKNOWN ] IPortableDeviceValuesCollection, where each element indicates the property settings for a supported profile.
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE                = _PropertyKey.create(WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1, 3)  # [ VT_UI4 ] Indicates whether a given entry (i.e. an IPortableDeviceValues) in WPD_RENDERING_INFORMATION_PROFILES relates to an Object or a Resource.
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES = _PropertyKey.create(WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1, 4)  # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection identifying the resources that can be created on an object with this rendering profile.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CLIENT_INFORMATION_PROPERTIES_V1 
#
# 
#############################################################################
WPD_CLIENT_INFORMATION_PROPERTIES_V1 = GUID("{204D9F0C-2292-4080-9F42-40664E70F859}")
WPD_CLIENT_NAME                          = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Specifies the name the client uses to identify itself.
WPD_CLIENT_MAJOR_VERSION                 = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  3)  # [ VT_UI4 ] Specifies the major version of the client.
WPD_CLIENT_MINOR_VERSION                 = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  4)  # [ VT_UI4 ] Specifies the major version of the client.
WPD_CLIENT_REVISION                      = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  5)  # [ VT_UI4 ] Specifies the revision (or build number) of the client.
WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  6)  # [ VT_VECTOR | VT_UI1 ] Specifies the Windows Media DRM application private key of the client.
WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  7)  # [ VT_VECTOR | VT_UI1 ] Specifies the Windows Media DRM application certificate of the client.
WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE   = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  8)  # [ VT_UI4 ] Specifies the Security Quality of Service for the connection to the driver. This relates to the Security Quality of Service flags for CreateFile. For example, these allow or disallow a driver to impersonate the client.
WPD_CLIENT_DESIRED_ACCESS                = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1,  9)  # [ VT_UI4 ] Specifies the desired access the client is requesting to this driver. The possible values are the same as for CreateFile (e.g. GENERIC_READ, GENERIC_WRITE etc.).
WPD_CLIENT_SHARE_MODE                    = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1, 10)  # [ VT_UI4 ] Specifies the share mode the client is requesting to this driver. The possible values are the same as for CreateFile (e.g. FILE_SHARE_READ, FILE_SHARE_WRITE etc.).
WPD_CLIENT_EVENT_COOKIE                  = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1, 11)  # [ VT_LPWSTR ] Client supplied cookie returned by the driver in events posted as a direct result of operations issued by this client.
WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE   = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1, 12)  # [ VT_UI4 ] Specifies the minimum buffer size (in bytes) used for sending commands to the driver.
WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT    = _PropertyKey.create(WPD_CLIENT_INFORMATION_PROPERTIES_V1, 13)  # [ VT_BOOL ] An advanced option for clients that wish to manually call IPortableDevice::Close or IPortableDeviceService::Close for each object on device disconnect, instead of relying on the API to call Close on its behalf.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_PROPERTY_ATTRIBUTES_V1 
#
# 
#############################################################################
WPD_PROPERTY_ATTRIBUTES_V1 = GUID("{AB7943D8-6332-445F-A00D-8D5EF1E96F37}")
WPD_PROPERTY_ATTRIBUTE_FORM                 = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  2)  # [ VT_UI4 ] Specifies the form of the valid values allowed for this property.
WPD_PROPERTY_ATTRIBUTE_CAN_READ             = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  3)  # [ VT_BOOL ] Indicates whether client applications have permission to Read the property.
WPD_PROPERTY_ATTRIBUTE_CAN_WRITE            = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  4)  # [ VT_BOOL ] Indicates whether client applications have permission to Write the property.
WPD_PROPERTY_ATTRIBUTE_CAN_DELETE           = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  5)  # [ VT_BOOL ] Indicates whether client applications have permission to Delete the property.
WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE        = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  6)  # [ VT_XXXX ] Specifies the default value for a write-able property.
WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY        = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  7)  # [ VT_BOOL ] If True, then this property belongs to the PORTABLE_DEVICE_FAST_PROPERTIES group.
WPD_PROPERTY_ATTRIBUTE_RANGE_MIN            = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  8)  # [ VT_XXXX ] The minimum value for a property whose form is of WPD_PROPERTY_ATTRIBUTE_FORM_RANGE.
WPD_PROPERTY_ATTRIBUTE_RANGE_MAX            = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1,  9)  # [ VT_XXXX ] The maximum value for a property whose form is of WPD_PROPERTY_ATTRIBUTE_FORM_RANGE.
WPD_PROPERTY_ATTRIBUTE_RANGE_STEP           = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1, 10)  # [ VT_XXXX ] The step value for a property whose form is of WPD_PROPERTY_ATTRIBUTE_FORM_RANGE.
WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1, 11)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection containing the enumeration values.
WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION   = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1, 12)  # [ VT_LPWSTR ] A regular expression string indicating acceptable values for properties whose form is WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION.
WPD_PROPERTY_ATTRIBUTE_MAX_SIZE             = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V1, 13)  # [ VT_UI8 ] This indicates the maximum size (in bytes) for the value of this property.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_PROPERTY_ATTRIBUTES_V2 
#
# This category defines additional property attributes used by device services.
#############################################################################
WPD_PROPERTY_ATTRIBUTES_V2 = GUID("{5D9DA160-74AE-43CC-85A9-FE555A80798E}")
WPD_PROPERTY_ATTRIBUTE_NAME    = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V2,  2)  # [ VT_LPWSTR ] Contains the name of the property.
WPD_PROPERTY_ATTRIBUTE_VARTYPE = _PropertyKey.create(WPD_PROPERTY_ATTRIBUTES_V2,  3)  # [ VT_UI4 ] Contains the VARTYPE of the property.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CLASS_EXTENSION_OPTIONS_V1 
#
# This category of properties relates to options used for the WPD device class extension
#############################################################################
WPD_CLASS_EXTENSION_OPTIONS_V1 = GUID("{6309FFEF-A87C-4CA7-8434-797576E40A96}")
WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES               = _PropertyKey.create(WPD_CLASS_EXTENSION_OPTIONS_V1, 2)  # [ VT_UNKNOWN ] Indicates the (super-set) list of content types supported by the driver (similar to calling WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES on WPD_FUNCTIONAL_CATEGORY_ALL).
WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE    = _PropertyKey.create(WPD_CLASS_EXTENSION_OPTIONS_V1, 3)  # [ VT_BOOL ] Indicates that the caller does not want the WPD class extension library to register the WPD Device Class interface. The caller will take responsibility for doing it.
WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE = _PropertyKey.create(WPD_CLASS_EXTENSION_OPTIONS_V1, 4)  # [ VT_BOOL ] Indicates that the caller wants the WPD class extension library to register the private WPD Device Class interface.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CLASS_EXTENSION_OPTIONS_V2 
#
# This category of properties relates to options used for the WPD device class extension
#############################################################################
WPD_CLASS_EXTENSION_OPTIONS_V2 = GUID("{3E3595DA-4D71-49FE-A0B4-D4406C3AE93F}")
WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE          = _PropertyKey.create(WPD_CLASS_EXTENSION_OPTIONS_V2, 2)  # [ VT_BOOL ] Indicates that the caller wants the WPD class extension library to go into Multi-Transport mode (if TRUE).
WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES = _PropertyKey.create(WPD_CLASS_EXTENSION_OPTIONS_V2, 3)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the device identification values (WPD_DEVICE_MANUFACTURER, WPD_DEVICE_MODEL, WPD_DEVICE_FIRMWARE_VERSION and WPD_DEVICE_FUNCTIONAL_UNIQUE_ID). Include this with other Class Extension options when initializing.
WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH          = _PropertyKey.create(WPD_CLASS_EXTENSION_OPTIONS_V2, 4)  # [ VT_UI4 ] Indicates the theoretical maximum bandwidth of the transport in kilobits per second.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CLASS_EXTENSION_OPTIONS_V3 
#
# This category of properties relates to options used for the WPD device class extension
#############################################################################
WPD_CLASS_EXTENSION_OPTIONS_V3 = GUID("{65C160F8-1367-4CE2-939D-8310839F0D30}")
WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY = _PropertyKey.create(WPD_CLASS_EXTENSION_OPTIONS_V3, 2)  # [ VT_BOOL ] Indicates that the caller wants Autoplay to be silent when the device is connected (if TRUE).

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_RESOURCE_ATTRIBUTES_V1 
#
# 
#############################################################################
WPD_RESOURCE_ATTRIBUTES_V1 = GUID("{1EB6F604-9278-429F-93CC-5BB8C06656B6}")
WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE                = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 2)  # [ VT_UI8 ] Total size in bytes of the resource data.
WPD_RESOURCE_ATTRIBUTE_CAN_READ                  = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 3)  # [ VT_BOOL ] Indicates whether client applications have permission to open the resource for Read access.
WPD_RESOURCE_ATTRIBUTE_CAN_WRITE                 = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 4)  # [ VT_BOOL ] Indicates whether client applications have permission to open the resource for Write access.
WPD_RESOURCE_ATTRIBUTE_CAN_DELETE                = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 5)  # [ VT_BOOL ] Indicates whether client applications have permission to Delete a resource from the device.
WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE  = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 6)  # [ VT_UI4 ] The recommended buffer size a caller should use when doing buffered reads on the resource.
WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 7)  # [ VT_UI4 ] The recommended buffer size a caller should use when doing buffered writes on the resource.
WPD_RESOURCE_ATTRIBUTE_FORMAT                    = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 8)  # [ VT_CLSID ] Indicates the format of the resource data.
WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY              = _PropertyKey.create(WPD_RESOURCE_ATTRIBUTES_V1, 9)  # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection containing a single value, which is the key identifying the resource.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_DEVICE_PROPERTIES_V1 
#
# 
#############################################################################
WPD_DEVICE_PROPERTIES_V1 = GUID("{26D4979A-E643-4626-9E2B-736DC0C92FDC}")
WPD_DEVICE_SYNC_PARTNER                  = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Indicates a human-readable description of a synchronization partner for the device.
WPD_DEVICE_FIRMWARE_VERSION              = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  3)  # [ VT_LPWSTR ] Indicates the firmware version for the device.
WPD_DEVICE_POWER_LEVEL                   = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  4)  # [ VT_UI4 ] Indicates the power level of the device's battery.
WPD_DEVICE_POWER_SOURCE                  = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  5)  # [ VT_UI4 ] Indicates the power source of the device e.g. whether it is battery or external.
WPD_DEVICE_PROTOCOL                      = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  6)  # [ VT_LPWSTR ] Identifies the device protocol being used.
WPD_DEVICE_MANUFACTURER                  = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  7)  # [ VT_LPWSTR ] Identifies the device manufacturer.
WPD_DEVICE_MODEL                         = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  8)  # [ VT_LPWSTR ] Identifies the device model.
WPD_DEVICE_SERIAL_NUMBER                 = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1,  9)  # [ VT_LPWSTR ] Identifies the serial number of the device.
WPD_DEVICE_SUPPORTS_NON_CONSUMABLE       = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1, 10)  # [ VT_BOOL ] Indicates whether the device supports non-consumable objects.
WPD_DEVICE_DATETIME                      = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1, 11)  # [ VT_DATE ] Represents the current date and time settings of the device.
WPD_DEVICE_FRIENDLY_NAME                 = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1, 12)  # [ VT_LPWSTR ] Represents the friendly name set by the user on the device.
WPD_DEVICE_SUPPORTED_DRM_SCHEMES         = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1, 13)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of VT_LPWSTR values indicating the Digital Rights Management schemes supported by the driver.
WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1, 14)  # [ VT_BOOL ] Indicates whether the supported formats returned from the device are in a preferred order. (First format in the list is most preferred by the device, while the last is the least preferred.)
WPD_DEVICE_TYPE                          = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1, 15)  # [ VT_UI4 ] Indicates the device type, used for representation purposes only. Functional characteristics of the device are decided through functional objects.
WPD_DEVICE_NETWORK_IDENTIFIER            = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V1, 16)  # [ VT_UI8 ] Indicates the EUI-64 network identifier of the device, used for out-of-band Network Association operations.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_DEVICE_PROPERTIES_V2 
#
# 
#############################################################################
WPD_DEVICE_PROPERTIES_V2 = GUID("{463DD662-7FC4-4291-911C-7F4C9CCA9799}")
WPD_DEVICE_FUNCTIONAL_UNIQUE_ID = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V2, 2)  # [ VT_VECTOR | VT_UI1 ] Indicates a unique 16 byte identifier common across multiple transports supported by the device.
WPD_DEVICE_MODEL_UNIQUE_ID      = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V2, 3)  # [ VT_VECTOR | VT_UI1 ] Indicates a unique 16 byte identifier for cosmetic differentiation among different models of the device.
WPD_DEVICE_TRANSPORT            = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V2, 4)  # [ VT_UI4 ] Indicates the transport type (USB, IP, Bluetooth, etc.).
WPD_DEVICE_USE_DEVICE_STAGE     = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V2, 5)  # [ VT_BOOL ] If this property exists and is set to TRUE, the device can be used with Device Stage.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_DEVICE_PROPERTIES_V3 
#
# 
#############################################################################
WPD_DEVICE_PROPERTIES_V3 = GUID("{6C2B878C-C2EC-490D-B425-D7A75E23E5ED}")
WPD_DEVICE_EDP_IDENTITY = _PropertyKey.create(WPD_DEVICE_PROPERTIES_V3, 1)  # [ VT_LPWSTR ] Represents EDP identity of the device.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_SERVICE_PROPERTIES_V1 
#
# 
#############################################################################
WPD_SERVICE_PROPERTIES_V1 = GUID("{7510698A-CB54-481C-B8DB-0D75C93F1C06}")
WPD_SERVICE_VERSION = _PropertyKey.create(WPD_SERVICE_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Indicates the implementation version of a service.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_EVENT_PROPERTIES_V1 
#
# The properties in this category are for properties that may be needed for event processing, but do not have object property equivalents (i.e. they are not exposed as object properties, but rather, used only as event parameters).
#############################################################################
WPD_EVENT_PROPERTIES_V1 = GUID("{15AB1953-F817-4FEF-A921-5676E838F6E0}")
WPD_EVENT_PARAMETER_PNP_DEVICE_ID                      = _PropertyKey.create(WPD_EVENT_PROPERTIES_V1, 2)  # [ VT_LPWSTR ] Indicates the device that originated the event.
WPD_EVENT_PARAMETER_EVENT_ID                           = _PropertyKey.create(WPD_EVENT_PROPERTIES_V1, 3)  # [ VT_CLSID ] Indicates the event sent.
WPD_EVENT_PARAMETER_OPERATION_STATE                    = _PropertyKey.create(WPD_EVENT_PROPERTIES_V1, 4)  # [ VT_UI4 ] Indicates the current state of the operation (e.g. started, running, stopped etc.).
WPD_EVENT_PARAMETER_OPERATION_PROGRESS                 = _PropertyKey.create(WPD_EVENT_PROPERTIES_V1, 5)  # [ VT_UI4 ] Indicates the progress of a currently executing operation. Value is from 0 to 100, with 100 indicating that the operation is complete.
WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID = _PropertyKey.create(WPD_EVENT_PROPERTIES_V1, 6)  # [ VT_LPWSTR ] Uniquely identifies the parent object, similar to WPD_OBJECT_PARENT_ID, but this ID will not change between sessions.
WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE             = _PropertyKey.create(WPD_EVENT_PROPERTIES_V1, 7)  # [ VT_LPWSTR ] This is the cookie handed back to a client when it requested an object creation using the IPortableDeviceContent::CreateObjectWithPropertiesAndData method.
WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED            = _PropertyKey.create(WPD_EVENT_PROPERTIES_V1, 8)  # [ VT_BOOL ] Indicates that the child hiearchy for the object has changed.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_EVENT_PROPERTIES_V2 
#
# The properties in this category are for properties that may be needed for event processing, but do not have object property equivalents (i.e. they are not exposed as object properties, but rather, used only as event parameters).
#############################################################################
WPD_EVENT_PROPERTIES_V2 = GUID("{52807B8A-4914-4323-9B9A-74F654B2B846}")
WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT = _PropertyKey.create(WPD_EVENT_PROPERTIES_V2, 2)  # [ VT_LPWSTR ] Indicates the service method invocation context.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_EVENT_OPTIONS_V1 
#
# The properties in this category describe event options.
#############################################################################
WPD_EVENT_OPTIONS_V1 = GUID("{B3D8DAD7-A361-4B83-8A48-5B02CE10713B}")
WPD_EVENT_OPTION_IS_BROADCAST_EVENT = _PropertyKey.create(WPD_EVENT_OPTIONS_V1, 2)  # [ VT_BOOL ] Indicates that the event is broadcast to all clients.
WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT  = _PropertyKey.create(WPD_EVENT_OPTIONS_V1, 3)  # [ VT_BOOL ] Indicates that the event is sent to and handled by Autoplay.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_EVENT_ATTRIBUTES_V1 
#
# The properties in this category describe event attributes.
#############################################################################
WPD_EVENT_ATTRIBUTES_V1 = GUID("{10C96578-2E81-4111-ADDE-E08CA6138F6D}")
WPD_EVENT_ATTRIBUTE_NAME       = _PropertyKey.create(WPD_EVENT_ATTRIBUTES_V1, 2)  # [ VT_LPWSTR ] Contains the name of the event.
WPD_EVENT_ATTRIBUTE_PARAMETERS = _PropertyKey.create(WPD_EVENT_ATTRIBUTES_V1, 3)  # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the event parameters.
WPD_EVENT_ATTRIBUTE_OPTIONS    = _PropertyKey.create(WPD_EVENT_ATTRIBUTES_V1, 4)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the event options.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_API_OPTIONS_V1 
#
# The properties in this category describe API options.
#############################################################################
WPD_API_OPTIONS_V1 = GUID("{10E54A3E-052D-4777-A13C-DE7614BE2BC4}")
WPD_API_OPTION_USE_CLEAR_DATA_STREAM = _PropertyKey.create(WPD_API_OPTIONS_V1, 2)  # [ VT_BOOL ] Indicates that the data stream created for data transfer will be clear only (i.e. No DRM will be involved).
WPD_API_OPTION_IOCTL_ACCESS          = _PropertyKey.create(WPD_API_OPTIONS_V1, 3)  # [ VT_UI4 ] An optional property that clients can add to the IN parameter set of IPortableDevice::SendCommand to specify the access required for the command. The Portable Device API uses this to identify whether the IOCTL sent to the driver is sent with FILE_READ_ACCESS or (FILE_READ_ACCESS | FILE_WRITE_ACCESS) access flags.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_FORMAT_ATTRIBUTES_V1 
#
# The properties in this category describe format attributes.
#############################################################################
WPD_FORMAT_ATTRIBUTES_V1 = GUID("{A0A02000-BCAF-4BE8-B3F5-233F231CF58F}")
WPD_FORMAT_ATTRIBUTE_NAME     = _PropertyKey.create(WPD_FORMAT_ATTRIBUTES_V1, 2)  # [ VT_LPWSTR ] Contains the name of the format.
WPD_FORMAT_ATTRIBUTE_MIMETYPE = _PropertyKey.create(WPD_FORMAT_ATTRIBUTES_V1, 3)  # [ VT_LPWSTR ] Contains the MIME type of the format.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_METHOD_ATTRIBUTES_V1 
#
# The properties in this category describe method attributes.
#############################################################################
WPD_METHOD_ATTRIBUTES_V1 = GUID("{F17A5071-F039-44AF-8EFE-432CF32E432A}")
WPD_METHOD_ATTRIBUTE_NAME              = _PropertyKey.create(WPD_METHOD_ATTRIBUTES_V1, 2)  # [ VT_LPWSTR ] Contains the name of the method.
WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT = _PropertyKey.create(WPD_METHOD_ATTRIBUTES_V1, 3)  # [ VT_CLSID ] Contains the format this method applies to. This is GUID_NULL if the method does not apply to a format.
WPD_METHOD_ATTRIBUTE_ACCESS            = _PropertyKey.create(WPD_METHOD_ATTRIBUTES_V1, 4)  # [ VT_UI4 ] Indicates the required access for a method.
WPD_METHOD_ATTRIBUTE_PARAMETERS        = _PropertyKey.create(WPD_METHOD_ATTRIBUTES_V1, 5)  # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection containing the method parameters.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_PARAMETER_ATTRIBUTES_V1 
#
# The properties in this category describe parameter attributes.
#############################################################################
WPD_PARAMETER_ATTRIBUTES_V1 = GUID("{E6864DD7-F325-45EA-A1D5-97CF73B6CA58}")
WPD_PARAMETER_ATTRIBUTE_ORDER                = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  2)  # [ VT_UI4 ] The order (starting from 0) of a method parameter.
WPD_PARAMETER_ATTRIBUTE_USAGE                = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  3)  # [ VT_UI4 ] The usage of the method parameter.
WPD_PARAMETER_ATTRIBUTE_FORM                 = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  4)  # [ VT_UI4 ] Specifies the form of the valid values allowed for this parameter.
WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE        = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  5)  # [ VT_XXXX ] Specifies the default value for this parameter.
WPD_PARAMETER_ATTRIBUTE_RANGE_MIN            = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  6)  # [ VT_XXXX ] The minimum value for a parameter whose form is of WPD_PARAMETER_ATTRIBUTE_FORM_RANGE.
WPD_PARAMETER_ATTRIBUTE_RANGE_MAX            = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  7)  # [ VT_XXXX ] The maximum value for a parameter whose form is of WPD_PARAMETER_ATTRIBUTE_FORM_RANGE.
WPD_PARAMETER_ATTRIBUTE_RANGE_STEP           = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  8)  # [ VT_XXXX ] The step value for a parameter whose form is of WPD_PARAMETER_ATTRIBUTE_FORM_RANGE.
WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1,  9)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection containing the enumeration values.
WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION   = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1, 10)  # [ VT_LPWSTR ] A regular expression string indicating acceptable values for parameters whose form is WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION.
WPD_PARAMETER_ATTRIBUTE_MAX_SIZE             = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1, 11)  # [ VT_UI8 ] This indicates the maximum size (in bytes) for the value of this parameter.
WPD_PARAMETER_ATTRIBUTE_VARTYPE              = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1, 12)  # [ VT_UI4 ] Contains the VARTYPE of the parameter.
WPD_PARAMETER_ATTRIBUTE_NAME                 = _PropertyKey.create(WPD_PARAMETER_ATTRIBUTES_V1, 13)  # [ VT_LPWSTR ] Contains the parameter name.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_COMMON 
#
# 
#############################################################################
WPD_CATEGORY_COMMON = GUID("{F0422A9C-5DC8-4440-B5BD-5DF28835658A}")
WPD_COMMAND_COMMON_RESET_DEVICE                              = _PropertyKey.create(WPD_CATEGORY_COMMON,    2)  # This command is sent by clients to reset the device.
WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS = _PropertyKey.create(WPD_CATEGORY_COMMON,    3)  # This command is sent when a client wants to get current ObjectIDs representing objects specified by previously acquired Persistent Unique IDs.
WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION                   = _PropertyKey.create(WPD_CATEGORY_COMMON,    4)  # This command is sent when a client first connects to a device.
WPD_PROPERTY_COMMON_COMMAND_CATEGORY                         = _PropertyKey.create(WPD_CATEGORY_COMMON, 1001)  # [ VT_CLSID ] Specifies the command Category (i.e. the GUID portion of the _PropertyKey indicating the command).
WPD_PROPERTY_COMMON_COMMAND_ID                               = _PropertyKey.create(WPD_CATEGORY_COMMON, 1002)  # [ VT_UI4 ] Specifies the command ID, which is the PID portion of the _PropertyKey indicating the command.
WPD_PROPERTY_COMMON_HRESULT                                  = _PropertyKey.create(WPD_CATEGORY_COMMON, 1003)  # [ VT_ERROR ] The driver sets this to be the HRESULT of the requested operation.
WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE                        = _PropertyKey.create(WPD_CATEGORY_COMMON, 1004)  # [ VT_UI4 ] Special driver specific code which driver may return on error. Typically only for use with diagnostic tools or vertical solutions.
WPD_PROPERTY_COMMON_COMMAND_TARGET                           = _PropertyKey.create(WPD_CATEGORY_COMMON, 1006)  # [ VT_LPWSTR ] Identifies the object which the command is intended for.
WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS                    = _PropertyKey.create(WPD_CATEGORY_COMMON, 1007)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR specifying list of Persistent Unique IDs.
WPD_PROPERTY_COMMON_OBJECT_IDS                               = _PropertyKey.create(WPD_CATEGORY_COMMON, 1008)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR specifying list of Objects IDs.
WPD_PROPERTY_COMMON_CLIENT_INFORMATION                       = _PropertyKey.create(WPD_CATEGORY_COMMON, 1009)  # [ VT_UNKNOWN ] IPortableDeviceValues used to identify itself to the driver.
WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT               = _PropertyKey.create(WPD_CATEGORY_COMMON, 1010)  # [ VT_LPWSTR ] Driver specified context which will be sent for the particular client on all subsequent operations.
WPD_PROPERTY_COMMON_ACTIVITY_ID                              = _PropertyKey.create(WPD_CATEGORY_COMMON, 1011)  # [ VT_CLSID ] An optional ActivityID set either by a client or by WPD API, when ETW tracing is enabled.
WPD_OPTION_VALID_OBJECT_IDS                                  = _PropertyKey.create(WPD_CATEGORY_COMMON, 5001)  # [ VT_UNKNOWN ]  IPortableDevicePropVariantCollection of type VT_LPWSTR specifying list of Objects IDs of the objects that support the command.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_OBJECT_ENUMERATION 
#
# The commands in this category are used for basic object enumeration.
#############################################################################
WPD_CATEGORY_OBJECT_ENUMERATION = GUID("{B7474E91-E7F8-4AD9-B400-AD1A4B58EEEC}")
WPD_COMMAND_OBJECT_ENUMERATION_START_FIND             = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION,    2)  # The driver receives this command when a client wishes to start enumeration.
WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT              = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION,    3)  # This command is used when the client requests the next batch of ObjectIDs during enumeration. Only objects that match the constraints set up in WPD_COMMAND_OBJECT_ENUMERATION_START_FIND should be returned.
WPD_COMMAND_OBJECT_ENUMERATION_END_FIND               = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION,    4)  # The driver should destroy any resources associated with this enumeration context.
WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID             = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION, 1001)  # [ VT_LPWSTR ] The ObjectID specifying the parent object where enumeration should start.
WPD_PROPERTY_OBJECT_ENUMERATION_FILTER                = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION, 1002)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which specifies the properties used to filter on. If the caller does not want filtering, then this value will not be set.
WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS            = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION, 1003)  # [ VT_UNKNOWN ] This is an IPortableDevicePropVariantCollection of ObjectIDs (of type VT_LPWSTR). If 0 objects are returned, this should be an empty collection, not NULL.
WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT               = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION, 1004)  # [ VT_LPWSTR ] This is a driver-specified identifier for the context associated with this enumeration.
WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED = _PropertyKey.create(WPD_CATEGORY_OBJECT_ENUMERATION, 1005)  # [ VT_UI4 ] The maximum number of ObjectIDs to return back to the client.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_OBJECT_PROPERTIES 
#
# This category of commands is used to perform basic property operations such as Reading/Writing values, listing supported values and so on.
#############################################################################
WPD_CATEGORY_OBJECT_PROPERTIES = GUID("{9E5582E4-0814-44E6-981A-B2998D583804}")
WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED            = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES,    2)  # This command is used when the client requests the list of properties supported by the specified object.
WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES           = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES,    3)  # This command is used when the client requests the property attributes for the specified object properties.
WPD_COMMAND_OBJECT_PROPERTIES_GET                      = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES,    4)  # This command is used when the client requests a set of property values for the specified object.
WPD_COMMAND_OBJECT_PROPERTIES_SET                      = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES,    5)  # This command is used when the client requests to write a set of property values on the specified object.
WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL                  = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES,    6)  # This command is used when the client requests all property values for the specified object.
WPD_COMMAND_OBJECT_PROPERTIES_DELETE                   = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES,    7)  # This command is sent when the caller wants to delete properties from the specified object.
WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID               = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES, 1001)  # [ VT_LPWSTR ] The ObjectID specifying the object whose properties are being queried/manipulated.
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS           = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES, 1002)  # [ VT_UNKNOWN ] An IPortableDeviceKeyCollection identifying which specific property values we are querying/manipulating.
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES     = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES, 1003)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the attributes for each property requested.
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES         = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES, 1004)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the values read. For any property whose value could not be read, the type must be set to VT_ERROR, and the 'scode' field must contain the failure HRESULT.
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS  = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES, 1005)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the result of each property write operation.
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES, 1006)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the result of each property delete operation.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_OBJECT_PROPERTIES_BULK 
#
# This category contains commands and properties for property operations across multiple objects.
#############################################################################
WPD_CATEGORY_OBJECT_PROPERTIES_BULK = GUID("{11C824DD-04CD-4E4E-8C7B-F6EFB794D84E}")
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START   = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    2)  # Initializes the operation to get the property values for all caller-specified objects.
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT    = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    3)  # Get the next set of property values.
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END     = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    4)  # Ends the bulk property operation for getting property values by object list.
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    5)  # Initializes the operation to get the property values for objects of the specified format
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT  = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    6)  # Get the next set of property values.
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END   = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    7)  # Ends the bulk property operation for getting property values by object format.
WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START   = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    8)  # Initializes the operation to set the property values for specified objects.
WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT    = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,    9)  # Set the next set of property values.
WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END     = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK,   10)  # Ends the bulk property operation for setting property values by object list.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS                       = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1001)  # [ VT_UNKNOWN ] A collection of ObjectIDs for which supported property list must be returned.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1002)  # [ VT_LPWSTR ] The driver-specified context identifying this particular bulk operation.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES                           = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1003)  # [ VT_UNKNOWN ] Contains an IPortableDeviceValuesCollection specifying the next set of IPortableDeviceValues elements.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS                    = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1004)  # [ VT_UNKNOWN ] Contains an IPortableDeviceKeyCollection specifying which properties the caller wants to return. May not exist, which indicates caller wants ALL properties.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH                            = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1005)  # [ VT_UI4 ] Contains a value specifying the hierarchical depth from the parent to include in this operation.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID                 = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1006)  # [ VT_LPWSTR ] Contains the ObjectID of the object to start the operation from.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT                    = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1007)  # [ VT_CLSID ] Specifies the object format the client is interested in.
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS                    = _PropertyKey.create(WPD_CATEGORY_OBJECT_PROPERTIES_BULK, 1008)  # [ VT_UNKNOWN ] Contains an IPortableDeviceValuesCollection specifying the set of IPortableDeviceValues elements indicating the write results for each property set.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_OBJECT_RESOURCES 
#
# The commands in this category are used for basic object resource enumeration and transfer.
#############################################################################
WPD_CATEGORY_OBJECT_RESOURCES = GUID("{B3A2B22D-A595-4108-BE0A-FC3C965F3D4A}")
WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED                 = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    2)  # This command is sent when a client wants to get the list of resources supported on a particular object.
WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES                = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    3)  # This command is used when the client requests the attributes for the specified object resource.
WPD_COMMAND_OBJECT_RESOURCES_OPEN                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    4)  # This command is sent when a client wants to use a particular resource on an object.
WPD_COMMAND_OBJECT_RESOURCES_READ                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    5)  # This command is sent when a client wants to read the next band of data from a previously opened object resource.
WPD_COMMAND_OBJECT_RESOURCES_WRITE                         = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    6)  # This command is sent when a client wants to write the next band of data to a previously opened object resource.
WPD_COMMAND_OBJECT_RESOURCES_CLOSE                         = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    7)  # This command is sent when a client is finished transferring data to a previously opened object resource.
WPD_COMMAND_OBJECT_RESOURCES_DELETE                        = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    8)  # This command is sent when the client wants to delete the data associated with the specified resources from the specified object.
WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE               = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,    9)  # This command is sent when a client wants to create a new object resource on the device.
WPD_COMMAND_OBJECT_RESOURCES_REVERT                        = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,   10)  # This command is sent when a client wants to cancel the resource creation request that is currently still in progress.
WPD_COMMAND_OBJECT_RESOURCES_SEEK                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,   11)  # This command is sent when a client wants to seek to a specific offset in the data stream.
WPD_COMMAND_OBJECT_RESOURCES_COMMIT                        = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,   12)  # This command is sent when a client wants to commit changes to a data stream.
WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS                 = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES,   13)  # This command is sent when a client wants to seek to a specific offset in the data stream using alternate units.
WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID                    = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1001)  # [ VT_LPWSTR ]
WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE                  = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1002)  # [ VT_UI4 ] Specifies the type of access the client is requesting for the resource.
WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS                = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1003)  # [ VT_UNKNOWN ]
WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES          = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1004)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the attributes for the resource requested.
WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT                      = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1005)  # [ VT_LPWSTR ] This is a driver-specified identifier for the context associated with the resource operation.
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ            = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1006)  # [ VT_UI4 ] Specifies the number of bytes the client is requesting to read.
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ               = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1007)  # [ VT_UI4 ] Specifies the number of bytes actually read from the resource.
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE           = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1008)  # [ VT_UI4 ] Specifies the number of bytes the client is requesting to write.
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN            = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1009)  # [ VT_UI4 ] Driver sets this to let caller know how many bytes were actually written.
WPD_PROPERTY_OBJECT_RESOURCES_DATA                         = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1010)  # [ VT_VECTOR | VT_UI1 ]
WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1011)  # [ VT_UI4 ] Indicates the optimal transfer buffer size (in bytes) that clients should use when reading/writing this resource.
WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET                  = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1012)  # [ VT_I8 ] Displacement to be added to the location indicated by the WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG parameter.
WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG             = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1013)  # [ VT_UI4 ] Specifies the origin of the displacement for the seek operation.
WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START          = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1014)  # [ VT_UI8 ] Value of the new seek pointer from the beginning of the data stream.
WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS               = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1015)  # [ VT_BOOL ] A Boolean value that specifies whether this resource supports operations (such as seek) using alternate units. This occurs if the driver can understand WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS.
WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS                 = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 1016)  # [ VT_UI4 ] The units for the WPD_PROPERTY_OBJECT_SEEK_OFFSET parameter and the WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START result.
WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED        = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 5002)  # [ VT_BOOL ]  Indicates whether the driver can Seek on a resource opened for Write access.
WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ        = _PropertyKey.create(WPD_CATEGORY_OBJECT_RESOURCES, 5003)  # [ VT_BOOL ]  Indicates whether the driver requires an input buffer for WPD_COMMAND_OBJECT_RESOURCES_READ. If not set, defaults to False.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_OBJECT_MANAGEMENT 
#
# The commands specified in this category are used to Create/Delete objects on the device.
#############################################################################
WPD_CATEGORY_OBJECT_MANAGEMENT = GUID("{EF1E43DD-A9ED-4341-8BCC-186192AEA089}")
WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY     = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    2)  # This command is sent when a client wants to create a new object on the device, specified only by properties.
WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    3)  # This command is sent when a client wants to create a new object on the device, specified by properties and data.
WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA                      = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    4)  # This command is sent when a client wants to write the next band of data to a newly created object or an object being updated.
WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    5)  # This command is sent when a client has finished sending all the data associated with an object creation or update request, and wishes to ensure that the object is saved to the device.
WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    6)  # This command is sent when a client wants to cancel the object creation or update request that is currently still in progress.
WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS                         = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    7)  # This command is sent when the client wishes to remove a set of objects from the device.
WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS                           = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    8)  # This command will move the specified objects to the destination folder.
WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS                           = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,    9)  # This command will copy the specified objects to the destination folder.
WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT,   10)  # This command is sent when a client wants to update the object's data and dependent properties simultaneously.
WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES                   = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1001)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which specifies the properties used to create the new object.
WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT                               = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1002)  # [ VT_LPWSTR ] This is a driver-specified identifier for the context associated with this 'create object' operation.
WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE                    = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1003)  # [ VT_UI4 ] Specifies the number of bytes the client is requesting to write.
WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN                     = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1004)  # [ VT_UI4 ] Indicates the number of bytes written for the object.
WPD_PROPERTY_OBJECT_MANAGEMENT_DATA                                  = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1005)  # [ VT_VECTOR | VT_UI1 ] Indicates binary data of the object being created on the device.
WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID                             = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1006)  # [ VT_LPWSTR ] Identifies a newly created object on the device.
WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS                        = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1007)  # [ VT_UI4 ] Indicates if the delete operation should be recursive or not.
WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE          = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1008)  # [ VT_UI4 ] Indicates the optimal transfer buffer size (in bytes) that clients should use when writing this object's data.
WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS                            = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1009)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR, containing the ObjectIDs to delete.
WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS                        = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1010)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_ERROR, where each element is the HRESULT indicating the success or failure of the operation.
WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID          = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1011)  # [ VT_LPWSTR ] Indicates the destination folder for the move operation.
WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1012)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_ERROR, where each element is the HRESULT indicating the success or failure of the operation.
WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS                          = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1013)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_ERROR, where each element is the HRESULT indicating the success or failure of the operation.
WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES                     = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1014)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the object properties to update.
WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS                         = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1015)  # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the property keys required to update this object.
WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT                         = _PropertyKey.create(WPD_CATEGORY_OBJECT_MANAGEMENT, 1016)  # [ VT_CLSID ] Indicates the object format the caller is interested in.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_CAPABILITIES 
#
# This command category is used to query capabilities of the device.
#############################################################################
WPD_CATEGORY_CAPABILITIES = GUID("{0CABEC78-6B74-41C6-9216-2639D1FCE356}")
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS              = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    2)  # Return all commands supported by this driver. This includes custom commands, if any.
WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS                 = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    3)  # Returns the supported options for the specified command.
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    4)  # This command is used by clients to query the functional categories supported by the driver.
WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS              = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    5)  # Retrieves the ObjectIDs of the objects belonging to the specified functional category.
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES         = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    6)  # Retrieves the list of content types supported by this driver for the specified functional category.
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS               = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    7)  # This command is used to query the possible formats supported by the specified content type (e.g. for image objects, the driver may choose to support JPEG and BMP files).
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES     = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    8)  # Get the list of properties that an object of the given format supports.
WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES       = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,    9)  # Returns the property attributes that are the same for all objects of the given format.
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS                = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,   10)  # Return all events supported by this driver. This includes custom events, if any.
WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS                   = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES,   11)  # Return extra information about a specified event, such as whether the event is for notification or action purposes.
WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS                 = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1001)  # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing all commands a driver supports.
WPD_PROPERTY_CAPABILITIES_COMMAND                            = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1002)  # [ VT_UNKNOWN ] Indicates the command whose options the caller is interested in.
WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS                    = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1003)  # [ VT_UNKNOWN ] Contains an IPortableDeviceValues with the relevant command options.
WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES              = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1004)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type VT_CLSID which indicates the functional categories supported by the driver.
WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY                = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1005)  # [ VT_CLSID ] The category the caller is interested in.
WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS                 = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1006)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection (of type VT_LPWSTR) containing the ObjectIDs of the functional objects who belong to the specified functional category.
WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES                      = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1007)  # [ VT_UNKNOWN ] Indicates list of content types supported for the specified functional category.
WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE                       = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1008)  # [ VT_CLSID ] Indicates the content type whose formats the caller is interested in.
WPD_PROPERTY_CAPABILITIES_FORMATS                            = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1009)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of VT_CLSID values indicating the formats supported for the specified content type.
WPD_PROPERTY_CAPABILITIES_FORMAT                             = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1010)  # [ VT_CLSID ] Specifies the format the caller is interested in.
WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS                      = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1011)  # [ VT_UNKNOWN ] An IPortableDeviceKeyCollection containing the property keys.
WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES                = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1012)  # [ VT_UNKNOWN ] An IPortableDeviceValues containing the property attributes.
WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS                   = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1013)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of VT_CLSID values containing all events a driver supports.
WPD_PROPERTY_CAPABILITIES_EVENT                              = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1014)  # [ VT_CLSID ] Indicates the event the caller is interested in.
WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS                      = _PropertyKey.create(WPD_CATEGORY_CAPABILITIES, 1015)  # [ VT_UNKNOWN ] Contains an IPortableDeviceValues with the relevant event options.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_STORAGE 
#
# This category is for commands and parameters for storage functional objects.
#############################################################################
WPD_CATEGORY_STORAGE = GUID("{D8F907A6-34CC-45FA-97FB-D007FA47EC94}")
WPD_COMMAND_STORAGE_FORMAT                 = _PropertyKey.create(WPD_CATEGORY_STORAGE,    2)  # This command will format the storage.
WPD_COMMAND_STORAGE_EJECT                  = _PropertyKey.create(WPD_CATEGORY_STORAGE,    4)  # This will eject the storage, if it is a removable store and is capable of being ejected by the device.
WPD_PROPERTY_STORAGE_OBJECT_ID             = _PropertyKey.create(WPD_CATEGORY_STORAGE, 1001)  # [ VT_LPWSTR ] Indicates the object to format, move or eject.
WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID = _PropertyKey.create(WPD_CATEGORY_STORAGE, 1002)  # [ VT_LPWSTR ] Indicates the (folder) object destination for a move operation.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_SMS 
#
# The commands in this category relate to Short-Message-Service functionality, typically exposed on mobile phones.
#############################################################################
WPD_CATEGORY_SMS = GUID("{AFC25D66-FE0D-4114-9097-970C93E920D1}")
WPD_COMMAND_SMS_SEND            = _PropertyKey.create(WPD_CATEGORY_SMS,    2)  # This command is used to initiate the sending of an SMS message.
WPD_PROPERTY_SMS_RECIPIENT      = _PropertyKey.create(WPD_CATEGORY_SMS, 1001)  # [ VT_LPWSTR ] Indicates the recipient's address.
WPD_PROPERTY_SMS_MESSAGE_TYPE   = _PropertyKey.create(WPD_CATEGORY_SMS, 1002)  # [ VT_UI4 ] Indicates whether the message is binary or text.
WPD_PROPERTY_SMS_TEXT_MESSAGE   = _PropertyKey.create(WPD_CATEGORY_SMS, 1003)  # [ VT_LPWSTR ] if WPD_PROPERTY_SMS_MESSAGE_TYPE == SMS_TEXT_MESSAGE, then this will contain the message body.
WPD_PROPERTY_SMS_BINARY_MESSAGE = _PropertyKey.create(WPD_CATEGORY_SMS, 1004)  # [ VT_VECTOR | VT_UI1 ] if WPD_PROPERTY_SMS_MESSAGE_TYPE == SMS_BINARY_MESSAGE, then this will contain the binary message body.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_STILL_IMAGE_CAPTURE 
#
# 
#############################################################################
WPD_CATEGORY_STILL_IMAGE_CAPTURE = GUID("{4FCD6982-22A2-4B05-A48B-62D38BF27B32}")
WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE = _PropertyKey.create(WPD_CATEGORY_STILL_IMAGE_CAPTURE, 2)  # Initiates a still image capture. This is processed as a single command i.e. there is no start or stop required.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_MEDIA_CAPTURE 
#
# 
#############################################################################
WPD_CATEGORY_MEDIA_CAPTURE = GUID("{59B433BA-FE44-4D8D-808C-6BCB9B0F15E8}")
WPD_COMMAND_MEDIA_CAPTURE_START = _PropertyKey.create(WPD_CATEGORY_MEDIA_CAPTURE, 2)  # Initiates a media capture operation that will only be ended by a subsequent WPD_COMMAND_MEDIA_CAPTURE_STOP command. Typically used to capture media streams such as audio and video.
WPD_COMMAND_MEDIA_CAPTURE_STOP  = _PropertyKey.create(WPD_CATEGORY_MEDIA_CAPTURE, 3)  # Ends a media capture operation started by a WPD_COMMAND_MEDIA_CAPTURE_START command. Typically used to end capture of media streams such as audio and video.
WPD_COMMAND_MEDIA_CAPTURE_PAUSE = _PropertyKey.create(WPD_CATEGORY_MEDIA_CAPTURE, 4)  # Pauses a media capture operation started by a WPD_COMMAND_MEDIA_CAPTURE_START command. Typically used to pause capture of media streams such as audio and video.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_DEVICE_HINTS 
#
# The commands in this category relate to hints that a device can provide to improve end-user experience.
#############################################################################
WPD_CATEGORY_DEVICE_HINTS = GUID("{0D5FB92B-CB46-4C4F-8343-0BC3D3F17C84}")
WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION = _PropertyKey.create(WPD_CATEGORY_DEVICE_HINTS,    2)  # This command is used to retrieve the ObjectIDs of folders that contain the specified content type.
WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE        = _PropertyKey.create(WPD_CATEGORY_DEVICE_HINTS, 1001)  # [ VT_CLSID ] Indicates the WPD content type that the caller is looking for. For example, to get the top-level folder objects that contain images, this parameter would be WPD_CONTENT_TYPE_IMAGE.
WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS   = _PropertyKey.create(WPD_CATEGORY_DEVICE_HINTS, 1002)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR indicating a list of folder ObjectIDs.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CLASS_EXTENSION_V1 
#
# The commands in this category relate to the WPD device class extension.
#############################################################################
WPD_CLASS_EXTENSION_V1 = GUID("{33FB0D11-64A3-4FAC-B4C7-3DFEAA99B051}")
WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION          = _PropertyKey.create(WPD_CLASS_EXTENSION_V1,    2)  # This command is used to update the a cache of device-specific information.
WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES        = _PropertyKey.create(WPD_CLASS_EXTENSION_V1, 1001)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the values.
WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS = _PropertyKey.create(WPD_CLASS_EXTENSION_V1, 1002)  # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the result of each value write operation.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CLASS_EXTENSION_V2 
#
# The commands in this category relate to the WPD device class extension.
#############################################################################
WPD_CLASS_EXTENSION_V2 = GUID("{7F0779B5-FA2B-4766-9CB2-F73BA30B6758}")
WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES   = _PropertyKey.create(WPD_CLASS_EXTENSION_V2,    2)  # This command is used to register a service's Plug and Play interfaces.
WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES = _PropertyKey.create(WPD_CLASS_EXTENSION_V2,    3)  # This command is used to unregister a service's Plug and Play interfaces.
WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID            = _PropertyKey.create(WPD_CLASS_EXTENSION_V2, 1001)  # [ VT_LPWSTR ] The Object ID of the service.
WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES           = _PropertyKey.create(WPD_CLASS_EXTENSION_V2, 1002)  # [ VT_UNKNOWN ] This is an IPortablePropVariantCollection of type VT_CLSID which contains the interface GUIDs that this service implements, including the service type GUID.
WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS = _PropertyKey.create(WPD_CLASS_EXTENSION_V2, 1003)  # [ VT_UNKNOWN ] This is an IPortablePropVariantCollection of type VT_ERROR, where each element is the HRESULT indicating the success or failure of the operation.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_NETWORK_CONFIGURATION 
#
# The commands in this category are used for Network Association and WiFi Configuration.
#############################################################################
WPD_CATEGORY_NETWORK_CONFIGURATION = GUID("{78F9C6FC-79B8-473C-9060-6BD23DD072C4}")
WPD_COMMAND_GENERATE_KEYPAIR         = _PropertyKey.create(WPD_CATEGORY_NETWORK_CONFIGURATION,    2)  # Initiates the generation of a public/private key pair and returns the public key.
WPD_COMMAND_COMMIT_KEYPAIR           = _PropertyKey.create(WPD_CATEGORY_NETWORK_CONFIGURATION,    3)  # Commits a public/private key pair.
WPD_COMMAND_PROCESS_WIRELESS_PROFILE = _PropertyKey.create(WPD_CATEGORY_NETWORK_CONFIGURATION,    4)  # Initiates the processing of a Wireless Profile file.
WPD_PROPERTY_PUBLIC_KEY              = _PropertyKey.create(WPD_CATEGORY_NETWORK_CONFIGURATION, 1001)

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_SERVICE_COMMON 
#
# The commands in this category relate to a device service.
#############################################################################
WPD_CATEGORY_SERVICE_COMMON = GUID("{322F071D-36EF-477F-B4B5-6F52D734BAEE}")
WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID = _PropertyKey.create(WPD_CATEGORY_SERVICE_COMMON,    2)  # This command is used to get the service object identifier.
WPD_PROPERTY_SERVICE_OBJECT_ID                   = _PropertyKey.create(WPD_CATEGORY_SERVICE_COMMON, 1001)

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_SERVICE_CAPABILITIES 
#
# The commands in this category relate to capabilities of a device service.
#############################################################################
WPD_CATEGORY_SERVICE_CAPABILITIES = GUID("{24457E74-2E9F-44F9-8C57-1D1BCB170B89}")
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS           = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    2)  # This command is used to get the methods that apply to a service.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    3)  # This command is used to get the methods that apply to a format of a service.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES           = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    4)  # This command is used to get the attributes of a method.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    5)  # This command is used to get the attributes of a parameter used in a method.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS           = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    6)  # This command is used to get formats supported by this service.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES           = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    7)  # This command is used to get attributes of a format, such as the format name.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    8)  # This command is used to get supported properties of a format.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES  = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,    9)  # This command is used to get the property attributes that are same for all objects of a given format on the service.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS            = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,   10)  # This command is used to get the supported events of the service.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES            = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,   11)  # This command is used to get the attributes of an event.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES  = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,   12)  # This command is used to get the attributes of a parameter used in an event.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES          = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,   13)  # This command is used to get the inherited services.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES   = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,   14)  # This command is used to get the resource rendering profiles for a format.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS          = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,   15)  # Return all commands supported by this driver for a service. This includes custom commands, if any.
WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS             = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES,   16)  # Returns the supported options for the specified command.
WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS              = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1001)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection (of type VT_CLSID) containing methods that apply to a service.
WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT                         = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1002)  # [ VT_CLSID ] Indicates the format the caller is interested in.
WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD                         = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1003)  # [ VT_CLSID ] Indicates the method the caller is interested in.
WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES              = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1004)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the method attributes.
WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER                      = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1005)  # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the parameter the caller is interested in.
WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES           = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1006)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the parameter attributes.
WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS                        = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1007)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection (of type VT_CLSID) containing the formats.
WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES              = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1008)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the format attributes, such as the format name and MIME Type.
WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS                  = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1009)  # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the supported property keys.
WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES            = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1010)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the property attributes.
WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS               = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1011)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection (of type VT_CLSID) containing all events supported by the service.
WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT                          = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1012)  # [ VT_CLSID ] Indicates the event the caller is interested in.
WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES               = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1013)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the event attributes.
WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE               = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1014)  # [ VT_UI4 ] Indicates the inheritance type the caller is interested in.
WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES             = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1015)  # [ VT_UNKNOWN ] Contains the list of inherited services.
WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES             = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1016)  # [ VT_UNKNOWN ] Contains the list of format rendering profiles.
WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS             = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1017)  # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing all commands a driver supports for a service.
WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND                        = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1018)  # [ VT_UNKNOWN ] Indicates the command whose options the caller is interested in.
WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS                = _PropertyKey.create(WPD_CATEGORY_SERVICE_CAPABILITIES, 1019)  # [ VT_UNKNOWN ] Contains an IPortableDeviceValues with the relevant command options.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CATEGORY_SERVICE_METHODS 
#
# The commands in this category relate to methods of a device service.
#############################################################################
WPD_CATEGORY_SERVICE_METHODS = GUID("{2D521CA8-C1B0-4268-A342-CF19321569BC}")
WPD_COMMAND_SERVICE_METHODS_START_INVOKE     = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS,    2)  # Invokes a service method.
WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE    = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS,    3)  # This command is sent when a client wants to cancel a method that is currently still in progress.
WPD_COMMAND_SERVICE_METHODS_END_INVOKE       = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS,    4)  # This command is sent in response to a WPD_EVENT_SERVICE_METHOD_COMPLETE event from the driver to retrieve the method results.
WPD_PROPERTY_SERVICE_METHOD                  = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS, 1001)  # [ VT_CLSID ] Indicates the method to invoke.
WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS, 1002)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the method parameters.
WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES    = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS, 1003)  # [ VT_UNKNOWN ] IPortableDeviceValues containing the method results.
WPD_PROPERTY_SERVICE_METHOD_CONTEXT          = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS, 1004)  # [ VT_LPWSTR ] The unique context identifying this method operation.
WPD_PROPERTY_SERVICE_METHOD_HRESULT          = _PropertyKey.create(WPD_CATEGORY_SERVICE_METHODS, 1005)  # [ VT_ERROR ] Contains the status HRESULT of this method invocation.

#############################################################################
# This section defines all Resource keys.  Resources are place-holders for
# binary data.
#
#############################################################################
WPD_RESOURCE_DEFAULT       = _PropertyKey.create(GUID("{E81E79BE-34F0-41BF-B53F-F1A06AE87842}"), 0)  # Represents the entire object's data. There can be only one default resource on an object. 
WPD_RESOURCE_CONTACT_PHOTO = _PropertyKey.create(GUID("{2C4D6803-80EA-4580-AF9A-5BE1A23EDDCB}"), 0)  # Represents the contact's photo data. 
WPD_RESOURCE_THUMBNAIL     = _PropertyKey.create(GUID("{C7C407BA-98FA-46B5-9960-23FEC124CFDE}"), 0)  # Represents the thumbnail data for an object. 
WPD_RESOURCE_ICON          = _PropertyKey.create(GUID("{F195FED8-AA28-4EE3-B153-E182DD5EDC39}"), 0)  # Represents the icon data for an object. 
WPD_RESOURCE_AUDIO_CLIP    = _PropertyKey.create(GUID("{3BC13982-85B1-48E0-95A6-8D3AD06BE117}"), 0)  # Represents an audio sample data for an object. 
WPD_RESOURCE_ALBUM_ART     = _PropertyKey.create(GUID("{F02AA354-2300-4E2D-A1B9-3B6730F7FA21}"), 0)  # Represents the album artwork this media originated from. 
WPD_RESOURCE_GENERIC       = _PropertyKey.create(GUID("{B9B9F515-BA70-4647-94DC-FA4925E95A07}"), 0)  # Represents an arbitrary binary blob associated with this object. 
WPD_RESOURCE_VIDEO_CLIP    = _PropertyKey.create(GUID("{B566EE42-6368-4290-8662-70182FB79F20}"), 0)  # Represents a video sample for an object. 
WPD_RESOURCE_BRANDING_ART  = _PropertyKey.create(GUID("{B633B1AE-6CAF-4A87-9589-22DED6DD5899}"), 0)  # Represents the product branding artwork or logo for an object. This resource is typically found on, but not limited to the device object. 


#############################################################################
# This section defines the legacy WPD definitions
#
# When WPD_SERVICES_STRICT mode is defined, these definitions are removed
# from this header file. You may find replacements or equivalents
# in the Device Services headers (for example, BridgeDeviceService.h).
#############################################################################
#ifndef WPD_SERVICES_STRICT

#############################################################################
# This section defines the legacy WPD Formats
#############################################################################
WPD_OBJECT_FORMAT_PROPERTIES_ONLY        = GUID("{30010000-AE6C-4804-98BA-C57B46965FE7}")  # This object has no data stream and is completely specified by properties only.
WPD_OBJECT_FORMAT_UNSPECIFIED            = GUID("{30000000-AE6C-4804-98BA-C57B46965FE7}")  # An undefined object format on the device (e.g. objects that can not be classified by the other defined WPD format codes)
WPD_OBJECT_FORMAT_SCRIPT                 = GUID("{30020000-AE6C-4804-98BA-C57B46965FE7}")  # A device model-specific script
WPD_OBJECT_FORMAT_EXECUTABLE             = GUID("{30030000-AE6C-4804-98BA-C57B46965FE7}")  # A device model-specific binary executable
WPD_OBJECT_FORMAT_TEXT                   = GUID("{30040000-AE6C-4804-98BA-C57B46965FE7}")  # A text file
WPD_OBJECT_FORMAT_HTML                   = GUID("{30050000-AE6C-4804-98BA-C57B46965FE7}")  # A HyperText Markup Language file (text)
WPD_OBJECT_FORMAT_DPOF                   = GUID("{30060000-AE6C-4804-98BA-C57B46965FE7}")  # A Digital Print Order File (text)
WPD_OBJECT_FORMAT_AIFF                   = GUID("{30070000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format
WPD_OBJECT_FORMAT_WAVE                   = GUID("{30080000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format
WPD_OBJECT_FORMAT_MP3                    = GUID("{30090000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format
WPD_OBJECT_FORMAT_AVI                    = GUID("{300A0000-AE6C-4804-98BA-C57B46965FE7}")  # Video file format
WPD_OBJECT_FORMAT_MPEG                   = GUID("{300B0000-AE6C-4804-98BA-C57B46965FE7}")  # Video file format
WPD_OBJECT_FORMAT_ASF                    = GUID("{300C0000-AE6C-4804-98BA-C57B46965FE7}")  # Video file format (Microsoft Advanced Streaming Format)
WPD_OBJECT_FORMAT_EXIF                   = GUID("{38010000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Exchangeable File Format), JEIDA standard
WPD_OBJECT_FORMAT_TIFFEP                 = GUID("{38020000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Tag Image File Format for Electronic Photography)
WPD_OBJECT_FORMAT_FLASHPIX               = GUID("{38030000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Structured Storage Image Format)
WPD_OBJECT_FORMAT_BMP                    = GUID("{38040000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Microsoft Windows Bitmap file)
WPD_OBJECT_FORMAT_CIFF                   = GUID("{38050000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Canon Camera Image File Format)
WPD_OBJECT_FORMAT_GIF                    = GUID("{38070000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Graphics Interchange Format)
WPD_OBJECT_FORMAT_JFIF                   = GUID("{38080000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (JPEG Interchange Format)
WPD_OBJECT_FORMAT_PCD                    = GUID("{38090000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (PhotoCD Image Pac)
WPD_OBJECT_FORMAT_PICT                   = GUID("{380A0000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Quickdraw Image Format)
WPD_OBJECT_FORMAT_PNG                    = GUID("{380B0000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Portable Network Graphics)
WPD_OBJECT_FORMAT_TIFF                   = GUID("{380D0000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Tag Image File Format)
WPD_OBJECT_FORMAT_TIFFIT                 = GUID("{380E0000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Tag Image File Format for Informational Technology) Graphic Arts
WPD_OBJECT_FORMAT_JP2                    = GUID("{380F0000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (JPEG2000 Baseline File Format)
WPD_OBJECT_FORMAT_JPX                    = GUID("{38100000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (JPEG2000 Extended File Format)
WPD_OBJECT_FORMAT_WBMP                   = GUID("{B8030000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (Wireless Application Protocol Bitmap Format)
WPD_OBJECT_FORMAT_JPEGXR                 = GUID("{B8040000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format (JPEG XR, also known as HD Photo)
WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT     = GUID("{B8810000-AE6C-4804-98BA-C57B46965FE7}")  # Image file format
WPD_OBJECT_FORMAT_WMA                    = GUID("{B9010000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format (Windows Media Audio)
WPD_OBJECT_FORMAT_WMV                    = GUID("{B9810000-AE6C-4804-98BA-C57B46965FE7}")  # Video file format (Windows Media Video)
WPD_OBJECT_FORMAT_WPLPLAYLIST            = GUID("{BA100000-AE6C-4804-98BA-C57B46965FE7}")  # Playlist file format
WPD_OBJECT_FORMAT_M3UPLAYLIST            = GUID("{BA110000-AE6C-4804-98BA-C57B46965FE7}")  # Playlist file format
WPD_OBJECT_FORMAT_MPLPLAYLIST            = GUID("{BA120000-AE6C-4804-98BA-C57B46965FE7}")  # Playlist file format
WPD_OBJECT_FORMAT_ASXPLAYLIST            = GUID("{BA130000-AE6C-4804-98BA-C57B46965FE7}")  # Playlist file format
WPD_OBJECT_FORMAT_PLSPLAYLIST            = GUID("{BA140000-AE6C-4804-98BA-C57B46965FE7}")  # Playlist file format
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP = GUID("{BA060000-AE6C-4804-98BA-C57B46965FE7}")  # Generic format for contact group objects
WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST    = GUID("{BA0B0000-AE6C-4804-98BA-C57B46965FE7}")  # MediaCast file format
WPD_OBJECT_FORMAT_VCALENDAR1             = GUID("{BE020000-AE6C-4804-98BA-C57B46965FE7}")  # VCALENDAR file format (VCALENDAR Version 1)
WPD_OBJECT_FORMAT_ICALENDAR              = GUID("{BE030000-AE6C-4804-98BA-C57B46965FE7}")  # ICALENDAR file format (VCALENDAR Version 2)
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT       = GUID("{BB810000-AE6C-4804-98BA-C57B46965FE7}")  # Abstract contact file format
WPD_OBJECT_FORMAT_VCARD2                 = GUID("{BB820000-AE6C-4804-98BA-C57B46965FE7}")  # VCARD file format (VCARD Version 2)
WPD_OBJECT_FORMAT_VCARD3                 = GUID("{BB830000-AE6C-4804-98BA-C57B46965FE7}")  # VCARD file format (VCARD Version 3)
WPD_OBJECT_FORMAT_XML                    = GUID("{BA820000-AE6C-4804-98BA-C57B46965FE7}")  # XML file format.
WPD_OBJECT_FORMAT_AAC                    = GUID("{B9030000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format
WPD_OBJECT_FORMAT_AUDIBLE                = GUID("{B9040000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format
WPD_OBJECT_FORMAT_FLAC                   = GUID("{B9060000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format
WPD_OBJECT_FORMAT_QCELP                  = GUID("{B9070000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format (Qualcomm Code Excited Linear Prediction)
WPD_OBJECT_FORMAT_AMR                    = GUID("{B9080000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format (Adaptive Multi-Rate audio codec)
WPD_OBJECT_FORMAT_OGG                    = GUID("{B9020000-AE6C-4804-98BA-C57B46965FE7}")  # Audio file format
WPD_OBJECT_FORMAT_MP4                    = GUID("{B9820000-AE6C-4804-98BA-C57B46965FE7}")  # Audio or Video file format
WPD_OBJECT_FORMAT_MP2                    = GUID("{B9830000-AE6C-4804-98BA-C57B46965FE7}")  # Audio or Video file format
WPD_OBJECT_FORMAT_MICROSOFT_WORD         = GUID("{BA830000-AE6C-4804-98BA-C57B46965FE7}")  # Microsoft Office Word Document file format.
WPD_OBJECT_FORMAT_MHT_COMPILED_HTML      = GUID("{BA840000-AE6C-4804-98BA-C57B46965FE7}")  # MHT Compiled HTML Document file format.
WPD_OBJECT_FORMAT_MICROSOFT_EXCEL        = GUID("{BA850000-AE6C-4804-98BA-C57B46965FE7}")  # Microsoft Office Excel Document file format.
WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT   = GUID("{BA860000-AE6C-4804-98BA-C57B46965FE7}")  # Microsoft Office PowerPoint Document file format.
WPD_OBJECT_FORMAT_3GP                    = GUID("{B9840000-AE6C-4804-98BA-C57B46965FE7}")  # Audio or Video file format
WPD_OBJECT_FORMAT_3G2                    = GUID("{B9850000-AE6C-4804-98BA-C57B46965FE7}")  # Audio or Video file format
WPD_OBJECT_FORMAT_AVCHD                  = GUID("{B9860000-AE6C-4804-98BA-C57B46965FE7}")  # Audio or Video file format
WPD_OBJECT_FORMAT_ATSCTS                 = GUID("{B9870000-AE6C-4804-98BA-C57B46965FE7}")  # Audio or Video file format
WPD_OBJECT_FORMAT_DVBTS                  = GUID("{B9880000-AE6C-4804-98BA-C57B46965FE7}")  # Audio or Video file format
WPD_OBJECT_FORMAT_MKV                    = GUID("{B9900000-AE6C-4804-98BA-c57B46965FE7}")  # Audio or Video file format

#############################################################################
# This section defines the legacy WPD Properties
#############################################################################
WPD_OBJECT_ID                   = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Uniquely identifies object on the Portable Device.
WPD_OBJECT_PARENT_ID            = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1,  3)  # [ VT_LPWSTR ] Object identifier indicating the parent object.
WPD_OBJECT_NAME                 = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1,  4)  # [ VT_LPWSTR ] The display name for this object.
WPD_OBJECT_PERSISTENT_UNIQUE_ID = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1,  5)  # [ VT_LPWSTR ] Uniquely identifies the object on the Portable Device, similar to WPD_OBJECT_ID, but this ID will not change between sessions.
WPD_OBJECT_FORMAT               = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1,  6)  # [ VT_CLSID ] Indicates the format of the object's data.
WPD_OBJECT_ISHIDDEN             = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1,  9)  # [ VT_BOOL ] Indicates whether the object should be hidden.
WPD_OBJECT_ISSYSTEM             = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 10)  # [ VT_BOOL ] Indicates whether the object represents system data.
WPD_OBJECT_SIZE                 = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 11)  # [ VT_UI8 ] The size of the object data.
WPD_OBJECT_ORIGINAL_FILE_NAME   = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 12)  # [ VT_LPWSTR ] Contains the name of the file this object represents.
WPD_OBJECT_NON_CONSUMABLE       = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 13)  # [ VT_BOOL ] This property determines whether or not this object is intended to be understood by the device, or whether it has been placed on the device just for storage.
WPD_OBJECT_KEYWORDS             = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 15)  # [ VT_LPWSTR ] String containing a list of keywords associated with this object.
WPD_OBJECT_SYNC_ID              = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 16)  # [ VT_LPWSTR ] Opaque string set by client to retain state between sessions without retaining a catalogue of connected device content.
WPD_OBJECT_IS_DRM_PROTECTED     = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 17)  # [ VT_BOOL ] Indicates whether the media data is DRM protected.
WPD_OBJECT_DATE_CREATED         = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 18)  # [ VT_DATE ] Indicates the date and time the object was created on the device.
WPD_OBJECT_DATE_MODIFIED        = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 19)  # [ VT_DATE ] Indicates the date and time the object was modified on the device.
WPD_OBJECT_DATE_AUTHORED        = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 20)  # [ VT_DATE ] Indicates the date and time the object was authored (e.g. for music, this would be the date the music was recorded).
WPD_OBJECT_BACK_REFERENCES      = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 21)  # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR indicating a list of ObjectIDs.
WPD_OBJECT_CAN_DELETE           = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 26)  # [ VT_BOOL ] Indicates whether the object can be deleted, or not.
WPD_OBJECT_LANGUAGE_LOCALE      = _PropertyKey.create(WPD_OBJECT_PROPERTIES_V1, 27)  # [ VT_LPWSTR ] Identifies the language of this object. If multiple languages are contained in this object, it should identify the primary language (if any).
        
#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_FOLDER_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all folder objects.
#############################################################################
WPD_FOLDER_OBJECT_PROPERTIES_V1 = GUID("{7E9A7ABF-E568-4B34-AA2F-13BB12AB177D}")
WPD_FOLDER_CONTENT_TYPES_ALLOWED = _PropertyKey.create(WPD_FOLDER_OBJECT_PROPERTIES_V1, 2)  # [ VT_UNKNOWN ] Indicates the subset of content types that can be created in this folder directly (i.e. children may have different restrictions).

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_IMAGE_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all image objects.
#############################################################################
WPD_IMAGE_OBJECT_PROPERTIES_V1 = GUID("{63D64908-9FA1-479F-85BA-9952216447DB}")
WPD_IMAGE_BITDEPTH               = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1,  3)  # [ VT_UI4 ] Indicates the bitdepth of an image
WPD_IMAGE_CROPPED_STATUS         = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1,  4)  # [ VT_UI4 ] Signals whether the file has been cropped.
WPD_IMAGE_COLOR_CORRECTED_STATUS = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1,  5)  # [ VT_UI4 ] Signals whether the file has been color corrected.
WPD_IMAGE_FNUMBER                = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1,  6)  # [ VT_UI4 ] Identifies the aperture setting of the lens when this image was captured.
WPD_IMAGE_EXPOSURE_TIME          = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1,  7)  # [ VT_UI4 ] Identifies the shutter speed of the device when this image was captured.
WPD_IMAGE_EXPOSURE_INDEX         = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1,  8)  # [ VT_UI4 ] Identifies the emulation of film speed settings when this image was captured.
WPD_IMAGE_HORIZONTAL_RESOLUTION  = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1,  9)  # [ VT_R8 ] Indicates the horizontal resolution (DPI) of an image
WPD_IMAGE_VERTICAL_RESOLUTION    = _PropertyKey.create(WPD_IMAGE_OBJECT_PROPERTIES_V1, 10)  # [ VT_R8 ] Indicates the vertical resolution (DPI) of an image

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_DOCUMENT_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all document objects.
#############################################################################
WPD_DOCUMENT_OBJECT_PROPERTIES_V1 = GUID("{0B110203-EB95-4F02-93E0-97C631493AD5}")

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_MEDIA_PROPERTIES_V1 
#
# This category is for properties common to media objects (e.g. audio and video).
#############################################################################
WPD_MEDIA_PROPERTIES_V1 = GUID("{2ED8BA05-0AD3-42DC-B0D0-BC95AC396AC8}")
WPD_MEDIA_TOTAL_BITRATE           = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  2)  # [ VT_UI4 ] The total number of bits that one second will consume.
WPD_MEDIA_BITRATE_TYPE            = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  3)  # [ VT_UI4 ] Further qualifies the bitrate of audio or video data.
WPD_MEDIA_COPYRIGHT               = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  4)  # [ VT_LPWSTR ] Indicates the copyright information.
WPD_MEDIA_SUBSCRIPTION_CONTENT_ID = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  5)  # [ VT_LPWSTR ] Provides additional information to identify a piece of content relative to an online subscription service.
WPD_MEDIA_USE_COUNT               = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  6)  # [ VT_UI4 ] Indicates the total number of times this media has been played or viewed on the device.
WPD_MEDIA_SKIP_COUNT              = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  7)  # [ VT_UI4 ] Indicates the total number of times this media was setup to be played or viewed but was manually skipped by the user.
WPD_MEDIA_LAST_ACCESSED_TIME      = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  8)  # [ VT_DATE ] Indicates the date and time the media was last accessed on the device.
WPD_MEDIA_PARENTAL_RATING         = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1,  9)  # [ VT_LPWSTR ] Indicates the parental rating of the media file.
WPD_MEDIA_META_GENRE              = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 10)  # [ VT_UI4 ] Further qualifies a piece of media in a contextual way.
WPD_MEDIA_COMPOSER                = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 11)  # [ VT_LPWSTR ] Identifies the composer when the composer is not the artist who performed it.
WPD_MEDIA_EFFECTIVE_RATING        = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 12)  # [ VT_UI4 ] Contains an assigned rating for media not set by the user, but is generated based upon usage statistics.
WPD_MEDIA_SUB_TITLE               = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 13)  # [ VT_LPWSTR ] Further qualifies the title when the title is ambiguous or general.
WPD_MEDIA_RELEASE_DATE            = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 14)  # [ VT_DATE ] Indicates when the media was released.
WPD_MEDIA_SAMPLE_RATE             = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 15)  # [ VT_UI4 ] Indicates the number of times media selection was sampled per second during encoding.
WPD_MEDIA_STAR_RATING             = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 16)  # [ VT_UI4 ] Indicates the star rating for this media.
WPD_MEDIA_USER_EFFECTIVE_RATING   = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 17)  # [ VT_UI4 ] Indicates the rating for this media.
WPD_MEDIA_TITLE                   = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 18)  # [ VT_LPWSTR ] Indicates the title of this media.
WPD_MEDIA_DURATION                = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 19)  # [ VT_UI8 ] Indicates the duration of this media in milliseconds.
WPD_MEDIA_BUY_NOW                 = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 20)  # [ VT_BOOL ] TBD
WPD_MEDIA_ENCODING_PROFILE        = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 21)  # [ VT_LPWSTR ] Media codecs may be encoded in accordance with a profile, which defines a particular encoding algorithm or optimization process.
WPD_MEDIA_WIDTH                   = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 22)  # [ VT_UI4 ] Indicates the width of an object in pixels
WPD_MEDIA_HEIGHT                  = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 23)  # [ VT_UI4 ] Indicates the height of an object in pixels
WPD_MEDIA_ARTIST                  = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 24)  # [ VT_LPWSTR ] Indicates the artist for this media.
WPD_MEDIA_ALBUM_ARTIST            = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 25)  # [ VT_LPWSTR ] Indicates the artist of the entire album rather than for a particular track.
WPD_MEDIA_OWNER                   = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 26)  # [ VT_LPWSTR ] Indicates the e-mail address of the owner for this media.
WPD_MEDIA_MANAGING_EDITOR         = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 27)  # [ VT_LPWSTR ] Indicates the e-mail address of the managing editor for this media.
WPD_MEDIA_WEBMASTER               = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 28)  # [ VT_LPWSTR ] Indicates the e-mail address of the Webmaster for this media.
WPD_MEDIA_SOURCE_URL              = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 29)  # [ VT_LPWSTR ] Identifies the source URL for this object.
WPD_MEDIA_DESTINATION_URL         = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 30)  # [ VT_LPWSTR ] Identifies the URL that an object is linked to if a user clicks on it.
WPD_MEDIA_DESCRIPTION             = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 31)  # [ VT_LPWSTR ] Contains a description of the media content for this object.
WPD_MEDIA_GENRE                   = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 32)  # [ VT_LPWSTR ] A text field indicating the genre this media belongs to.
WPD_MEDIA_TIME_BOOKMARK           = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 33)  # [ VT_UI8 ] Indicates a bookmark (in milliseconds) of the last position played or viewed on media that have duration.
WPD_MEDIA_OBJECT_BOOKMARK         = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 34)  # [ VT_LPWSTR ] Indicates a WPD_OBJECT_ID of the last object viewed or played for those objects that refer to a list of objects (such as playlists or media casts).
WPD_MEDIA_LAST_BUILD_DATE         = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 35)  # [ VT_DATE ] Indicates the last time a series in a media cast was changed or edited.
WPD_MEDIA_BYTE_BOOKMARK           = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 36)  # [ VT_UI8 ] Indicates a bookmark (as a zero-based byte offset) of the last position played or viewed on this media object.
WPD_MEDIA_TIME_TO_LIVE            = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 37)  # [ VT_UI8 ] It is the number of minutes that indicates how long a channel can be cached before refreshing from the source. Applies to WPD_CONTENT_TYPE_MEDIA_CAST objects.
WPD_MEDIA_GUID                    = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 38)  # [ VT_LPWSTR ] A text field indicating the GUID of this media.
WPD_MEDIA_SUB_DESCRIPTION         = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 39)  # [ VT_LPWSTR ] Contains a sub description of the media content for this object.
WPD_MEDIA_AUDIO_ENCODING_PROFILE  = _PropertyKey.create(WPD_MEDIA_PROPERTIES_V1, 49)  # [ VT_LPWSTR ] Media codecs may be encoded in accordance with a profile, which defines a particular encoding algorithm or optimization process.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_CONTACT_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all contact objects.
#############################################################################
WPD_CONTACT_OBJECT_PROPERTIES_V1 = GUID("{FBD4FDAB-987D-4777-B3F9-726185A9312B}")
WPD_CONTACT_DISPLAY_NAME                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Indicates the display name of the contact (e.g "John Doe")
WPD_CONTACT_FIRST_NAME                          = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  3)  # [ VT_LPWSTR ] Indicates the first name of the contact (e.g. "John")
WPD_CONTACT_MIDDLE_NAMES                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  4)  # [ VT_LPWSTR ] Indicates the middle name of the contact
WPD_CONTACT_LAST_NAME                           = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  5)  # [ VT_LPWSTR ] Indicates the last name of the contact (e.g. "Doe")
WPD_CONTACT_PREFIX                              = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  6)  # [ VT_LPWSTR ] Indicates the prefix of the name of the contact (e.g. "Mr.")
WPD_CONTACT_SUFFIX                              = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  7)  # [ VT_LPWSTR ] Indicates the suffix of the name of the contact (e.g. "Jr.")
WPD_CONTACT_PHONETIC_FIRST_NAME                 = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  8)  # [ VT_LPWSTR ] The phonetic guide for pronouncing the contact's first name.
WPD_CONTACT_PHONETIC_LAST_NAME                  = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1,  9)  # [ VT_LPWSTR ] The phonetic guide for pronouncing the contact's last name.
WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 10)  # [ VT_LPWSTR ] Indicates the full postal address of the contact (e.g. "555 Dial Drive, PhoneLand, WA 12345")
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1       = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 11)  # [ VT_LPWSTR ] Indicates the first line of a postal address of the contact (e.g. "555 Dial Drive")
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2       = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 12)  # [ VT_LPWSTR ] Indicates the second line of a postal address of the contact
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 13)  # [ VT_LPWSTR ] Indicates the city of a postal address of the contact (e.g. "PhoneLand")
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION      = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 14)  # [ VT_LPWSTR ] Indicates the region of a postal address of the contact
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 15)  # [ VT_LPWSTR ] Indicates the postal code of the address.
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY     = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 16)  # [ VT_LPWSTR ]
WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 17)  # [ VT_LPWSTR ] Indicates the full postal address of the contact (e.g. "555 Dial Drive, PhoneLand, WA 12345")
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1       = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 18)  # [ VT_LPWSTR ] Indicates the first line of a postal address of the contact (e.g. "555 Dial Drive")
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2       = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 19)  # [ VT_LPWSTR ] Indicates the second line of a postal address of the contact
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 20)  # [ VT_LPWSTR ] Indicates the city of a postal address of the contact (e.g. "PhoneLand")
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION      = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 21)  # [ VT_LPWSTR ]
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 22)  # [ VT_LPWSTR ] Indicates the postal code of the address.
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY     = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 23)  # [ VT_LPWSTR ]
WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS           = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 24)  # [ VT_LPWSTR ] Indicates the full postal address of the contact (e.g. "555 Dial Drive, PhoneLand, WA 12345").
WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1          = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 25)  # [ VT_LPWSTR ] Indicates the first line of a postal address of the contact (e.g. "555 Dial Drive").
WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2          = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 26)  # [ VT_LPWSTR ] Indicates the second line of a postal address of the contact.
WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY           = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 27)  # [ VT_LPWSTR ] Indicates the city of a postal address of the contact (e.g. "PhoneLand").
WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION         = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 28)  # [ VT_LPWSTR ] Indicates the region of a postal address of the contact.
WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE    = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 29)  # [ VT_LPWSTR ] Indicates the postal code of the address.
WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 30)  # [ VT_LPWSTR ] Indicates the country/region of the postal address.
WPD_CONTACT_PRIMARY_EMAIL_ADDRESS               = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 31)  # [ VT_LPWSTR ] Indicates the primary email address for the contact e.g. "someone@example.com"
WPD_CONTACT_PERSONAL_EMAIL                      = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 32)  # [ VT_LPWSTR ] Indicates the personal email address for the contact e.g. "someone@example.com"
WPD_CONTACT_PERSONAL_EMAIL2                     = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 33)  # [ VT_LPWSTR ] Indicates an alternate personal email address for the contact e.g. "someone@example.com"
WPD_CONTACT_BUSINESS_EMAIL                      = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 34)  # [ VT_LPWSTR ] Indicates the business email address for the contact e.g. "someone@example.com"
WPD_CONTACT_BUSINESS_EMAIL2                     = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 35)  # [ VT_LPWSTR ] Indicates an alternate business email address for the contact e.g. "someone@example.com"
WPD_CONTACT_OTHER_EMAILS                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 36)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type VT_LPWSTR, where each element is an alternate email addresses for the contact.
WPD_CONTACT_PRIMARY_PHONE                       = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 37)  # [ VT_LPWSTR ] Indicates the primary phone number for the contact.
WPD_CONTACT_PERSONAL_PHONE                      = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 38)  # [ VT_LPWSTR ] Indicates the personal phone number for the contact.
WPD_CONTACT_PERSONAL_PHONE2                     = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 39)  # [ VT_LPWSTR ] Indicates an alternate personal phone number for the contact.
WPD_CONTACT_BUSINESS_PHONE                      = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 40)  # [ VT_LPWSTR ] Indicates the business phone number for the contact.
WPD_CONTACT_BUSINESS_PHONE2                     = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 41)  # [ VT_LPWSTR ] Indicates an alternate business phone number for the contact.
WPD_CONTACT_MOBILE_PHONE                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 42)  # [ VT_LPWSTR ] Indicates the mobile phone number for the contact.
WPD_CONTACT_MOBILE_PHONE2                       = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 43)  # [ VT_LPWSTR ] Indicates an alternate mobile phone number for the contact.
WPD_CONTACT_PERSONAL_FAX                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 44)  # [ VT_LPWSTR ] Indicates the personal fax number for the contact.
WPD_CONTACT_BUSINESS_FAX                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 45)  # [ VT_LPWSTR ] Indicates the business fax number for the contact.
WPD_CONTACT_PAGER                               = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 46)  # [ VT_LPWSTR ]
WPD_CONTACT_OTHER_PHONES                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 47)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type VT_LPWSTR, where each element is an alternate phone number for the contact.
WPD_CONTACT_PRIMARY_WEB_ADDRESS                 = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 48)  # [ VT_LPWSTR ] Indicates the primary web address for the contact.
WPD_CONTACT_PERSONAL_WEB_ADDRESS                = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 49)  # [ VT_LPWSTR ] Indicates the personal web address for the contact.
WPD_CONTACT_BUSINESS_WEB_ADDRESS                = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 50)  # [ VT_LPWSTR ] Indicates the business web address for the contact.
WPD_CONTACT_INSTANT_MESSENGER                   = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 51)  # [ VT_LPWSTR ] Indicates the instant messenger address for the contact.
WPD_CONTACT_INSTANT_MESSENGER2                  = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 52)  # [ VT_LPWSTR ] Indicates an alternate instant messenger address for the contact.
WPD_CONTACT_INSTANT_MESSENGER3                  = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 53)  # [ VT_LPWSTR ] Indicates an alternate instant messenger address for the contact.
WPD_CONTACT_COMPANY_NAME                        = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 54)  # [ VT_LPWSTR ] Indicates the company name for the contact.
WPD_CONTACT_PHONETIC_COMPANY_NAME               = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 55)  # [ VT_LPWSTR ] The phonetic guide for pronouncing the contact's company name.
WPD_CONTACT_ROLE                                = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 56)  # [ VT_LPWSTR ] Indicates the role for the contact e.g. "Software Engineer".
WPD_CONTACT_BIRTHDATE                           = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 57)  # [ VT_DATE ] Indicates the birthdate for the contact.
WPD_CONTACT_PRIMARY_FAX                         = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 58)  # [ VT_LPWSTR ] Indicates the primary fax number for the contact.
WPD_CONTACT_SPOUSE                              = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 59)  # [ VT_LPWSTR ] Indicates the full name of the spouse/domestic partner for the contact.
WPD_CONTACT_CHILDREN                            = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 60)  # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type VT_LPWSTR, where each element is the full name of a child of the contact.
WPD_CONTACT_ASSISTANT                           = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 61)  # [ VT_LPWSTR ] Indicates the full name of the assistant for the contact.
WPD_CONTACT_ANNIVERSARY_DATE                    = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 62)  # [ VT_DATE ] Indicates the anniversary date for the contact.
WPD_CONTACT_RINGTONE                            = _PropertyKey.create(WPD_CONTACT_OBJECT_PROPERTIES_V1, 63)  # [ VT_LPWSTR ] Indicates an object id of a ringtone file on the device.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_MUSIC_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all music objects.
#############################################################################
WPD_MUSIC_OBJECT_PROPERTIES_V1 = GUID("{B324F56A-DC5D-46E5-B6DF-D2EA414888C6}")
WPD_MUSIC_ALBUM           = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1,  3)  # [ VT_LPWSTR ] Indicates the album of the music file.
WPD_MUSIC_TRACK           = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1,  4)  # [ VT_UI4 ] Indicates the track number for the music file.
WPD_MUSIC_LYRICS          = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1,  6)  # [ VT_LPWSTR ] Indicates the lyrics for the music file.
WPD_MUSIC_MOOD            = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1,  8)  # [ VT_LPWSTR ] Indicates the mood for the music file.
WPD_AUDIO_BITRATE         = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1,  9)  # [ VT_UI4 ] Indicates the bit rate for the audio data, specified in bits per second.
WPD_AUDIO_CHANNEL_COUNT   = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1, 10)  # [ VT_R4 ] Indicates the number of channels in this audio file e.g. 1, 2, 5.1 etc.
WPD_AUDIO_FORMAT_CODE     = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1, 11)  # [ VT_UI4 ] Indicates the registered WAVE format code.
WPD_AUDIO_BIT_DEPTH       = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1, 12)  # [ VT_UI4 ] This property identifies the bit-depth of the audio.
WPD_AUDIO_BLOCK_ALIGNMENT = _PropertyKey.create(WPD_MUSIC_OBJECT_PROPERTIES_V1, 13)  # [ VT_UI4 ] This property identifies the audio block alignment

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_VIDEO_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all video objects.
#############################################################################
WPD_VIDEO_OBJECT_PROPERTIES_V1 = GUID("{346F2163-F998-4146-8B01-D19B4C00DE9A}")
WPD_VIDEO_AUTHOR                    = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Indicates the author of the video file.
WPD_VIDEO_RECORDEDTV_STATION_NAME   = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1,  4)  # [ VT_LPWSTR ] Indicates the TV station the video was recorded from.
WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1,  5)  # [ VT_UI4 ] Indicates the TV channel number the video was recorded from.
WPD_VIDEO_RECORDEDTV_REPEAT         = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1,  7)  # [ VT_BOOL ] Indicates whether the recorded TV program was a repeat showing.
WPD_VIDEO_BUFFER_SIZE               = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1,  8)  # [ VT_UI4 ] Indicates the video buffer size.
WPD_VIDEO_CREDITS                   = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1,  9)  # [ VT_LPWSTR ] Indicates the credit text for the video file.
WPD_VIDEO_KEY_FRAME_DISTANCE        = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1, 10)  # [ VT_UI4 ] Indicates the interval between key frames in milliseconds.
WPD_VIDEO_QUALITY_SETTING           = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1, 11)  # [ VT_UI4 ] Indicates the quality setting for the video file.
WPD_VIDEO_SCAN_TYPE                 = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1, 12)  # [ VT_UI4 ] This property identifies the video scan information.
WPD_VIDEO_BITRATE                   = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1, 13)  # [ VT_UI4 ] Indicates the bitrate for the video data.
WPD_VIDEO_FOURCC_CODE               = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1, 14)  # [ VT_UI4 ] The registered FourCC code indicating the codec used for the video file.
WPD_VIDEO_FRAMERATE                 = _PropertyKey.create(WPD_VIDEO_OBJECT_PROPERTIES_V1, 15)  # [ VT_UI4 ] Indicates the frame rate for the video data.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1 
#
# This category is properties that pertain to informational objects such as appointments, tasks, memos and even documents.
#############################################################################
WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1 = GUID("{B28AE94B-05A4-4E8E-BE01-72CC7E099D8F}")
WPD_COMMON_INFORMATION_SUBJECT        = _PropertyKey.create(WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1, 2)  # [ VT_LPWSTR ] Indicates the subject field of this object.
WPD_COMMON_INFORMATION_BODY_TEXT      = _PropertyKey.create(WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1, 3)  # [ VT_LPWSTR ] This property contains the body text of an object, in plaintext or HTML format.
WPD_COMMON_INFORMATION_PRIORITY       = _PropertyKey.create(WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1, 4)  # [ VT_UI4 ] Indicates the priority of this object.
WPD_COMMON_INFORMATION_START_DATETIME = _PropertyKey.create(WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1, 5)  # [ VT_DATE ] For appointments, tasks and similar objects, this indicates the date/time that this item is scheduled to start.
WPD_COMMON_INFORMATION_END_DATETIME   = _PropertyKey.create(WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1, 6)  # [ VT_DATE ] For appointments, tasks and similar objects, this indicates the date/time that this item is scheduled to end.
WPD_COMMON_INFORMATION_NOTES          = _PropertyKey.create(WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1, 7)  # [ VT_LPWSTR ] For appointments, tasks and similar objects, this indicates any notes for this object.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_MEMO_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all memo objects.
#############################################################################
WPD_MEMO_OBJECT_PROPERTIES_V1 = GUID("{5FFBFC7B-7483-41AD-AFB9-DA3F4E592B8D}")

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_EMAIL_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all email objects.
#############################################################################
WPD_EMAIL_OBJECT_PROPERTIES_V1 = GUID("{41F8F65A-5484-4782-B13D-4740DD7C37C5}")
WPD_EMAIL_TO_LINE         = _PropertyKey.create(WPD_EMAIL_OBJECT_PROPERTIES_V1,  2)  # [ VT_LPWSTR ] Indicates the normal recipients for the message.
WPD_EMAIL_CC_LINE         = _PropertyKey.create(WPD_EMAIL_OBJECT_PROPERTIES_V1,  3)  # [ VT_LPWSTR ] Indicates the copied recipients for the message.
WPD_EMAIL_BCC_LINE        = _PropertyKey.create(WPD_EMAIL_OBJECT_PROPERTIES_V1,  4)  # [ VT_LPWSTR ] Indicates the recipients for the message who receive a "blind copy".
WPD_EMAIL_HAS_BEEN_READ   = _PropertyKey.create(WPD_EMAIL_OBJECT_PROPERTIES_V1,  7)  # [ VT_BOOL ] Indicates whether the user has read this message.
WPD_EMAIL_RECEIVED_TIME   = _PropertyKey.create(WPD_EMAIL_OBJECT_PROPERTIES_V1,  8)  # [ VT_DATE ] Indicates at what time the message was received.
WPD_EMAIL_HAS_ATTACHMENTS = _PropertyKey.create(WPD_EMAIL_OBJECT_PROPERTIES_V1,  9)  # [ VT_BOOL ] Indicates whether this message has attachments.
WPD_EMAIL_SENDER_ADDRESS  = _PropertyKey.create(WPD_EMAIL_OBJECT_PROPERTIES_V1, 10)  # [ VT_LPWSTR ] Indicates who sent the message.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_APPOINTMENT_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all appointment objects.
#############################################################################
WPD_APPOINTMENT_OBJECT_PROPERTIES_V1 = GUID("{F99EFD03-431D-40D8-A1C9-4E220D9C88D3}")
WPD_APPOINTMENT_LOCATION            = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1,  3)  # [ VT_LPWSTR ] Indicates the location of the appointment e.g. "Building 5, Conf. room 7".
WPD_APPOINTMENT_TYPE                = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1,  7)  # [ VT_LPWSTR ] Indicates the type of appointment e.g. "Personal", "Business" etc.
WPD_APPOINTMENT_REQUIRED_ATTENDEES  = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1,  8)  # [ VT_LPWSTR ] Semi-colon separated list of required attendees.
WPD_APPOINTMENT_OPTIONAL_ATTENDEES  = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1,  9)  # [ VT_LPWSTR ] Semi-colon separated list of optional attendees.
WPD_APPOINTMENT_ACCEPTED_ATTENDEES  = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1, 10)  # [ VT_LPWSTR ] Semi-colon separated list of attendees who have accepted the appointment.
WPD_APPOINTMENT_RESOURCES           = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1, 11)  # [ VT_LPWSTR ] Semi-colon separated list of resources needed for the appointment.
WPD_APPOINTMENT_TENTATIVE_ATTENDEES = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1, 12)  # [ VT_LPWSTR ] Semi-colon separated list of attendees who have tentatively accepted the appointment.
WPD_APPOINTMENT_DECLINED_ATTENDEES  = _PropertyKey.create(WPD_APPOINTMENT_OBJECT_PROPERTIES_V1, 13)  # [ VT_LPWSTR ] Semi-colon separated list of attendees who have declined the appointment.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_TASK_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all task objects.
#############################################################################
WPD_TASK_OBJECT_PROPERTIES_V1 = GUID("{E354E95E-D8A0-4637-A03A-0CB26838DBC7}")
WPD_TASK_STATUS           = _PropertyKey.create(WPD_TASK_OBJECT_PROPERTIES_V1,  6)  # [ VT_LPWSTR ] Indicates the status of the task e.g. "In Progress".
WPD_TASK_PERCENT_COMPLETE = _PropertyKey.create(WPD_TASK_OBJECT_PROPERTIES_V1,  8)  # [ VT_UI4 ] Indicates how much of the task has been completed.
WPD_TASK_REMINDER_DATE    = _PropertyKey.create(WPD_TASK_OBJECT_PROPERTIES_V1, 10)  # [ VT_DATE ] Indicates the date and time set for the reminder. If this value is 0, then it is assumed that this task has no reminder.
WPD_TASK_OWNER            = _PropertyKey.create(WPD_TASK_OBJECT_PROPERTIES_V1, 11)  # [ VT_LPWSTR ] Indicates the owner of the task.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_SMS_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all objects whose functional category is WPD_FUNCTIONAL_CATEGORY_SMS
#############################################################################
WPD_SMS_OBJECT_PROPERTIES_V1 = GUID("{7E1074CC-50FF-4DD1-A742-53BE6F093A0D}")
WPD_SMS_PROVIDER    = _PropertyKey.create(WPD_SMS_OBJECT_PROPERTIES_V1, 2)  # [ VT_LPWSTR ] Indicates the service provider name.
WPD_SMS_TIMEOUT     = _PropertyKey.create(WPD_SMS_OBJECT_PROPERTIES_V1, 3)  # [ VT_UI4 ] Indicates the number of milliseconds until a timeout is returned.
WPD_SMS_MAX_PAYLOAD = _PropertyKey.create(WPD_SMS_OBJECT_PROPERTIES_V1, 4)  # [ VT_UI4 ] Indicates the maximum number of bytes that can be contained in a message.
WPD_SMS_ENCODING    = _PropertyKey.create(WPD_SMS_OBJECT_PROPERTIES_V1, 5)  # [ VT_UI4 ] Indicates how the driver will encode the text message sent by the client.

#############################################################################
# This section defines all Commands, Parameters and Options associated with:
# WPD_SECTION_OBJECT_PROPERTIES_V1 
#
# This category is for properties common to all objects whose content type is WPD_CONTENT_TYPE_SECTION
#############################################################################
WPD_SECTION_OBJECT_PROPERTIES_V1 = GUID("{516AFD2B-C64E-44F0-98DC-BEE1C88F7D66}")
WPD_SECTION_DATA_OFFSET                     = _PropertyKey.create(WPD_SECTION_OBJECT_PROPERTIES_V1, 2)  # [ VT_UI8 ] Indicates the zero-based offset of the data for the referenced object.
WPD_SECTION_DATA_LENGTH                     = _PropertyKey.create(WPD_SECTION_OBJECT_PROPERTIES_V1, 3)  # [ VT_UI8 ] Indicates the length of data for the referenced object.
WPD_SECTION_DATA_UNITS                      = _PropertyKey.create(WPD_SECTION_OBJECT_PROPERTIES_V1, 4)  # [ VT_UI4 ] Indicates the units for WPD_SECTION_DATA_OFFSET and WPD_SECTION_DATA_LENGTH properties on this object (e.g. offset in bytes, offset in milliseconds etc.).
WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE = _PropertyKey.create(WPD_SECTION_OBJECT_PROPERTIES_V1, 5)  # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection containing a single value, which is the key identifying the resource on the referenced object which the WPD_SECTION_DATA_OFFSET and WPD_SECTION_DATA_LENGTH apply to.


reverse_lookup = _ReverseLookup(globals())
