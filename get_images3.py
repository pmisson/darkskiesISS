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
import time,os

#mission = sys.argv[1]
#lista = sys.argv[2]
lista = "ISS042_lista3.txt"


def get_iss_photos(lista,size="small"):
    """
    Gets public photos from ISS missions
    :arg string size: Size of the image from ISS mission
    :returns: A list of photos.
    :rtype: list
    """
    photos = []
    lista=asciitable.read(lista)
    lista=lista.ID
    pattern_s_L=[]
    pattern_b_L=[]
    link_L=[]
    idiss=[] 
    for i in lista:
        pattern_s = "http://eol.jsc.nasa.gov/DatabaseImages/ESC/%s/%s/%s-E-%s.JPG" % (
            size,
            i[0:6],
            i[0:6],
            i[9:])
        pattern_b = "http://eol.jsc.nasa.gov/DatabaseImages/ESC/%s/%s/%s-E-%s.JPG" % (
            'large',
            i[0:6],
            i[0:6],
            i[9:])
        link = "http://eol.jsc.nasa.gov/SearchPhotos/photo.pl?mission=%s&roll=E&frame=%s" % (
            i[0:6],
            i[9:])
        idISS = "%s-E-%s" % (
            i[0:6],
            i[9:])
        pattern_s_L.append(pattern_s)
        pattern_b_L.append(pattern_b)
        link_L.append(link)
        idiss.append(idISS)

        tmp = dict(link_small=pattern_s,
                   link_big=pattern_b,
                   link=link,
                   idISS=idISS
                   )

        photos.append(tmp)
    return photos,pattern_s_L,pattern_b_L,link_L,idiss

photos,link_small,link_big,link,idiss=get_iss_photos(lista)

photos=np.array(photos)
photos=list(photos.astype(str))
f = open('tasks_darkskies.csv', 'w')
f.write("\n".join(photos))
f.close()
for h in list(np.array(range(len(idiss)/100+1))+1):
    idiss_j=np.array(idiss[(h-1)*100:h*100])
    link_j=np.array(link[(h-1)*100:h*100])
    link_small_j=np.array(link_small[(h-1)*100:h*100])
    link_big_j=np.array(link_big[(h-1)*100:h*100])

    print "Creating"
    asciitable.write({'idiss': idiss_j, 'link': link_j,'link_small':link_small_j,'link_big':link_big_j}, 'test2.csv', names=['idiss','link','link_small','link_big'],delimiter=',')
    print "Uploading"
    os.system('pbs add_tasks --tasks-file test2.csv --tasks-type csv --redundancy 5')
    print (h-1)*100
    print h*100
    print "Waiting"
    time.sleep(1000)
