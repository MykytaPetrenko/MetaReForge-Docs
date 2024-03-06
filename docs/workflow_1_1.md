# Workflow (1.1-beta)

**Currently, the documentation is under development.**

In update 1.1, metareforge has undergone a significant number of changes, therefore familiarizing yourself with this documentation is recommended even if you have confidently used version 1.0. Overall, we have tried to adhere to the same principles as in the development of version 1.0.
We've designed MetaReForge addon interface to be as clear and structured as possible. All features are organized into blocks within the N-panel under the 'MRF' category. The majority of these features are accessible in object mode, while additional utilities for armature editing become available in armature and mesh edit modes.

### Preliminary Setup
First, we need to prepare the files for editing. You will need:

1. The body's FBX file. It is prefered to use a body skeletal mesh that includs all polygons, without any deleted polygons under the clothing.
    - `Content/Metahumans/<NAME>/<SEX>/<HEIGHT>/<WEIGHT>/Body/<BODY_SKELETAL_MESH>`
    - right-click on the corresponding skeletal mesh in the content browser Asset Actions - Export as FBX).

<a href="./images/export_as_fbx.png">
  <p align="center">
    <img src="./images/export_as_fbx.png" width="50%" height="50%"/>
  </p>
</a>
    
2. The DNA file. It's usually found in the Quixel Bridge asset folder. By default, look in 

    - `C:\Users\<USER_NAME>\Documents\Megascans Library\Downloaded\UAssets\<ASSET_ID>\Tier0\asset_ue\MetaHumans\<METAHUMAN_NAME>\SourceAssets`).

<a href="./images/get_original_dna.png">
  <p align="center">
    <img src="./images/get_original_dna.png" width="50%" height="50%"/>
  </p>
</a>

3. Optionaly you may use the head from FBX file. **It is not recommended, but useful in certain cases listed in the [Import](#1-import) section**
    - `Content/Metahumans/<METAHUMAN_NAME>/Face/<METAHUMAN_NAME>_FaceMesh`
    - right-click on the corresponding skeletal mesh in the content browser Asset Actions - Export as FBX).
    - Convert FBX with [Autodesk FBX 2013 Converter](https://aps.autodesk.com/developer/overview/fbx-converter-archives). Do not ignore this step because otherwise, some data, such as shape keys, will be lost! The converter is not supported on Windows 11.

### Scene Setup
The first thing to do when opening a new scene in Blender is to set the units of measurement (this is necessary to match the units in Unreal Engine). The metric system should be selected with a Unit Scale = 0.01. If the units are not set up, the addon panel will display a **Setup Scene** button, which will configure the units as mentioned earlier.

### 1. Import
To import files, use the **"Import"** block on the N-panel of the addon (Object mode). Specify the path to the DNA file and the body FBX file. and click **"Import"**. The head mesh will be built from the DNA file.
If you want to import the head from FBX file you may untick "Build Head from DNA" and select head FBX file.
Importing the head FBX files is recommended only in a few situations:
- you are going to utilize your old edit meshes from Metareforge 1.0.X
- you are going to edit a metahuman that has already been edited after importing it from Quixel Bridge.

For all other cases, the "Build Head from DNA" option is preferred.

**Note.** It's not recommended to import FBX files in any other way. The addon removes unnecessary elements, analyzes LODs, and assigns them to the corresponding internal properties (which can be viewed by expanding the "Head Objects" and "Body Objects" drop-down lists).

### 2. Creating Edit Meshes, Edit Armature, and Other Auxiliary Objects