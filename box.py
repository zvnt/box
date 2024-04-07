import time, sys
import os
from os.path import exists as isfile
import json
from requests import get as HttpGet
from colorama import Fore, Style, init
from json import loads
from getpass import getuser
import pymem
import pymem.process

os.system('cls')
os.system('title 0 / by zcvnt.')
init(autoreset=True)

def banner():
    print(f'''                          
            {Fore.MAGENTA},,{Style.RESET_ALL}
            {Fore.MAGENTA}*MM     {Style.RESET_ALL}         
            {Fore.LIGHTMAGENTA_EX} MM   {Style.RESET_ALL}                       
            {Fore.MAGENTA} MM,dMMb.   ,pW"Wq.`7M'   `MF'{Style.RESET_ALL}
    ┌──[]─>>{Fore.MAGENTA} MM    `Mb 6W'   `Wb `VA ,V'  {Style.RESET_ALL}
    │       {Fore.LIGHTMAGENTA_EX} MM     M8 8M     M8   XMX    {Style.RESET_ALL}
    │       {Fore.MAGENTA} MM.   ,M9 YA.   ,A9 ,V' VA.  {Style.RESET_ALL}
    │       {Fore.MAGENTA} P^YbmdP'   `Ybmd9'.AM.   .MA.{Style.RESET_ALL}
    │        
    │      
    │      ''')

VersionRequest = HttpGet("https://clientsettings.roblox.com/v2/client-version/WindowsPlayer")

if VersionRequest:

    RobloxVersion = loads(VersionRequest.text)["clientVersionUpload"]
    FileLocation = f"C:/Users/{getuser()}/AppData/Local/Roblox/Versions/{RobloxVersion}"

def fetchrobloxversion():
    version_request = HttpGet("https://clientsettings.roblox.com/v2/client-version/WindowsPlayer")
    if version_request.status_code == 200:
        return json.loads(version_request.text)["clientVersionUpload"]
    else:
        return None

def updatefpssetting(robloxversion, fps, default_settings, fpsboost):
    user = getuser()
    file_location = f"C:/Users/{user}/AppData/Local/Roblox/Versions/{robloxversion}/ClientSettings/ClientAppSettings.json"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)

    if fpsboost == 'y':
        settings = default_settings.copy()
    else:
        settings = {}

    settings["DFIntTaskSchedulerTargetFps"] = int(fps)

    with open(file_location, "w") as file:
        json.dump(settings, file, indent=4)
        time.sleep(0.5)
        boost_status = f"{Fore.GREEN}enabled{Style.RESET_ALL}" if fpsboost == 'y' else f"{Fore.LIGHTRED_EX}disabled{Style.RESET_ALL}"
        print(f"{Style.RESET_ALL}    └[ {Fore.LIGHTBLACK_EX}+{Style.RESET_ALL} ] fps boost {boost_status}, fps updated to {Fore.GREEN}{fps}{Style.RESET_ALL}")

