
Application.runInBackground = True
UnityMolMain.disableSurfaceThread = True
UnityMolMain.allowIDLE = False

inVR = UnityMolMain.inVR()

bleu1 = ColorUtility.TryParseHtmlString("#6baed6")[1]
bleu2 = ColorUtility.TryParseHtmlString("#3182bd")[1]
bleu3 = ColorUtility.TryParseHtmlString("#08519c")[1]
vert1 = ColorUtility.TryParseHtmlString("#74c476")[1]
vert2 = ColorUtility.TryParseHtmlString("#31a354")[1]
vert3 = ColorUtility.TryParseHtmlString("#006d2c")[1]
oran1 = ColorUtility.TryParseHtmlString("#fd8d3c")[1]

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
    
    hideSelection("6cs2_not_protein_nucleic", "hb")
    showSelection("6cs2_not_protein_nucleic", "s")
    showSelection("6cs2_not_protein_nucleic", "s", SurfMethod.MSMS)
    colorSelection("6cs2_not_protein_nucleic", "s", RGBA(1.0, 1.0, 0.0, 1.0))
    
    select("6cs2 and chain B and resid 14:667", "B.S1", True, True, True, True, False, False, True)
    showSelection("B.S1", "hb")
    setHyperBallMetaphore("B.S1", "vdw", True)
    colorSelection("B.S1", "hb", bleu2)
    setRepSize("B.S1", "hb", 3.01)
    
    clearSelections()

def animation():
    rep1()
    setSolidCartoon("6cs2_protein_or_nucleic")
    setStructurePositionRotation("6cs2", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
    setHyperBallMetaphore("vdw")
    #View 1
    # setMolParentTransform( Vector3(-1.1592, 1.0424, -0.2460), Vector3(0.0064, 0.0064, 0.0064), Vector3(87.2821, 97.7300, 270.5491), Vector3(0.0000, 0.0000, -1.5500), lerp=False)
    # yield APIPython.pythonConsole.waitSeconds(1)
    setMolParentTransform( Vector3(-1.1606, 1.2043, -2.7047), Vector3(0.0064, 0.0064, 0.0064), Vector3(0.0419, 357.5057, 177.4474), Vector3(0.0000, 0.0000, -1.5500), lerp=False)
    yield APIPython.pythonConsole.waitSeconds(1.0)
    setMolParentTransform( Vector3(-1.4590, 0.5564, -3.9388), Vector3(0.0064, 0.0064, 0.0064), Vector3(353.2155, 356.5977, 200.2242), Vector3(0.0500, 0.0500, -2.6750), duration=7.5)
    yield APIPython.pythonConsole.waitSeconds(7.5)
    setHyperBallMetaphore("smooth", lerp=True, duration=2.0)
    setMolParentTransform( Vector3(-1.4590, 0.5564, -4.5638), Vector3(0.0064, 0.0064, 0.0064), Vector3(353.2155, 356.5977, 200.2242), Vector3(0.0500, 0.0500, -3.3000), duration=7.5)
    yield APIPython.pythonConsole.waitSeconds(7.5)
    yield APIPython.pythonConsole.waitSeconds(2.0)    
    #Go back now
    setMolParentTransform( Vector3(-1.4590, 0.5564, -3.9388), Vector3(0.0064, 0.0064, 0.0064), Vector3(353.2155, 356.5977, 200.2242), Vector3(0.0500, 0.0500, -2.6750), duration=7.5)
    yield APIPython.pythonConsole.waitSeconds(7.5)
    setHyperBallMetaphore("vdw", lerp=True, duration=5.0)
    setMolParentTransform( Vector3(-1.1606, 1.2043, -2.7047), Vector3(0.0064, 0.0064, 0.0064), Vector3(0.0419, 357.5057, 177.4474), Vector3(0.0000, 0.0000, -1.5500), duration=5.0)


load("fair_covid/ex1_spike/6cs2.pdb")
enableOutline()

if inVR:
    rep1()
    centerOnSelection("6cs2_protein_or_nucleic")
else:
    APIPython.pythonConsole.doCoroutine(animation())