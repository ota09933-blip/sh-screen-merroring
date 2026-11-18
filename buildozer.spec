[app]
title = Screen Mirror
package.name = screenmirror
package.domain = org.vampyr
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# المتطلبات الأساسية والمستقرة لأندرويد 6
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow

orientation = portrait
fullscreen = 1

# الأذونات المطلوبة للشبكة والاتصال
android.permissions = INTERNET, BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION

# إعدادات أندرويد 6 الدقيقة لضمان عدم حدوث تعارض (API 23)
android.api = 23
android.minapi = 23
android.ndk_api = 23
android.private_storage = True
android.accept_sdk_license = True
