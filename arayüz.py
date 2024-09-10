import customtkinter as ctk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk

# Global değişkenler
kayit_path = ""  # Seçilen klasör yolu
captured_image = None  # Çekilen fotoğraf
cap = None  # Kamera nesnesi
cam_open = False  # Kamera durumu
camera_index = 0  # Başlangıçta kullanılacak kamera indeksi

# Kayıt Yeri seçimi için fonksiyon
def kayit_yeri():
    global kayit_path
    kayit_path = filedialog.askdirectory()  # Klasör seçimi yap
    print(f"Seçilen Kayıt Yeri: {kayit_path}")  # Konsolda seçilen klasör yolunu göster

# Kamerayı açma ve görüntü işleme fonksiyonu
def kamera_cagirma():
    global cap, cam_open, captured_image
    
    # Kamera zaten açık değilse aç
    if not cam_open:
        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            print("Kamera açılamadı!")
            return
        cam_open = True

    # Kamera görüntüsünü sürekli yenileyen fonksiyon
    def update_frame():
        global captured_image
        ret, frame = cap.read()
        if ret:
            # Görüntünün boyutlarını al
            height, width, _ = frame.shape

            # Kırmızı kare için merkezi hesapla (50x50 boyutunda kare için)
            square_size = 50
            start_point = (width // 2 - square_size // 2, height // 2 - square_size // 2)
            end_point = (width // 2 + square_size // 2, height // 2 + square_size // 2)

            # Kırmızı kare ekleyelim
            cv2.rectangle(frame, start_point, end_point, (0, 0, 255), 2)

            # Fotoğrafı güncelle
            captured_image = frame.copy()

            # OpenCV görüntüsünü Tkinter uyumlu hale getirme
            cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2_image)
            imgtk = ImageTk.PhotoImage(image=img)

            # Tkinter label'a güncellenmiş görüntüyü yerleştir
            photo_label.imgtk = imgtk
            photo_label.configure(image=imgtk)

        # Her 20 ms'de bir tekrar çalıştır
        photo_label.after(20, update_frame)

    # Görüntü güncellemesini başlat
    update_frame()

# Kamera değişimi için fonksiyon
def switch_camera():
    global cap, camera_index, cam_open

    # Kamera kapalıysa fonksiyonu çalıştırma
    if not cam_open:
        return

    # Mevcut kamera kapat
    cap.release()

    # Kamera indeksini değiştir (0'dan 1'e veya 1'den 0'a)
    camera_index = 1 - camera_index

    # Yeni kamera indeksine göre kamerayı tekrar aç
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        # Kamera bulunamadı, uyarı mesajı göster ve ilk kameraya geri dön
        messagebox.showwarning("Kamera Bulunamadı", f"Kamera {camera_index} bulunamadı! İlk kameraya geri dönülüyor.")
        camera_index = 0  # İlk kameraya geri dön
        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            print(f"Kamera {camera_index} açılamadı!")
            return

    print(f"Kamera {camera_index} aktif!")

# Çekilen fotoğrafı kaydetme fonksiyonu
def save_photo():
    global captured_image
    
    # Kayıt yolu ve hata tipi kontrolü
    if not kayit_path:
        messagebox.showwarning("Kayıt Yolu Eksik", "Lütfen bir kayıt yeri seçin.")
        return

    error_type = error_type_textbox.get().strip()
    if not error_type:
        messagebox.showwarning("Hata Tipi Eksik", "Lütfen bir hata tipi girin.")
        return

    # Ön izleme alanındaki fotoğrafı kaydetme işlemi
    if captured_image is not None:
        file_path = f"{kayit_path}/{error_type}.png"
        cv2.imwrite(file_path, cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB))
        messagebox.showinfo("Başarılı", f"Fotoğraf '{file_path}' olarak kaydedildi.")
        print(f"Fotoğraf kaydedildi: {file_path}")
    else:
        messagebox.showwarning("Fotoğraf Yok", "Ön izleme alanında kaydedilecek fotoğraf yok.")

# Ana pencere oluştur
root = ctk.CTk()
root.geometry("1288x625")  # Pencere boyutu
root.title("Özelleştirilmiş Arayüz")

# Soldaki frame (Butonlar_Frame)
buttons_frame = ctk.CTkFrame(root, width=644, height=625, corner_radius=0, fg_color="#1E275C")
buttons_frame.grid(row=0, column=0, sticky="nswe")

# Sağdaki frame (Foto_Frame)
photo_frame = ctk.CTkFrame(root, width=644, height=625, corner_radius=0)
photo_frame.grid(row=0, column=1, sticky="nswe")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

buttons_frame.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)
buttons_frame.grid_columnconfigure(0, weight=1)

# Butonlar ve textboxları ekleyelim
record_button = ctk.CTkButton(buttons_frame, text="Kayıt Yeri", width=200, command=kayit_yeri)
record_button.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

error_type_textbox = ctk.CTkEntry(buttons_frame, placeholder_text="Hata Tipi", width=200)
error_type_textbox.grid(row=1, column=0, pady=20, padx=20, sticky="ew")

camera_button = ctk.CTkButton(buttons_frame, text="Kamera", width=200, command=kamera_cagirma)
camera_button.grid(row=2, column=0, pady=20, padx=20, sticky="ew")

switch_camera_button = ctk.CTkButton(buttons_frame, text="Kamera Değiştir", width=200, command=switch_camera)
switch_camera_button.grid(row=3, column=0, pady=20, padx=20, sticky="ew")

save_button = ctk.CTkButton(buttons_frame, text="Kaydet", width=200, command=save_photo)
save_button.grid(row=4, column=0, pady=20, padx=20, sticky="ew")

# Fotoğraf önizleme alanı
photo_label = ctk.CTkLabel(photo_frame, text="Fotoğraf Önizleme Alanı", width=644, height=625, fg_color="white")
photo_label.pack(padx=10, pady=10, expand=True)

# Ana pencereyi çalıştır
root.mainloop()
