from itertools import combinations
#Must: 
    #figure out how molecules form from collisions 
    #Which atoms will collide 
    #How to classify different atoms 
    #Figure out if there will be atoms and ions or just one 
    #prevent particles from being im the same location

def collisions(atoms,min_distance=.5):
    for atom1,atom2 in combinations(atoms,2):
        if abs(atom1.x-atom2.x) < min_distance and \
        abs(atom1.y-atom2.y) < min_distance: 
            atom1.vx *= -1
            atom1.vy *= -1
            atom2.vx *= -1
            atom2.vx *= -1

