# $Id: spike1.py,v 1.8 2020/04/22 21:39:41 baaden Exp baaden $
# Script (c) 2020 by Marc Baaden, <baaden@smplinux.de>
#
# UnityMol python script to visualize the Covid-19 spike protein

absolutePath = "C:/Users/ME/fair_covid_molvisexp/ex1_spike/"

# activate specific commands to simplify interactive raytracing of the scene
doRT = False

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

load(absolutePath+"6cs2.pdb", center=False)

if not inVR:
    setMolParentTransform( Vector3(-1.1592, 1.0424, -0.2460), Vector3(0.0064, 0.0064, 0.0064), Vector3(87.2821, 97.7300, 270.5491), Vector3(0.0000, 0.0000, -1.5500), False )
else:
    centerOnSelection("6cs2_protein_or_nucleic")

setTransparentCartoon("6cs2_protein_or_nucleic", 0.25)

# show surfaces
#showSelection("6cs2_protein_or_nucleic", "s")
##showSelection("6cs2_protein_or_nucleic", "s", SurfMethod.MSMS)

# color cartoon and surfaces
##colorByChain("6cs2_protein_or_nucleic", "c")
##colorByChain("6cs2_protein_or_nucleic", "s")

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

# helper function to reset and reload after the script has been modified
def restart():
    reset()
    loadScript(absolutePath+"spike1.py")

# helper function to toggle a selname/reptype from hidden to visible and vice versa
def toggleRep(repName,repType):
    if(areRepresentationsOn(repName,repType)):
        hideSelection(repName, repType)
    else:
        showSelection(repName, repType)

###
### Define first example view in terms of the representations, the viewpoint and the annotations
###

def rep1():
    print("Representation of the overall ectodomain")
    #showBoundingBox("6cs2")
    select("6cs2 and chain A and resid 14:667", "A.S1", True, True, True, True, False, False, True)
    showSelection("A.S1", "hb")
    setHyperBallMetaphore("A.S1", "vdw", True)
    colorSelection("A.S1", "hb", bleu1)
    setRepSize("A.S1", "hb", 3.01)
    
    select("6cs2 and chain C and resid 14:667", "C.S1", True, True, True, True, False, False, True)
    showSelection("C.S1", "hb")
    setHyperBallMetaphore("C.S1", "vdw", True)
    colorSelection("C.S1", "hb", bleu3)
    setRepSize("C.S1", "hb", 3.01)
    
    select("6cs2 and chain A and resid 655:1177", "A.S2", True, True, True, True, False, False, True)
    showSelection("A.S2", "hb")
    setHyperBallMetaphore("A.S2", "vdw", True)
    colorSelection("A.S2", "hb", vert1)
    setRepSize("A.S2", "hb", 3.01)
    
    select("6cs2 and chain B and resid 655:1177", "B.S2", True, True, True, True, False, False, True)
    showSelection("B.S2", "hb")
    setHyperBallMetaphore("B.S2", "vdw", True)
    colorSelection("B.S2", "hb", vert2)
    setRepSize("B.S2", "hb", 3.01)
    
    select("6cs2 and chain C and resid 655:1177", "C.S2", True, True, True, True, False, False, True)
    showSelection("C.S2", "hb")
    setHyperBallMetaphore("C.S2", "vdw", True)
    colorSelection("C.S2", "hb", vert3)
    setRepSize("C.S2", "hb", 3.01)
    
    select("6cs2 and chain D", "D.ACE", True, True, True, True, False, False, True)
    showSelection("D.ACE", "hb")
    setHyperBallMetaphore("D.ACE", "vdw", True)
    colorSelection("D.ACE", "hb", oran1)
    setRepSize("D.ACE", "hb", 3.01)
    
    showSelection("6cs2_not_protein_nucleic", "s")
    showSelection("6cs2_not_protein_nucleic", "s", SurfMethod.MSMS)
    colorSelection("6cs2_not_protein_nucleic", "s", RGBA(1.0, 1.0, 0.0, 1.0))
    
    select("6cs2 and chain B and resid 14:667", "B.S1", True, True, True, True, False, False, True)
    showSelection("B.S1", "hb")
    setHyperBallMetaphore("B.S1", "vdw", True)
    colorSelection("B.S1", "hb", bleu2)
    setRepSize("B.S1", "hb", 3.01)

    clearSelections()

