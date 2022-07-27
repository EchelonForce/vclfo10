# pcbname.GTL          Top Copper
# pcbname.GTS          Top Soldermask
# pcbname.GTO          Top Silkscreen
# pcbname.GBL          Bottom copper
# pcbname.GBS          Bottom Soldermask:
# pcbname.GBO          Bottom Silkscreen:
# pcbname.TXT          Drills
# pcbname.GML/GKO      Board Outline
# pcbname.GL2          Inner Layer 2 (for ≥ 4 layer)
# pcbname.GL3          Inner Layer 3 (for ≥ 4 layer)

# Notes:
# 1. Gerber files should be in RS-274X format (RS-274D is not recommended due to issues reading the files).
# 2. Drill file (PCBname.TXT) should be in Excellon format.
# 3. Gerber file and Drill file (PCB name.TXT) should be included in the same folder.
# 4. The board outline is required, ideally in an isolated mechanical layer.

import os, zipfile
from shutil import copyfile


def rename(folder, input_name, output_name):

    extensions = [
        ("-B_Cu.gbr", ".GBL"),
        ("-B_Mask.gbr", ".GBS"),
        ("-B_SilkScreen.gbr", ".GBO"),
        ("-Edge_Cuts.gbr", ".GML"),
        ("-F_Cu.gbr", ".GTL"),
        ("-F_Mask.gbr", ".GTS"),
        ("-F_SilkScreen.gbr", ".GTO"),
        (".drl", ".TXT"),
    ]

    os.mkdir(folder + "\\seeed_fusion\\")
    for a in extensions:
        (in_ext, out_ext) = a

        copyfile(
            folder + "\\" + input_name + in_ext,
            folder + "\\seeed_fusion\\" + output_name + out_ext,
        )

    os.chdir(folder + "\\seeed_fusion\\")
    with zipfile.ZipFile(output_name + ".zip", "w") as myzip:
        for a in extensions:
            (in_ext, out_ext) = a
            myzip.write(output_name + out_ext)

folder = ".\outputs"
input_name = "VCLFO10"
output_name = "VCLFO10"

rename(folder, input_name, output_name)
