
'''
Anual Water Yield
'''
args = {
    'biophysical_table_path': '/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table_AF_1.csv',
    'depth_to_root_rest_layer_path': '/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Soil_Depth_AF_1.tif',
    'do_scarcity_and_valuation': False,
    'eto_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/02-Evapotranspiration/02-Future/ETo_AF_1_YEAR_13.tif',
    'lulc_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/03-LandCover/LULC_AF_1.tif',
    'pawc_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/16-Plant_Available_Water/PAW_AF_1.tif',
    'precipitation_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/01-Precipitation/02-Future/Pcp_AF_1_YEAR_13.tif',
    'results_suffix': 'Skaphe',
    'seasonality_constant': '15',
    'sub_watersheds_path': '',
    'watersheds_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/05-Watersheds/Watersheds_AF_1.shp',
    'workspace_dir': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/01-InVEST_Skaphe/05-AWY',
}
# Run
awy.execute(args)

'''
Seasonal Water Yield
'''
args = {
    'alpha_m': '0.08333',
    'aoi_path': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\05-Watersheds\\Watersheds_AF_1.shp',
    'beta_i': '1',
    'biophysical_table_path': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\09-Biophysical_Table\\Biophysical_Table_AF_1.csv',
    'dem_raster_path': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\08-DEM\\DEM_AF.tif',
    'et0_dir': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\02-Evapotranspiration\\02-Future',
    'gamma': '1',
    'lulc_raster_path': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\03-LandCover\\LULC_AF_1.tif',
    'monthly_alpha': False,
    'precip_dir': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\01-Precipitation\\02-Future',
    'rain_events_table_path': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\10-Rainfall_Day_Table\\Rainfall_Day_Table_AF_1.csv',
    'results_suffix': 'Skaphe',
    'soil_group_path': 'T:\\01-WaterFundsApp\\00-Tester_InVEST_RIOS_V2\\INPUTS\\04-SoilGroup\\SoilGroup_AF_1.tif',
    'threshold_flow_accumulation': '20',
    'user_defined_climate_zones': False,
    'user_defined_local_recharge': False,
    'workspace_dir': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/01-InVEST_Skaphe/01-SWY',
}

# Run
swy.execute(args)

'''
Sediment Delivery Ratio
'''
args = {
    'biophysical_table_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/09-Biophysical_Table/Biophysical_Table_AF_1.csv',
    'dem_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/08-DEM/DEM_AF.tif',
    'drainage_path': '',
    'erodibility_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/06-SoilErodability/K_AF_1.tif',
    'erosivity_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/11-Rainfall-Erosivity/R_AF_1.tif',
    'ic_0_param': '0.5',
    'k_param': '2',
    'lulc_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/03-LandCover/LULC_AF_1.tif',
    'results_suffix': 'Skaphe',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '20',
    'watersheds_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/05-Watersheds/Watersheds_AF_1.shp',
    'workspace_dir': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/01-InVEST_Skaphe/02-SDR',
}

# Run
sdr.execute(args)

'''
Nutrient Delivery Ratio
'''
args = {
    'biophysical_table_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/09-Biophysical_Table/Biophysical_Table_AF_1.csv',
    'calc_n': True,
    'calc_p': True,
    'dem_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/08-DEM/DEM_AF.tif',
    'k_param': '2',
    'lulc_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/03-LandCover/LULC_AF_1.tif',
    'results_suffix': 'Skaphe',
    'runoff_proxy_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/OUTPUTS/02-Anual-Water-Yield/01-Historic/output/per_pixel/wyield_AF_1.tif',
    'subsurface_critical_length_n': '1000',
    'subsurface_critical_length_p': '1000',
    'subsurface_eff_n': '0.5',
    'subsurface_eff_p': '0.5',
    'threshold_flow_accumulation': '50',
    'watersheds_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/05-Watersheds/Watersheds_AF_1.shp',
    'workspace_dir': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/01-InVEST_Skaphe/03-NDR',
}

ndr.execute(args)