default_settings = {
  "FFlagHandleAltEnterFullscreenManually": "False",
  "FLogNetwork": "7",
  "DFLogHttpTraceLight": "0",
  "FFlagEnableMenuControlsABTest": "False",
  "FFlagFixGraphicsQuality": "True",
  "FFlagEnableInGameMenuModernization": "False",
  "FFlagDisableNewIGMinDUA": "True",
  "DFIntCanHideGuiGroupId": "32380007",
  "FFlagEnableInGameMenuControls": "False",
  "FFlagEnableMenuModernizationABTest": "False",
  "FStringPartTexturePackTable2022": "{\u0022foil\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022asphalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022basalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022brick\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022cobblestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022concrete\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022crackedlava\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022diamondplate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022fabric\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glacier\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://98732842556\u0022,\u0022rbxassetid://9438453972\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022granite\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022grass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ground\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ice\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022leafygrass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022limestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022marble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022metal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022mud\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pavement\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pebble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022plastic\u0022:{\u0022ids\u0022:[\u0022\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022rock\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022corrodedmetal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022salt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sand\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sandstone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022slate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022snow\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022wood\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022woodplanks\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]}}",
  "FFlagEnableMenuModernizationABTest2": "False",
  "FFlagEnableV3MenuABTest3": "False",
  "DFFlagDisableDPIScale": "True",
  "FFlagDebugForceFutureIsBrightPhase3": "True",
  "FFlagEnableInGameMenuChrome": "true",
  "FFlagEnableAccessibilitySettingsAPIV2": "True",
  "DFIntLightstepHTTPTransportHundredthsPercent2": "0",
  "FFlagDebugDisableTelemetryV2Event": "True",
  "FFlagEnableAccessibilitySettingsEffectsInCoreScripts2": "True",
  "DFStringRobloxAnalyticsURL": "null",
  "DFIntS2PhysicsSenderRate": "250",
  "FFlagCoreGuiTypeSelfViewPresent": "False",
  "DFIntTextureQualityOverride": "6",
  "FFlagInGameMenuV1FullScreenTitleBar": "False",
  "FFlagDebugDisableTelemetryEphemeralStat": "True",
  "FFlagDebugDisableTelemetryPoint": "True",
  "DFStringCrashUploadToBacktraceBaseUrl": "null",
  "FStringGamesUrlPath": "/games/",
  "DFFlagBaseNetworkMetrics": "False",
  "DFStringTelemetryV2Url": "null",
  "DFFlagTextureQualityOverrideEnabled": "True",
  "GoogleAnalyticsAccountPropertyIDPlayer": "null",
  "FIntCameraMaxZoomDistance": "99999",
  "DFStringAltTelegrafHTTPTransportUrl": "null",
  "FFlagVoiceBetaBadge": "false",
  "FFlagCommitToGraphicsQualityFix": "True",
  "FStringCoreScriptBacktraceErrorUploadToken": "null",
  "FFlagNewLightAttenuation": "True",
  "DFStringLightstepHTTPTransportUrlPath": "null",
  "FFlagEnableInGameMenuChromeABTest": "True",
  "DFStringLightstepToken": "null",
  "DFFlagEnableLightstepReporting2": "False",
  "DFStringLightstepHTTPTransportUrlHost": "null",
  "FFlagEnableInGameMenuV3": "False",
  "FFlagDebugDisableTelemetryEphemeralCounter": "True",
  "FFlagAdServiceEnabled": "False",
  "DFStringTelegrafHTTPTransportUrl": "null",
  "FFlagCloudsReflectOnWater": "True",
  "FFlagEnableAccessibilitySettingsInExperienceMenu2": "True",
  "FFlagPreloadAllFonts": "True",
  "DFFlagBrowserTrackerIdTelemetryEnabled": "False",
  "DFStringCrashUploadToBacktraceWindowsPlayerToken": "null",
  "FFlagDebugDisableTelemetryEventIngest": "True",
  "DFStringAltHttpPointsReporterUrl": "null",
  "DFFlagDebugPerfMode": "True",
  "FFlagFastGPULightCulling3": "True",
  "DFIntClientLightingTechnologyChangedTelemetryHundredthsPercent": "0",
  "DFStringHttpPointsReporterUrl": "null",
  "FFlagDebugDisableTelemetryV2Counter": "True",
  "FFlagEnableAccessibilitySettingsEffectsInExperienceChat": "True",
  "FFlagDebugDisableTelemetryV2Stat": "True",
  "GoogleAnalyticsAccountPropertyID": "null",
  "DFStringCrashUploadToBacktraceMacPlayerToken": "null",
  "FFlagLuaAppSystemBar": "False",
  "FFlagDontCreatePingJob": "True",
  "\u0022FIntCameraMaxZoomDistance\u0022: \u002299999\u0022": "99999",
  "DFStringAnalyticsEventStreamUrlEndpoint": "opt-out",
  "DFIntConnectionMTUSize": "900",
  "FFlagEnableBatteryStateLogger": "False",
  "FStringTerrainMaterialTablePre2022": "",
  "FIntMeshContentProviderForceCacheSize": "268435456",
  "DFIntCrashReportingHundredthsPercentage": "0",
  "FStringPerformanceSendMeasurementAPISubdomain": "opt-out",
  "FIntStartupInfluxHundredthsPercentage": "0",
  "FFlagRenderGpuTextureCompressor": "True",
  "FFlagImmersiveAdsWhitelistDisabled": "False",
  "DFFlagAddUserIdToSessionTracking": "False",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistanceL23\u0022": "0",
  "FIntTerrainOTAMaxTextureSize": "1024",
  "FIntReportDeviceInfoRollout": "0",
  "DFFlagDebugRenderForceTechnologyVoxel": "True",
  "DFFlagESGamePerfMonitorEnabled": "False",
  "FStringTerrainMaterialTable2022": "",
  "DFIntPredictedOOMPercent": "0",
  "FIntDefaultMeshCacheSizeMB": "256",
  "FIntFontSizePadding": "3",
  "FStringImmersiveAdsUniverseWhitelist": "0",
  "FIntBootstrapperTelemetryReportingHundredthsPercentage": "0",
  "FIntAbuseReportScreenshotMaxSize": "0",
  "FIntFRMMaxGrassDistance": "0",
  "DFIntDebugFRMQualityLevelOverride": "1",
  "FIntLinkBrowserTrackerToDeviceRollout": "0",
  "FFlagEnableAudioOutputDevice": "false",
  "FFlagDebugDisableOTAMaterialTexture": "true",
  "FStringErrorUploadToBacktraceBaseUrl": "https://opt-out.roblox.com",
  "FFlagGraphicsCheckComputeSupport": "True",
  "DFFlagGpuVsCpuBoundTelemetry": "False",
  "DFIntCSGLevelOfDetailSwitchingDistanceL12": "0",
  "FFlagLocServicePerformanceAnalyticsEnabled": "False",
  "FFlagEnableQuickGameLaunch": "False",
  "DFIntCSGLevelOfDetailSwitchingDistanceL34": "0",
  "FFlagTrackMacWebLaunchFlow": "False",
  "FFlagPreloadMinimalFonts": "True",
  "DFFlagPredictedOOM": "False",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistanceL12\u0022": "0",
  "DFIntCSGLevelOfDetailSwitchingDistance": "1",
  "DFIntWriteFullDmpPercent": "0",
  "FIntV1MenuLanguageSelectionFeaturePerMillageRollout": "0",
  "DFFlagHttpCacheCleanBasedOnMemory": "True",
  "DFIntDetectCrashEarlyPercentage": "0",
  "DFFlagEnableFmodErrorsTelemetry": "False",
  "FIntHSRClusterSymmetryDistancePercent": "10000",
  "FFlagAvatarChatSettingsEnabled2": "False",
  "FFlagReportFpsAndGfxQualityPercentiles": "False",
  "DFFlagDebugAnalyticsSendUserId": "False",
  "FFlagFacialAnimationStreamingServiceUniverseSettingsEnableAudio": "False",
  "FFlagRenderPerformanceTelemetry": "False",
  "DFLogHttpTrace": "0",
  "FFlagDebugDisplayFPS": "False",
  "FFlagTrackPlaceIdForCrashEnabled": "False",
  "DFFlagAvatarChatServiceUserPermissionsAudioEligible": "False",
  "FFlagVoiceChatServiceManagerUseAvatarChat": "False",
  "FFlagAddGameInstanceIdToSessionTracking": "False",
  "FFlagDebugForceChatDisabled": "False",
  "DFFlagAddPublicGettersForGfxQualityAndFpsForTelemCounters2": "False",
  "FFlagGraphicsEnableD3D10Compute": "True",
  "DFFlagAudioDeviceTelemetry": "False",
  "FIntRenderGrassDetailStrands": "0",
  "DFLogBatchAssetApiLog": "3",
  "DFFlagAvatarChatServiceUserPermissionsAudioOptIn": "False",
  "FFlagDebugGraphicsDisableDirect3D11": "False",
  "DFIntHttpCurlConnectionCacheSize": "134217728",
  "DFFlagEnableMemProfilingStorePlaceId": "False",
  "FFlagGraphicsSettingsOnlyShowValidModes": "True",
  "DFLogHttpTraceError": "0",
  "DFIntRunningBaseOrientationP": "450",
  "DFFlagQueueDataPingFromSendData": "True",
  "FFlagEnableAdsAPI": "False",
  "DFFlagCrashUploadFullDumps": "False",
  "FFlagAnimationClipMemCacheEnabled": "True",
  "FFlagDebugRenderingSetDeterministic": "True",
  "DFStringRobloxAnalyticsSubDomain": "opt-out",
  "DFIntUserIdPlayerNameCacheSize": "33554432",
  "FFlagFacialAnimationStreamingServiceUserSettingsOptInAudio": "False",
  "FFlagAudioDeviceTelemetry": "false",
  "FintRenderGrassHeightScaler": "0",
  "FFlagWindowsLaunchAnalytics": "False",
  "FFlagDebugGraphics": "False",
  "FIntUITextureMaxRenderTextureSize": "1024",
  "FFlagFacialAnimationStreamingServiceUniverseSettingsEnableVideo": "False",
  "FFlagGlobalWindRendering": "false",
  "FFlagGraphicsGLEnableHQShadersExclusion": "False",
  "DFFlagEnableGCapsHardwareTelemetry": "False",
  "DFIntUserIdPlayerNameLifetimeSeconds": "86400",
  "DFIntCrashUploadToBacktracePercentage": "0",
  "FFlagBatchAssetApi": "True",
  "DFFlagEnableMemProfilingOutsideClient": "False",
  "FStringPartTexturePackTablePre2022": "{\u0022foil\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022brick\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022cobblestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022concrete\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022diamondplate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022fabric\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://7547304948\u0022,\u0022rbxassetid://7546645118\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022granite\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022grass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ice\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022marble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022metal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pebble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022corrodedmetal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sand\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022slate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022wood\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022woodplanks\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022asphalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022basalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022crackedlava\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glacier\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ground\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022leafygrass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022limestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022mud\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pavement\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022rock\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022salt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sandstone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022snow\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]}}",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistanceL34\u0022": "0",
  "FIntTaskSchedulerAutoThreadLimit": "8",
  "FFlagDebugGraphicsPreferVulkan": "True",
  "FFlagDebugGraphicsDisableOpenGL": "True",
  "FFlagTrackWinWebLaunchFlow": "False",
  "FFlagDebugGraphicsCrashOnLeaks": "False",
  "FIntDebugForceMSAASamples": "0",
  "FIntLmsClientRollout2": "0",
  "FIntFlagUpdateVersion": "132",
  "FIntRenderShadowmapBias": "0",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistance\u0022": "0",
  "DFFlagEnableHardwareTelemetry": "false",
  "FIntRenderEnableGlobalInstancingD3D11Percent": "100",
  "FIntEmotesAnimationsPerPlayerCacheSize": "16777216",
  "FFlagDebugGraphicsPreferMetal": "True",
  "DFIntStartupTracingInfluxRollout": "0",
  "FFlagEnableSoundTelemetry": "False",
  "FFlagDisablePostFx": "True",
  "FFlagFacialAnimationStreamingServiceUserSettingsOptInVideo": "False",
  "DFIntGoogleAnalyticsLoadPlayerHundredth": "0",
  "DFIntCSGLevelOfDetailSwitchingDistanceL23": "0",
  "DFIntBrowserTrackerApiDeviceInitializeRolloutPercentage": "0",
  "FFlagNullCheckCloudsRendering": "True",
  "FFlagAvatarChatServiceExposeClientFeaturesForVoiceChat": "False",
  "FFlagGraphicsGLEnableSuperHQShadersExclusion": "False",
  "FFlagDebugGraphicsDisableVulkan": "True",
  "FFlagPreloadTextureItemsOption4": "True",
  "DFStringAnalyticsNS1ApplicationId": "opt-out",
  "DFFlagEphemeralCounterInfluxReportingEnabled": "False",
  "FFlagEnableCameraByDefault": "False",
  "FIntFRMMinGrassDistance": "0",
  "FIntRenderShadowIntensity": "0",
  "FFlagGpuGeometryManager7": "True",
  "FFlagDebugGraphicsDisableVulkan11": "True",
  "DFIntLoginTelemetryHundredthsPercent": "0",
  "DFFlagClientBaseNetworkMetrics": "False",
  "DFStringAnalyticsNS1BeaconConfig": "https://opt-out.roblox.com",
  "DFFlagVideoCaptureServiceEnabled": "False",
  "DFIntNewRunningBaseAltitudeD": "50",
  "FFlagRenderCheckThreading": "True",
  "FIntPGSAngularDampingPermillPersecond": "9999999999",
  "FIntLightingDefaultClearColorARGB": "True;255,255,255,255",
  "FIntRenderLocalLightFadeInMs_enabled": "99999",
  "FFlagDebugGraphicsPreferVulkan_enabled": "True",
  "FFlagTopBarUseNewBadge": "false",
  "FFlagEnableBetaBadgeLearnMore": "false",
  "FFlagBetaBadgeLearnMoreLinkFormview": "false",
  "FFlagControlBetaBadgeWithGuac": "false",
  "FStringVoiceBetaBadgeLearnMoreLink": "null"
}

