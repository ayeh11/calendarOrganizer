from tkinter import *
from tkinter import messagebox
import datetime
from calendar import monthrange
import csv

from misc_funcs import Text, Time, Misc
from gui_funcs import Screen

root = Tk()
root.title("Monthly Tracker")
root.geometry("1000x800")

data = []
emojis = []
fieldnames = ["date", "t1", "t2", "t3", "t4", "t5"]

num_topics = 5
topic_choices = ["choice", "text", "number", "y/n"]
days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]

themes = ["modern", "cute", "greenery"]
theme = "modern"
colors = ["lightgrey", "lightblue", "white"]

topictypes, topicsnames, topicformat, topicinfo = Text.read_topics()

now_month, now_day, now_year = Time.get_today(datetime)

class Month:
    def __init__(self, main_frame, month, year, boxwid):
        self.month = 0
        self.datas = []
        self.frames = []
        self.main_frame = main_frame
        self.boxwid = boxwid
        self.first_day_of_month, self.totdays = Time.get_first_and_total_days(year, month, monthrange)  # mon is 0

    # own day
    # data should be sorted by month

    def self_screen(self):
        self.create_top_header(self.frames, self.month)
        self.create_days(self.main_frame, self.first_day_of_month, self.totdays, now_day, self.boxwid, colors)

    def create_top_header(self, frame, month):
        Screen.main_top_header(frame, month, days)
        settings_but = Button(frame, text='settings', command=settings)
        settings_but.grid(row=0, column=2, sticky='nsew')

    def create_days(self, main_frame, first_day_of_month, totdays, today, boxwid, colors):
        Screen.main_days(main_frame, first_day_of_month, totdays, today, boxwid, colors)
        self.widgets_in_frames(self.frames, self.datas)

    def widgets_in_frames(self, frames, datas):
        done = False
        fontsize = 15
        nspace = []
        cspace = []
        ynspace = []
        for d in range(len(self.datas)):
            for tf in range(len(topicformat)):
                if topicformat[tf] == "T":
                    topicnum = int(topicformat[1])
                    day = datas[d]['date'].split("-")
                    Misc.reset(frames[int(day[1]) - 1], False)
                    Label(frames[int(day[1]) - 1], text=day[1], anchor='n').grid(row=0, column=0, columnspan=4)
                    text = "{}...".format(datas[d]['t{}'.format(topicnum + 1)][0:20])
                    Label(frames[int(day[1]) - 1], text=text, bg=topicinfo[topicnum]).grid(columnspan=4, rowspan=2)
                    done = True
                elif not done:
                    allminis = Screen.mini_frames(frames, datas)
                    if Misc.is_int(topicformat[tf]):
                        num = int(topicformat[tf])
                        type = topictypes[num]
                        if type == "number":
                            nspace.append((num, tf, d))
                        elif type == "choice":
                            cspace.append((num, tf, d))
                        elif type == "y/n":
                            ynspace.append((num, tf, d))

        for n in range(len(nspace)):
            num, space, d = nspace[n]
            text = datas[d]['t{}'.format(num + 1)]
            Label(allminis[d][space], text=text, font=("Arial", fontsize)).grid(sticky='e')
            Label(allminis[d][space + 1], text=topicinfo[num], font=("Arial", fontsize)).grid(sticky='w')

        for c in range(len(cspace)):
            num, space, d = cspace[c]
            text = datas[d]['t{}'.format(num + 1)]
            Label(allminis[d][space], text=text, font=("Arial", fontsize)).grid()

        for y in range(len(ynspace)):
            num, space, d = ynspace[y]
            text = datas[d]['t{}'.format(num + 1)]
            if text == "1":
                Label(allminis[d][space], text=topicinfo[num], font=("Arial", fontsize)).grid()


def settings():
    Misc.reset(root, False)
    topframe, leftframe, rightframe = Screen.settings(root, colors)

    Button(topframe, text="Home", padx=10, pady=10, command=main_screen).grid(row=0, column=1, sticky='ne')
    Label(topframe, text="Settings", font=("Arial", 40), padx=10).grid(row=1, column=0)

    topic_button = Button(leftframe, text='Topics', command=lambda: set_topics(rightframe), pady=10)
    format_button = Button(leftframe, text='Format', command=lambda: set_formatting(rightframe), pady=10)
    topic_button.grid(row=0, column=0, sticky='nsew')
    format_button.grid(row=1, column=0, sticky='nsew')

def main_screen():
    Misc.reset(root, True)

    top_main_frame, main_frame, boxwid = Screen.main_screen(root)

    month = Month(main_frame, now_month, now_year, boxwid)
    month.self_screen()

    # Button(main_frame, text="Log", command=lambda: daily_log(now_month, now_day, totdays)).grid(column=6)

Text.get_emojis(emojis)
Text.read_data(data)
main_screen()
root.mainloop()