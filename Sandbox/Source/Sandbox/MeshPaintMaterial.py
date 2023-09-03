import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

# Create new material
MeshPaintMaterial = AssetTools.create_asset("M_MeshPaint", "/Game/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

# Add texture params for each surface
base_colors = []
normals = []
orm = []

# Create vertex color nodes and positions
NodePositionX = -500
NodePositionY = -300

VertexColorNode_Color = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY)
VertexColorNode_Color.set_editor_property('Desc', 'Base_Color')

VertexColorNode_Normal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY*2)
VertexColorNode_Normal.set_editor_property('Desc', 'Normal')

VertexColorNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY*4)
VertexColorNode_R.set_editor_property('Desc', 'R_Occlusion')

VertexColorNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY*6)
VertexColorNode_G.set_editor_property('Desc', 'G_Roughness')

VertexColorNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY*8)
VertexColorNode_B.set_editor_property('Desc', 'B_Metallic')

# Create One minus nodes and positions
OneMinusNode_Color = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX*2, NodePositionY*2)
OneMinusNode_Normal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX*4, NodePositionY*4)
OneMinusNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX*6, NodePositionY*6)
OneMinusNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX*8, NodePositionY*8)
OneMinusNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX*10, NodePositionY*10)

# Create Base Color, Normal, and ORM Texture Parameters

for i in range(5):
    
    # Create Texture Params
    BaseColorParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)
    NormalParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)
    ORMParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)
    
    # Set names and sample types
    BaseColorParam.set_editor_property("ParameterName", unreal.Name("BaseColor_{}".format(i)))
    BaseColorParam.set_editor_property("SamplerSource", unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)

    NormalParam.set_editor_property("ParameterName", unreal.Name("Normal_{}".format(i)))
    NormalParam.set_editor_property("SamplerSource", unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    NormalParam.set_editor_property("SamplerType", unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)

    ORMParam.set_editor_property("ParameterName", unreal.Name("ORM_{}".format(i)))
    ORMParam.set_editor_property("SamplerSource", unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    ORMParam.set_editor_property("SamplerType", unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)

    # Append parameters to their arrays
    base_colors.append(BaseColorParam)
    normals.append(NormalParam)
    orm.append(ORMParam)

#Add lerps for each surface
base_color_lerps = []
normal_lerps = []
orm_r_lerps = []
orm_g_lerps = []
orm_b_lerps = []

for i in range(5):
    base_color_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    normal_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    orm_r_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    orm_g_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    orm_b_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)

    # Append parameters to their arrays
    base_color_lerps.append(base_color_lerp)
    normal_lerps.append(normal_lerp)
    orm_r_lerps.append(orm_r_lerp)
    orm_g_lerps.append(orm_g_lerp)
    orm_b_lerps.append(orm_b_lerp)

# Create Base Color node connections
# Connect Base Color Params to Lerps
MaterialEditLibrary.connect_material_expressions(base_colors[0], '', base_color_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[1], '', base_color_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[2], '', base_color_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[3], '', base_color_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_Color, '', base_color_lerps[0], 'Alpha')

# Connect Vertex Color nodes to Base Color lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', OneMinusNode_Color, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'R', base_color_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'G', base_color_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'B', base_color_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', base_color_lerps[4], 'Alpha')

# Make Base Color lerp connections
MaterialEditLibrary.connect_material_expressions(base_color_lerps[0], '', base_color_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[1], '', base_color_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[2], '', base_color_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[3], '', base_color_lerps[4], 'A')

# Connect last Base Color lerp to material Base Color channel
MaterialEditLibrary.connect_material_property(base_color_lerps[4], '', unreal.MaterialProperty.MP_BASE_COLOR)

# Create Base Color node connections
# Connect Base Color Params to Lerps
MaterialEditLibrary.connect_material_expressions(normals[0], '', normal_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(normals[1], '', normal_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(normals[2], '', normal_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(normals[3], '', normal_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_Normal, '', normal_lerps[0], 'Alpha')

# Connect Vertex Color nodes to Normal lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', OneMinusNode_Normal, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'R', normal_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'G', normal_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'B', normal_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', normal_lerps[4], 'Alpha')

# Make Normal lerp connections
MaterialEditLibrary.connect_material_expressions(normal_lerps[0], '', normal_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[1], '', normal_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[2], '', normal_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[3], '', normal_lerps[4], 'A')

# Connect last Normal lerp to material Normal channel
MaterialEditLibrary.connect_material_property(normal_lerps[4], '', unreal.MaterialProperty.MP_NORMAL)

# Create ORM Ambient Occlusion 'R' node connections
# Connect ORM Ambient Occlusion 'R' Params to Lerps
MaterialEditLibrary.connect_material_expressions(orm[0], 'R', orm_r_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], 'R', orm_r_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], 'R', orm_r_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], 'R', orm_r_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'R', orm_r_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'R', orm_r_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_R, '', orm_r_lerps[0], 'Alpha')

# Connect Vertex Color nodes to ORM Ambient Occlusion 'R' Params lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', OneMinusNode_R, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'R', orm_r_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'G', orm_r_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'B', orm_r_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', orm_r_lerps[4], 'Alpha')

# Make ORM Ambient Occlusion 'R' lerp connections
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[0], '', orm_r_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[1], '', orm_r_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[2], '', orm_r_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[3], '', orm_r_lerps[4], 'A')

