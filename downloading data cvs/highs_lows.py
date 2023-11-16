import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename_ca = 'death_valley_2014.csv'
with (open(filename_ca) as f):
    reader = csv.reader(f)
    header_row = next(reader)

    dates_ca, highs_ca, lows_ca = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_ca.append(current_date)
            highs_ca.append(high)
            lows_ca.append(low)

filename_al = 'sitka_weather_2014.csv'
with (open(filename_al) as f):
    reader = csv.reader(f)
    header_row = next(reader)

    dates_al, highs_al, lows_al = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_al.append(current_date)
            highs_al.append(high)
            lows_al.append(low)

    # Plot data.
    fig = plt.figure(dpi=128, figsize=(16, 6))
    plt.plot(dates_ca, highs_ca, c='red', alpha=0.5)
    plt.plot(dates_ca, lows_ca, c='blue', alpha=0.5)
    plt.fill_between(dates_ca,highs_ca,lows_ca, facecolor='blue', alpha=0.1)
    plt.plot(dates_al, highs_al, c='red', alpha=0.5)
    plt.plot(dates_al, lows_al, c='blue', alpha=0.5)
    plt.fill_between(dates_al, highs_al, lows_al, facecolor='red', alpha=0.1)

    # Format plot.
    title = "Daily high and low temperatures - 2014\nDeath Valley,CA"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)