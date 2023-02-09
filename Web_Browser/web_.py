import tkinter as tk
import webbrowser

class Browser:
    def __init__(self, master):
        self.master = master
        self.master.title("Web Browser")
        self.master.geometry("700x400")
        self.master.config(bg="light blue")
        
        self.url_entry = tk.Entry(self.master, width=60, font=("Helvetica", 14), bg="white")
        self.url_entry.pack(pady=10)
        
        self.open_button = tk.Button(self.master, text="Open", font=("Helvetica", 14), command=self.open_url, bg="light green", fg="white")
        self.open_button.pack(side="left", padx=10)
        
        self.back_button = tk.Button(self.master, text="<", font=("Helvetica", 14), command=self.back, bg="light green", fg="white")
        self.back_button.pack(side="left", padx=10)
        
        self.forward_button = tk.Button(self.master, text=">", font=("Helvetica", 14), command=self.forward, bg="light green", fg="white")
        self.forward_button.pack(side="left", padx=10)
        
        self.search_entry = tk.Entry(self.master, width=40, font=("Helvetica", 14), bg="white")
        self.search_entry.pack(side="right", padx=10, pady=10)
        
        self.search_button = tk.Button(self.master, text="Search", font=("Helvetica", 14), command=self.search, bg="light green", fg="white")
        self.search_button.pack(side="right", padx=10)
        
        self.history = []
        self.current = -1
    
    def open_url(self):
        url = self.url_entry.get()
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open_new(url)
        self.history.append(url)
        self.current += 1
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, url)
    
    def back(self):
        if self.current > 0:
            self.current -= 1
            url = self.history[self.current]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            webbrowser.open_new(url)
    
    def forward(self):
        if self.current < len(self.history) - 1:
            self.current += 1
            url = self.history[self.current]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            webbrowser.open_new(url)
    
    def search(self):
        query = self.search_entry.get()
        webbrowser.open_new("https://www.google.com/search?q=" + query)
        self.history.append("https://www.google.com/search?q=" + query)
        self.current += 1
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Browser(root)
    root.mainloop()
         
           








    
