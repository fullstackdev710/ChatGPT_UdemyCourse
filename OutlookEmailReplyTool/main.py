import openai
import win32com.client
import tkinter as tk

openai.api_key="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"

def last_10_emails():
   outlook=win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
   inbox=outlook.GetDefaultFolder(6)
   messages=inbox.Items
   emails=[messages.GetLast().Subject]
   email_number=10
   for i in range(email_number):
      emails.append(messages.GetPrevious().Subject)
   return emails

root=tk.Tk()
root.title("Outlook Emails")
root.geometry("300x300")

email_subjects=last_10_emails()
selected_subject=tk.StringVar()

dropdown=tk.OptionMenu(root, selected_subject, *email_subjects)
dropdown.pack()

label =tk.Label(root, text="")
label.pack()
root.mainloop()
