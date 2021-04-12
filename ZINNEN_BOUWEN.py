#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Katarina
'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import random
#import re
from check_entry import *

OUTPUT_FILE = open('user_entries.txt', 'w+')

def open_translation_window(text):
    window = tk.Tk()
    window.title("BUILDING SENTENCES")
    window.geometry('350x250')

    scroll = tk.Scrollbar(window)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    welcome_text = tk.Text(window, wrap=WORD, spacing2=5, font=("Arial", 12))
    scroll.config(command=welcome_text.yview)
    welcome_text.config(yscrollcommand=scroll.set)
    welcome_text.insert(tk.END, text)
    welcome_text.pack(side=tk.BOTTOM)

    window.mainloop()

def get_text_block(container, height=20, width=60):
    text = tk.Text(container, wrap=WORD, spacing2=5, font=("Arial", 12), height=height, width=width, bg='#B3D3D7')
    return(text)

def get_standard_button_font():
    button_font = font.Font(family='Arial', size=14, weight='bold')
    return(button_font)

def get_translation_button(container, text):
    translation_button = tk.Button(container, text='Translation?', command= lambda: open_translation_window(text))
    translation_button['font'] = get_standard_button_font()
    return(translation_button)

def show_word_translation(container, index, translation):
    widget = tk.Label(container, text=translation)
    widget.grid(row=index, column=1)

def check_and_give_feedback(exercise_frame, container, controller, user_entry_field, words):
    entry = user_entry_field.get('1.0', 'end-1c')
    OUTPUT_FILE.write(entry)
    OUTPUT_FILE.write('\n')
    feedback, translation = get_feedback(entry, words)
    OUTPUT_FILE.write(feedback)
    OUTPUT_FILE.write('\n\n\n')

    feedback_frame = NotificationFrame(exercise_frame, feedback)
    feedback_frame.grid(row=0, rowspan=7, column=0, sticky='nsew')

    translation_button = get_translation_button(exercise_frame, translation)
    translation_button.grid(row=6, column=0, sticky='sw')

    continue_button = tk.Button(exercise_frame, text='OK', bg = 'gray', fg = 'red', height=3, width=7, command=lambda: controller.change_to_next_in_exercise_loop(container))
    continue_button['font'] = font.Font(family='Arial', size=30, weight='bold')
    continue_button.grid(row=6, column=1)

    try_again_button = tk.Button(exercise_frame, text='Probeer opnieuw', command = lambda:controller.repeat_exercise(container))
    try_again_button['font'] = get_standard_button_font()
    try_again_button.grid(row=6, column=0, sticky='se')

class FinalFrame(ttk.Frame):
    def __init__(self, container, text):
        super().__init__(container)

        self.rowconfigure(0,weight=4)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0)
        self.columnconfigure(1)

        text = 'Goed gedaan!!! Je bent klaar met het programma ZINNEN BOUWEN. Ik hoop dat je het leuk vond om te oefenen met het maken van Nederlandse zinnen. Vergeet niet de survey over wat je ervan vond in te vullen! Je kunt dit scherm nu wegklikken.'
        translation = 'Well done!!! You finished the exercises in ZINNEN BOUWEN. I hope you enjoyed building Dutch sentences. Don\'t forget to fill out the survey about your thoughts and experiences with this application! You can now close this window.'

        text_block = tk.Text(self, wrap=WORD, spacing2=5, font=("Arial", 17), height=10, width=50, bg='#00FF09', fg='#FF0000')
        text_block.insert(tk.END, text)
        text_block.grid(row=0, columnspan=2)

        translation_button = get_translation_button(self, translation)
        translation_button.grid(row=1, column=0, sticky='w')

class IntermediateFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.rowconfigure(0,weight=4)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0)
        self.columnconfigure(1)

        text = 'Goed gedaan! Nu je weet hoe het werkt kunnen we beginnen. Klik op \'Start\' om te beginnen met de oefeningen.'
        translation = 'Well done! Now you know how it works, let\'s start! Click \'Start\' to start the exercises.'

        text_block = get_text_block(self)
        text_block.insert(tk.END, text)
        text_block.grid(column=0)

        translation_button = get_translation_button(self, translation)
        translation_button.grid(row=1, column=0, sticky='w')

        continue_button = tk.Button(self, text='Start!', bg = 'gray', fg = 'red', command= lambda: controller.change_to_next_in_exercise_loop(container))
        continue_button['font'] = font.Font(family='Arial', size=20, weight='bold')
        continue_button.grid(row=1, column=1)



