import os, sys
# Seasonal Water Yield
from natcap.invest.seasonal_water_yield import seasonal_water_yield as swy
# Sediment Delivery Ratio
from natcap.invest.sdr import sdr
# Nutrient Delivery Ratio
from natcap.invest.ndr import ndr
# Anual Water Yield
from natcap.invest.hydropower import hydropower_water_yield as awy
# Carbons
from natcap.invest import carbon

# Inputs
PathInput       = os.path.join(os.path.split(os.getcwd())[0], 'DATA', '03-InVEST')
LULC            = os.path.join(PathInput, 'LULC.tif' )
BioTable        = os.path.join(PathInput, 'Biophysical_Table.csv' )
RainfallTable   = os.path.join(PathInput, 'Rainfall_Day_Table.csv' )
DEM             = os.path.join(PathInput, 'DEM.tif' )
Soil_Texture    = os.path.join(PathInput, 'Texture_Index.tif' )
Soil_Group      = os.path.join(PathInput, 'Soil_Group.tif' )
PAW             = os.path.join(PathInput, 'PAW.tif' )
Pcp_Annual      = os.path.join(PathInput, 'P_Year.tif' )
Pcp_Month       = os.path.join(PathInput, 'P' )
Erosivity       = os.path.join(PathInput, 'R.tif' )
Erodibility     = os.path.join(PathInput, 'K.tif' )
Soil_Depth      = os.path.join(PathInput, 'Soil_Depth.tif' )
ETR_Annual      = os.path.join(PathInput, 'ETR.tif' )
ETo_Annual      = os.path.join(PathInput, 'ETO.tif')
ETo_Month       = os.path.join(PathInput, 'ETo' )
Suffix          = 'Skaphe'
Watershed       = os.path.join(PathInput, 'Basin' ,'Basin.shp')

#
args = {}
args['biophysical_table_path']          = BioTable
args['lulc_path']                       = LULC
args['depth_to_root_rest_layer_path']   = Soil_Depth
args['do_scarcity_and_valuation']       = False
args['eto_path']                        = ETo_Annual
args['pawc_path']                       = PAW
args['precipitation_path']              = Pcp_Annual
args['results_suffix']                  = 'Skaphe'
args['seasonality_constant']            = '15'
args['sub_watersheds_path']             = ''
args['watersheds_path']                 = Watershed
args['alpha_m']                         = '0.08333'
args['aoi_path']                        = Watershed
args['beta_i']                          = '1'
args['dem_raster_path']                 = DEM
args['et0_dir']                         = ETo_Month
args['gamma']                           = '1'
args['lulc_raster_path']                = LULC
args['monthly_alpha']                   = False
args['precip_dir']                      = Pcp_Month
args['rain_events_table_path']          = RainfallTable
args['soil_group_path']                 = Soil_Group
args['threshold_flow_accumulation']     = '20'
args['user_defined_climate_zones']      = False
args['user_defined_local_recharge']     = False
args['dem_path']                        = DEM
args['drainage_path']                   = ''
args['erodibility_path']                = Erodibility
args['erosivity_path']                  = Erosivity
args['ic_0_param']                      = '0.5'
args['k_param']                         = '2'
args['sdr_max']                         = '0.8'
args['calc_n']                          = True
args['calc_p']                          = True
args['k_param']                         = '2'
args['runoff_proxy_path']               = Pcp_Annual
args['subsurface_critical_length_n']    = '1000'
args['subsurface_critical_length_p']    = '1000'
args['subsurface_eff_n']                = '0.5'
args['subsurface_eff_p']                = '0.5'
args['calc_sequestration']              = False
args['carbon_pools_path']               = BioTable
args['do_redd']                         = False
args['do_valuation']                    = False
args['lulc_cur_path']                   = LULC


# Seasonal Water Yield
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS', '02-Seasonal-Water-Yield')
swy.execute(args)

# Anual Water Yield
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','01-Anual-Water-Yield')
awy.execute(args)

# Sediment Delivery Ratio
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','03-Sediment-Delivery-Ratio')
sdr.execute(args)

# Nutrient Delivery Ratio
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','04-Nutrient-Delivery-Ratio')
ndr.execute(args)

# Carbons
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','05-Carbons')
carbon.execute(args)