def memory():
    try:
        pymem.Pymem("RobloxPlayerBeta.exe")
        return f"{Fore.LIGHTRED_EX}running{Style.RESET_ALL}"
    except pymem.exception.ProcessNotFound:
        return f"{Fore.RED}not running{Style.RESET_ALL}"
    
robloxversion = fetchrobloxversion()
status = memory()
    
banner()
if robloxversion:
    print(f"{Style.RESET_ALL}    ├[ {Fore.LIGHTBLACK_EX}+{Style.RESET_ALL} ] roblox: {status}")
    time.sleep(0.5)
    print(f"{Style.RESET_ALL}    ├[ {Fore.LIGHTBLACK_EX}+{Style.RESET_ALL} ] version: {robloxversion}")
    time.sleep(0.5)
    fps = input(f"{Style.RESET_ALL}    ├[ {Fore.LIGHTBLACK_EX}?{Style.RESET_ALL} ] fps: {Fore.GREEN}")
    fpsboost = input(f"{Style.RESET_ALL}    ├[ {Fore.LIGHTBLACK_EX}?{Style.RESET_ALL} ] enable boost (y/n):{Fore.GREEN} ").lower()
    if fps.isdigit():
        updatefpssetting(robloxversion, int(fps), default_settings, fpsboost)
    else:
        print(f"{Style.RESET_ALL}    └[ {Fore.LIGHTRED_EX}!{Style.RESET_ALL} ] invalid fps input")
else:
    print(f"{Style.RESET_ALL}    └[ {Fore.LIGHTRED_EX}!{Style.RESET_ALL} ] error: failed to fetch roblox version")

input()
sys.exit()