def rep1bis():
    print("Representation of the overall ectodomain")
    #showBoundingBox("6cs2")
    select("6cs2 and chain A and resid 14:667", "A.S1", True, True, True, True, False, False, True)
    showSelection("A.S1", "s")
    colorSelection("A.S1", "s", bleu1)
    
    select("6cs2 and chain C and resid 14:667", "C.S1", True, True, True, True, False, False, True)
    showSelection("C.S1", "s")
    colorSelection("C.S1", "s", bleu3)
    
    select("6cs2 and chain A and resid 655:1177", "A.S2", True, True, True, True, False, False, True)
    showSelection("A.S2", "s")
    colorSelection("A.S2", "s", vert1)
    
    select("6cs2 and chain B and resid 655:1177", "B.S2", True, True, True, True, False, False, True)
    showSelection("B.S2", "s")
    colorSelection("B.S2", "s", vert2)
    
    select("6cs2 and chain C and resid 655:1177", "C.S2", True, True, True, True, False, False, True)
    showSelection("C.S2", "s")
    colorSelection("C.S2", "s", vert3)
    
    select("6cs2 and chain D", "D.ACE", True, True, True, True, False, False, True)
    showSelection("D.ACE", "s")
    colorSelection("D.ACE", "s", oran1)
    
    showSelection("6cs2_not_protein_nucleic", "s")
    showSelection("6cs2_not_protein_nucleic", "s", SurfMethod.MSMS)
    colorSelection("6cs2_not_protein_nucleic", "s", RGBA(1.0, 1.0, 0.0, 1.0))
    
    select("6cs2 and chain B and resid 14:667", "B.S1", True, True, True, True, False, False, True)
    showSelection("B.S1", "s")
    colorSelection("B.S1", "s", bleu2)
    clearSelections()

def rep1off():
    hideSelection("A.S1")
    hideSelection("A.S2")
    hideSelection("B.S1")
    hideSelection("B.S2")
    hideSelection("C.S1")
    hideSelection("C.S2")
    hideSelection("D.ACE")
    hideSelection("6cs2_not_protein_nucleic")

# define a helper function to orient the system nicely
def view1():
    #setStructurePositionRotation("6cs2", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
    setMolParentTransform( Vector3(-1.1592, 1.0424, -0.2460), Vector3(0.0064, 0.0064, 0.0064), Vector3(87.2821, 97.7300, 270.5491), Vector3(0.0000, 0.0000, -1.5500) )

def view1b():
    setMolParentTransform( Vector3(-1.0644, 0.9179, -3.0181), Vector3(0.0064, 0.0064, 0.0064), Vector3(345.6059, 355.2745, 176.1258), Vector3(0.0000, 0.0000, -1.5500) )

def doTour():
    rep1()
    clearTour()
    mm = getManipulationManager()
    addSelectionToTour("A.S1")#Equivalent to 'mm.addTour(selM.selections["A.S1"])'
    addSelectionToTour("A.S2")
    addSelectionToTour("B.S1")
    addSelectionToTour("B.S2")
    addSelectionToTour("C.S1")
    addSelectionToTour("C.S2")
    addSelectionToTour("D.ACE")
    mm.resetTour()# Reset the tour to the first selection
    mm.startTour(2.0, 0.75)# Start the tour animation, stop 2 seconds on each selection and transition time is 0.75 seconds

def loadEMMap():
    rep1off()
    hideSelection("D.ACE")
    hideSelection("6cs2_protein_or_nucleic", "c")
    loadDXmap(last().name, absolutePath+"6CS2_chainD_3A_EM.dx")#Load the EM map
    select("6cs2 and chain D", "D.ACE_iso", True, True, True, True, False, False, True)
    showSelection("D.ACE_iso", "dxiso", "6cs2")#Create the iso surface
    showSelection("D.ACE_iso", "c")#Create the iso surface
    colorSelection("D.ACE_iso", "c", Color.white)
    updateDXIso("D.ACE_iso", 0.012)#Default value does not show anything but 0.012 is a "good" level
    setWireframeSurface("D.ACE_iso")#show as a wireframe surface
    setSurfaceWireframe("D.ACE_iso", "dxiso", 0.02)#set the size of the wireframe
    colorSelection("D.ACE_iso", "dxiso", Color.black)#color the map in black
    last().dxr.hideLines()#hide bounding box of the EM map
    clearSelections()
    centerOnSelection("D.ACE_iso", True)

