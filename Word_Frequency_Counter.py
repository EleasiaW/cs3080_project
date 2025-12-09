import tkinter as tk
from tkinter import filedialog, messagebox
import re
from collections import Counter

class WordFrequencyCounter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x700")
        self.root.title("Word Frequency Counter")

        #Create the tkinter label
        self.label = tk.Label(self.root, text="Word Frequency Counter", font=('Arial', 22))
        self.label.pack(padx=10, pady=10)

        #Create the text box
        self.text = tk.Text(self.root, width=80, height=20)
        self.text.pack(pady=20)

        #Create button that opens file
        self.button = tk.Button(self.root, text="Open a text file", font=("Arial", 18), command=self.openFile)
        self.button.pack(padx=10, pady=10)

        #Start event loop
        self.root.mainloop()

    def openFile(self):
        #Use filedialog so users can navigate to text file
        self.filename = filedialog.askopenfilename(initialdir="", title="Select a text file", filetypes=[("text files", "*.txt")])
        
        #Display error message if file cannot be read
        if self.filename:
            try:
                self.count_words(self.filename)
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file:\n{e}")

    def count_words(self, filename):
        with open(self.filename, 'r') as f:
                #Put each word as an element of the list self.words
                self.file_contents = f.read().lower()
                self.words = re.split(r'\W+', self.file_contents)
                self.words = [word for word in self.words if word]

        #Use Counter to find the ten most frequent words in the string        
        self.word_count = Counter(self.words)
        self.top_ten = self.word_count.most_common(10)
        #Print the top ten most frequent words and the amount of times it appears into textbox
        for i, (word, count) in enumerate(self.top_ten, 1):
            self.text.insert(tk.END, f"{i}. The word '{word}' appears {count} times.\n")    


WordFrequencyCounter()