from exchange_rate import main


def extracter() -> float:  # extracts last line from time_rate.csv
    whole = open('time_rate.csv', mode='r')
    last = whole.readlines()[-1]
    last = last.split(',')

    return last[0]


delta = float(0.5)


def last_rate_saver():  # saves the last rate to tg_rate.csv to later check it before sending a TG notification
    f = open('tg_rate.csv', mode='r')
    was_rate = float(f.readline())
    if float(extracter()) + delta >= was_rate:
        f = open('tg_rate.csv', mode='w')
        f.write(extracter())

    return 0


if __name__ == '__main__':
    extracter()
    last_rate_saver()
