import tkinter as tk
from pptx import Presentation
from pptx.utill import Inches


def slide_generator(text, prs):
    pass


def get_slides():
    """
    This is paragraph 1

    This is a paragraph 2
    ["This is paragraph 1", "This is a paragraph 2"]
    """
    text = text_field.get("1.0", "end-1c")
    paragraphs = text.split("\n\n")
    prs = Presentation()
    width = Pt(1920)
    height = Pt(1080)
    prs.slide_width = width
    prs.slide_height = height
    for paragraph in paragraphs:
        slide_generator(paragraph, prs)

    prs.save("my_presentation.pptx")


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