class NotificationFrame(ttk.Frame):
    def __init__(self, container, text):
        super().__init__(container)

        self.rowconfigure(0)
        self.columnconfigure(0)

        text_block = get_text_block(self)
        text_block.insert(tk.END, text)
        text_block.grid(column=0)

class ExerciseFrame(ttk.Frame):
    def __init__(self, container, controller, words, is_test=False):
        super().__init__(container)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=2)
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=2)

        text = ""
        translation = ""

        if is_test:
            text = "Dit is een probeeroefening om te wennen aan de oefeningen van ZINNEN BOUWEN. Aan de rechterkant van het venster zie je drie Nederlandse woorden. Je kan op het woord klikken om de Engelse vertaling te zien. Schrijf hieronder een korte tekst met deze woorden en klik op \'Controleer\'."
            translation = "This is a dummy exercise to help you get used to the exercises of ZINNEN BOUWEN. The right side of the window has three Dutch words. You can click a word to display its translation in English. Write down a short texts using these three words and click \'Controleer\'."
            frame_text = get_text_block(self, width=50, height=9)
            frame_text.insert(tk.END, text)
            frame_text.grid(row=0, rowspan = 2, column=0)
        else:
            text = "Schrijf hieronder een korte tekst met de drie woorden rechts en klik op \'Controleer\'."
            translation = "Write a short text with the three words to the right and click \'Controleer\'."
            frame_text = get_text_block(self, width=50, height=4)
            frame_text.insert(tk.END, text)
            frame_text.grid(row=0, rowspan = 2, column=0)

        user_entry_field = tk.Text(self, width=60, height=5, font=("Arial", 12), spacing2=8)
        user_entry_field.grid(row = 2, rowspan=4, column=0)

        self.add_words_to_screen(words)

        translation_button = get_translation_button(self, translation)
        translation_button.grid(row=6, column=0, sticky='w')

        check_button = tk.Button(self, text='Controleer!', bg = 'gray', fg = 'red', command= lambda: check_and_give_feedback(self, container, controller, user_entry_field, words))
        check_button['font'] = font.Font(family='Arial', size=20, weight='bold')
        check_button.grid(row=6, column=1)

    def add_words_to_screen(self, words):
        index=0
        for word in words:
            word_translation = words[word]
            translation_index = index+1
            word_button = tk.Button(self, text=word, command= lambda translation_index=translation_index, word_translation=word_translation: show_word_translation(self, translation_index, word_translation))
            word_button['font'] = get_standard_button_font()
            word_button.grid(row=index, column=1)
            index += 2


class ExplanationFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.rowconfigure(0,weight=4)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0)
        self.columnconfigure(1)

        text = "Het doel van ZINNEN BOUWEN is... zinnen bouwen! In elke opdracht zul je drie woorden te zien krijgen. Jij moet een korte tekst te schrijven met die drie woorden. Je mag meerdere zinnen schrijven, of juist maar één. Je mag woorden veranderen, bijvoorbeeld:\n\n - \'koude\' in plaats van \'koud\'\n - \'ik loop\' in plaats van \'lopen\'\n - \'appels\' in plaats van \'appel\'\n\nEerst zul je een oefening krijgen om het systeem uit te proberen, daarna gaan we beginnen!"
        translation = "The goal of BUILDING SENTENCES is... building sentences! You will be shown three words in each exercise. You have to write a short text that include these three words. You can write multiple sentences or only one. You are allowed to change words, for example:\n\n - \'koude\' instead of \'koud\' (\'cold\')\n - \'ik loop\' (\'I walk\') instead of 'lopen\' (\'to walk\')\n - \'appels\' (\'apples\') instead of \'appel\' (\'apple\')\n\nFirst you will be shown an exercise to try out the system, then we will start!\n"

        frame_text = get_text_block(self)
        frame_text.insert(tk.END, text)
        frame_text.grid(row=0, columnspan=3)

        translation_button = get_translation_button(self, translation)
        translation_button.grid(row=1, column=0, sticky='w')

        continue_button = tk.Button(self, text='Probeer het systeem uit', bg = 'gray', fg = 'red', command=lambda: controller.change_frame_to_test_exercise_frame(container, controller.test_words))
        continue_button['font'] = font.Font(family='Arial', size=20, weight='bold')
        continue_button.grid(row=1, column=1)


class LevelChoiceFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0)
        self.columnconfigure(1)
        self.columnconfigure(2)

        text = "Eerst moet ik je niveau weten. Hoe goed is je Nederlands al?"
        translation = "First, I need to know your level. How well do you know Dutch already? hint: if you needed this translation, you might want to pick \'Beginner\'! :)"

        frame_text = get_text_block(self, height=5)
        frame_text.insert(tk.END, text)
        frame_text.grid(row=0, columnspan=3)

        beginner_button = tk.Button(self, text='Beginner', command = lambda: controller.change_frame_and_set_level('ExplanationFrame', 0))
        beginner_button['font'] = get_standard_button_font()
        beginner_button.grid(row=1, column=0)

        intermediate_button = tk.Button(self, text='ertussenin', command = lambda: controller.change_frame_and_set_level('ExplanationFrame', 1))
        intermediate_button['font'] = get_standard_button_font()
        intermediate_button.grid(row=1, column=1)

        pro_button = tk.Button(self, text='Gevorderd', command = lambda: controller.change_frame_and_set_level('ExplanationFrame', 2))
        pro_button['font'] = get_standard_button_font()
        pro_button.grid(row=1, column=2)

        translation_button = tk.Button(self, text='Translation?', command= lambda: open_translation_window(translation))
        translation_button['font'] = get_standard_button_font()
        translation_button.grid(row=2, column=0)



class WelcomeFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        text = "Welkom bij ZINNEN BOUWEN! Leuk dat je er bent. Ik ben Katarina Laken, ik studeer aan de Radboud Universiteit en ik heb dit programma gemaakt voor het vak \'Technology Enhanced Language Learning\' van Helmer Strik.\n\nHet programma \'ZINNEN BOUWEN\' is  gemaakt om je te laten oefenen met het schrijven van korte teksten in het Nederlands. Op die manier wil ik onderzoeken hoe we technologie kunnen gebruiken bij het leren van een taal. NB: het is mogelijk dat de feedback van ZINNEN BOUWEN niet correct of volledig is!\nNa het oefenen zou ik graag willen dat je mijn vragenlijst over \'ZINNEN BOUWEN\' invult. \n\nJe kunt me bereiken op katarina.laken@student.ru.nl.\n\nLaten we beginnen!"

        translation = "Welcome to BUILDING SENTENCES! Nice to have you here. My name is Katarina Laken, I study at Radboud University and I made this program for the course \'Technology Enhanced Language Learning\', taught by Helmer Strik.\n\nThe program \'ZINNEN BOUWEN\' (\'Building Sentences\') is made to help you to write short texts in Dutch in order to research how technology can be used when learning and teaching languages. Note: it is possible that the feedback in ZINNEN BOUWEN is incomplete or incorrect!\nI would like you  to fill out my survey after you completed one round of exercises.\n\nYou can reach me at katarina.laken@student.ru.nl.\n\nLet's get started!"

        translation_button = get_translation_button(self, translation)
        translation_button.grid(row=1, column=0, sticky='w')

        continue_button = tk.Button(self, text='Start!', bg = 'gray', fg = 'red', command=lambda: controller.change_frame('LevelChoiceFrame'))
        continue_button['font'] = font.Font(family='Arial', size=20, weight='bold')
        continue_button.grid(row=1, column=1)

        welcome_text = get_text_block(self)
        welcome_text.insert(tk.END, text)
        welcome_text.grid(row=0, columnspan=2)

class ControlFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

