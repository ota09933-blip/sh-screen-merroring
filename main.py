from kivymd.app import MDApp
from kivy.uix.image import Image as KivyImage
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
import socket
import io
import threading

class ScreenReceiverApp(MDApp):
    def build(self):
        self.img_widget = KivyImage()
        # بدء الاتصال في خلفية البرنامج حتى لا تتجمد الواجهة
        threading.Thread(target=self.connect_to_pc, daemon=True).start()
        return self.img_widget

    def connect_to_pc(self):
        # استخدام اتصال الشبكة اللاسلكية أو البلوتوث المباشر المستقر عبر السوكيت
        # يمكنك تعديل الـ IP هنا ليتوافق مع IP كمبيوترك لاحقاً
        host = "192.168.1.100" 
        port = 5005

        print("جاري محاولة الاتصال بالكمبيوتر...")
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            print("تم الاتصال بالكمبيوتر بنجاح!")
        except Exception as e:
            print(f"فشل الاتصال: {e}")
            return

        # استقبال بايتات الصور وعرضها
        while True:
            try:
                size_data = self.sock.recv(8).decode()
                if not size_data: break
                size = int(size_data)

                img_bytes = b""
                while len(img_bytes) < size:
                    packet = self.sock.recv(size - len(img_bytes))
                    if not packet: break
                    img_bytes += packet

                Clock.schedule_once(lambda dt: self.update_image(img_bytes))
            except:
                break

    def update_image(self, img_bytes):
        try:
            data = io.BytesIO(img_bytes)
            core_img = CoreImage(data, ext="jpeg")
            self.img_widget.texture = core_img.texture
        except:
            pass

if __name__ == '__main__':
    ScreenReceiverApp().run()
