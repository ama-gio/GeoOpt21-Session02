#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg

def createRandomSphere(count, rX, rY, rZ, rR):

    randomSphere = []
    

    for i in range(count):

        #in each itereation generate some random points and radii
        random_x = r.randrange(-rX, rX, 2)
        random_y = r.randrange(-rY, rY, 2)
        random_z = r.randrange(-rZ, rZ, 2)
        random_r = r.randrange(-rR, rR, 2)

        #create a sphere with rhino3dm
        random_center = rg.Point3d(random_x, random_y, random_z)
        random_sphere = rg.Sphere(random_center, random_r)
       
        #add sphere to the list
        randomSphere.append(random_sphere)

    return randomSphere