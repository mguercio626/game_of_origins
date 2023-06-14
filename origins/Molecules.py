from itertools import combinations
#Must: 
    #figure out how molecules form from collisions 
    #Which atoms will collide 
    #How to classify different atoms 
    #Figure out if there will be atoms and ions or just one 
    #prevent particles from being im the same location
molecules=[]
def form_molecule(atoms,min_distance=1):
    for atom1,atom2 in combinations(atoms,2):
        if abs(atom1.x-atom2.x) < min_distance and \
        abs(atom1.y-atom2.y) < min_distance:
       
        #add in requiements for molecule formation
             if abs(atom1.charge)== -abs(atom2.charge): 
                 atom1.vx = atom2.vx
                 atom1.vy = atom2.vx
                 atom1.x = atom2.x + min_distance
                 atom1.y = atom2.y + min_distance
                # add in way to switch list from atoms to molecules
                # need to update rules to apply for molcules and atoms??
             else: 
                 atom1.vx *= -1
                 atom1.vy *= -1
                 atom2.vx *= -1
                 atom2.vx *= -1