#applying the Subset Multidimensional Raster tool in ArcGIS Pro to subset CDD and HDD projections for each of the four climate scenarios  

arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA Historical",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\CDD_Hist.crf",
    variables="'Cooling Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster="U.S. Climate Thresholds - LOCA RCP 4.5 Early Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\CDD_EC_45.crf",
    variables="'Cooling Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\CDD_LC_45.crf",
    variables="'Cooling Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 8.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\CDD_LC_85.crf",
    variables="'Cooling Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA Historical",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\HDD_Hist.crf",
    variables="'Heating Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Early Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\HDD_EC_45.crf",
    variables="'Heating Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\HDD_LC_45.crf",
    variables="'Heating Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 8.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\HDD_LC_85.crf",
    variables="'Heating Degree Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)

#Extract Multi Values to Points for SLR Flooding, CDD, HDD, Dry Days, Days over 90F
arcpy.sa.ExtractMultiValuesToPoints(
    in_point_features="MDF Museums",
    in_rasters=r"'Climate Projections\Sea Level Rise\U.S. Minor High Tide Flooding' SLR_HighTide;'Climate Projections\Sea Level Rise\  U.S. Sea Level Rise - Intermediate (2030)' SLR_EC_Int;'Climate Projections\Sea Level Rise\U.S. Sea Level Rise - Intermediate (2090)' SLR_LC_Int;'Climate Projections\Sea Level Rise\U.S. Sea Level Rise - Intermediate-High (2090)' SLR_LC_IntHigh;'Climate Projections\Heating Degree Days\HDD_Hist.crf' HDD_Hist;'Climate Projections\Heating Degree Days\HDD_EC_45.crf' HDD_EC_45;'Climate Projections\Heating Degree Days\HDD_LC_45.crf' HDD_LC_45;'Climate Projections\Heating Degree Days\HDD_LC_85.crf' HDD_LC_85;'Climate Projections\Consecutive Dry Days\DryDays_Hist.crf' DryDays_Hist;'Climate Projections\Consecutive Dry Days\DryDays_EC_45.crf' DryDays_EC_45;'Climate Projections\Consecutive Dry Days\DryDays_LC_45.crf' DryDays_LC_45;'Climate Projections\Consecutive Dry Days\DryDays_LC_85.crf' DryDays_LC_85;'Climate Projections\Cooling Degree Days\CDD_Hist.crf' CDD_Hist_v2;'Climate Projections\Cooling Degree Days\CDD_EC_45.crf' CDD_EC_45;'Climate Projections\Cooling Degree Days\CDD_LC_45.crf' CDD_LC_45;'Climate Projections\Cooling Degree Days\CDD_LC_85.crf' CDD_LC_85;'Climate Projections\Days Above 90F\A90F_Hist.crf' A90F_Hist;'Climate Projections\Days Above 90F\A90F_EC_45.crf' A90F_EC_45;'Climate Projections\Days Above 90F\A90F_LC_45.crf' A90F_LC_45;'Climate Projections\Days Above 90F\A90F_LC_85.crf' A90F_LC_85",
    bilinear_interpolate_values="NONE"
)

#Create grid to divide CONUS into smaller pieces, then interate over each grid square applying Extract Multi Values to Points on FEMA Flood Values

arcpy.management.GenerateTessellation(
    Output_Feature_Class=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\Museums.gdb\GenerateTessellation2",
    Extent='-3336830.29706174 -67562.6395372031 2916831.99492706 4109323.74205233 PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]',
    Shape_Type="SQUARE",
    Size="5625000000 SquareMeters",
    Spatial_Reference='PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]];-16901100 -6972200 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision',
    H3_Resolution=7
)

import arcpy

# Inputs
tess = "GenerateTessellation2"
points = "MDF Museums"
raster = "USA_Flood_Hazard_Areas"

small_grid_ids = []
# Iterate through only the selected features
with arcpy.da.SearchCursor(tess, ["GRID_ID"]) as cursor:
    for row in cursor:
        small_grid_ids.append(row[0])

print("GRID_ID values from selected features:", small_grid_ids)

# Create an accumulator field to hold running totals
accum_field = "FloodVal"
fields = [f.name for f in arcpy.ListFields(points)]
if accum_field not in fields:
    arcpy.AddField_management(points, accum_field, "SHORT")

