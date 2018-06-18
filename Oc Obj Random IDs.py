"""

v03

"""

import c4d, random
from random import randint

"""Pendings:

-Support for UnDo y Redo
-revisar el funcionamiento con los octane tags.
-Que soporte childs y seleccione todo.
-Iteracion de objetos correcta.

"""

OCTANE_TAG_ID = 000000000

def get_actObjs():
    #get active objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.')
        return None
    return activeObjects

def main():
    #get all scene objects
    c4d.CallCommand(12112, 12112) # Select All

    activeObjects = get_actObjs()
    if not activeObjects:
        return

    # octane tags list
    obj_octaneTag = []

    for obj in activeObjects:
        obj_tags = obj.GetTags()

        for tag in obj_tags:
            if tag.GetType() == c4d.Tcompositing: # tag operations
                obj_octaneTag.append(tag)

    tag_max_value = 0

    for tag in obj_octaneTag:
        if tag_max_value < tag[c4d.COMPOSITINGTAG_IDCHN0]:
            tag_max_value = tag[c4d.COMPOSITINGTAG_IDCHN0]

    # if octane tag ID is 0, max value will be the len list
    if tag_max_value == 0:
    	tag_max_value = len(obj_octaneTag)

    for tag in obj_octaneTag:
        tag[c4d.COMPOSITINGTAG_IDCHN0] = randint(0, tag_max_value)

    print 'Octane tags updated: ' + str(len(obj_octaneTag))
    print 'Octane tag maximun interation value: ' + str(tag_max_value)

    tag_max_value_toMaterial = 0

    for tag in obj_octaneTag:
    	if tag_max_value_toMaterial < tag[c4d.COMPOSITINGTAG_IDCHN0]:
            tag_max_value_toMaterial = tag[c4d.COMPOSITINGTAG_IDCHN0]

    print 'Octane tag maximun iteration for material: ' + str(tag_max_value_toMaterial)

    # deselect all scene objs
    c4d.CallCommand(12113, 12113) # Deselect All

    c4d.EventAdd()

if __name__=='__main__':
    main()
