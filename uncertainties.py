# uncertainties.py

import numpy as np


def get_uncertainties(
    velocity,
    U=0,
):
    uncertainty = {}

    uncertainty[1] = 4 / 1
    uncertainty[2] = 2 / np.sqrt(3)

    uncertainty[3] = 0.5 / np.sqrt(3) / 200

    uncertainty[4] = (
        0.3
        * velocity
        / np.sqrt(3)
        / 1e3
    )

    uncertainty[5] = (
        0.1
        * velocity
        / np.sqrt(3)
        / 1e3
    )

    uncertainty[7] = 1.0

    uncertainty[8] = 0.0

    uncertainty[9] = (
        0.01
        * np.mean(np.atleast_1d(U))
    )

    uncertainty[10] = 5.0

    uncertainty[11] = (
        0.5 / np.sqrt(3)
    )

    uncertainty[12] = (
        0.013 / np.sqrt(3)
    )

    uncertainty[13] = (
        0.2 / np.sqrt(3)
    )

    uncertainty[14] = (
        0.29 / np.sqrt(3)
    )

    uncertainty[15] = (
        (10 / 3)
        / np.sqrt(3)
    )

    uncertainty[16] = (
        2 / np.sqrt(3)
    )

    return uncertainty


def calculate_output_uncertainties(
    velocities,
    distances,
    times,
    ymax,
    ymin,
    periods_max,
    periods_min,
    v_average,
    d_average,
    t_average,
):
    unc = get_uncertainties(
        v_average
    )

    std_d = 2 * unc[3]

    Lmax_std = (
        2
        * np.sqrt(
            (
                np.std(
                    ymax,
                    ddof=1,
                )
                / np.sqrt(
                    len(ymax)
                )
            )
            ** 2
            + unc[3] ** 2
        )
    )

    Lmin_std = (
        2
        * np.sqrt(
            (
                np.std(
                    ymin,
                    ddof=1,
                )
                / np.sqrt(
                    len(ymin)
                )
            )
            ** 2
            + unc[3] ** 2
        )
    )

    d_std = (
        2
        * np.sqrt(
            (
                np.nanstd(
                    distances,
                    ddof=1,
                )
                / np.sqrt(
                    np.sum(
                        ~np.isnan(
                            distances
                        )
                    )
                )
            )
            ** 2
            + std_d ** 2
        )
    )

    v_std_A = (
        np.nanstd(
            velocities,
            ddof=1,
        )
        / np.sqrt(
            np.sum(
                ~np.isnan(
                    velocities
                )
            )
        )
    )

    std_t = (
        2
        * unc[14]
    )

    t_std = (
        2
        * np.sqrt(
            (
                np.std(
                    times,
                    ddof=1,
                )
                / np.sqrt(
                    len(times)
                )
            )
            ** 2
            + std_t ** 2
        )
    )

    v_std_B = (
        v_average
        * np.sqrt(
            (std_d / d_average)
            ** 2
            + (std_t / t_average)
            ** 2
        )
    )

    v_std = (
        2
        * np.sqrt(
            v_std_A ** 2
            + v_std_B ** 2
        )
    )

    t_periods_std_A = (
        (
            np.std(
                periods_max,
                ddof=1,
            )
            / np.sqrt(
                len(periods_max)
            )
        )
        +
        (
            np.std(
                periods_min,
                ddof=1,
            )
            / np.sqrt(
                len(periods_min)
            )
        )
    ) / 2

    t_periods_std_B = np.sqrt(
        (
            2
            * unc[14]
        )
        ** 2
    )

    t_periods_std = (
        2
        * np.sqrt(
            t_periods_std_A ** 2
            + t_periods_std_B ** 2
        )
    )

    return {
        "v_std": v_std,
        "t_std": t_std,
        "d_std": d_std,
        "t_periods_std": t_periods_std,
        "Lmin_std": Lmin_std,
        "Lmax_std": Lmax_std,
    }