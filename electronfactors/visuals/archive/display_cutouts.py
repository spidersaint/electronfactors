# Copyright (C) 2015 Simon Biggs
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public
# License along with this program. If not, see
# http://www.gnu.org/licenses/.

# Make this contain the functions required to show the user the model inputs

import yaml
from glob import glob

import numpy as np
import shapely.affinity as aff

import matplotlib.pyplot as plt
# from matplotlib import pylab

import descartes as des

from ..ellipse.utilities import shapely_ellipse, shapely_cutout
from ..ellipse.fitting import VisualFit, VisualRotate


def find_cached_models(directory="model_cache/"):
    return glob(directory + "*.yml")


def shapely_plot(shapes):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for shape in shapes:
        patch = des.PolygonPatch(
            shape, fc=np.random.uniform(size=3), alpha=0.3)
        ax.add_patch(patch)

    # plt.scatter(0, 0)
    ax.axis("equal")


def display_cutout(**kwargs):
    width = kwargs['width']
    length = kwargs['length']
    factor = kwargs['factor']

    try:
        predicted_factor = kwargs['predicted_factor']

        print(
            "    - Width: %0.2f\n"
            "    - Length: %0.2f\n"
            "    - Measured Factor: %0.4f\n"
            "    - Predicted Factor: %0.4f\n" %
            (
                width, length, factor, predicted_factor
            )
        )
    except:
        print(
            "    - Width: %0.2f\n"
            "    - Length: %0.2f\n"
            "    - Measured Factor: %0.4f\n" %
            (
                width, length, factor
            )
        )

    XCoords = kwargs['XCoords']
    YCoords = kwargs['YCoords']
    cutout = shapely_cutout(XCoords, YCoords)
    ellipse = shapely_ellipse([0, 0, width, length, -45])

    visual_fit = VisualFit(cutout, ellipse)

    shapely_plot([cutout, visual_fit.fitted_shape])
    plt.show()


def load_and_display(directory="model_cache/"):
    filepaths = find_cached_models(directory)

    for path in filepaths:
        print(path + "\n==================================\n")

        with open(path, 'r') as file:
            cache = yaml.load(file)

        label = [key for key in cache]

        for key in label:
            print("  - " + str(key))
            display_cutout(**cache[key])


def display_equivalent_ellipse(eqivalent_ellipse):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # rotate_fit = VisualRotate(
    #     eqivalent_ellipse.straightenedCutout,
    #     eqivalent_ellipse.centredCutout
    # )

    # adjusted_cutout = rotate_fit.fitted_shape

    patch = des.PolygonPatch(
        eqivalent_ellipse.centredCutout,
        fc=np.random.uniform(size=3),
        alpha=0.5)
    ax.add_patch(patch)

    patch = des.PolygonPatch(
        eqivalent_ellipse.straightenedCutout,
        fc=np.random.uniform(size=3),
        alpha=0.3)
    ax.add_patch(patch)

    patch = des.PolygonPatch(
        eqivalent_ellipse.eqEllipse,
        fc=np.random.uniform(size=3),
        alpha=0.3)
    ax.add_patch(patch)

    plt.scatter(0, 0)
    ax.axis("equal")
    plt.grid(True)

    plt.show()