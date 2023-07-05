import matplotlib.pyplot as plt
import numpy as np

from remote.client import fetch_data


def generate_charts(start_date, end_date):
    views = fetch_data(start_date, end_date)

    dates = []
    owners = []

    for view in views:
        if view.data not in dates:
            dates.append(view.data)
        if view.wlasciciel not in owners:
            owners.append(view.wlasciciel)

    means = {}

    for date in dates:
        for wlasiciel in owners:
            energia_oddana = 0
            for view in views:
                if view.data == date and view.wlasciciel == wlasiciel:
                    energia_oddana = view.energia_oddana
            if wlasiciel not in means:
                means[wlasiciel] = []
            means[wlasiciel].append(energia_oddana)
    x = np.arange(len(dates))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Energia oddana')
    ax.set_title('Energia oddana względem daty')
    ax.set_xticks(x + width, dates)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 250)

    plt.show()

