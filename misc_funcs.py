import csv


class Text:

# READ
    @staticmethod # returns the 4 lists
    def read_topics():
        f = open("topics.txt", "r")
        lines = []
        for line in f:
            li = line.replace("\n", "")
            lines.append(li)
        l = [line.split(",") for line in lines]
        ttypes = l[0]
        tnames = l[1]
        tformat = l[2]
        tinfo = []
        for i in range(len(l) - 3):
            i += 3
            tinfo.append(l[i])
        f.close()

        return ttypes, tnames, tformat, tinfo

    @staticmethod # inputs data from text to list
    def read_data(datas):
        with open("data.txt", 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                datas.append(line)

    @staticmethod
    def get_emojis(emojis):
        f = open("emojist.txt", "r")
        for line in f:
            l = line.replace("\n", "")
            emojis.append(l)
        f.close()

# UPDATE
    @staticmethod
    def update_topics(topictypes, topicsnames, topicformat, topicinfo): # updates topic list
        f = open("topics.txt", "w")
        lines = []
        lists = [topictypes, topicsnames, topicformat]
        for l in lists:
            line = ",".join(l)
            lines.append(line)
        for s in topicinfo:
            line = ",".join(s)
            lines.append(line)
        for line in lines:
            f.write("{}\n".format(line))
        f.close()

    @staticmethod
    def update_data(fieldnames, datas):
        with open("data.txt", 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for thing in datas:
                writer.writerow(thing)


class Time:

    @staticmethod  # returns today's month, day, year
    def get_today(datetime):
        today = datetime.date.today()
        year = today.year
        month = today.month
        day = today.day
        return month, day, year

    @staticmethod  # for the calendar to align w/ weekday names
    def get_first_and_total_days(year, month, monthrange):
        dayofweek, totdays = monthrange(year, month)
        return dayofweek, totdays


class Misc:

    @staticmethod
    def is_int(n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    @staticmethod
    def reset(frame, rowscols):
        for child in frame.winfo_children():
            child.destroy()

        if rowscols:
            for i in range(10):
                frame.grid_rowconfigure(i, weight=0)
                frame.grid_columnconfigure(i, weight=0)