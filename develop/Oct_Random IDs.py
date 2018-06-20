"""

v04

"""

import c4d, random
from random import randint ; from c4d import gui

"""Pendings:

-Support for UnDo y Redo
-disclaimer correcto

"""

OCTANE_TAG_ID = 1029603
  
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
    
    activeObjects = get_allObjs()
    if not activeObjects:
        return

    # octane tags list
    obj_octaneTag = []

    for obj in activeObjects:
        obj_tags = obj.GetTags()

        for tag in obj_tags:
            if tag.GetType() == OCTANE_TAG_ID: # tag operations
                obj_octaneTag.append(tag)

    tag_max_value = 0

    for tag in obj_octaneTag:
        if tag_max_value < tag[c4d.OBJECTTAG_INSTANCE_ID]:
            tag_max_value = tag[c4d.OBJECTTAG_INSTANCE_ID]

    # if octane tag ID is 0, max value will be the len list
    if tag_max_value == 0:
        tag_max_value = len(obj_octaneTag)

    for tag in obj_octaneTag:
        tag[c4d.OBJECTTAG_INSTANCE_ID] = randint(0, tag_max_value)

    print 'Octane tags updated: ' + str(len(obj_octaneTag))
    print 'Octane tag maximun interation value: ' + str(tag_max_value)

    tag_max_value_toMaterial = 0

    for tag in obj_octaneTag:
        if tag_max_value_toMaterial < tag[c4d.OBJECTTAG_INSTANCE_ID]:
            tag_max_value_toMaterial = tag[c4d.OBJECTTAG_INSTANCE_ID]

    print 'Octane tag maximun iteration for material: ' + str(tag_max_value_toMaterial)

    # deselect all scene objs
    c4d.CallCommand(12113, 12113) # Deselect All

    c4d.EventAdd()

if __name__=='__main__':
    main()