'''
Carbons
'''
args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/09-Biophysical_Table/Biophysical_Table_AF_1.csv',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/INPUTS/03-LandCover/LULC_AF_1.tif',
    'results_suffix': 'AF_1',
    'workspace_dir': 'T:/01-WaterFundsApp/00-Tester_InVEST_RIOS_V2/01-InVEST_Skaphe/04-Carbon',
}

carbon.execute(args)




""""
This is a saved model run from natcap.rios.rios.
Generated: 08/20/20 16:22:43
"""
import os, sys
sys.path.append(os.path.split(os.getcwd())[0] + os.path.sep + 'FUNCTION')
import RIOS_Toolbox.rios as rios


PathInput   = os.path.join(os.path.split(os.getcwd())[0], 'DATA', '02-RIOS')
PathOutput  = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS', '07-RIOS')

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

args = {
        u'activities': {
            u'agroforestry': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 1.0,
            },
            u'grass_strips': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 1.0,
            },
            u'riparian_mgmt': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 1.0,
            },
            u'terracing': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 1.0,
            },
        },
        u'activity_shapefiles': [],
        u'budget_config': {
            u'activity_budget': {
                u'agroforestry': {
                    u'budget_amount': 50000.0,
                },
                u'grass_strips': {
                    u'budget_amount': 50000.0,
                },
                u'riparian_mgmt': {
                    u'budget_amount': 50000.0,
                },
                u'terracing': {
                    u'budget_amount': 50000.0,
                },
            },
            u'floating_budget': 26329000,
            u'if_left_over': u'Report remainder',
            u'years_to_spend': 5,
        },
        u'lulc_activity_potential_map': {
            1: [],
            2: [],
            3: [
                u'agroforestry',
            ],
            4: [
                u'agroforestry',
                u'grass_strips',
                u'terracing',
            ],
            5: [],
            6: [
                u'grass_strips',
                u'terracing',
            ],
            7: [],
        },
        u'lulc_coefficients_table_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
        u'lulc_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
        u'objectives': {
            u'baseflow': {
                u'factors': {
                    u'Actual Evapotranspiration': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/ETR.tif',
                    },
                    u'Annual Average Rainfall': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/P_Year.tif',
                    },
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Beneficiaries.tif',
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_downslope_retention_index_AF_1.tif',
                    },
                    u'Land Use Land Cover Retention at pixel': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Rough_Rank',
                        },
                    },
                    u'Slope Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_slope_index_AF_1.tif',
                    },
                    u'Soil Texture Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Texture_Index.tif',
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Soil_Depth.tif',
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/gwater_upslope_source_AF_1.tif',
                    },
                    u'Vegetative Cover Index': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Cover_Rank',
                        },
                    },
                },
                u'priorities': {
                    u'agricultural_vegetation_managment': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'ditching': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'fertilizer_management': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'keep_native_vegetation': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': 0.5,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': 0.2,
                    },
                    u'pasture_management': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'revegetation_assisted': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'revegetation_unassisted': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                },
                u'rios_model_type': u'rios_tier_0',
            },
            u'erosion_drinking_control': {
                u'factors': {
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Beneficiaries.tif',
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/erosion_downslope_retention_index_AF_1.tif',
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Sed_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Sed_Exp',
                        },
                    },
                    u'Rainfall erosivity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/R.tif',
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/erosion_riparian_index_AF_1.tif',
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Soil_Depth.tif',
                    },
                    u'Soil erodibility': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/K.tif',
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/erosion_upslope_source_AF_1.tif',
                    },
                },
                u'priorities': {
                    u'agricultural_vegetation_managment': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'ditching': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'fertilizer_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'keep_native_vegetation': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': 0.5,
                        u'On-pixel source': u'~0.25',
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'pasture_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_assisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_unassisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                },
                u'rios_model_type': u'rios_tier_0',
            },
            u'erosion_reservoir_control': {
                u'factors': {
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Beneficiaries.tif',
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/erosion_downslope_retention_index_AF_1.tif',
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Sed_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Sed_Exp',
                        },
                    },
                    u'Rainfall erosivity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/R.tif',
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/erosion_riparian_index_AF_1.tif',
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Soil_Depth.tif',
                    },
                    u'Soil erodibility': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/K.tif',
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/erosion_upslope_source_AF_1.tif',
                    },
                },
                u'priorities': {
                    u'agricultural_vegetation_managment': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'ditching': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'fertilizer_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'keep_native_vegetation': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': 0.5,
                        u'On-pixel source': u'~0.25',
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'pasture_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_assisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_unassisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                },
                u'rios_model_type': u'rios_tier_0',
            },
            u'flood_mitigation_impact': {
                u'factors': {
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Beneficiaries.tif',
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_downslope_retention_index_AF_1.tif',
                    },
                    u'Land Use Land Cover Retention at pixel': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Rough_Rank',
                        },
                    },
                    u'Rainfall depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/R.tif',
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_riparian_index_AF_1.tif',
                    },
                    u'Slope Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_slope_index_AF_1.tif',
                    },
                    u'Soil Texture Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Texture_Index.tif',
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_upslope_source_AF_1.tif',
                    },
                    u'Vegetative Cover Index': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Cover_Rank',
                        },
                    },
                },
                u'priorities': {
                    u'agricultural_vegetation_managment': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Rainfall depth': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Slope Index': 0.25,
                        u'Soil Texture Index': 0.25,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.25',
                    },
                    u'ditching': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Rainfall depth': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Slope Index': 0.25,
                        u'Soil Texture Index': 0.25,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.25',
                    },
                    u'fertilizer_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Rainfall depth': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Slope Index': 0.25,
                        u'Soil Texture Index': 0.25,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.25',
                    },
                    u'keep_native_vegetation': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': 0.5,
                        u'Rainfall depth': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Slope Index': 0.25,
                        u'Soil Texture Index': 0.25,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': 0.25,
                    },
                    u'pasture_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Rainfall depth': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Slope Index': 0.25,
                        u'Soil Texture Index': 0.25,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.25',
                    },
                    u'revegetation_assisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Rainfall depth': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Slope Index': 0.25,
                        u'Soil Texture Index': 0.25,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.25',
                    },
                    u'revegetation_unassisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Rainfall depth': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Slope Index': 0.25,
                        u'Soil Texture Index': 0.25,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.25',
                    },
                },
                u'rios_model_type': u'rios_tier_0',
            },
            u'groundwater_recharge': {
                u'factors': {
                    u'Actual Evapotranspiration': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/ETR.tif',
                    },
                    u'Annual Average Rainfall': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/P_Year.tif',
                    },
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Beneficiaries.tif',
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_downslope_retention_index_AF_1.tif',
                    },
                    u'Land Use Land Cover Retention at pixel': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Rough_Rank',
                        },
                    },
                    u'Preferential Recharge Areas': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Aquifer_Area.tif',
                    },
                    u'Slope Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/flood_slope_index_AF_1.tif',
                    },
                    u'Soil Texture Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Texture_Index.tif',
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Soil_Depth.tif',
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/gwater_upslope_source_AF_1.tif',
                    },
                    u'Vegetative Cover Index': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'Cover_Rank',
                        },
                    },
                },
                u'priorities': {
                    u'agricultural_vegetation_managment': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Preferential Recharge Areas': 1.0,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'ditching': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Preferential Recharge Areas': 1.0,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'fertilizer_management': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Preferential Recharge Areas': 1.0,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'keep_native_vegetation': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': 0.5,
                        u'Preferential Recharge Areas': 1.0,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': 0.2,
                    },
                    u'pasture_management': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Preferential Recharge Areas': 1.0,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'revegetation_assisted': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Preferential Recharge Areas': 1.0,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                    u'revegetation_unassisted': {
                        u'Actual Evapotranspiration': u'~0.2',
                        u'Annual Average Rainfall': 0.2,
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'Land Use Land Cover Retention at pixel': u'~0.5',
                        u'Preferential Recharge Areas': 1.0,
                        u'Slope Index': u'~0.2',
                        u'Soil Texture Index': u'~0.2',
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                        u'Vegetative Cover Index': u'~0.2',
                    },
                },
                u'rios_model_type': u'rios_tier_0',
            },
            u'nutrient_retention_nitrogen': {
                u'factors': {
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Beneficiaries.tif',
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/nitrogen_downslope_retention_index_AF_1.tif',
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'N_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'N_Exp',
                        },
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/nitrogen_riparian_index_AF_1.tif',
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Soil_Depth.tif',
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/nitrogen_upslope_source_AF_1.tif',
                    },
                },
                u'priorities': {
                    u'agricultural_vegetation_managment': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.5,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                    },
                    u'ditching': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.5,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                    },
                    u'fertilizer_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.5,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                    },
                    u'keep_native_vegetation': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': 0.5,
                        u'On-pixel source': u'~0.5',
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                    },
                    u'pasture_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.5,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_assisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.5,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_unassisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.5,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.5,
                        u'Upslope source': 1.0,
                    },
                },
                u'rios_model_type': u'rios_tier_0',
            },
            u'nutrient_retention_phosphorus': {
                u'factors': {
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Beneficiaries.tif',
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/phosphorus_downslope_retention_index_AF_1.tif',
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'P_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/LULC.tif',
                            u'uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Biophysical_Table.csv',
                            u'value_field': u'P_Exp',
                        },
                    },
                    u'Rainfall erosivity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/R.tif',
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/phosphorus_riparian_index_AF_1.tif',
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/Soil_Depth.tif',
                    },
                    u'Soil erodibility': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/03-INPUTS_RIOS_InVEST/K.tif',
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': u'/home/tnc/Documents/01-PreProcessing_RIOS/02-OUTPUTS_PrePro_RIOS/phosphorus_upslope_source_AF_1.tif',
                    },
                },
                u'priorities': {
                    u'agricultural_vegetation_managment': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'ditching': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'fertilizer_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'keep_native_vegetation': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': 0.5,
                        u'On-pixel source': u'~0.25',
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'pasture_management': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_assisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                    u'revegetation_unassisted': {
                        u'Beneficiaries': 1.0,
                        u'Downslope retention index': u'~1',
                        u'On-pixel retention': u'~0.5',
                        u'On-pixel source': 0.25,
                        u'Rainfall erosivity': 0.25,
                        u'Riparian continuity': 0.5,
                        u'Soil depth': 0.25,
                        u'Soil erodibility': 0.25,
                        u'Upslope source': 1.0,
                    },
                },
                u'rios_model_type': u'rios_tier_0',
            },
        },
        u'open_html_on_completion': True,
        u'priorities': {
            u'agricultural_vegetation_managment': {
                u'baseflow': 1.0,
                u'erosion_drinking_control': 1.0,
                u'erosion_reservoir_control': 1.0,
                u'flood_mitigation_impact': 1.0,
                u'groundwater_recharge': 1.0,
                u'nutrient_retention_nitrogen': 1.0,
                u'nutrient_retention_phosphorus': 1.0,
            },
            u'ditching': {
                u'baseflow': 1.0,
                u'erosion_drinking_control': 1.0,
                u'erosion_reservoir_control': 1.0,
                u'flood_mitigation_impact': 1.0,
                u'groundwater_recharge': 1.0,
                u'nutrient_retention_nitrogen': 1.0,
                u'nutrient_retention_phosphorus': 1.0,
            },
            u'fertilizer_management': {
                u'baseflow': 1.0,
                u'erosion_drinking_control': 1.0,
                u'erosion_reservoir_control': 1.0,
                u'flood_mitigation_impact': 1.0,
                u'groundwater_recharge': 1.0,
                u'nutrient_retention_nitrogen': 1.0,
                u'nutrient_retention_phosphorus': 1.0,
            },
            u'keep_native_vegetation': {
                u'baseflow': 1.0,
                u'erosion_drinking_control': 1.0,
                u'erosion_reservoir_control': 1.0,
                u'flood_mitigation_impact': 1.0,
                u'groundwater_recharge': 1.0,
                u'nutrient_retention_nitrogen': 1.0,
                u'nutrient_retention_phosphorus': 1.0,
            },
            u'pasture_management': {
                u'baseflow': 1.0,
                u'erosion_drinking_control': 1.0,
                u'erosion_reservoir_control': 1.0,
                u'flood_mitigation_impact': 1.0,
                u'groundwater_recharge': 1.0,
                u'nutrient_retention_nitrogen': 1.0,
                u'nutrient_retention_phosphorus': 1.0,
            },
            u'revegetation_assisted': {
                u'baseflow': 1.0,
                u'erosion_drinking_control': 1.0,
                u'erosion_reservoir_control': 1.0,
                u'flood_mitigation_impact': 1.0,
                u'groundwater_recharge': 1.0,
                u'nutrient_retention_nitrogen': 1.0,
                u'nutrient_retention_phosphorus': 1.0,
            },
            u'revegetation_unassisted': {
                u'baseflow': 1.0,
                u'erosion_drinking_control': 1.0,
                u'erosion_reservoir_control': 1.0,
                u'flood_mitigation_impact': 1.0,
                u'groundwater_recharge': 1.0,
                u'nutrient_retention_nitrogen': 1.0,
                u'nutrient_retention_phosphorus': 1.0,
            },
        },
        u'results_suffix': 'Dummy',
        u'transition_map': {
            u'agricultural_vegetation_managment': {
                u'agroforestry': 1.0,
                u'grass_strips': 1.0,
                u'riparian_mgmt': 1.0,
                u'terracing': 1.0,
            },
            u'ditching': {
                u'agroforestry': 1.0,
                u'grass_strips': 1.0,
                u'riparian_mgmt': 1.0,
                u'terracing': 1.0,
            },
            u'fertilizer_management': {
                u'agroforestry': 1.0,
                u'grass_strips': 1.0,
                u'riparian_mgmt': 1.0,
                u'terracing': 1.0,
            },
            u'keep_native_vegetation': {
                u'agroforestry': 1.0,
                u'grass_strips': 1.0,
                u'riparian_mgmt': 1.0,
                u'terracing': 1.0,
            },
            u'pasture_management': {
                u'agroforestry': 1.0,
                u'grass_strips': 1.0,
                u'riparian_mgmt': 1.0,
                u'terracing': 1.0,
            },
            u'revegetation_assisted': {
                u'agroforestry': 1.0,
                u'grass_strips': 1.0,
                u'riparian_mgmt': 1.0,
                u'terracing': 1.0,
            },
            u'revegetation_unassisted': {
                u'agroforestry': 1.0,
                u'grass_strips': 1.0,
                u'riparian_mgmt': 1.0,
                u'terracing': 1.0,
            },
        },
        u'transition_types': [
            {
                u'file_name': u'agricultural_vegetation_managment',
                u'id': u'trans4',
                u'label': u'Agricultural \nvegetation \nmanagement',
                u'transition_type': u'agriculture',
            },
            {
                u'file_name': u'ditching',
                u'id': u'trans5',
                u'label': u'Ditching',
                u'transition_type': u'agriculture',
            },
            {
                u'file_name': u'fertilizer_management',
                u'id': u'trans6',
                u'label': u'Fertilizer \nmanagement',
                u'transition_type': u'agriculture',
            },
            {
                u'file_name': u'keep_native_vegetation',
                u'id': u'trans1',
                u'label': u'Keep native \nvegetation',
                u'transition_type': u'protection',
            },
            {
                u'file_name': u'pasture_management',
                u'id': u'trans7',
                u'label': u'Pasture \nmanagement',
                u'transition_type': u'agriculture',
            },
            {
                u'file_name': u'revegetation_assisted',
                u'id': u'trans3',
                u'label': u'Revegetation \n(assisted)',
                u'transition_type': u'restoration',
            },
            {
                u'file_name': u'revegetation_unassisted',
                u'id': u'trans2',
                u'label': u'Revegetation \n(unassisted)',
                u'transition_type': u'restoration',
            },
        ],
        u'workspace_dir': u'/home/tnc/Documents/01-PreProcessing_RIOS/04-OUTPUTS_RIOS_InVEST/RIOS',
}

if __name__ == '__main__':
    rios.execute(args)