# Connect last ORM Ambient Occlusion 'R' lerp to material ORM Ambient Occlusion 'R' channel
MaterialEditLibrary.connect_material_property(orm_r_lerps[4], '', unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

# Create ORM Roughness 'G' node connections
# Connect ORM Roughness 'G' to Lerps
MaterialEditLibrary.connect_material_expressions(orm[0], 'G', orm_g_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], 'G', orm_g_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], 'G', orm_g_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], 'G', orm_g_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'G', orm_g_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'G', orm_g_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_G, '', orm_g_lerps[0], 'Alpha')

# Connect Vertex Color nodes to ORM Roughness 'G' Params lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', OneMinusNode_G, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'R', orm_g_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'G', orm_g_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'B', orm_g_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', orm_g_lerps[4], 'Alpha')

# Make ORM Roughness 'G' lerp connections
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[0], '', orm_g_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[1], '', orm_g_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[2], '', orm_g_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[3], '', orm_g_lerps[4], 'A')

# Connect last ORM Roughness 'G' lerp to material ORM Roughness 'G' channel
MaterialEditLibrary.connect_material_property(orm_g_lerps[4], '', unreal.MaterialProperty.MP_ROUGHNESS)

# Create ORM Metallic 'B' node connections
# Connect ORM Metallic 'B' to Lerps
MaterialEditLibrary.connect_material_expressions(orm[0], 'B', orm_b_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], 'B', orm_b_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], 'B', orm_b_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], 'B', orm_b_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'B', orm_b_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'B', orm_b_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_B, '', orm_b_lerps[0], 'Alpha')

# Connect Vertex Color nodes to ORM Metallic 'B' Params lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', OneMinusNode_B, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'R', orm_b_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'G', orm_b_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'B', orm_b_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', orm_b_lerps[4], 'Alpha')

# Make ORM Metallic 'B' lerp connections
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[0], '', orm_b_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[1], '', orm_b_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[2], '', orm_b_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[3], '', orm_b_lerps[4], 'A')

# Connect last ORM Metallic 'B' lerp to material ORM Metallic 'B' channel
MaterialEditLibrary.connect_material_property(orm_b_lerps[4], '', unreal.MaterialProperty.MP_METALLIC)

# Create Material Instance
MeshPaintInstance = AssetTools.create_asset("MI_MeshPaint", "/Game/MasterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
MaterialEditLibrary.set_material_instance_parent(MeshPaintInstance, MeshPaintMaterial)
MeshPaintInstance.set_editor_property("Parent", MeshPaintMaterial)
MaterialEditLibrary.update_material_instance(MeshPaintInstance)

# Save Material and Instance
EditorAssetLibrary.save_asset("/Game/MasterMaterials/M_MeshPaint", True)
EditorAssetLibrary.save_asset("/Game/MasterMaterials/MI_MeshPaint", True)