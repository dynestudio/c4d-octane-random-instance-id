"""

v01

"""

import c4d, random
from random import randint ; from c4d import gui

"""Pendings:

-Support for UnDo y Redo
-disclaimer correcto

"""
 
blend_name = 'bricks b2_no displ'

def get_allObjs():
    def GetNextObject(op): # object manager iteration
        if not op: return None
        if op.GetDown(): return op.GetDown()
        while not op.GetNext() and op.GetUp(): op = op.GetUp()
        return op.GetNext()

    # get first obj
    first_obj = doc.GetFirstObject()
    if not first_obj:
        return None
    # list of all objects in the scene
    list_objs = []
    # add the first obj
    list_objs.append(first_obj) 

    # obj loop iteration
    while first_obj:          
        first_obj = GetNextObject(first_obj)
        if first_obj:
            list_objs.append(first_obj)

    return list_objs

def main():
    # get obj list
    activeObjects = get_allObjs()
    if not activeObjects:
        return

    mat = doc.SearchMaterial(blend_name)

    for obj in activeObjects:
        obj_tags = obj.GetTags()

        for tag in obj_tags:
            if tag.GetType() == c4d.Ttexture: # tag operations
                if tag[c4d.TEXTURETAG_MATERIAL] == mat:
                    print 'Object with blend material detected: ' + obj[c4d.ID_BASELIST_NAME]


if __name__=='__main__':
    main()
