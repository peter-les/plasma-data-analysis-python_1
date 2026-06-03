# statistics.py

import numpy as np


def calculate_periods(
    time,
    imax,
    imin,
):

    periods_max = np.abs(
        np.diff(
            time[imax]
        )
    )

    periods_min = np.abs(
        np.diff(
            time[imin]
        )
    )

    t_average_help = np.mean(
        [
            np.mean(periods_max),
            np.mean(periods_min),
        ]
    )

    filtered_max = periods_max[
        periods_max
        < 2 * t_average_help
    ]

    filtered_min = periods_min[
        periods_min
        < 2 * t_average_help
    ]

    t_periods = np.mean(
        [
            np.mean(filtered_max),
            np.mean(filtered_min),
        ]
    )

    return (
        t_periods,
        periods_max,
        periods_min,
    )


def calculate_motion_statistics(
    ymax,
    ymin,
    imax,
    imin,
    time,
):

    distances = ymax - ymin

    d_average = np.mean(
        distances
    )

    Lmax_average = np.mean(
        ymax
    )

    Lmin_average = np.mean(
        ymin
    )

    times = (
        time[imax]
        - time[imin]
    )

    t_average = np.mean(
        times
    )

    velocities = (
        distances
        / times
        * 1000
    )

    v_average = np.nanmean(
        velocities
    )

    restrike_length = np.mean(
        ymax - ymin
    )

    return {
        "distances": distances,
        "times": times,
        "velocities": velocities,
        "d_average": d_average,
        "Lmax_average": Lmax_average,
        "Lmin_average": Lmin_average,
        "t_average": t_average,
        "v_average": v_average,
        "restrike_length": restrike_length,
    }