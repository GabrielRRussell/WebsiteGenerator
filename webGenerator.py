# Random Website Generator
"""
Author:        Gabriel Russell
Creation Date: 2/25/2020
Standards:     I. 5,6,9,1
"""
# We need random to pick various elements/words, and tkinter for graphics
import random
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename

# List of Valid HTML Tags
openingTags = [
    "<h1>",
    "<h2>",
    "<h3>",
    "<h4>",
    "<h5>",
    "<h6>",
    "<p>",
    "<marquee>",
    "<ol><li>",
    "<ul><li>",
    "<blockquote>",
    "<figcaption>",
    "<code>",
    "<s>",
    "<strong>"
]

closingTags = [
    "</h1>",
    "</h2>",
    "</h3>",
    "</h4>",
    "</h5>",
    "</h6>",
    "</p>",
    "</marquee>",
    "</li></ol>",
    "</li></ul>",
    "</blockquote>",
    "</figcaption>",
    "</code>",
    "</s>",
    "</strong>"
]

def generateElement():
    # Select a random number of words, insert them, then add a closing tag
    select = random.randint(0, len(openingTags) - 1)
    curString = openingTags[select]

    numWords = random.randint(1, 50)
    for i in range(0, numWords):
        curString += word_split[random.randint(0, len(word_split) - 1)]
        curString += " "
    curString += closingTags[select]
    return curString

# Generate File
def generate():
    global htmlOutput
    htmlOutput = "<!DOCTYPE html>\n<html>\n"
    
    # Number of elements to create
    numElements = random.randint(1, 150)
    # Iterate and add each element
    for i in range(0, numElements):
        htmlOutput += generateElement()
    htmlOutput+="</html>"
    
def save_file():
    file = open(asksaveasfilename(), "w")
    file.write(htmlOutput)

# Create Tkinter Window
window = tkinter.Tk()
window.title("Website Generator")

# Open a file
words = askopenfilename()
words = open(words, "r")
# Split said file into array of words
word_dump = words.read()
word_split = word_dump.split()

# Set labels, and buttons
helpLabel = tkinter.Label(window, text="Click Generate to generate a website!")
helpLabel.pack()

generate_button = tkinter.Button(window, text="Generate Website", command=generate)
generate_button.pack()

save_file_button = tkinter.Button(window, text="Save File", command=save_file)
save_file_button.pack()