def EMMapOff():
    hideSelection("D.ACE_iso", "dxiso")
    hideSelection("D.ACE_iso", "c")


def reprt():
    #setRTMaterialType("FP2", "cartoon", 7)
    setRTMaterial("D.ACE", "hb", "plastic")
    setRTMaterial("B.S1", "hb", "plastic")
    setRTMaterial("C.S2", "hb", "plastic")
    setRTMaterial("B.S2", "hb", "plastic")
    setRTMaterial("A.S2", "hb", "plastic")
    setRTMaterial("C.S1", "hb", "plastic")
    setRTMaterial("A.S1", "hb", "plastic")
    setRTMaterialType("6cs2_not_protein_nucleic", "hyperball", 7)
    #setRTMaterialProperty("6cs2_not_protein_nucleic", "surface", "intensity", 1.000)
    #setRTMaterialProperty("6cs2_not_protein_nucleic", "surface", "transparency", 0.000)
    #setRTMaterialProperty("6cs2_not_protein_nucleic", "surface", "color", Vector3(1.000, 1.000, 0.120))
    #setRTMaterialType("6cs2_not_protein_nucleic", "surface", 5)
    #setRTMaterialProperty("6cs2_not_protein_nucleic", "surface", "color", Vector3(1.000, 1.000, 0.000))

