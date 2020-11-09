clearAnnotations()
setMouseMoveSpeed(5.000)
bg_color("white")
UnityMolMain.disableSurfaceThread = True

inVR = UnityMolMain.inVR()

load(filePath="fair_covid/ex3_mdtraj/bp151.pdb", readHetm=True, forceDSSP=False, showDefaultRep=False, center=False, modelsAsTraj=True, forceStructureType=-1)
loadTraj("bp151", "fair_covid/ex3_mdtraj/bp151.xtc")

#show('c')

#Go to frame 110 
select("resnum 597:900 and protein", "SRBD")
select("resnum 0:596 and protein", "ACE")

showSelection("SRBD", "c")
showSelection("ACE", "c")

select("protein and not ACE and (byres around 3.5 ACE and protein) and not type H", "ITF1", forceCreate=True)
select("protein and not SRBD and (byres around 3.5 SRBD and protein) and not type H", "ITF2", forceCreate=True)

setUpdateSelectionTraj("ITF1", True)
setUpdateSelectionTraj("ITF2", True)

showSelection("ITF1", "hb")
showSelection("ITF2", "hb")

setHyperBallMetaphore("ITF1", "Licorice", True)
setHyperBallMetaphore("ITF2", "Licorice", True)

setRepSize("ITF1", "hb", 0.80)
setRepSize("ITF2", "hb", 0.80)

colorSelection("ACE", "c", RGBA(1.000, 0.756, 0.473, 1.000))
colorSelection("SRBD", "c", RGBA(0.609, 0.735, 1.000, 1.000))

# showSelection("SRBD", "s", True, False, False, SurfMethod.MSMS)
# showSelection("ACE", "s", True, False, False, SurfMethod.MSMS)

# setTransparentSurface("SRBD")
# setTransparentSurface("ACE")

# colorSelection("ACE", "s", RGBA(1.000, 0.756, 0.473, 1.000))
# colorSelection("SRBD", "s", RGBA(0.609, 0.735, 1.000, 1.000))

clearSelections()

enableOutline()
setOutlineThickness(2.0)

if not inVR:
    enableDepthCueing()
    setDepthCueingDensity(0.38)
    setDepthCueingStart(-5.70)
    enableDOF()
    setDOFFocusDistance(0.747)
    setDOFAperture(10.0)
    setDOFFocalLength(75)

if inVR:
    centerOnStructure("bp151")
else:
    setStructurePositionRotation("bp151", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
    #Save parent position
    setMolParentTransform( Vector3(0.0979, -0.0452, -2.1001), Vector3(0.0131, 0.0131, 0.0131), Vector3(325.9454, 225.7427, 342.7948), Vector3(0.0975, -0.0450, -2.1000), lerp=False)

screenshot("fair_covid/ex3_mdtraj/Figure3B.png", 1920, 1080)