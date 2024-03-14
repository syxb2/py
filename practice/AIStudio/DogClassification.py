import os
import paddlehub as hub

modulexcp = hub.Module(name="xception71_imagenet")
moduleres = hub.Module(name="resnet_v2_50_imagenet")
modulevgg = hub.Module(name="vgg19_imagenet")


# identify the function used to iterate through all the files in the folder
def listdir(path, pathlist):  # input the list which is used to store the paths
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if os.path.isdir(file_path):
            listdir(file_path, pathlist)
        else:
            pathlist.append(file_path)


bassetpath = "/home/aistudio/test-dog10/1-basset-test"
beaglepath = "/home/aistudio/test-dog10/2-beagle-test"
houndpath = "/home/aistudio/test-dog10/3-gray hound-test"
shepherdpath = "/home/aistudio/test-dog10/4-german shepherd-test"
chnauzerpath = "/home/aistudio/test-dog10/5-schnauzer-test"
spanielpath = "/home/aistudio/test-dog10/6-springer spaniel-test"
labradorpath = "/home/aistudio/test-dog10/7-labrador-test"
cockerpath = "/home/aistudio/test-dog10/8-cocker-test"
sheepdogpath = "/home/aistudio/test-dog10/9-old english sheepdog-test"
shetlandpath = "/home/aistudio/test-dog10/10-shetland-test"
allpath = "/home/aistudio/test-dog10"

bassetlist = []
beaglelist = []
houndlist = []
shepherdlist = []
chnauzerlist = []
spaniellist = []
labradorlist = []
cockerlist = []
sheepdoglist = []
shetlandlist = []

petpath = [
    bassetpath,
    beaglepath,
    houndpath,
    shepherdpath,
    chnauzerpath,
    spanielpath,
    labradorpath,
    cockerpath,
    sheepdogpath,
    shetlandpath,
]
petlist = [
    bassetlist,
    beaglelist,
    houndlist,
    shepherdlist,
    chnauzerlist,
    spaniellist,
    labradorlist,
    cockerlist,
    sheepdoglist,
    shetlandlist,
]

# Identify the dog with one word (identify the folder tags):
pett = [
    "basset",
    "beagle",
    "gray",
    "german",
    "schnauzer",
    "springer",
    "labrador",
    "cocker",
    "sheepdog",
    "shetland",
]

# give value to '<pet>list'
for path, pet in zip(petpath, petlist):
    listdir(path, pet)
# print(bassetlist)

# 'path: animal' in 'dic'
dic = dict()
for petli, pet in zip(petlist, pett):  # petlist is a list
    for petl in petli:
        dic[petl] = [pet]
# print(dic)

# 'pathlist' has all-pic's path
pathlist = []
listdir(allpath, pathlist)
# print(pathlist)

# ------------------------------------------------------CONDUCT CLASSIFICATION--------------------------------------------------------- #

# conduct classification with xcption17:
xcor = 0
xtot = 0
for i in pathlist:
    xtot += 1
    input_dict = {"image": [i]}
    results = modulexcp.classification(data=input_dict)
    print("xcption17's predicted class: %s" % (list(results[0][0].keys()))[0])
    l = list((results[0][0]).keys())
    print("real class: %s" % (dic[i][0]))
    if l[0].lower().find(dic[i][0]) != -1:
        xcor += 1
        print("True")
    else:
        print("False")
    print(" ")

print(
    "/*------------------------------------RESULT----------------------------------------*/"
)
print("xcption17's correctness is : %lf" % (xcor / xtot))
print(" ")

# conduct classification with resnet50:
rcor = 0
rtot = 0
for i in pathlist:
    rtot += 1
    input_dict = {"image": [i]}
    results = moduleres.classification(data=input_dict)
    print("resnet50's predicted class: %s" % (list(results[0][0].keys()))[0])
    l = list((results[0][0]).keys())
    print("real class: %s" % (dic[i][0]))
    if l[0].lower().find(dic[i][0]) != -1:
        rcor += 1
        print("True")
    else:
        print("False")
    print(" ")

print(
    "/*------------------------------------RESULT----------------------------------------*/"
)
print("resnet50's correctness is : %lf" % (rcor / rtot))
print(" ")

# conduct classification with vgg19:
vcor = 0
vtot = 0
for i in pathlist:
    vtot += 1
    input_dict = {"image": [i]}
    results = modulevgg.classification(data=input_dict)
    print("vgg19's predicted class: %s" % (list(results[0][0].keys()))[0])
    l = list((results[0][0]).keys())
    print("real class: %s" % (dic[i][0]))
    if l[0].lower().find(dic[i][0]) != -1:
        vcor += 1
        print("True")
    else:
        print("False")
    print(" ")

print(
    "/*------------------------------------RESULT----------------------------------------*/"
)
print("vgg19's correctness is : %lf" % (vcor / vtot))
print(" ")
