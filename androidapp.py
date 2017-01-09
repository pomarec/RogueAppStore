from lib.googleplay.infos.googleplay import GooglePlayAPI
from lib.googleplay.downloader.Market import Market
from lib.googleplay.downloader.OperatorModel import Operator
from lib.googleplay.downloader.AssetRequest import AssetRequest
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, StringProperty

CREDENTIALS = {
    "email": "salvi.peon@gmail.com",
    "password": "Mobbles4Life",
    "deviceId": "38c6523ac43ef9e1",
    'country': "France",
    'operator': "SFR"
}

api = GooglePlayAPI(CREDENTIALS["deviceId"])
api.login(CREDENTIALS["email"], CREDENTIALS["password"])
downloader = Market(CREDENTIALS["email"], CREDENTIALS["password"])
downloader.login()
operator = Operator(CREDENTIALS['country'], CREDENTIALS['operator'])

class AndroidApp(EventDispatcher):
    bundle = StringProperty()
    storeInfos = ObjectProperty()
    installedVersion = StringProperty()

    # def __init__(self, **kwargs):
    #     self.bundle = kwargs["bundle"]
    #     self.storeInfos = kwargs.get('storeInfos')
    #     self.installedVersion = kwargs.get('installedVersion')

    @classmethod
    def installedApps(cls):
        return [AndroidApp(bundle = "com.mobbles.mobbles", installedVersion = "1.2"),
                AndroidApp(bundle = "org.coursera.android")]#, installedVersion = "1.5")]

    @classmethod
    def fetchStoreInfos(cls, apps):
        result = api.bulkDetails([a.bundle for a in apps])
        appsDict = { a.bundle : a for a in apps}
        for e in result.entry:
            appsDict[e.doc.docid].storeInfos = e.doc
        return apps

    def isUpdatable(self):
        #storeVersion = self.storeInfos.details.appDetails.majorVersionNumber
        # optional int32 majorVersionNumber = 2;
        # optional int32 versionCode = 3;
        # optional string versionString = 4;

        if self.installedVersion:
            return True
        else:
            return False
    
    def update(self):
        request = AssetRequest(self.bundle, downloader.token, CREDENTIALS['deviceId'],
                               operator, "None", 19)
        (url, market_da) = downloader.get_asset(request.encode())
        print(url)


"""
Intent mainIntent = new Intent(Intent.ACTION_MAIN, null);
mainIntent.addCategory(Intent.CATEGORY_LAUNCHER);
List<ResolveInfo> pkgAppsList = context.getPackageManager().queryIntentActivities( mainIntent, 0)

---

inal PackageManager pm = getPackageManager();
//get a list of installed apps.
List<ApplicationInfo> packages = pm.getInstalledApplications(PackageManager.GET_META_DATA);

for (ApplicationInfo packageInfo : packages) {
    Log.d(TAG, "Installed package :" + packageInfo.packageName);
    Log.d(TAG, "Source dir : " + packageInfo.sourceDir);
    Log.d(TAG, "Launch Activity :" + pm.getLaunchIntentForPackage(packageInfo.packageName)); 
}
// the getLaunchIntentForPackage returns an intent that you can use with startActivity() 


https://github.com/kivy/pyjnius
https://developer.android.com/reference/android/content/pm/ResolveInfo.html
http://stackoverflow.com/questions/18369938/how-to-use-default-package-installer-android-when-trying-to-install-an-apk-fro
"""







