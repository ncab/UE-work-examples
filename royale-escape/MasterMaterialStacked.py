import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

MasterMaterialStacked = AssetTools.create_asset("M_MasterStacked", "/Game/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

# Create 2D texture param and connect to Base Color
BaseColorTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -500, -200)
MaterialEditLibrary.connect_material_property(BaseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)
BaseColorTextureParam.set_editor_property("parameter_name", "Base Color")

# Create constant value and connect to Specular
SpecParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionScalarParameter, -500, 50)
SpecParam.set_editor_property("default_value", 0.3)
MaterialEditLibrary.connect_material_property(SpecParam, "", unreal.MaterialProperty.MP_SPECULAR)
SpecParam.set_editor_property("parameter_name", "Specular")


# Create 2D texture param and connect to Normal
NormalTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -500, 300)
MaterialEditLibrary.connect_material_property(NormalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)
NormalTextureParam.set_editor_property("parameter_name", "Normal")

# Create 2D texture param and connect to Occlusion, Roughness, and Metallic
ORMTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -500, 550)
MaterialEditLibrary.connect_material_property(ORMTextureParam, "R", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(ORMTextureParam, "G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(ORMTextureParam, "B", unreal.MaterialProperty.MP_METALLIC)
ORMTextureParam.set_editor_property("parameter_name", "ORM")

# Create Material Instance
StackedMatInstance = AssetTools.create_asset("MI_MasterStacked", "/Game/MasterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
StackedMatInstance.set_editor_property("parent", MasterMaterialStacked)

#Save the material and material instance
EditorAssetLibrary.save_asset("/Game/MasterMaterials/M_MasterStacked", True)
EditorAssetLibrary.save_asset("/Game/MasterMaterials/MI_MasterStacked", True)