for i, grid_id in enumerate(small_grid_ids, start=1):
    # Select polygon by GRID_ID
    where_clause = f"GRID_ID = '{grid_id}'"
    arcpy.management.SelectLayerByAttribute(tess, "NEW_SELECTION", where_clause)

    # Get extent of selected feature
    with arcpy.da.SearchCursor(tess, ["SHAPE@"]) as cursor:
        for row in cursor:
            extent = row[0].extent
            arcpy.env.extent = extent
            print(f"Processing GRID_ID {grid_id} with extent {extent}")

            # Name a temp field for this iteration
            temp_field = f"FloodVal_tmp{i}"

            # Extract values into the temporary field
            arcpy.sa.ExtractMultiValuesToPoints(
                in_point_features=points,
                in_rasters=[[raster, temp_field]],
                bilinear_interpolate_values="NONE"
            )

            # Update the accumulator field by adding the temporary field values
            with arcpy.da.UpdateCursor(points, [accum_field, temp_field]) as ucur:
                for urow in ucur:
                    if urow[1] is not None:
                        urow[0] = urow[1]   # Replace instead of accumulate
                        ucur.updateRow(urow)

            # Delete the temporary field
            arcpy.DeleteField_management(points, [temp_field])

    arcpy.env.extent = None
print("all done")

#Extract Multi Values to Points for Storm Surge

arcpy.sa.ExtractMultiValuesToPoints(
    in_point_features="MDF Museums",
    in_rasters="us_Category5_MOM_Inundation_HIGH.tif East_Cat5;us_Category4_MOM_Inundation_HIGH.tif East_Cat4;us_Category3_MOM_Inundation_HIGH.tif East_Cat3;us_Category2_MOM_Inundation_HIGH.tif East_Cat2;us_Category1_MOM_Inundation_HIGH.tif East_Cat1",
    bilinear_interpolate_values="NONE"
)

#Subset Multidimensional Rasters and Extract Multi Values to Point for Wildfire Risk Factors
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA Historical",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\PrecipTotal_Hist.crf",
    variables="'Precip Annual Total'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Early Century",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\PrecipTotal_EC_4.5.crf",
    variables="'Precip Annual Total'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\PrecipTotal_LC_4.5.crf",
    variables="'Precip Annual Total'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 8.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\PrecipTotal_LC_8.5.crf",
    variables="'Precip Annual Total'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA Historical",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\Precip99_Hist.crf",
    variables="'Precip Days Above 99th pctl'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Early Century",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\Precip99_EC_45.crf",
    variables="'Precip Days Above 99th pctl'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\Precip99_LC_45.crf",
    variables="'Precip Days Above 99th pctl'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 8.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdh51\Documents\ArcGIS\Projects\Museums\Precip99_LC_85.crf",
    variables="'Precip Days Above 99th pctl'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA Historical",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\DryDays_Hist.crf",
    variables="'Consecutive Dry Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Early Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\DryDays_EC_45.crf",
    variables="'Consecutive Dry Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\DryDays_LC_45.crf",
    variables="'Consecutive Dry Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 8.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\DryDays_LC_85.crf",
    variables="'Consecutive Dry Days'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA Historical",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\A90F_Hist.crf",
    variables="'Days Above 90F'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Early Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\A90F_EC_45.crf",
    variables="'Days Above 90F'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 4.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\A90F_LC_45.crf",
    variables="'Days Above 90F'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)
arcpy.md.SubsetMultidimensionalRaster(
    in_multidimensional_raster=r"Original Multidimensional Rasters\U.S. Climate Thresholds - LOCA RCP 8.5 Late Century",
    out_multidimensional_raster=r"C:\Users\mdhowlan\Documents\ArcGIS\Projects\Museums\A90F_LC_85.crf",
    variables="'Days Above 90F'",
    dimension_def="ALL",
    dimension_ranges=None,
    dimension_values=None,
    dimension="",
    start_of_first_iteration="",
    end_of_first_iteration="",
    iteration_step=None,
    iteration_unit=""
)

arcpy.sa.ExtractMultiValuesToPoints(
    in_point_features="MDF Museums",
    in_rasters=r"'Total Precipitation\PrecipTotal_Hist.crf' PrecipTotal_Hist;'Total Precipitation\PrecipTotal_EC_4.5.crf' PrecipTotal_EC_45;'Total Precipitation\PrecipTotal_LC_4.5.crf' PrecipTotal_LC_45;'Total Precipitation\PrecipTotal_LC_8.5.crf' PrecipTotal_LC_85;'Precipitation Days Above 99th]\Precip99_Hist.crf' Precip99_Hist;'Precipitation Days Above 99th]\Precip99_EC_45.crf' Precip99_EC_45;'Precipitation Days Above 99th]\Precip99_LC_45.crf' Precip99_LC_45;'Precipitation Days Above 99th]\Precip99_LC_85.crf' Precip99_LC_85",
    bilinear_interpolate_values="NONE"
)

#Extract Multi Values to Points for Wildfire Hazard Potential

arcpy.sa.ExtractMultiValuesToPoints(
    in_point_features="MDF Museums",
    in_rasters=r"'WILDFIRE\USFS Wildfire Hazard Potential.tif' WHP",
    bilinear_interpolate_values="NONE"
)
