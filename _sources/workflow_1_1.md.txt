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
To import files, use the **"Import"** block on the N-panel of the addon (Object mode). Specify the path to the DNA file and the body FBX file. and click **"Import"**. The head mesh will be built from the DNA file. The import operation can take up to a few minutes. Afterwards, you will see two collections: "FBX_HEAD" and "FBX_BODY". The objects that are created in these collections are intended for further export as FBX files. Unlike previous versions, in Metareforge 1.1 each LOD of the head is represented by several objects. This helps in more conveniently editing individual objects in third-party applications, as well as more accurately transferring changes from the editable object to the objects intended for export to UE (for more details on transferring changes, refer to [section 2](#2-creating-edit-meshes-edit-armature-and-other-auxiliary-objects)). 

If you want to import the head from FBX file you may untick "Build Head from DNA" and select head FBX file.
Importing the head FBX files is recommended only in a few situations:
- you are going to utilize your old edit meshes from Metareforge 1.0.X
- you are going to edit a metahuman that has already been edited after importing it from Quixel Bridge.

For all other cases, the "Build Head from DNA" option is preferred.

**Note.** It's not recommended to import FBX files in any other way. The addon removes unnecessary elements, analyzes LODs, and assigns them to the corresponding internal properties (which can be viewed by expanding the "Head Objects" and "Body Objects" drop-down lists).

### 2. Creating Edit Meshes, Edit Armature, and Other Auxiliary Objects
Once the FBX files are imported, we can proceed to initialize auxiliary and editable objects. For this, we move to the **"Edit Shape"** block.

There are two parameters available:
- **Weld Distance:** Determines the distance (centimeters) at which the vertices of the meshes will be welded. The Weld Distance should be sufficient to weld all points at seams intended to be smooth, but at the same time, too large a Weld Distance value might cause other points to merge, making it impossible to apply the Surface Deform modifier, which is vital for subsequent processing. After initialization, you can preliminarily check the meshes for the most common issues that may arise during welding by clicking on the "Validate Edges" and "Validate Faces" buttons, which we will discuss a bit later in this section.

- **Keep ShapeKeys:** By default, this is turned on. You can turn it off to avoid storing shape key data for edit objects and to keep the blend file size manageable. However, in this case, you will not be able to edit corrective shape keys. Remember that the Metahuman LOD0 uses many corrective shape keys to achieve a more realistic appearance, and sometimes it's necessary to adjust some of these shape keys as well as the base mesh.

<a href="./images/initialized.png">
  <p align="center">
    <img src="./images/initialized.png" width="40%" height="40%"/>
  </p>
</a>

To ensure clarity, let's review the terminology used in the addon:

- **Final Mesh:** a mesh tailored for editing. When editing the entire body, the head and body are joined, and all seams are welded.
- **Final Armature:** an armature created for editing. If the entire body is edited, the head and body skeletons are merged into one, removing all duplicates.
- **edit_id:** a tag that links Edit Meshes with the corresponding objects from the FBX collections, which will be exported to Unreal Engine. It is also necessary for the automatic adjustment of bones. For example the changes from the Final Mesh with `edit_id="skin"` will be transfered to the objects with `edit_id="skin"` from FBX_HEAD collection. Similarly the teeth bones will use only the Final Mesh with tag `"teeth"` to adjust their location etc.

Additionally, the add-on creates auxiliary Basis objects:
- **Basis Mesh:** a mesh intended to store the original shape of the mesh.
- **Basis Armature:** the initial skeleton.

**IMPORTANT:** It is advised not to alter these objects unless absolutely necessary. In a standard workflow, these objects do not require any manual editing.

After clicking on "Initialize", you will see the Final Armature and Basis Armature have already been assigned, as well as a list of various parts of the metahuman. By clicking on the arrow in each item of the list, you can select the Final Mesh for the corresponding body part. Expanding the 'Item Details', you can see the assigned Final and Basis meshes for each body part, as well as their edit_id. All these parameters are filled in automatically.

### 3. Switch Between Object Groups
Use the **"View"** block at the top of the menu to switch between LODs and editable objects.
<a href="./images/view.png">
  <p align="center">
    <img src="./images/view.png" width="40%" height="40%"/>
  </p>
</a>

### 3. Editing the Mesh
Once the auxiliary objects are initialized, you can start editing the mesh. Blender offers a wide range of editing capabilities, but if you need more, you can export the Final Mesh and edit it in an external editor.

**It's crucial to remember:**
- The topology and vertex indexing must remain UNCHANGED.
- Always disable symmetry when working in Edit Mode. At first glance, it may seem that it does not work anyway, but in reality, it sometimes snaps individual points, which can result in unwanted cavities or spikes.

Even considering that there are now many different objects, this does not mean that each one needs to be manually edited. We can recommend the following course of action:

- Position the eyes and the teeth meshes according to your sketch or simply where you, as an artist, see them fitting.
- If you have moved the objects in Object Mode, don't forget to apply the transformations (`Ctrl + A -> All Transforms`).
Next, in Sculpt Mode (enable x symmetry if you need), you can work on the skin model. I prefer to start with the Grab and Elastic Deform brushes at the initial stage. I recommend starting with sculpting because only then can you properly use symmetry. In Edit Mode, symmetry does not work as expected due to the fact that Metahuman has asymmetry.
- By combining Edit Mode and Sculpt Mode, you can add more details.
- Transfer changes from skin and teeth to the other objects.


**Editing in third party application:**
If you wish to modify any part of the body in an external application, you will need to export the necessary Final Mesh and then, after editing, import it back into Blender and assign it in the 'Final' field for the corresponding body part. It's important to ensure that the vertex order remains unchanged.

