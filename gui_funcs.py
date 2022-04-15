import datetime
from tkinter import *

class Screen:

    @staticmethod
    def main_screen(root):
        top_main_frame = Frame(root)
        main_frame = Frame(root)
        top_main_frame.grid(row=0, column=0, sticky='nsew')
        main_frame.grid(row=1, column=0, stick='nsew')

        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=5)

        boxwid = root.winfo_screenwidth() / 7 / 1.92
        for c in range(7):
            if c != 6:
                main_frame.grid_rowconfigure(c, minsize=100, weight=1)
            main_frame.grid_columnconfigure(c, minsize=boxwid, weight=1)

        return top_main_frame, main_frame, boxwid

    @staticmethod
    def main_top_header(frame, month, days):
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=5)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=10)
        frame.grid_columnconfigure(2, weight=1)

        x = datetime.datetime(2000, month, 1)
        Label(frame, text=x.strftime("%B"), font=("Arial", 40), anchor='w').grid(row=1, column=1, sticky='nsew')

        botframe = Frame(frame)
        botframe.grid(row=2, column=0, columnspan=3, sticky="ew")
        for d in range(len(days)):
            Label(botframe, text=days[d]).grid(row=0, column=d)
            botframe.grid_columnconfigure(d, weight=1)

    @staticmethod
    def main_days(main_frame, first_day_of_month, totdays, today, boxwid, colors):
        frames = []
        for t in range(1, totdays + 1):
            c = (t + first_day_of_month) % 7
            r = (t + first_day_of_month) // 7
            f = Frame(main_frame, width=boxwid, highlightbackground=colors[0], highlightthickness="1", bg=colors[2])
            f.grid(row=r, column=c, sticky='nsew')
            frames.append(f)
            f.grid_columnconfigure(0, weight=1)
            Label(f, text=t, anchor='n').grid(row=0, column=0, columnspan=4)

        frames[today - 1]["bg"] = colors[1]

    @staticmethod
    def mini_frames(frames, datas):
        allminis = []
        for d in range(len(datas)):
            minis = []
            splitdate = datas[d]['date'].split("-")
            frame = frames[int(splitdate[1]) - 1]
            for r in range(2):
                frame.grid_rowconfigure(r + 1, weight=1)
                for c in range(4):
                    frame.grid_columnconfigure(c, weight=1)
                    f = Frame(frame)
                    f.grid(row=r + 1, column=c, sticky='nsew')
                    f.grid_columnconfigure(0, weight=1)
                    f.grid_rowconfigure(0, weight=1)
                    minis.append(f)
            allminis.append(minis)

        return allminis

    @staticmethod
    def settings(root, colors):
        topframe = Frame(root)
        frame = Frame(root)
        leftframe = Frame(frame, highlightbackground=colors[0], highlightthickness="2")
        rightframe = Frame(frame, highlightbackground=colors[0], highlightthickness="2")

        root.grid_rowconfigure(1, weight=10)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=2)
        leftframe.grid_columnconfigure(0, weight=1)
        topframe.grid_columnconfigure(0, weight=1)
        topframe.grid_columnconfigure(1, weight=1)

        topframe.grid(row=0, column=0, sticky='nsew')
        frame.grid(row=1, column=0, sticky='nsew')
        leftframe.grid(row=0, column=0, sticky='nsew')
        rightframe.grid(row=0, column=1, sticky='nsew')

        return topframe, leftframe, rightframe