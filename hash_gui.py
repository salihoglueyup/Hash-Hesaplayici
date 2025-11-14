import tkinter as tk
from tkinter import ttk, messagebox
import hashlib


class HashingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Hesaplayıcı")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        title_label = tk.Label(
            main_frame,
            text="Hash Hesaplayıcı",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 5))

        subtitle_label = tk.Label(
            main_frame,
            text="Metninizi girin ve farklı hash algoritmalarıyla şifreleyin",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#7f8c8d"
        )
        subtitle_label.pack(pady=(0, 20))

        algo_frame = tk.LabelFrame(
            main_frame,
            text="Hash Algoritması Seçin",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#2c3e50",
            padx=15,
            pady=15
        )
        algo_frame.pack(fill=tk.X, pady=(0, 15))

        self.selected_algo = tk.StringVar(value="SHA-256")
        algorithms = ["MD5", "SHA-1", "SHA-256", "SHA-384", "SHA-512"]

        button_frame = tk.Frame(algo_frame, bg="white")
        button_frame.pack()

        for algo in algorithms:
            btn = tk.Radiobutton(
                button_frame,
                text=algo,
                variable=self.selected_algo,
                value=algo,
                font=("Arial", 10),
                bg="white",
                fg="#2c3e50",
                selectcolor="#3498db",
                command=self.on_algo_change,
                cursor="hand2"
            )
            btn.pack(side=tk.LEFT, padx=10)

        input_frame = tk.LabelFrame(
            main_frame,
            text="Metninizi Girin",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#2c3e50",
            padx=15,
            pady=15
        )
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        self.text_input = tk.Text(
            input_frame,
            height=8,
            font=("Arial", 11),
            wrap=tk.WORD,
            relief=tk.SOLID,
            borderwidth=1,
            padx=10,
            pady=10
        )
        self.text_input.pack(fill=tk.BOTH, expand=True)
        self.text_input.bind("<KeyRelease>", self.on_text_change)

        bottom_input_frame = tk.Frame(input_frame, bg="white")
        bottom_input_frame.pack(fill=tk.X, pady=(5, 0))

        self.char_label = tk.Label(
            bottom_input_frame,
            text="Karakter sayısı: 0",
            font=("Arial", 9),
            bg="white",
            fg="#7f8c8d"
        )
        self.char_label.pack(side=tk.LEFT)

        clear_button = tk.Button(
            bottom_input_frame,
            text="Temizle",
            command=self.clear_all,
            font=("Arial", 9, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=10,
            pady=3,
            relief=tk.FLAT,
            cursor="hand2"
        )
        clear_button.pack(side=tk.RIGHT)

        result_frame = tk.LabelFrame(
            main_frame,
            text="Hash Sonucu",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#2c3e50",
            padx=15,
            pady=15
        )
        result_frame.pack(fill=tk.BOTH, pady=(0, 10))

        self.result_text = tk.Text(
            result_frame,
            height=4,
            font=("Courier", 9),
            wrap=tk.WORD,
            relief=tk.SOLID,
            borderwidth=1,
            bg="#ecf0f1",
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.result_text.pack(fill=tk.BOTH)

        bottom_result_frame = tk.Frame(result_frame, bg="white")
        bottom_result_frame.pack(fill=tk.X, pady=(5, 0))

        self.info_label = tk.Label(
            bottom_result_frame,
            text="",
            font=("Arial", 9),
            bg="white",
            fg="#7f8c8d",
            justify=tk.LEFT
        )
        self.info_label.pack(side=tk.LEFT)

        self.copy_button = tk.Button(
            bottom_result_frame,
            text="Panoya Kopyala",
            command=self.copy_to_clipboard,
            font=("Arial", 9, "bold"),
            bg="#27ae60",
            fg="white",
            padx=15,
            pady=5,
            relief=tk.FLAT,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.copy_button.pack(side=tk.RIGHT)

    def on_text_change(self, event=None):
        text = self.text_input.get("1.0", tk.END).strip()
        char_count = len(text)

        self.char_label.config(text=f"Karakter sayısı: {char_count}")

        if text:
            self.calculate_hash()
        else:
            self.clear_result()

    def on_algo_change(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            self.calculate_hash()

    def calculate_hash(self):
        text = self.text_input.get("1.0", tk.END).strip()

        if not text:
            self.clear_result()
            return

        algo = self.selected_algo.get()

        try:
            if algo == "MD5":
                hash_obj = hashlib.md5(text.encode('utf-8'))
            elif algo == "SHA-1":
                hash_obj = hashlib.sha1(text.encode('utf-8'))
            elif algo == "SHA-256":
                hash_obj = hashlib.sha256(text.encode('utf-8'))
            elif algo == "SHA-384":
                hash_obj = hashlib.sha384(text.encode('utf-8'))
            elif algo == "SHA-512":
                hash_obj = hashlib.sha512(text.encode('utf-8'))
            else:
                hash_obj = hashlib.sha256(text.encode('utf-8'))

            hash_value = hash_obj.hexdigest()

            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", hash_value)
            self.result_text.config(state=tk.DISABLED)

            bit_length = len(hash_value) * 4
            self.info_label.config(
                text=f"Uzunluk: {len(hash_value)} karakter | {bit_length} bit | {algo}"
            )

            self.copy_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Hata", f"Hash hesaplanırken hata oluştu:\n{str(e)}")

    def copy_to_clipboard(self):
        hash_value = self.result_text.get("1.0", tk.END).strip()
        if hash_value:
            self.root.clipboard_clear()
            self.root.clipboard_append(hash_value)
            messagebox.showinfo("Başarılı", "Hash değeri panoya kopyalandı!")
        else:
            messagebox.showwarning("Uyarı", "Kopyalanacak hash değeri yok!")

    def clear_result(self):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state=tk.DISABLED)
        self.info_label.config(text="")
        self.copy_button.config(state=tk.DISABLED)

    def clear_all(self):
        self.text_input.delete("1.0", tk.END)
        self.clear_result()
        self.char_label.config(text="Karakter sayısı: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashingApp(root)
    root.mainloop()