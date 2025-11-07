import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ddgs import DDGS

root = ttk.Window(themename="darkly")

b1 = ttk.Button(root, text="Button 1", bootstyle=WARNING)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

if __name__ == "__main__":
    # EXEMPLE
    results = DDGS().text('russia filetype:pdf', region='us-en', safesearch='off', timelimit='y', page=1,
                          backend="auto")
    for r in results:
        print(r['title'])
        print(r['href'])
        print()

    root.mainloop()
