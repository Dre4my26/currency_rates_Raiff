from exchange_rate import main


def extractor() -> list:  # extracts last line from time_rate.csv
    whole = open('time_rate.csv', mode='r')
    last = whole.readlines()[-1]
    last = last.split(',')
    whole.close()

    return last


delta = float(0.5)


def last_rate_saver() -> bool:  # saves the last rate to tg_rate.csv to later check it before sending a TG notification
    f = open('tg_rate.csv', mode='r')
    was_rate_datetime = f.readline()
    was_rate = float(was_rate_datetime.split(',')[0])
    if float(extractor()[0]) + delta >= was_rate:
        f = open('tg_rate.csv', mode='w')
        f.write(extractor()[0] + "," + extractor()[1])
        f.close()
        return True
    else:
        return False


if __name__ == '__main__':
    extractor()
    last_rate_saver()
