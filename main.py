import pandas as pd
from argparse import ArgumentParser


def print_mail_from(csv_filename):
    df = pd.read_csv(csv_filename)
    saved_column = df.Email
    mails = saved_column.tolist()
    mail_file = open("verteiler.txt", mode='w')
    for i in range(0, len(mails)-1):
        mail_file.write(mails[i] + ", ")
    mail_file.write(mails[-1])
    mail_file.close()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="csv_file", help="Open specified file")

    args = parser.parse_args()
    csv_file = args.csv_file

    print_mail_from(csv_file)
