from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior


from kivy.properties import BooleanProperty

class AppCell(RecycleDataViewBehavior, BoxLayout):
    Builder.load_file('appcell.kv')
    app = ObjectProperty()

    def refresh_view_attrs(self, rv, index, data):
        self.app = data["app"]
        self.ids["title"].text = "%s (%s)" % (self.app.storeInfos.title, self.app.storeInfos.details.appDetails.versionCode)
        self.ids["details"].text = self.app.bundle
        self.ids["button"].opacity = 1 if self.app.isUpdatable() else 0

    def on_button_press(self):
        if self.app.isUpdatable():
            self.app.update()