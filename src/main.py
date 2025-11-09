import ttkbootstrap as ttk
from ddgs import DDGS
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

root.geometry("1600x900")
root.title("WebSearch++")

entry_frame = ttk.Frame(root)
entry_frame.pack(side=TOP, expand=True, fill=X, padx=80, pady=80)

search_bar = ttk.Entry(master=entry_frame,textvariable="search_request")
search_bar.insert(END, "Search")
search_bar.pack(side=LEFT,expand=True, fill=X)

b1 = ttk.Button(entry_frame, text="Search", bootstyle=PRIMARY)
b1.pack(side=RIGHT, expand=False, padx=5, pady=10)

if __name__ == "__main__":
    # EXEMPLE
    results = DDGS().text(
        "russia filetype:pdf",
        region="us-en",
        safesearch="off",
        timelimit="y",
        page=1,
        backend="auto",
    )
    for r in results:
        print(r["title"])
        print(r["href"])
        print()

    root.mainloop()
