from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
import webbrowser

class NexusApp(App):
    def build(self):
        # Ovo otvara tvoj Streamlit sajt čim se pokrene aplikacija
        Clock.schedule_once(lambda dt: webbrowser.open("https://tvoj-sajt.streamlit.app"), 0.5)
        return ModalView()

if __name__ == '__main__':
    NexusApp().run()
