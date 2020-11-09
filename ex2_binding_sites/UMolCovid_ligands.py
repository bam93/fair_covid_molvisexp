#Set screen resolution, mandatory for recording in raytracing mode
Screen.SetResolution(1920, 1080, False)

#Useful when recording a long video
Application.runInBackground = True
UnityMolMain.allowIDLE = False

bg_color("gray")
#Avoid pre-computing surfaces for memory and perf purpose
UnityMolMain.disableSurfaceThread = True

#Start raytracing mdoe
UnityMolMain.raytracingMode = True

#Not used in raytracing mode
enableDepthCueing()
setDepthCueingStart(-2.92)
setDepthCueingDensity(0.50)

enableDOF()
setDOFFocusDistance(0.448)
setDOFFocalLength(27.652)
setDOFAperture(7.520)


def renderVideo(path):
    pdbids = ["5RGG","5RGI","5RGH","5RG3","5RG2","5RG1","5RGS","5RGR","5RGK","5RGJ","5RGM","5RGL","5RGO","5RGN","5RGQ","5RGP","5R8T","5REO","5REN","5RFZ","5RFY","5RFR","5RFQ","5RFT","5RFS","5RFV","5RFU","5RFX","5RFW","5RFJ","5RFI","5RFL","5RFK","5RFN","5RFM","5RFP","5RFO","5RG0","5REA","5REC","5REB","5REE","5RED","5REG","5REF","5RE9","5RE8","5RE5","5RE4","5RE7","5RE6","5RFB","5RFA","5RFD","5RFC","5RFF","5RFE","5RFH","5RFG","5REY","5REX","5RF9","5REZ","5RF2","5REP","5RF1","5RES","5RF4","5RER","5RF3","5REU","5RF6","5RET","5RF5","5REW","5RF8","5REV","5RF7","5REI","5REH","5REK","5REJ","5REM","5REL","5RF0","5R84","5R83","5R7Y","5R80","5R82","5R81","5R7Z"]
    startVideo(path, 1920, 1080, 60, pauseAtStart=True)
    pauseVideo()
    for i in pdbids:
        s = fetch(i, showDefaultRep=False, center=False, bioAssembly=True)
        setMolParentTransform(Vector3(0.0036, 0.0101, -1.4304), Vector3(0.0168, 0.0168, 0.0168), Vector3(356.6070, 50.6462, 147.5536), Vector3(0.0000, 0.0000, -1.4250), False)
        sel = select(s.name+" and not protein and not water and not resname DMS PEG IMD", s.name+"_notprotwations", setAsCurrentSelection=False)
        showSelection(sel.name, "hb")
        setRTMaterialType(sel.name, "hb", 7)
        setRTMaterialProperty(sel.name, "hb", "color", Vector3(0.900, 1.000, 0.000))
        setRTMaterialProperty(sel.name, "hb", "intensity", float(2.0))
        setRTMaterialProperty(sel.name, "hb", "transparency", float(0.0))
        protChain = 0
        for c in s.currentModel.GetChains():
            if c.Count > 1000:
                sel = select(c.ToSelectionMDA(), c.ToSelectionName(), setAsCurrentSelection=False);
                showSelection(sel.name, "s", True, True, True, SurfMethod.MSMS)
                if protChain % 2 == 0:
                    #setTransparentSurface(sel.name, 0.20)
                    showSelection(sel.name, "c")
                    colorSelection(sel.name, "c", Color(0.97, 0.535, 0.03, 1.0))
                    # setRTMaterialType(sel.name, "s", 5)
                    # setRTMaterialProperty(sel.name, "s", "eta", float(0.900))
                    setRTMaterialProperty(sel.name, "s", "baseColor", Vector3(0.800, 0.257, 0.221))
                    setRTMaterialProperty(sel.name, "s", "opacity", float(0.350))
                    setRTMaterialProperty(sel.name, "s", "metallic", float(0.800))
                else:
                    colorSelection(sel.name, "s", Color(0.4, 0.6, 0.95, 1.0))
                protChain += 1
        # setHyperBallMetaphore(sel.name, "vdw", False)
        #annotate2DText(Vector2(0.1,0.1), 3.0, s.name, Color.black)
        annotateWorldText(Vector3(0.000, 0.000, -60.000), 0.250, s.name, RGBA(1.000, 1.000, 1.000, 1.000))
        #Restart RT frame !
        RaytracerManager.Instance.restartRTFrame();
        yield APIPython.pythonConsole.waitFrames(1)
        # while RaytracerManager.Instance.denoiserRan() == False and RaytracerManager.Instance.getRTFrameId() < 30:
        while RaytracerManager.Instance.getRTFrameId() < 15: #Wait for enough RT sampling
            yield APIPython.pythonConsole.waitFrames(1)
        unpauseVideo()#Record several frames
        yield APIPython.pythonConsole.waitFrames(90)#Record 1.5 sec (60 frames = 1 sec)
        pauseVideo()
        delete(s.name)
        clearAnnotations()
    stopVideo()#Done
    Application.OpenURL(path)#Open the recorded video


APIPython.pythonConsole.doCoroutine(renderVideo("C:/Users/ME/Desktop/CovidFAIRUMol_ex2.mp4"))