class ZinnenBouwen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('ZINNEN BOUWEN')
        self.geometry('800x450')

        control_frame = ControlFrame(self)
        control_frame.grid()

        self.frames = {}

        for frame_type in (WelcomeFrame, LevelChoiceFrame, ExplanationFrame):
            frame_name = frame_type.__name__
            frame_instance = frame_type(control_frame, self)
            self.frames[frame_name] = frame_instance
            frame_instance.grid(row=0, column=0)

        self.change_frame('WelcomeFrame')

        self.user_level = 0
        self.user_words = []
        self.user_mistakes_log = {}
        self.exercise_loop_index = 100
        self.test_words = {'lopen':'to walk', 'straat':'street', 'vriend':'friend'}

    def change_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.grid(sticky='nsew')
        frame.tkraise()

    def change_frame_and_set_level(self, frame_name, level):
        frame = self.frames[frame_name]
        frame.grid(sticky='nsew')
        frame.tkraise()
        self.user_level = level
        self.set_user_words()

    def set_user_words(self):
        pass

    def set_user_words(self):
        if self.user_level == 0:
            words = {'eten':'to eat', 'mes':'knife', 'vork':'fork'}
            self.user_words.append(words)
            words = {'brood':'bread', 'eten':'to eat', 'boter':'butter'}
            self.user_words.append(words)
            words = {'nodig hebben':'to need', 'geld':'money', 'vaak':'often'}
            self.user_words.append(words)
            words = {'schrijven':'to write', 'brief':'letter', 'tante':'aunt'}
            self.user_words.append(words)
            words = {'slapen':'to sleep', 'bed':'bed', 'eigen':'own'}
            self.user_words.append(words)
        elif self.user_level == 1:
            words = {'paard':'horse', 'wei':'meadow, pasture', 'gras':'grass'}
            self.user_words.append(words)
            words = {'popmuziek':'pop music', 'luisteren':'to listen', 'vriendengroep':'friends group'}
            self.user_words.append(words)
            words = {'volkorenbrood':'wholegrain bread', 'roomboter':'butter (creamy)', 'lekker':'tasty'}
            self.user_words.append(words)
            words = {'hond':'dog', 'blaffen':'to bark', 'mevrouw':'madam'}
            self.user_words.append(words)
            words = {'klasgenoot':'classmate', 'trui':'sweater', 'breien':'to knit'}
            self.user_words.append(words)
        elif self.user_level == 2:
            words = {'schubben':'scale (fish)', 'kieuwen':'gills', 'graat':'bone (fish)'}
            self.user_words.append(words)
            words = {'popmuziek':'pop music', 'luisteren':'to listen', 'vriendengroep':'friends group'}
            self.user_words.append(words)
            words = {'autoband':'car tire', 'pompstation':'gas station', 'tanken':'to refuel'}
            self.user_words.append(words)
            words = {'klasgenoot':'classmate', 'kraag':'collar', 'haken':'to crochet'}
            self.user_words.append(words)
            words = {'zalm':'salmon', 'hengel':'rod', 'aas':'bait'}
            self.user_words.append(words)
        random.shuffle(self.user_words)

    def change_frame_to_test_exercise_frame(self, container, words, is_test=False):
        frame = ExerciseFrame(container, self, words, is_test=True)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def change_to_next_in_exercise_loop(self, container):
        if self.exercise_loop_index == 100:
            self.exercise_loop_index = 0
            frame = IntermediateFrame(container, self)
            frame.grid(row=0, column=0, sticky='nsew')
            frame.tkraise()
        elif len(self.user_words) > self.exercise_loop_index:
            words = self.user_words[self.exercise_loop_index]
            self.exercise_loop_index += 1
            frame = ExerciseFrame(container, self, words)
            frame.grid(row=0, column=0, sticky='nsew')
            frame.tkraise()
        else:
            self.switch_to_final_screen(container)

    def repeat_exercise(self, container):
        words = self.test_words
        if not self.exercise_loop_index == 100: #100 is the value until the program enters the exercise loop after the intermediate frame
            words = self.user_words[self.exercise_loop_index - 1]
        frame = ExerciseFrame(container, self, words)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def switch_to_final_screen(self, container):
        frame = FinalFrame(container, self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()


def main():
    programma = ZinnenBouwen()
    programma.mainloop()
    OUTPUT_FILE.close()

if __name__ == '__main__':
    main()