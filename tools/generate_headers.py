import comtypes.client

comtypes.client.GetModule("portabledeviceapi.dll")
comtypes.client.GetModule("portabledevicetypes.dll")

# noinspection PyProtectedMember,PyUnresolvedReferences
import comtypes.gen._1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0  # PortableDeviceApiLib
# noinspection PyProtectedMember,PyUnresolvedReferences
import comtypes.gen._2B00BA2F_E750_4BEB_9235_97142EDE1D3E_0_1_0  # PortableDeviceTypesLib
# noinspection PyProtectedMember,PyUnresolvedReferences
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0  # stdole
