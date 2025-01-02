import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

import chinese_algorithm as c_a
import chinese_translation as c_t

ctk.set_appearance_mode("light")  # Modes: "System" (default), "Light", "Dark"
ctk.set_default_color_theme("green")  # Themes: "blue" (default), "green", "dark-blue"

##Methods

has_word = False
can_rightwrong = False

def button_test():
    print("bruh")

def button_test_2():
    print("test")

def add_word_function():
    word_text = insert_word.get()
    word_pinyin = insert_pinyin.get()
    word_type = insert_type.get()
    word_def = insert_definition.get()
    word_topic = insert_topic.get()

    c_a.add_word(word_text, word_pinyin, word_type, word_def, word_topic)

def next_word_function():
    _word_type = practice_word_type.get()
    _word_topic = practice_word_topic.get()

    c_a.next_word(_word_type, _word_topic)

    pinyin_text.configure(text=c_a.word_display[0])
    word_text.configure(text="")
    word_definition_text.configure(text=c_a.word_display[2])

    prof_string = "Profficiency:", c_a.word_display[3]

    word_profficiency_label.configure(text=prof_string)

    global has_word
    has_word = True

    global pinyin_size
    global word_size

    if (len(c_a.word_display[0]) >= 40):
        pinyin_size = pinyin_size_profiles[0]
    elif(len(c_a.word_display[0]) >= 20):
        pinyin_size = pinyin_size_profiles[1]
    else:
        pinyin_size = pinyin_size_profiles[2]

    if (len(c_a.word_display[1]) >= 10):
        word_size = word_size_profiles[0]
    elif(len(c_a.word_display[1]) >= 5):
        word_size = word_size_profiles[1]
    else:
        word_size = word_size_profiles[2]

    pinyin_text.configure(font=('Callibri', pinyin_size, 'bold'))
    word_text.configure(font=('Arial', word_size, 'bold'))

def word_right_function():
    global can_rightwrong
    if(has_word and can_rightwrong):
        _word_type = practice_word_type.get()

        c_a.word_right(_word_type)

        prof_string = "Proficiency:", c_a.word_display[3]

        word_profficiency_label.configure(text=prof_string)

        message_text.configure(text="Good Job! You got this word right. Move on to the next word and keep practicing.")

        can_rightwrong = False
    else:
        message_text.configure(text="No word right now. Click 'Next Word' to start practicing")

def word_wrong_function():
    global can_rightwrong
    if(has_word and can_rightwrong):
        _word_type = practice_word_type.get()

        c_a.word_wrong(_word_type)

        prof_string = "Proficiency:", c_a.word_display[3]

        word_profficiency_label.configure(text=prof_string)

        message_text.configure(text="You got this word wrong. Write it 5 times before moving on to the next word")

        can_rightwrong = False
    else:
        message_text.configure(text="No word right now. Click 'Next Word' to start practicing")

def check_answer_function():
    global can_rightwrong
    if(has_word):
        word_text.configure(text=c_a.word_display[1])

        message_text.configure(text="Word Revealed. Did you get this right? No Cheating.")

        can_rightwrong = True

    else:
        message_text.configure(text="No word right now. Click 'Next Word' to start practicing")

def translate_function():
    chinese_word = str(translater_input.get())

    #print(chinese_word)

    english_translation = c_t.translate_chinese_word(chinese_word)

    translation_label.configure(text="EN Translation: " + english_translation)




        

left_background_color = "#E3E1D9"
right_background_color = "#F5F5F5"
bottom_background_color = "#C7C8CC"

input_background_color = "#F2EFE5"

# Create the main window
root = ctk.CTk()
root.title("Chinese Practice App")

# Set the window properties
root.geometry("1600x900")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)
root.grid_columnconfigure(2, weight=1)
# Create the left frame
left_frame = ctk.CTkFrame(root)
left_frame.grid_propagate(False)
left_frame.grid(row=0, rowspan=2, column=0, sticky="nsew")

# Create the right frame
right_frame = ctk.CTkFrame(root)
right_frame.grid_propagate(False)
right_frame.grid(row=0, rowspan=2, column=1, sticky="nsew")

# Create the Manual Frame
practice_frame = ctk.CTkFrame(root)
practice_frame.grid_propagate(False)
practice_frame.grid(row=0, rowspan=2, column=2, sticky="nsew")

##Actual App Stuff

title_label = ctk.CTkLabel(left_frame, text="中文詞語練習APP", font=('Callibri', 25, 'bold'), pady=8)
title_label.pack(side=tk.TOP, fill=tk.X)

#Insert Word

insert_word_label = ctk.CTkLabel(left_frame, text="Add Chinese Word", font=('Callibri', 12, 'bold'), pady=3)
insert_word_label.pack(side=tk.TOP, fill=tk.X)

insert_word = ctk.CTkEntry(master=left_frame, placeholder_text="Insert Word", width=100)
insert_word.pack(fill=tk.BOTH, expand=False, padx=50, pady=10)

insert_pinyin = ctk.CTkEntry(master=left_frame, placeholder_text="Insert Pinyin")
insert_pinyin.pack(fill=tk.BOTH, expand=False, padx=50, pady=10)

insert_type = ctk.CTkEntry(master=left_frame, placeholder_text="Insert Type (listening/ciyu/chengyu/suyu)")
insert_type.pack(fill=tk.BOTH, expand=False, padx=50, pady=10)

insert_definition = ctk.CTkEntry(master=left_frame, placeholder_text="Insert Definition")
insert_definition.pack(fill=tk.BOTH, expand=False, padx=50, pady=10)

insert_topic = ctk.CTkEntry(master=left_frame, placeholder_text="Insert Topic")
insert_topic.pack(fill=tk.BOTH, expand=False, padx=50, pady=10)


