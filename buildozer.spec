[app]
# (str) Title of your application
title = NexusAI

# (str) Package name
package.name = nexusai

# (str) Package domain (needed for android packaging)
package.domain = org.nexus

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements
# IZBAČENO: hostpython3 i fiksne verzije koje su pucale
requirements = python3,kivy,requests,openssl

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, CAMERA, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid any unnecessary network calls.
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# AGREEMENT. This will allow automatic builds.
android.accept_sdk_license = True

# (str) Android architecture to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (str) The Android arch to build for. (deprecated)
android.arch = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1
