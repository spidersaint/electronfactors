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

import numpy as np
from electronfactors.ellipse.equivalent import poi_distance_method


def test_centre_of_square():

    XCoords = np.array([-3, 3, 3, -3])
    YCoords = np.array([3, 3, -3, -3])

    poi = poi_distance_method(
        XCoords=XCoords, YCoords=YCoords
    )

    assert np.abs(poi[0]) < 0.1
    assert np.abs(poi[1]) < 0.1


def test_centre_of_arbitrary_cutout():

    XCoords = np.array([-1, -0.2, 0, 0.7, 1, 0]) * 4 + 1
    YCoords = np.array([0, -1, -.8, 0, .6, 1]) * 4 - 1

    poi = poi_distance_method(
        XCoords=XCoords, YCoords=YCoords
    )

    assert np.abs(poi[0] - 0.92) < 0.1
    assert np.abs(poi[1] + 0.62) < 0.1