add_word = ctk.CTkButton(
    master=left_frame,
    text="Add Word",
    command=add_word_function
)

add_word.pack(side=ctk.TOP, padx=15, pady=15)

#Word Bank Directory Stuff

word_bank_directory_label = ctk.CTkLabel(left_frame, text="Word Bank Directory", font=('Callibri', 12, 'bold'), pady=3)
word_bank_directory_label.pack(side=tk.TOP, fill=tk.X)

word_bank_directory = ctk.CTkEntry(master=left_frame, placeholder_text="Word Bank Directory")
word_bank_directory.pack(fill=tk.BOTH, expand=False, padx=50, pady=10)

listening_word_bank_directory_label = ctk.CTkLabel(left_frame, text="聽力 Word Bank Directory", font=('Callibri', 12, 'bold'), pady=3)
listening_word_bank_directory_label.pack(side=tk.TOP, fill=tk.X)

listening_word_bank_directory = ctk.CTkEntry(master=left_frame, placeholder_text="Listening Word Bank Directory")
listening_word_bank_directory.pack(fill=tk.BOTH, expand=False, padx=50, pady=10)

word_bank_directory_confirm = ctk.CTkButton(
    master=left_frame,
    text="Confirm Directories",
    command=button_test
)

word_bank_directory_confirm.pack(side=ctk.TOP, padx=15, pady=15)

#Translator Stuff

translator_label = ctk.CTkLabel(left_frame, text="Translate word to English", font=('Callibri', 15, 'bold'), pady=3)
translator_label.pack(side=ctk.TOP, fill=ctk.X)

translater_input = ctk.CTkEntry(master=left_frame, placeholder_text="Enter Word")
translater_input.pack(fill=ctk.BOTH, expand=False, padx=50, pady=10)

translate_word_button = ctk.CTkButton(
    master=left_frame,
    text="Translate Word",
    command=translate_function
)

translate_word_button.pack(side=ctk.TOP, padx=15, pady=2)

translation_label = ctk.CTkLabel(left_frame, text="EN Translation: ", font=('Callibri', 15, 'bold'), pady=3)
translation_label.pack(side=ctk.TOP, fill=ctk.X)

quit_button = ctk.CTkButton(left_frame, text="Quit", command=root.destroy, fg_color="#FF6666", text_color="white")
quit_button.pack(side=ctk.BOTTOM, pady=25)


##Practice Function Stuff

practice_label = ctk.CTkLabel(practice_frame, text="Practice", font=('Callibri', 25, 'bold'), pady=10)
practice_label.pack(side=ctk.TOP, fill=ctk.X)

practice_word_type_label = ctk.CTkLabel(practice_frame, text="Type (listening/ciyu/chengyu/suyu)", font=('Callibri', 10, 'bold'), pady=2)
practice_word_type_label.pack(side=ctk.TOP, fill=ctk.X)

practice_word_type = ctk.CTkEntry(master=practice_frame, placeholder_text="Word Type")
practice_word_type.pack(fill=tk.BOTH, expand=False, padx=50, pady=5)

practice_word_topic_label = ctk.CTkLabel(practice_frame, text="Topic (leave blank for any topic)", font=('Callibri', 10, 'bold'), pady=2)
practice_word_topic_label.pack(side=ctk.TOP, fill=ctk.X)

practice_word_topic = ctk.CTkEntry(master=practice_frame, placeholder_text="Word Topic")
practice_word_topic.pack(fill=ctk.BOTH, expand=False, padx=50, pady=5)

random_word = ctk.CTkButton(
    master=practice_frame,
    text="Next Word",
    command=next_word_function
)

random_word.pack(side=ctk.TOP, padx=15, pady=15)


word_profficiency_label = ctk.CTkLabel(practice_frame, text="Current Word Profeciency: 0", font=('Callibri', 10, 'bold'), pady=10, wraplength=300)
word_profficiency_label.pack(side=ctk.TOP, fill=ctk.X)


##Pinyin Display

pinyin_size_profiles = [30, 45, 55]
word_size_profiles = [50, 80, 120]

pinyin_size = pinyin_size_profiles[2]
word_size = word_size_profiles[2]

pinyin_text = ctk.CTkLabel(right_frame, text="Pin Yin", font=('Callibri', pinyin_size, 'bold'), pady=50,  wraplength=800)
pinyin_text.pack(fill=ctk.Y)

word_text = ctk.CTkLabel(right_frame, text="詞語", font=('Arial', word_size, 'bold'),  wraplength=800)
word_text.pack(fill=tk.Y)

word_definition_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

word_definition_text = ctk.CTkLabel(right_frame, text=word_definition_string, font=('Callibri', 25, 'bold'), pady = 50, wraplength=800)
word_definition_text.pack(fill=tk.Y)

message_text = ctk.CTkLabel(right_frame, text="Hello!", font=('Callibri', 15), pady=5)
message_text.pack(side=ctk.BOTTOM, fill=ctk.X)

check_word_button = ctk.CTkButton(
    master=right_frame,
    text="Check Answer",
    command=check_answer_function
)

check_word_button.pack(side=ctk.BOTTOM, padx=15, pady=35)

wrong_button = ctk.CTkButton(
    master=right_frame,
    text="I got this word Wrong",
    #fg_color="#343131",
    command=word_wrong_function
)

wrong_button.pack(side=ctk.BOTTOM, padx=15, pady=5)

right_button = ctk.CTkButton(
    master=right_frame,
    text="I got this word Right",
    #fg_color="#343131",
    command=word_right_function
)

right_button.pack(side=ctk.BOTTOM, padx=15, pady=5)

root.mainloop()