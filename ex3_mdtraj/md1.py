# $Id: md1.py,v 1.8 2020/04/22 21:39:41 baaden Exp baaden $
# Script (c) 2020 by Marc Baaden, <baaden@smplinux.de>
#
# UnityMol python script to visualize the Covid-19 spike protein

# activate specific commands to simplify interactive raytracing of the scene
doRT = False;

inVR = UnityMolMain.inVR()

#Useful when recording a long video
Application.runInBackground = True
UnityMolMain.allowIDLE = False

if(doRT):
    bg_color("gray")
    #Avoid pre-computing surfaces for memory and perf purpose
    UnityMolMain.disableSurfaceThread = True
    #Start raytracing mdoe
    UnityMolMain.raytracingMode = True
    #Set screen resolution, mandatory for recording in raytracing mode
    Screen.SetResolution(1920, 1080, False)



# Color definitions
bleu1 = ColorUtility.TryParseHtmlString("#6baed6")[1]
bleu2 = ColorUtility.TryParseHtmlString("#3182bd")[1]
bleu3 = ColorUtility.TryParseHtmlString("#08519c")[1]
vert1 = ColorUtility.TryParseHtmlString("#74c476")[1]
vert2 = ColorUtility.TryParseHtmlString("#31a354")[1]
vert3 = ColorUtility.TryParseHtmlString("#006d2c")[1]
oran1 = ColorUtility.TryParseHtmlString("#fd8d3c")[1]


# Start clean
reset()
clearAnnotations()
annotationStatus = False
setMouseMoveSpeed(5)

load("bp151.pdb")
loadTraj("bp151", "bp151.xtc")

if inVR:
    centerOnStructure("bp151")
else:
    #fetch(PDBId="6cs2", usemmCIF=True, readHetm=True, forceDSSP=False, showDefaultRep=True, modelsAsTraj=True, center=False)
    #setStructurePositionRotation("bp151", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
    #Save parent position
    setMolParentTransform( Vector3(0.1509, 0.0289, -2.3742), Vector3(0.0064, 0.0064, 0.0064), Vector3(11.1974, 316.3117, 184.7349), Vector3(0.1375, 0.0250, -2.3702) )
    #setMolParentTransform( Vector3(0.1196, 0.1039, -2.1867), Vector3(0.0064, 0.0064, 0.0064), Vector3(11.1974, 316.3117, 184.7349), Vector3(0.1062, 0.1000, -2.1827) )

# draw an outline around the objects
enableOutline()
# add depth cueing
#setDepthCueingDensity(1.00)
#setDepthCueingStart(-1.94)
#enableDepthCueing()

# hide user interface
#GameObject.Find("CanvasMainUI/CloseUI").GetComponent("Button").onClick.Invoke();
# hide python console
#GameObject.Find("ConsolePython_Autocomplete/Canvas/CloseUI").GetComponent("Button").onClick.Invoke();

hideSelection("bp151_protein_or_nucleic", "c")
showHideHydrogensInSelection("bp151_not_protein_nucleic")
setHyperBallMetaphore("bp151_not_protein_nucleic", "Licorice", True)



# helper function to reset and reload after the script has been modified
def restart():
    reset()
    loadScript("md1.py")

# helper function to toggle a selname/reptype from hidden to visible and vice versa
def toggleRep(repName,repType):
    if(areRepresentationsOn(repName,repType)):
        hideSelection(repName, repType)
    else:
        showSelection(repName, repType)

###
### Define first example view in terms of the representations, the viewpoint and the annotations
###

SRBD=select("resnum 597:900 and protein", "SRBD")
ACE=select("resnum 0:596 and protein", "ACE")

def rep1():
    print("Representation of the overall ectodomain")
    #showBoundingBox("6cs2")
    showSelection("SRBD", "c")
    colorSelection("SRBD", "c", bleu3)
    showSelection("ACE", "c")
    colorSelection("ACE", "c", oran1)
    #select("(resnum 154 65 155 10 157 141 539 124 524 76 77 83 143 1 162 121 16 74 161 17 13 143 335 20 173 19 168 23 339 337 117 169 27 166 and protein) or resname UNK7", "ITF")
    select("byres ((around 3.5 ACE) and protein and not ACE)","ITF1")
    setUpdateSelectionTraj("ITF1", True)
    showSelection("ITF1", "hb")
    select("byres ((around 3.5 SRBD) and protein and not SRBD)","ITF2")
    setUpdateSelectionTraj("ITF2", True)
    showSelection("ITF2", "hb")
    clearSelections()

rep1()

def rep1off():
    hideSelection("SRBD")
    hideSelection("ACE")
    hideSelection("ITF1")
    hideSelection("ITF2")
    clearSelections()

# define a helper function to orient the system nicely
def view1():
    #setStructurePositionRotation("6cs2", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
    setMolParentTransform( Vector3(-1.1592, 1.0424, -0.2460), Vector3(0.0064, 0.0064, 0.0064), Vector3(87.2821, 97.7300, 270.5491), Vector3(0.0000, 0.0000, -1.5500) )
    return;
