"""Plots for Homework 4, Problems 1 and 2."""

import numpy as np
import matplotlib.pyplot as plt


def quadratic_sum(x, n):
    y = np.full_like(x, np.pi**2 / 3)
    for k in range(1, n + 1):
        y += 4 * (-1)**k * np.cos(k*x) / k**2
    return y


def pulse_sum(x, n):
    y = np.full_like(x, 0.5)
    for k in range(1, n + 1):
        y += 2 * np.sin(k*np.pi/2) * np.cos(k*np.pi*x) / (k*np.pi)
    return y


def draw(x, f, terms, partial_sum, filename):
    plt.figure(figsize=(8, 4.5))
    plt.plot(x, f, color="black", linewidth=2, label=r"$f$")
    for n in terms:
        plt.plot(x, partial_sum(x, n), label=rf"$S_{{{n}}}$")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")
    plt.grid(alpha=0.2)
    plt.legend(ncol=5, fontsize=9)
    plt.tight_layout()
    plt.savefig(filename, dpi=180)
    plt.close()


x = np.linspace(-np.pi, np.pi, 1601)
draw(x, x**2, (1, 2, 5, 7), quadratic_sum, "hw04_problem1_plot.png")

x = np.linspace(-2*np.pi, 2*np.pi, 2401)
wrapped = (x + np.pi) % (2*np.pi) - np.pi
draw(x, wrapped**2, (1, 2, 5, 7), quadratic_sum,
     "hw04_problem1_periodic_plot.png")

x = np.linspace(-1, 1, 2401)
f = np.where((x > -0.5) & (x <= 0.5), 1, 0)
draw(x, f, (5, 10, 20, 40), pulse_sum, "hw04_problem2_plot.png")
