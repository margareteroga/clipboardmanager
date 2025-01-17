import tkinter as tk
from tkinter import messagebox, simpledialog
import pyperclip

class ClipboardManager:
    def __init__(self):
        self.history = []
        self.root = tk.Tk()
        self.root.title("Clipboard Manager")
        self.root.geometry("300x400")

        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.save_button = tk.Button(self.root, text="Save Clipboard", command=self.save_clipboard)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.retrieve_button = tk.Button(self.root, text="Retrieve", command=self.retrieve_clipboard)
        self.retrieve_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_clipboard)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.root.mainloop()

    def save_clipboard(self):
        current_clipboard = pyperclip.paste()
        if current_clipboard:
            self.history.append(current_clipboard)
            self.listbox.insert(tk.END, current_clipboard)
            messagebox.showinfo("Clipboard Manager", "Clipboard content saved!")
        else:
            messagebox.showwarning("Clipboard Manager", "Clipboard is empty!")

    def retrieve_clipboard(self):
        try:
            selected_index = self.listbox.curselection()[0]
            selected_text = self.listbox.get(selected_index)
            pyperclip.copy(selected_text)
            messagebox.showinfo("Clipboard Manager", f"Text copied to clipboard: {selected_text}")
        except IndexError:
            messagebox.showwarning("Clipboard Manager", "No item selected!")

    def delete_clipboard(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
            del self.history[selected_index]
            messagebox.showinfo("Clipboard Manager", "Entry deleted!")
        except IndexError:
            messagebox.showwarning("Clipboard Manager", "No item selected!")

if __name__ == "__main__":
    ClipboardManager()