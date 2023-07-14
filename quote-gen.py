import tkinter as tk

def process_titles():
    titles = text_box.get("1.0", "end").strip().split("\n")
    quote_type = quote_var.get()
    add_comma = comma_var.get()

    if quote_type == "single":
        quoted_titles = ["'" + title + "'" for title in titles]
    elif quote_type == "double":
        quoted_titles = ['"' + title + '"' for title in titles]
    else:
        quoted_titles = [title.strip('\'"') for title in titles]

    if add_comma:
        quoted_titles = [title + "," for title in quoted_titles]

    result = "\n".join(quoted_titles)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", result)

    # Update result text box size
    result_text.update_idletasks()
    result_text.config(height=result_text.cget("height"))

root = tk.Tk()
root.title("Title Quoter")

def on_text_change(event):
    text_box.update_idletasks()  # Update text box size
    text_box.config(height=text_box.cget("height"))  # Auto-resize height

text_box = tk.Text(root, height=10, width=30, wrap=tk.WORD)
text_box.bind("<<Modified>>", on_text_change)  # Bind text change event
text_box.pack(fill=tk.BOTH, expand=True)

quote_var = tk.StringVar()
quote_var.set("single")  # Default quote type

single_quote_radio = tk.Radiobutton(root, text="Single Quotes", variable=quote_var, value="single")
single_quote_radio.pack()

double_quote_radio = tk.Radiobutton(root, text="Double Quotes", variable=quote_var, value="double")
double_quote_radio.pack()


none_quote_radio = tk.Radiobutton(root, text="Remove Quotes", variable=quote_var, value="none")
none_quote_radio.pack()

comma_var = tk.BooleanVar()
comma_check = tk.Checkbutton(root, text="Add Comma", variable=comma_var)
comma_check.pack()

process_button = tk.Button(root, text="Process", command=process_titles)
process_button.pack()

result_label = tk.Label(root, text="Program Result:")
result_label.pack()

result_text = tk.Text(root, height=10, width=30)
result_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
