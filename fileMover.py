import os
from os import path
import shutil

def copyPastaFiles():
    src = "C:\\sbsdev\\SAFEWorkflow\\SBS.Platform.safeworkflow\\SAFEWorkflow.UITestFramework\\build\\netcoreapp3.1\\Reports\\"
    dst = "C:\\Users\\sekick\\Desktop\\KemoRELX\\Canopy\\Archived Reports\\December"

    files = [i for i in os.listdir(src) if i.startswith("testResults") and path.isfile(path.join(src, i))]

    for f in files:
        shutil.copy(path.join(src, f), dst)