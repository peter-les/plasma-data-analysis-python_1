# plotting.py

import matplotlib.pyplot as plt


def plot_attachment(
    time,
    position,
    imax,
    imin,
    ymax,
    ymin,
    pressure,
):
    plt.figure(
        figsize=(12, 8)
    )

    plt.plot(
        time / 1000,
        position,
        "xm",
        markersize=6,
        label="Position",
    )

    plt.plot(
        time[imax] / 1000,
        ymax,
        "ro",
        markersize=8,
        label="Maxima",
    )

    plt.plot(
        time[imin] / 1000,
        ymin,
        "go",
        markersize=8,
        label="Minima",
    )

    plt.xlabel(
        "time [ms]"
    )

    plt.ylabel(
        "position [mm]"
    )

    plt.ylim(
        [0, 20]
    )

    plt.title(
        f"{pressure} mbar"
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()