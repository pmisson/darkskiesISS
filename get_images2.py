# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.
import numpy as np
import json
import asciitable
#mission = sys.argv[1]
#lista = sys.argv[2]
mission = "ISS030"
lista = "City_ISS030_3_40_999.txt"


def get_iss_photos(lista, mission, size="small"):
    """
    Gets public photos from ISS missions
    :arg string size: Size of the image from ISS mission
    :returns: A list of photos.
    :rtype: list
    """
    photos = []
    lista=asciitable.read(lista)
    lista=lista.ID
    for i in lista:
        pattern_s = "http://eol.jsc.nasa.gov/sseop/images/ESC/%s/%s/%s-E-%s.JPG" % (
            size,
            mission,
            mission,
            i)
        pattern_b = "http://eol.jsc.nasa.gov/sseop/images/ESC/%s/%s/%s-E-%s.JPG" % (
            'large',
            mission,
            mission,
            i)
        link = "http://eol.jsc.nasa.gov/scripts/sseop/photo.pl?mission=%s&roll=E&frame=%s" % (
            mission,
            i)
        idISS = "%s-E-%s" % (
            mission,
            i)

        tmp = dict(link_small=pattern_s,
                   link_big=pattern_b,
                   link=link,
                   idISS=idISS
                   )

        photos.append(tmp)
    return photos

photos=get_iss_photos(lista,mission)

photos=np.array(photos)
photos=list(photos.astype(str))
f = open('tasks_darkskies.csv', 'w')
f.write("\n".join(photos))
f.close()
