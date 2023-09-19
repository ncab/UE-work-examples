import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

MasterMaterial = AssetTools.create_asset("M_Master", "/Game/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

# Create 2D texture param and connect to Base Color
BaseColorTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, -200)
MaterialEditLibrary.connect_material_property(BaseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

# Create 2D texture param and connect to Metallic
MetalTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, 50)
MaterialEditLibrary.connect_material_property(MetalTextureParam, "RGB", unreal.MaterialProperty.MP_METALLIC)

# Create constant value and connect to Specular
SpecParam = MaterialEditLibrary.create_material_expression(MasterMaterial, unreal.MaterialExpressionConstant, -500, 300)
SpecParam.set_editor_property("R", 0.3)
MaterialEditLibrary.connect_material_property(SpecParam, "", unreal.MaterialProperty.MP_SPECULAR)

# Create 2D texture param and connect to Roughness
RoughnessTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, 550)
MaterialEditLibrary.connect_material_property(RoughnessTextureParam, "RGB", unreal.MaterialProperty.MP_ROUGHNESS)

# Create 2D texture param and connect to Normal
NormalTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, 800)
MaterialEditLibrary.connect_material_property(NormalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

# Create 2D texture param and connect to Ambient Occlusion
AOTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, 1050)
MaterialEditLibrary.connect_material_property(AOTextureParam, "RGB", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

#Save the material
EditorAssetLibrary.save_asset("/Game/MasterMaterials/M_Master", True)