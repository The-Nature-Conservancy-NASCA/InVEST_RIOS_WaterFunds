# Guía para la configuración de RIOS y InVEST - LINUX

Autor: Jonathan Nogales Pimentel
Fecha: 24/08/2020

En el actual documento se realiza una breve descripción de la configuración de los ambientes Python para los modelos de RIOS y InVEST en plataformas Linux

## Instalaciones preliminares

RIOS y InVEST para poder llevar acabo procesos espaciales hacen uso de librerías como GDAL. Ésta requiere para su instalación que en el sistema operativo se encuentre configurado los compiladores GCC/g++. En este sentido, se recomienda instalar el paquete Build-Essential el cual proporciona dichos compiladores. Las siguientes líneas de código ilustran el proceso de instalación:
Actualizar repositorio
```
sudo apt-get update
```

Instalar paquete
```
sudo apt-get install build-essential
```

El paquete build-essentials es una referencia para todos los paquetes necesarios para compilar un paquete Debian. Generalmente incluye los compiladores y bibliotecas GCC/g ++ y algunas otras utilidades.

## ¿Qué es un ambiente Python?

Un entorno virtual es una herramienta que ayuda a mantener separadas las dependencias requeridas por un programa escrito en Python. En esencia, el propósito principal de los entornos virtuales de Python es crear un entorno aislado para los proyectos de Python. Esto significa que cada proyecto puede tener sus propias dependencias, independientemente de las dependencias que tengan los demás proyectos.