def viewrt1():
    setStructurePositionRotation("6cs2", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
    setMolParentTransform( Vector3(-0.6684, 1.2884, -0.1273), Vector3(0.0064, 0.0064, 0.0064), Vector3(82.0037, 296.6358, 97.5696), Vector3(0.0000, 0.0000, -1.5500) )
    return;

def viewrt2():
    setStructurePositionRotation("6cs2", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
    setMolParentTransform( Vector3(-0.6184, 1.3509, -0.9129), Vector3(0.0064, 0.0064, 0.0064), Vector3(82.0038, 296.6358, 97.5696), Vector3(0.0500, 0.0625, -2.3356) )

def annot1(mode=1):
    global annotationStatus
    clearAnnotations()
    if mode==0 or (mode==-1 and annotationStatus):
        annotationStatus = False
        return
    s = last()
    if hasattr(UnityMolMain, "iversion"):#introduced in 1.1.3
        # GLYCOSYLATION
        annotateAtomText(s.name, 26768, "<b>Glycosylated chains</b>\n on spike surface", Color.yellow)
        # RED CHAIN
        annotateAtomText(s.name, 1236, "<b>Spike S1</b>\nDown conformation", bleu1)
        # BLUE CHAIN
        annotateAtomText(s.name, 6928, "<b>Spike S1</b>\nUp conformation", bleu2)
        # PINK CHAIN
        annotateAtomText(s.name, 16337, "<b>Spike S1</b>\nDown conformation", bleu3)
        # PURPLE CHAIN
        annotateAtomText(s.name, 24449, "<b>ACE 2\nreceptor</b>", oran1)

        annotateAtomText(s.name, 10449, "SARS Spike Glycoprotein - human ACE2 complex", Color.white)
        annotateAtomText(s.name, 22239, "<b>Spike S2 regions</b>", vert2)
    else:
        # add annotations >>> -1 bug workaround temporary <<<
        #annotateAtomText("6cs2", 26768, "<size=30>Glycosylated chains\n are shown in yellow</size>")
        #
        # structure.currentModel.getAtomWithID() to get access to a specific atom
        # GLYCOSYLATION
        apos = s.currentModel.getAtomWithID(26768).position + Vector3(0.0, 0.0, -10.0)
        annotateWorldText(apos, 0.3, "<b>Glycosylated chains</b>\n on spike surface", RGBA(1, 1, 0, 1))
        # RED CHAIN
        apos = s.currentModel.getAtomWithID(1236).position + Vector3(-10.0, 0.0, -10.0)
        annotateWorldText(apos, 0.3, "<b>Spike S1</b>\nDown conformation", bleu1)
        # BLUE CHAIN
        apos = s.currentModel.getAtomWithID(6928).position + Vector3(15.0, 0.0, 0.0)
        annotateWorldText(apos, 0.3, "<b>Spike S1</b>\nUp conformation", bleu2)
        # PINK CHAIN
        apos = s.currentModel.getAtomWithID(16337).position + Vector3(15.0, 0.0, 0.0)
        annotateWorldText(apos, 0.3, "<b>Spike S1</b>\nDown conformation", bleu3)
        # PURPLE CHAIN
        apos = s.currentModel.getAtomWithID(24449).position + Vector3(15.0, 0.0, 0.0)
        annotateWorldText(apos, 0.3, "<b>ACE 2\nreceptor</b>", oran1)
        # sel.centerOfGravity or structure.currentModel.centerOfGravity to get centroid
        apos = s.currentModel.centroid + Vector3(0.0, 0.0, -100.0)
        annotateWorldText(apos, 0.3, "SARS Spike Glycoprotein - human ACE2 complex", RGBA(1.0, 1.0, 1.0, 1.0))
        apos = s.currentModel.getAtomWithID(22239).position + Vector3(0.0, 0.0, 10.0)
        annotateWorldText(apos, 0.3, "<b>Spike S2 regions</b>", vert2)
        # Some distances to annotate
        #annotateLine("6cs2", 1236, "6cs2", 26768)
        #removeAnnotationLine("6cs2", 1236, "6cs2", 26768)
        #p1 = s.currentModel.getAtomWithID(1236).position
        #p2 = s.currentModel.getAtomWithID(26768).position
        #annotateWorldLine(p1, p2, 0.03, RGBA(1.0, 1.0, 0.0, 1.0))
    annotationStatus = True


###
### Define second example view in terms of the representations, the viewpoint and the annotations
###

def rep2():
    print("Representation of the pre-fusion peptide region FP2")
    select("6cs2 and chain B and resid 820:837", "FP2", True, True, True, True, False, False, True)
    showSelection("FP2", "hb")
    setHyperBallMetaphore("FP2", "Licorice", True)
    showSelection("FP2", "c")
    setMetal("FP2", "c", 0.26)
    setSmoothness("FP2", "c", 1.00)
    setTubeSizeCartoon("FP2", 2.02)
    clearSelections()

def rep2off():
    hideSelection("FP2")

def view2():
    setStructurePositionRotation("6cs2", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
#Save parent position
    setMolParentTransform( Vector3(-0.6251, 0.9782, -0.9723), Vector3(0.0064, 0.0064, 0.0064), Vector3(47.6491, 92.7963, 225.2679), Vector3(-0.0250, 0.0062, -2.8030) )#centerOnSelection("FP2", True, -1.0000)
    #setStructurePositionRotation("6cs2", Vector3(5.9304, 0.0000, 7.0238), Vector3(0.0000, 358.0000, 0.0000))
    #setMolParentTransform( Vector3(1.0390, 1.1267, -1.6719), Vector3(0.0064, 0.0064, 0.0064), Vector3(86.7802, 232.0620, 326.2160), Vector3(0.0000, -0.0001, -2.8085) )
    clearSelections()

#view1()
#ex1()

def rtstartup():
    RaytracerManager.Instance.restartRTFrame();
    while RaytracerManager.Instance.getRTFrameId() < 2: #Wait for enough RT sampling
        yield APIPython.pythonConsole.waitFrames(1)
    #RaytracerManager.Instance.forceDenoiserOff(True)

def screenshotloop():
    counter=1
    RaytracerManager.Instance.restartRTFrame();
    yield APIPython.pythonConsole.waitSeconds(5)
    reprt()
    yield APIPython.pythonConsole.waitSeconds(5)
    while(True):
        screenshot(absolutePath+"rtshot"+str(counter)+".png",1900,1080)
        yield APIPython.pythonConsole.waitSeconds(5)
        counter += 1

# routine to save screenshots of an interactive raytracing session used for the paper
if(doRT):
    rep1()
    hide("s")
    APIPython.pythonConsole.doCoroutine(rtstartup())
    reprt()
    viewrt2()
    reprt()
    APIPython.pythonConsole.doCoroutine(screenshotloop())

# Command line to export scene for import in eg google poly
#exportRepsToFBXFile("6cs2", "ex1_spike.fbx")

