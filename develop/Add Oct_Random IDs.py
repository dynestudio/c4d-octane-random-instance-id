"""

v05

"""

import c4d, random
from random import randint ; from c4d import gui

"""Pendings:

-Support for UnDo y Redo
-disclaimer correcto

"""

OCTANE_TAG_ID = 1029603
  
def get_sel_objects(): # get active objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.') ; return None
    return activeObjects

def addTag(obj, tag_ID):
    # get obj tags
    obj_tags = obj.GetTags()

    if not obj_tags:
        tag = obj.MakeTag(tag_ID) # new tag
    else:
        obj_tags_types = [] # list of tag types
        for t in obj_tags:
            obj_tags_types.append(t.GetType())
            if t.GetType() == tag_ID:
                tag = t

        if not tag_ID in obj_tags_types:
            tag = obj.MakeTag(tag_ID)

    return tag

def main():
    # get obj list
    activeObjects = get_sel_objects()
    if not activeObjects:
        return

    # octane tags list
    obj_octaneTag = []

    # add all octane tags on a list
    for obj in activeObjects:
        octane_tag = addTag(obj, OCTANE_TAG_ID)
        octane_tag[c4d.OBJECTTAG_INSTANCE_ID] = len(activeObjects)
        obj_octaneTag.append(octane_tag)

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

    c4d.EventAdd() # update scene

if __name__=='__main__':
    main()