plugins {
    id("com.android.application") version "8.10.1"
    id("org.jetbrains.kotlin.android") version "2.2.20"
}

android {
    namespace = "com.dmc5.launcher"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.dmc5.launcher"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }
}