Figura 2.1 Esquema explicativo de ambientes Python con anaconda.
![Sin titulo](https://protostar.space/wp-content/uploads/2019/04/conda-root-and-additional-environments.jpeg)
Fuente: https://protostar.space/wp-content/uploads/2019/04/conda-root-and-additional-environments.jpeg

Anaconda es una distribución de Python que permite de manera amigable crear y administrar ambientes Python, así como también instalar módulos y paquetes. Para efectos del presente documento, la configuración de los ambientes Python se realiza haciendo uso de esta distribución (link de descarga https://www.anaconda.com/).

## Ambiente Python RIOS

Resource Investment Optimization System (RIOS) es un software que se inició a desarrollar hace ya mas de 5 años. De acuerdo con el registro de versiones en su repositorio de GitHub, la primera versión de RIOS en una estructura de proyecto tuvo lugar el 17 de agosto del 2015. Desde ese entonces se han lanzado 12 versiones de este software. Lastimosamente, RIOS ya no es compatible con Natural Capital Project, lo que significa que no proporcionan instalador para descargar, ni tampoco proporcionan corrección de errores ni asistencia al usuario. No obstante, Natural Capital a liberado el código fuente para libre desarrollo, es así que este apartado se centra en la configuración de un ambiente Python para la ejecución de este código.

### Descripción del repositorio de RIOS

La URL en la cual se encuentra el repositorio de RIOS corresponde a https://github.com/richpsharp/rios-deprecated . El repositorio se encuentra distribuido en 5 carpetas a saber:

- Arcgis_preprocessor: contiene el toolbox desarrollado en ArcGIS para la construcción de los preprocesamientos requeridos por RIOS.
- Exescripts: contiene la secuencia de comandos que concluye las llamadas para iniciar los distintos usuarios interfaces de RIOS.
- Intaller/Windows: código del instalador para windows
- Src/natcap: códigos Python de procesamiento
- User_guide: guías de usuario en inglés y español

Para efectos prácticos de la WáterFunds App, la única carpeta que es necesaria es la de src/natcap, específicamente los siguientes códigos:
- disk_dort.py
- porter_core.py
- rios.py
- rios_build_scenario.py

Los códigos pueden ser descargados directamente del repositorio con ayuda del navegador o haciendo uso de programa git.

### Configuración de ambiente Python 

Dato que RIOS se encuentra programado en Python 2, es necesario crear un ambiente Python con versión 2.7 haciendo uso de la siguiente línea de comando. El ambiente se crea con nombre RIOS, sin embargo, el nombre puede ser modificado por el que sea de mayor preferencia.

```
conda create --name RIOS python=2.7
```

Creado al ambiente, se procede a realizar su activación. Esta se realizada a través de la siguiente línea de comando:

```
conda activate RIOS
```

El primer paquete que se debe instalar es gdal versión 2.4.4 haciendo uso del comando conda:

```
conda install -c conda-forge gdal=2.4.4
```

RIOS para su funcionamiento necesita una serie de procesamientos previos a su ejecución. Como se menciono en el numeral anterior, el repositorio de RIOS trae consigo un preprocesador el cual se encuentra programa en Python, pero haciendo uso de librerías especificas de ArcGIS. Dado que ArcGIS es un software licenciado del TNC tiene su licencia, se opto por no hacer uso de este toolbox dado que se debe realizar un tramite legal para poder tener una licencia que permita su implementación web. Afortunadamente, Natural Capital desarrollo una librería totalmente independiente de ArcGIS. Ésta se encuentra disponible el repositorio de pip y puede ser instalada a través de la siguiente línea de código:

```
pip install rios_preprocessor
```

El ultimo requerimiento que necesita RIOS es la librería de análisis estadísticos Scipy, la cual puede instalarse de la siguiente manera.

```
conda install -c anaconda scipy
```
 
Con esto, se da por terminada la configuración del ambiente Python para RIOS.

### Ambiente Python InVEST

A diferencia de RIOS, InVEST se encuentra programado en Python 3, por lo que es neceario configurar un ambiente con Python 3.7. Esto se pude hacer con la siguiente línea de código:

```
conda create --name InVEST python=3.7
```
 
Creado el ambiente, se realiza su activación :

```
conda activate InVEST
```

Al igual que en la configuración del ambiente Python para RIOS, el primer paquete que se debe instalar es gdal versión 2.4.4 haciendo uso del comando conda:

```
conda install -c conda-forge gdal=2.4.4
```

Luego instalamos la librería rtree versión 0.9.4 con ayuda de conda:

```
conda install -c conda-forge rtree=0.9.4
```

Luego se instala la librería de InVEST la cual se encuentra disponible en el repositorio de pip.

```
pip install natcap.invest==3.8.9
```

Por ultimo, se debe modificar la libreria geoprocessing del paquete pygeoprocessing las lineas 1309 a la 1318 (se muestran a continuación)
```
aggregate_stats[agg_fid]['min'] = min(
    numpy.min(masked_clipped_block),
    aggregate_stats[agg_fid]['min'])
aggregate_stats[agg_fid]['max'] = max(
    numpy.max(masked_clipped_block),
    aggregate_stats[agg_fid]['max'])
aggregate_stats[agg_fid]['count'] += (
    masked_clipped_block.size)
aggregate_stats[agg_fid]['sum'] += numpy.sum(
    masked_clipped_block)
```

por las siguientes lineas
```
aggregate_stats[agg_fid]['min'] = min(
    numpy.nanmin(masked_clipped_block),
    aggregate_stats[agg_fid]['min'])
aggregate_stats[agg_fid]['max'] = max(
    numpy.nanmax(masked_clipped_block),
    aggregate_stats[agg_fid]['max'])
aggregate_stats[agg_fid]['count'] += (
    masked_clipped_block.size)
aggregate_stats[agg_fid]['sum'] += numpy.nansum(
    masked_clipped_block)
```

Igual manera las lineas 1386 a la 1391 (muestran a continuación)
```
aggregate_stats[unset_fid]['min'] = numpy.min(
    valid_unset_fid_block)
aggregate_stats[unset_fid]['max'] = numpy.max(
    valid_unset_fid_block)
aggregate_stats[unset_fid]['sum'] = numpy.sum(
    valid_unset_fid_block)
```

por las siguientes lineas
```
aggregate_stats[unset_fid]['min'] = numpy.nanmin(
    valid_unset_fid_block)
aggregate_stats[unset_fid]['max'] = numpy.nanmax(
    valid_unset_fid_block)
aggregate_stats[unset_fid]['sum'] = numpy.nansum(
    valid_unset_fid_block)
```

Con esto se da por finalizada la configuración del ambiente Python para InVEST

## Modificaciones de código

Para los pre-procesamientos de RIOS si bien esta librería en pip, fue necesario modificar su código. Básicamente se realizo el cambio de las funciones max y min para que omitan los valores NaN. Es asi que se cambiaron por nanmax y nanmin repectivamente 

## Configuración de código
En el siguiente apartado se presenta la configuración de los argumentos de entrada para los modelos de RIOS y InVEST incluyendo el preprocesamiento.

### Configuracion general para InVEST

```
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

```

### Anual Water Yield

```
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','01-Anual-Water-Yield')
awy.execute(args)
```

### Seasonal Water Yield

```
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS', '02-Seasonal-Water-Yield')
swy.execute(args)
```

### Sediment Delivery Ratio

```
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','03-Sediment-Delivery-Ratio')
sdr.execute(args)

```

### Nutrient Delivery Ratio

```
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','04-Nutrient-Delivery-Ratio')
ndr.execute(args)
```

### Carbons

```
args['workspace_dir'] = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS','05-Carbons')
carbon.execute(args)
```

### Pre-processor RIOS

```
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

```

### RIOS

```
import os, sys
sys.path.append(os.path.split(os.getcwd())[0] + os.path.sep + 'FUNCTIONS')
import RIOS_Toolbox.rios as rios


PathInput   = os.path.join(os.path.split(os.getcwd())[0], 'DATA', '02-RIOS')
PathInput1  = os.path.join(os.path.split(os.getcwd())[0])
PathOutput  = os.path.join(os.path.split(os.getcwd())[0], 'RESULTS', '07-RIOS')

working_path            = PathOutput
output_path             = PathOutput
hydro_path              = PathOutput
lulc_raster_uri         = os.path.join(PathInput, 'LULC.tif')
rios_coeff_table        = os.path.join(PathInput, 'Biophysical_Table.csv')
dem_raster_uri          = os.path.join(PathInput, 'DEM.tif')
precip_month_raster_uri = os.path.join(PathInput, 'P_Peak.tif')
soil_texture_raster_uri = os.path.join(PathInput, 'Texture_Index.tif')
precip_annual_raster_uri= os.path.join(PathInput, 'P_Year.tif')
erosivity_raster_uri    = os.path.join(PathInput, 'R.tif')
erodibility_raster_uri  = os.path.join(PathInput, 'K.tif')
soil_depth_raster_uri   = os.path.join(PathInput, 'Soil_Depth.tif')
aet_raster_uri          = os.path.join(PathInput, 'ETO.tif')
ETR_raster_uri          = os.path.join(PathInput, 'ETR.tif')
Beneficiaries           = os.path.join(PathInput, 'Beneficiaries.tif')
Aquifer                 = os.path.join(PathInput, 'Aquifer_Area.tif')
suffix                  = r'AF_1'
aoi_shape_uri           = os.path.join(PathInput, 'Basin','Basin.shp',)
streams_raster_uri      = os.path.join(PathInput, 'Stream.tif')

#
baseflow_downslope      = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','erosion_downslope_retention_index_' + suffix + '.tif')
baseflow_slope          = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','flood_slope_index_' + suffix + '.tif')
baseflow_upslope        = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','gwater_upslope_source_' + suffix + '.tif')

gw_downslope            = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','erosion_downslope_retention_index_' + suffix + '.tif')
gw_slope                = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','flood_slope_index_' + suffix + '.tif')
gw_upslope              = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','gwater_upslope_source_' + suffix + '.tif')

flood_downslope         = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','flood_downslope_retention_index_' + suffix + '.tif')
flood_riparian          = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','flood_riparian_index_' + suffix + '.tif')
flood_slope             = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','flood_slope_index_' + suffix + '.tif')
flood_upslope           = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','flood_upslope_source_' + suffix + '.tif')

erosion_downslope       = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','erosion_downslope_retention_index_' + suffix + '.tif')
erosion_riparian        = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','erosion_riparian_index_' + suffix + '.tif')
erosion_upslope         = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','erosion_upslope_source_' + suffix + '.tif')

phosphorus_downslope    = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','phosphorus_downslope_retention_index_' + suffix + '.tif')
phosphorus_riparian     = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','phosphorus_riparian_index_' + suffix + '.tif')
phosphorus_upslope      = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','phosphorus_upslope_source_' + suffix + '.tif')

nitrogen_downslope      = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','nitrogen_downslope_retention_index_' + suffix + '.tif')
nitrogen_riparian       = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','nitrogen_riparian_index_' + suffix + '.tif')
nitrogen_upslope        = os.path.join(PathInput1, 'RESULTS','06-Pre_Processing_RIOS','nitrogen_upslope_source_' + suffix + '.tif')


args = {
        u'activities': {
            u'agroforestry': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 100.0,
            },
            u'grass_strips': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 100.0,
            },
            u'riparian_mgmt': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 100.0,
            },
            u'terracing': {
                u'measurement_unit': u'area',
                u'measurement_value': 1000000.0,
                u'unit_cost': 100.0,
            },
        },
        u'activity_shapefiles': [],
        u'budget_config': {
            u'activity_budget': {
                u'agroforestry': {
                    u'budget_amount': 100.0,
                },
                u'grass_strips': {
                    u'budget_amount': 100.0,
                },
                u'riparian_mgmt': {
                    u'budget_amount': 100.0,
                },
                u'terracing': {
                    u'budget_amount': 100.0,
                },
            },
            u'floating_budget': 3000,
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
        u'lulc_coefficients_table_uri': rios_coeff_table,
        u'lulc_uri': lulc_raster_uri,
        u'objectives': {
            u'baseflow': {
                u'factors': {
                    u'Actual Evapotranspiration': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': ETR_raster_uri,
                    },
                    u'Annual Average Rainfall': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': precip_annual_raster_uri,
                    },
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': Beneficiaries,
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': baseflow_downslope,
                    },
                    u'Land Use Land Cover Retention at pixel': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'Rough_Rank',
                        },
                    },
                    u'Slope Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': baseflow_slope,
                    },
                    u'Soil Texture Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_texture_raster_uri,
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_depth_raster_uri,
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': baseflow_upslope,
                    },
                    u'Vegetative Cover Index': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
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
                        u'raster_uri': Beneficiaries,
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosion_downslope,
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'Sed_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'Sed_Exp',
                        },
                    },
                    u'Rainfall erosivity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosivity_raster_uri,
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosion_riparian,
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_depth_raster_uri,
                    },
                    u'Soil erodibility': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erodibility_raster_uri,
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosion_upslope,
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
                        u'raster_uri': Beneficiaries,
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosion_downslope,
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'Sed_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'Sed_Exp',
                        },
                    },
                    u'Rainfall erosivity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosivity_raster_uri,
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosion_riparian,
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_depth_raster_uri,
                    },
                    u'Soil erodibility': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erodibility_raster_uri,
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosion_upslope,
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
                        u'raster_uri': Beneficiaries,
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': flood_downslope,
                    },
                    u'Land Use Land Cover Retention at pixel': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'Rough_Rank',
                        },
                    },
                    u'Rainfall depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosivity_raster_uri,
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': flood_riparian,
                    },
                    u'Slope Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': flood_slope,
                    },
                    u'Soil Texture Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_texture_raster_uri,
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': flood_upslope,
                    },
                    u'Vegetative Cover Index': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
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
                        u'raster_uri': ETR_raster_uri,
                    },
                    u'Annual Average Rainfall': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': precip_annual_raster_uri,
                    },
                    u'Beneficiaries': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': Beneficiaries,
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': gw_downslope,
                    },
                    u'Land Use Land Cover Retention at pixel': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'Rough_Rank',
                        },
                    },
                    u'Preferential Recharge Areas': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': Aquifer,
                    },
                    u'Slope Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': gw_slope,
                    },
                    u'Soil Texture Index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_texture_raster_uri,
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_depth_raster_uri,
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': gw_upslope,
                    },
                    u'Vegetative Cover Index': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
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
                        u'raster_uri': Beneficiaries,
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': nitrogen_downslope,
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'N_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'N_Exp',
                        },
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': nitrogen_riparian,
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_depth_raster_uri,
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': nitrogen_upslope,
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
                        u'raster_uri': Beneficiaries,
                    },
                    u'Downslope retention index': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': phosphorus_downslope,
                    },
                    u'On-pixel retention': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'P_Ret',
                        },
                    },
                    u'On-pixel source': {
                        u'bins': {
                            u'key_field': u'lulc_general',
                            u'raster_uri': lulc_raster_uri,
                            u'uri': rios_coeff_table,
                            u'value_field': u'P_Exp',
                        },
                    },
                    u'Rainfall erosivity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erosivity_raster_uri,
                    },
                    u'Riparian continuity': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': phosphorus_riparian,
                    },
                    u'Soil depth': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': soil_depth_raster_uri,
                    },
                    u'Soil erodibility': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': erodibility_raster_uri,
                    },
                    u'Upslope source': {
                        u'bins': {
                            'interpolation': 'linear',
                            'inverted': False,
                            'type': 'interpolated',
                        },
                        u'raster_uri': phosphorus_upslope,
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
        u'workspace_dir': PathOutput,
}


rios.execute(args)

```
