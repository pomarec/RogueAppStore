import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.recycleview import RecycleView

from androidapp import AndroidApp
from appcell import AppCell


class RogueAppMarket(RecycleView):
    pass

class App(App):
    def build(self):
        root = RogueAppMarket()
        installed_apps = AndroidApp.fetchStoreInfos(AndroidApp.installedApps())
        root.data = [{"app" : a} for a in installed_apps]
        return root

if __name__ == '__main__':
    App().run()
