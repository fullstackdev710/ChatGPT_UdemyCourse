import tkinter as tk


def get_slides():
    print("Hi you are creating PPT slides.")


app = tk.Tk()
app.title("Create PPT Slides")
app.geometry("800x600")

# Create text field
text_field = tk.Text(app)
text_field.pack(fill="both", expand=True)
text_field.configure(wrap="word", font=("Arial", 12))
text_field.focus_set()

# Create the button to create slides
create_button = tk.Button(app, text="Create Slides", command=get_slides())
create_button.pack()

app.mainloop()
