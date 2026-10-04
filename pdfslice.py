import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter


class PDFSplitter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDFSlice")
        self.geometry("520x260")
        self.resizable(False, False)

        self.reader = None
        self.pdf_path = None

        # --- PDF file path ---
        tk.Label(self, text="PDF file path:").place(x=15, y=15)
        self.path_entry = tk.Entry(self, width=55)
        self.path_entry.place(x=15, y=40)
        tk.Button(self, text="Browse...", command=self.browse).place(x=370, y=36)
        tk.Button(self, text="Confirm File", command=self.confirm).place(x=440, y=36)

        # --- Status ---
        self.status = tk.Label(self, text="No file selected", fg="gray")
        self.status.place(x=15, y=75)

        # --- Start and end pages ---
        tk.Label(self, text="Start page:").place(x=15, y=115)
        self.start_entry = tk.Entry(self, width=10, state="disabled")
        self.start_entry.place(x=100, y=115)

        tk.Label(self, text="End page:").place(x=200, y=115)
        self.end_entry = tk.Entry(self, width=10, state="disabled")
        self.end_entry.place(x=285, y=115)

        self.save_btn = tk.Button(
            self,
            text="Save output.pdf",
            command=self.save,
            state="disabled",
            width=20,
        )
        self.save_btn.place(x=15, y=160)

        self.result = tk.Label(
            self,
            text="",
            fg="green",
            wraplength=480,
            justify="left",
        )
        self.result.place(x=15, y=200)

    def browse(self):
        path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )

        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)

    def confirm(self):
        path = self.path_entry.get().strip().strip('"')

        if not path:
            messagebox.showwarning("Error", "Please enter a file path.")
            return

        if not os.path.isfile(path):
            messagebox.showerror("Error", "No file was found at this path.")
            self.status.config(text="File not found", fg="red")
            self._lock()
            return

        try:
            self.reader = PdfReader(path)
            total = len(self.reader.pages)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to read the PDF:\n{e}")
            self._lock()
            return

        self.pdf_path = path
        self.status.config(
            text=f"✔ File loaded: {os.path.basename(path)}  |  Pages: {total}",
            fg="green",
        )

        self._unlock()

        self.start_entry.delete(0, tk.END)
        self.start_entry.insert(0, "1")

        self.end_entry.delete(0, tk.END)
        self.end_entry.insert(0, str(total))

    def _unlock(self):
        for widget in (self.start_entry, self.end_entry, self.save_btn):
            widget.config(state="normal")

    def _lock(self):
        self.reader = None
        self.pdf_path = None

        for widget in (self.start_entry, self.end_entry, self.save_btn):
            widget.config(state="disabled")

    def save(self):
        total = len(self.reader.pages)

        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())
        except ValueError:
            messagebox.showwarning("Error", "Page numbers must be integers.")
            return

        if not (1 <= start <= total) or not (1 <= end <= total):
            messagebox.showwarning(
                "Error",
                f"Page numbers must be between 1 and {total}.",
            )
            return

        if start > end:
            messagebox.showwarning(
                "Error",
                "The start page cannot be greater than the end page.",
            )
            return

        writer = PdfWriter()

        for page_index in range(start - 1, end):
            writer.add_page(self.reader.pages[page_index])

        out_path = os.path.join(os.path.dirname(self.pdf_path), "output.pdf")

        try:
            with open(out_path, "wb") as file:
                writer.write(file)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to save the PDF:\n{e}")
            return

        self.result.config(
            text=f"✔ Pages {start} through {end} were saved to:\n{out_path}"
        )
        messagebox.showinfo("Success", f"PDF saved successfully:\n{out_path}")


if __name__ == "__main__":
    PDFSplitter().mainloop()
