import os, sys
sys.path.append(os.path.split(os.getcwd())[0] + os.path.sep + 'FUNCTIONS')
import RIOS_Toolbox.rios_preprocessor as Pro
from timeit import default_timer as timer

PathInput   = os.path.join(os.path.split(os.getcwd())[0], 'DATA', '01-Pre_Processor_RIOS')
PathOutput  = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS', '06-Pre_Processing_RIOS')

working_path            = PathOutput
output_path             = PathOutput
hydro_path              = PathOutput
lulc_raster_uri         = os.path.join(PathInput, "LULC.tif")
rios_coeff_table        = os.path.join(PathInput, "Biophysical_Table.csv")
dem_raster_uri          = os.path.join(PathInput, "DEM.tif")
precip_month_raster_uri = os.path.join(PathInput, "P_Peak.tif")
soil_texture_raster_uri = os.path.join(PathInput, "Texture_Index.tif")
precip_annual_raster_uri= os.path.join(PathInput, "P_Year.tif")
erosivity_raster_uri    = os.path.join(PathInput, "R.tif")
erodibility_raster_uri  = os.path.join(PathInput, "K.tif")
soil_depth_raster_uri   = os.path.join(PathInput, "Soil_Depth.tif")
aet_raster_uri          = os.path.join(PathInput, "ETO.tif")
suffix                  = r"AF_1"
aoi_shape_uri           = os.path.join(PathInput, "Basin","Basin.shp",)
streams_raster_uri      = os.path.join(PathInput, "Stream.tif")

start = timer()

Pro.main(   working_path                = working_path,
            output_path                 = output_path ,
            hydro_path                  = hydro_path,
            rios_coeff_table            = rios_coeff_table,
            lulc_raster_uri             = lulc_raster_uri,
            dem_raster_uri              = dem_raster_uri,
            erosivity_raster_uri        = erosivity_raster_uri,
            erodibility_raster_uri      = erodibility_raster_uri,
            soil_depth_raster_uri       = soil_depth_raster_uri,
            precip_month_raster_uri     = precip_month_raster_uri,
            soil_texture_raster_uri     = soil_texture_raster_uri,
            precip_annual_raster_uri    = precip_annual_raster_uri,
            aet_raster_uri              = aet_raster_uri,
            suffix                      = suffix,
            aoi_shape_uri               = aoi_shape_uri,
            streams_raster_uri          = streams_raster_uri,
            do_erosion          = True,
            do_nutrient_p       = True,
            do_nutrient_n       = True,
            do_flood            = True,
            do_gw_bf            = True,
            river_buffer_dist   = 1000)


end = timer()
print(end - start)
