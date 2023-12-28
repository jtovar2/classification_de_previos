import csv
import shapefile

print('ejemplooo')
minimo_y_maximos_por_atributo = dict()
minimo_y_maximos_por_atributo['PROFUNDIDA'] = dict()
minimo_y_maximos_por_atributo['PROFUNDIDA']['minimo'] = 0
minimo_y_maximos_por_atributo['PROFUNDIDA']['maximo'] = 151

## array based
##  <50


prueba = dict()
prueba['CLIMA_AMBIENTAL'] = '9'
prueba['DISTRIBUCION_LLUVIAS'] = ['Monomodal , Bimodal']
prueba['PORC_PENDIENTE'] = '1-3'
prueba['GRADO_EROSION'] = "N/A"
prueba['DRENAJE_NATURAL'] = 'Bien Drenado'
prueba['FRECUENCIA_INUNDACION'] = 'Frecuente'
prueba['H1_VOLUMEN_POR_CFR_1'] = '0'
prueba['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '15-50'
prueba['PROFUNDIDAD_EFECTIVA'] = '<25>'
prueba['H1_CLASE_ESTRUCTURA_1'] = 'Fina'
prueba['FERTILIDAD'] = 'Muy baja'
prueba['CE_dS_m'] = '0'
prueba['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '0'
prueba['PORC_SAI'] = '0'
prueba['PORC_CARBONO ORGANICO'] = '19.33'

clases = dict()
clases["CTIc"] = dict()
clases["CTIc"]['CLIMA_AMBIENTAL'] = ['4']
clases["CTIc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["CTIc"]['PORC_PENDIENTE'] = "<7"
clases["CTIc"]['GRADO_EROSION'] = ["No hay"]
clases["CTIc"]['DRENAJE_NATURAL'] = ['Bien Drenado']
clases["CTIc"]['FRECUENCIA_INUNDACION'] = ['No hay']
clases["CTIc"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CTIc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CTIc"]['PROFUNDIDAD_EFECTIVA'] = '>100'
clases["CTIc"]['H1_CLASE_ESTRUCTURA_1'] = ['Media', 'Muy fina y fina']
clases["CTIc"]['FERTILIDAD'] = '>6.8'
clases["CTIc"]['CE_(dS_m)'] = '<4'
clases["CTIc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CTIc"]['PORC_SAI'] = '<15'
clases["CTIc"]['PORC_CARBONO ORGANICO'] = '>3'

clases["CTIm"] = dict()
clases["CTIm"]['CLIMA_AMBIENTAL'] = ['9']
clases["CTIm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["CTIm"]['PORC_PENDIENTE'] = "<7"
clases["CTIm"]['GRADO_EROSION'] = ["No hay"]
clases["CTIm"]['DRENAJE_NATURAL'] = ['Bien Drenado']
clases["CTIm"]['FRECUENCIA_INUNDACION'] = ['No hay']
clases["CTIm"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CTIm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CTIm"]['PROFUNDIDAD_EFECTIVA'] = '>100'
clases["CTIc"]['H1_CLASE_ESTRUCTURA_1'] = ['Media', 'Muy fina y fina']
clases["CTIm"]['FERTILIDAD'] = '>6.8'
clases["CTIm"]['CE_(dS_m)'] = '<4'
clases["CTIm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CTIm"]['PORC_SAI'] = '<15'
clases["CTIm"]['PORC_CARBONO ORGANICO'] = '>4.2'

clases["CTIf"] = dict()
clases["CTIf"]['CLIMA_AMBIENTAL'] = ['13']
clases["CTIf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["CTIf"]['PORC_PENDIENTE'] = "<7"
clases["CTIf"]['GRADO_EROSION'] = ["No hay"]
clases["CTIf"]['DRENAJE_NATURAL'] = ['Bien Drenado']
clases["CTIf"]['FRECUENCIA_INUNDACION'] = ['No hay']
clases["CTIf"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CTIf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CTIf"]['PROFUNDIDAD_EFECTIVA'] = '>100'
clases["CTIf"]['H1_CLASE_ESTRUCTURA_1'] = ['Media', 'Muy fina y fina']
clases["CTIf"]['FERTILIDAD'] = '>6.8'
clases["CTIf"]['CE_(dS_m)'] = '<4'
clases["CTIf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CTIf"]['PORC_SAI'] = '<15'
clases["CTIf"]['PORC_CARBONO ORGANICO'] = '>5.3'

clases["CTSc"] = dict()
clases["CTSc"]['CLIMA_AMBIENTAL'] = ['3', '4']
clases["CTSc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CTSc"]['PORC_PENDIENTE'] = "<12"
clases["CTSc"]['GRADO_EROSION'] = ["No hay"]
clases["CTSc"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderadamente excesivo', 'Imperfecto']
clases["CTSc"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["CTSc"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CTSc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["CTSc"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["CTSc"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina']
clases["CTSc"]['FERTILIDAD'] = '>3.6'
clases["CTSc"]['CE_(dS_m)'] = '<4'
clases["CTSc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<30'
clases["CTSc"]['PORC_SAI'] = '<15'
clases["CTSc"]['PORC_CARBONO ORGANICO'] = '>0.5'

clases["CTSm"] = dict()
clases["CTSm"]['CLIMA_AMBIENTAL'] = ['8', '9']
clases["CTSm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CTSm"]['PORC_PENDIENTE'] = "<12"
clases["CTSm"]['GRADO_EROSION'] = ["No hay"]
clases["CTSm"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderadamente excesivo', 'imperfecto']
clases["CTSm"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["CTSm"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CTSm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CTSm"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["CTSm"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina']
clases["CTSm"]['FERTILIDAD'] = '>3.6'
clases["CTSm"]['CE_(dS_m)'] = '<4'
clases["CTSm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CTSm"]['PORC_SAI'] = '<30'
clases["CTSm"]['PORC_CARBONO ORGANICO'] = '>1.8'

clases["CTSf"] = dict()
clases["CTSf"]['CLIMA_AMBIENTAL'] = ['12', '13']
clases["CTSf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CTSf"]['PORC_PENDIENTE'] = "<12"
clases["CTSf"]['GRADO_EROSION'] = ["No hay"]
clases["CTSf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto']
clases["CTSf"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["CTSf"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CTSf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CTSf"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["CTSf"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina']
clases["CTSf"]['FERTILIDAD'] = '>3.6'
clases["CTSf"]['CE_(dS_m)'] = '<4'
clases["CTSf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CTSf"]['PORC_SAI'] = '<30'
clases["CTSf"]['PORC_CARBONO ORGANICO'] = '>2.7'

clases["CPIc"] = dict()
clases["CPIc"]['CLIMA_AMBIENTAL'] = ['3', '4']
clases["CPIc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["CPIc"]['PORC_PENDIENTE'] = "<12"
clases["CPIc"]['GRADO_EROSION'] = ["No hay"]
clases["CPIc"]['DRENAJE_NATURAL'] = ['Bien Drenado', 'Moderado']
clases["CPIc"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["CPIc"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CPIc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CPIc"]['PROFUNDIDAD_EFECTIVA'] = '>100'
clases["CPIc"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina']
clases["CPIc"]['FERTILIDAD'] = '>5.2'
clases["CPIc"]['CE_(dS_m)'] = '<4'
clases["CPIc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CPIc"]['PORC_SAI'] = '<15'
clases["CPIc"]['PORC_CARBONO ORGANICO'] = '>1.7'

clases["CPIm"] = dict()
clases["CPIm"]['CLIMA_AMBIENTAL'] = ['8', '9']
clases["CPIm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["CPIm"]['PORC_PENDIENTE'] = "<25"
clases["CPIm"]['GRADO_EROSION'] = ["No hay"]
clases["CPIm"]['DRENAJE_NATURAL'] = ['Bien Drenado', 'Moderado']
clases["CPIm"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["CPIm"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CPIm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CPIm"]['PROFUNDIDAD_EFECTIVA'] = '>100'
clases["CPIm"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina']
clases["CPIm"]['FERTILIDAD'] = '>5.2'
clases["CPIm"]['CE_(dS_m)'] = '<4'
clases["CPIm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CPIm"]['PORC_SAI'] = '<15'
clases["CPIm"]['PORC_CARBONO ORGANICO'] = '>3.0'

clases["CPIf"] = dict()
clases["CPIf"]['CLIMA_AMBIENTAL'] = ['12', '13']
clases["CPIf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["CPIf"]['PORC_PENDIENTE'] = "<12"
clases["CPIf"]['GRADO_EROSION'] = ["No hay"]
clases["CPIf"]['DRENAJE_NATURAL'] = ['Bien Drenado', 'Moderado']
clases["CPIf"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["CPIf"]['H1_VOLUMEN_POR_CFR_1'] = '<3'
clases["CPIf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<1'
clases["CPIf"]['PROFUNDIDAD_EFECTIVA'] = '>100'
clases["CPIf"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina']
clases["CPIf"]['FERTILIDAD'] = '>5.2'
clases["CPIf"]['CE_(dS_m)'] = '<4'
clases["CPIf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CPIf"]['PORC_SAI'] = '<15'
clases["CPIf"]['PORC_CARBONO ORGANICO'] = '>4.1'

clases["CPSc"] = dict()
clases["CPSc"]['CLIMA_AMBIENTAL'] = ['3', '4', '5']
clases["CPSc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CPSc"]['PORC_PENDIENTE'] = "<25"
clases["CPSc"]['GRADO_EROSION'] = ["No hay"]
clases["CPSc"]['DRENAJE_NATURAL'] = ['Bien Drenado', 'Moderado', 'Imperfecto']
clases["CPSc"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["CPSc"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["CPSc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["CPSc"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["CPSc"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina', 'Fina']
clases["CPSc"]['FERTILIDAD'] = '>3.6'
clases["CPSc"]['CE_(dS_m)'] = '<4'
clases["CPSc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CPSc"]['PORC_SAI'] = '<30'
clases["CPSc"]['PORC_CARBONO ORGANICO'] = '>0.5'

clases["CPSm"] = dict()
clases["CPSm"]['CLIMA_AMBIENTAL'] = ['8', '9']
clases["CPSm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CPSm"]['PORC_PENDIENTE'] = "<50"
clases["CPSm"]['GRADO_EROSION'] = ["No hay"]
clases["CPSm"]['DRENAJE_NATURAL'] = ['Bien Drenado', 'Moderado', 'Imperfecto']
clases["CPSm"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["CPSm"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["CPSm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["CPSm"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["CPSm"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina', 'Fina']
clases["CPSm"]['FERTILIDAD'] = '>3.6'
clases["CPSm"]['CE_(dS_m)'] = '<4'
clases["CPSm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CPSm"]['PORC_SAI'] = '<30'
clases["CPSm"]['PORC_CARBONO ORGANICO'] = '>1.8'

clases["CPSf"] = dict()
clases["CPSf"]['CLIMA_AMBIENTAL'] = ['12', '13']
clases["CPSf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CPSf"]['PORC_PENDIENTE'] = "<25"
clases["CPSf"]['GRADO_EROSION'] = ["No hay"]
clases["CPSf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto']
clases["CPSf"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["CPSf"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["CPSf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["CPSf"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["CPSf"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina', 'Fina']
clases["CPSf"]['FERTILIDAD'] = '>3.6'
clases["CPSf"]['CE_(dS_m)'] = '<4'
clases["CPSf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["CPSf"]['PORC_SAI'] = '<30'
clases["CPSf"]['PORC_CARBONO ORGANICO'] = '>2.7'

clases["PINc"] = dict()
clases["PINc"]['CLIMA_AMBIENTAL'] = ['4']
clases["PINc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["PINc"]['PORC_PENDIENTE'] = "<7"
clases["PINc"]['GRADO_EROSION'] = ["No hay"]
clases["PINc"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado']
clases["PINc"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["PINc"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["PINc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["PINc"]['PROFUNDIDAD_EFECTIVA'] = '<50'
clases["PINc"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa', 'Media', 'Muy fina y fina']
clases["PINc"]['FERTILIDAD'] = '>5.2'
clases["PINc"]['CE_(dS_m)'] = '<4'
clases["PINc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PINc"]['PORC_SAI'] = '<30'
clases["PINc"]['PORC_CARBONO ORGANICO'] = '>3.0'

clases["PINm"] = dict()
clases["PINm"]['CLIMA_AMBIENTAL'] = ['9']
clases["PINm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["PINm"]['PORC_PENDIENTE'] = "<7"
clases["PINm"]['GRADO_EROSION'] = ["No hay"]
clases["PINm"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado']
clases["PINm"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["PINm"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["PINm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["PINm"]['PROFUNDIDAD_EFECTIVA'] = '<50'
clases["PINm"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa , Media', 'Muy fina y fina']
clases["PINm"]['FERTILIDAD'] = '>5.2'
clases["PINm"]['CE_(dS_m)'] = '<4'
clases["PINm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PINm"]['PORC_SAI'] = '<30'
clases["PINm"]['PORC_CARBONO ORGANICO'] = '>4.2'

clases["PINf"] = dict()
clases["PINf"]['CLIMA_AMBIENTAL'] = ['13']
clases["PINf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal']
clases["PINf"]['PORC_PENDIENTE'] = "<7"
clases["PINf"]['GRADO_EROSION'] = ["No hay"]
clases["PINf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado']
clases["PINf"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["PINf"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["PINf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["PINf"]['PROFUNDIDAD_EFECTIVA'] = '<50'
clases["PINf"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa , Media', 'Muy fina y fina']
clases["PINf"]['FERTILIDAD'] = '>5.2'
clases["PINf"]['CE_(dS_m)'] = '<4'
clases["PINf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PINf"]['PORC_SAI'] = '<30'
clases["PINf"]['PORC_CARBONO ORGANICO'] = '>5.3'

clases["PSIc"] = dict()
clases["PSIc"]['CLIMA_AMBIENTAL'] = ['3', '4', '5']
clases["PSIc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["PSIc"]['PORC_PENDIENTE'] = "<12"
clases["PSIc"]['GRADO_EROSION'] = ["Ligero"]
clases["PSIc"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto']
clases["PSIc"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["PSIc"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["PSIc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["PSIc"]['PROFUNDIDAD_EFECTIVA'] = '<25'
clases["PSIc"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa , Media', 'Muy fina y fina', 'Fina']
clases["PSIc"]['FERTILIDAD'] = '>3.6'
clases["PSIc"]['CE_(dS_m)'] = '<8'
clases["PSIc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PSIc"]['PORC_SAI'] = '<30'
clases["PSIc"]['PORC_CARBONO ORGANICO'] = '>0.5'

clases["PSIm"] = dict()
clases["PSIm"]['CLIMA_AMBIENTAL'] = ['8', '9']
clases["PSIm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["PSIm"]['PORC_PENDIENTE'] = "<12"
clases["PSIm"]['GRADO_EROSION'] = ["Ligero"]
clases["PSIm"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto']
clases["PSIm"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["PSIm"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["PSIm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["PSIm"]['PROFUNDIDAD_EFECTIVA'] = '<25'
clases["PSIm"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa , Media', 'Muy fina y fina', 'Fina']
clases["PSIm"]['FERTILIDAD'] = '>3.6'
clases["PSIm"]['CE_(dS_m)'] = '<8'
clases["PSIm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PSIm"]['PORC_SAI'] = '<30'
clases["PSIm"]['PORC_CARBONO ORGANICO'] = '>1.8'

clases["PSIf"] = dict()
clases["PSIf"]['CLIMA_AMBIENTAL'] = ['12', '13']
clases["PSIf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["PSIf"]['PORC_PENDIENTE'] = "<12"
clases["PSIf"]['GRADO_EROSION'] = ["Ligero"]
clases["PSIf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto']
clases["PSIf"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["PSIf"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["PSIf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["PSIf"]['PROFUNDIDAD_EFECTIVA'] = '<25'
clases["PSIf"]['H1_CLASE_ESTRUCTURA_1'] = ['Media y gruesa , Media', 'Muy fina y fina', 'Fina']
clases["PSIf"]['FERTILIDAD'] = '>3.6'
clases["PSIf"]['CE_(dS_m)'] = '<8'
clases["PSIf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PSIf"]['PORC_SAI'] = '<30'
clases["PSIf"]['PORC_CARBONO ORGANICO'] = '>2.7'

clases["PEXc"] = dict()
clases["PEXc"]['CLIMA_AMBIENTAL'] = ['2', '3', '4', '5']
clases["PEXc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["PEXc"]['PORC_PENDIENTE'] = "<25"
clases["PEXc"]['GRADO_EROSION'] = ["Ligero"]
clases["PEXc"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["PEXc"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["PEXc"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["PEXc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["PEXc"]['PROFUNDIDAD_EFECTIVA'] = '>10'
clases["PEXc"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa , Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["PEXc"]['FERTILIDAD'] = '>0.5'
clases["PEXc"]['CE_(dS_m)'] = '<8'
clases["PEXc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PEXc"]['PORC_SAI'] = '<60'
clases["PEXc"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["PEXm"] = dict()
clases["PEXm"]['CLIMA_AMBIENTAL'] = ['7', '8', '9', '10']
clases["PEXm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["PEXm"]['PORC_PENDIENTE'] = "<25"
clases["PEXm"]['GRADO_EROSION'] = ["Ligero"]
clases["PEXm"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["PEXm"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["PEXm"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["PEXm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["PEXm"]['PROFUNDIDAD_EFECTIVA'] = '>10'
clases["PEXm"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa , Media y gruesa , Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["PEXm"]['FERTILIDAD'] = '>0.5'
clases["PEXm"]['CE_(dS_m)'] = '<8'
clases["PEXm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PEXm"]['PORC_SAI'] = '<60'
clases["PEXm"]['PORC_CARBONO ORGANICO'] = '>0.6'

clases["PEXf"] = dict()
clases["PEXf"]['CLIMA_AMBIENTAL'] = ['12', '13', '14']
clases["PEXf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["PEXf"]['PORC_PENDIENTE'] = "<25"
clases["PEXf"]['GRADO_EROSION'] = ["Ligero"]
clases["PEXf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["PEXf"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["PEXf"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["PEXf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["PEXf"]['PROFUNDIDAD_EFECTIVA'] = '>10'
clases["PEXf"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["PEXf"]['FERTILIDAD'] = '>0.5'
clases["PEXf"]['CE_(dS_m)'] = '<8'
clases["PEXf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PEXf"]['PORC_SAI'] = '<60'
clases["PEXf"]['PORC_CARBONO ORGANICO'] = '>1.4'

clases["PEXmf"] = dict()
clases["PEXmf"]['CLIMA_AMBIENTAL'] = ['16', '17']
clases["PEXmf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["PEXmf"]['PORC_PENDIENTE'] = "<12"
clases["PEXmf"]['GRADO_EROSION'] = ["Ligero"]
clases["PEXmf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["PEXmf"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["PEXmf"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["PEXmf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["PEXmf"]['PROFUNDIDAD_EFECTIVA'] = '>10'
clases["PEXmf"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                            'Muy gruesa', 'Fina y media']
clases["PEXmf"]['FERTILIDAD'] = '>0.5'
clases["PEXmf"]['CE_(dS_m)'] = '<8'
clases["PEXmf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["PEXmf"]['PORC_SAI'] = '<60'
clases["PEXmf"]['PORC_CARBONO ORGANICO'] = '>1.4'

clases["AGSt"] = dict()
clases["AGSt"]['CLIMA_AMBIENTAL'] = ['3', '4', '8', '9', '13', '14', '15']
clases["AGSt"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["AGSt"]['PORC_PENDIENTE'] = "<25"
clases["AGSt"]['GRADO_EROSION'] = ["No hay"]
clases["AGSt"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto']
clases["AGSt"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["AGSt"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["AGSt"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["AGSt"]['PROFUNDIDAD_EFECTIVA'] = '>25'
clases["AGSt"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["AGSt"]['FERTILIDAD'] = '>0.5'
clases["AGSt"]['CE_(dS_m)'] = '<8'
clases["AGSt"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["AGSt"]['PORC_SAI'] = '<60'
clases["AGSt"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["AGSp"] = dict()
clases["AGSp"]['CLIMA_AMBIENTAL'] = ['3', '4', '5', '6', '8', '9', '13', '14', '15']
clases["AGSp"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["AGSp"]['PORC_PENDIENTE'] = "<75"
clases["AGSp"]['GRADO_EROSION'] = ["Ligero"]
clases["AGSp"]['DRENAJE_NATURAL'] = ['Excesivo , Bien drenado', 'Moderado']
clases["AGSp"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["AGSp"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["AGSp"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["AGSp"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["AGSp"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["AGSp"]['FERTILIDAD'] = '>0.5'
clases["AGSp"]['CE_(dS_m)'] = '<8'
clases["AGSp"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["AGSp"]['PORC_SAI'] = '<60'
clases["AGSp"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["ASPt"] = dict()
clases["ASPt"]['CLIMA_AMBIENTAL'] = ['3', '4', '8', '9', '13', '14', '18']
clases["ASPt"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["ASPt"]['PORC_PENDIENTE'] = "<25"
clases["ASPt"]['GRADO_EROSION'] = ["Moderado"]
clases["ASPt"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto']
clases["ASPt"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["ASPt"]['H1_VOLUMEN_POR_CFR_1'] = '<15'
clases["ASPt"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<3'
clases["ASPt"]['PROFUNDIDAD_EFECTIVA'] = '>25'
clases["ASPt"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["ASPt"]['FERTILIDAD'] = '>0.5'
clases["ASPt"]['CE_(dS_m)'] = '<8'
clases["ASPt"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["ASPt"]['PORC_SAI'] = '<60'
clases["ASPt"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["ASPp"] = dict()
clases["ASPp"]['CLIMA_AMBIENTAL'] = ['3', '4', '5', '8', '9', '10', '13', '14']
clases["ASPp"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["ASPp"]['PORC_PENDIENTE'] = "<50"
clases["ASPp"]['GRADO_EROSION'] = ["Moderado"]
clases["ASPp"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado']
clases["ASPp"]['FRECUENCIA_INUNDACION'] = ['Raras']
clases["ASPp"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["ASPp"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["ASPp"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["ASPp"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["ASPp"]['FERTILIDAD'] = '>0.5'
clases["ASPp"]['CE_(dS_m)'] = '<8'
clases["ASPp"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["ASPp"]['PORC_SAI'] = '<60'
clases["ASPp"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["SPA"] = dict()
clases["SPA"]['CLIMA_AMBIENTAL'] = ['2', '3', '4', '5', '7', '8', '9', '10', '12', '13', '15', '17', '18']
clases["SPA"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["SPA"]['PORC_PENDIENTE'] = "<50"
clases["SPA"]['GRADO_EROSION'] = ["Moderado"]
clases["SPA"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["SPA"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["SPA"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["SPA"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["SPA"]['PROFUNDIDAD_EFECTIVA'] = '>25'
clases["SPA"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Muy fina',
                                          'Muy gruesa', 'Fina y media']
clases["SPA"]['FERTILIDAD'] = '>0.5'
clases["SPA"]['CE_(dS_m)'] = '<16'
clases["SPA"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["SPA"]['PORC_SAI'] = '<90'
clases["SPA"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["FPDc"] = dict()
clases["FPDc"]['CLIMA_AMBIENTAL'] = ['3', '4', '5', '6']
clases["FPDc"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["FPDc"]['PORC_PENDIENTE'] = "<25"
clases["FPDc"]['GRADO_EROSION'] = ["Ligero"]
clases["FPDc"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["FPDc"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["FPDc"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["FPDc"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["FPDc"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["FPDc"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["FPDc"]['FERTILIDAD'] = '>1.0'
clases["FPDc"]['CE_(dS_m)'] = '<4'
clases["FPDc"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["FPDc"]['PORC_SAI'] = '<30'
clases["FPDc"]['PORC_CARBONO ORGANICO'] = '>0.5'

clases["FPDm"] = dict()
clases["FPDm"]['CLIMA_AMBIENTAL'] = ['8', '9', '10']
clases["FPDm"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["FPDm"]['PORC_PENDIENTE'] = "<25"
clases["FPDm"]['GRADO_EROSION'] = ["Ligero"]
clases["FPDm"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["FPDm"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["FPDm"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["FPDm"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["FPDm"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["FPDm"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina' , 'Muy fina', 'Muy gruesa',
                                           'Fina y media']
clases["FPDm"]['FERTILIDAD'] = '>1.0'
clases["FPDm"]['CE_(dS_m)'] = '<4'
clases["FPDm"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["FPDm"]['PORC_SAI'] = '<30'
clases["FPDm"]['PORC_CARBONO ORGANICO'] = '>1.8'

clases["FPDf"] = dict()
clases["FPDf"]['CLIMA_AMBIENTAL'] = ['13', '14', '15', '16']
clases["FPDf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["FPDf"]['PORC_PENDIENTE'] = "<25"
clases["FPDf"]['GRADO_EROSION'] = ["Ligero"]
clases["FPDf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["FPDf"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["FPDf"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["FPDf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["FPDf"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["FPDf"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                           'Muy gruesa', 'Fina y media']
clases["FPDf"]['FERTILIDAD'] = '>1.0'
clases["FPDf"]['CE_(dS_m)'] = '<4'
clases["FPDf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["FPDf"]['PORC_SAI'] = '<30'
clases["FPDf"]['PORC_CARBONO ORGANICO'] = '>2.7'

clases["FPDmf"] = dict()
clases["FPDmf"]['CLIMA_AMBIENTAL'] = ['17', '18']
clases["FPDmf"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["FPDmf"]['PORC_PENDIENTE'] = "<12"
clases["FPDmf"]['GRADO_EROSION'] = ["Ligero"]
clases["FPDmf"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["FPDmf"]['FRECUENCIA_INUNDACION'] = ['Ocasional']
clases["FPDmf"]['H1_VOLUMEN_POR_CFR_1'] = '<35'
clases["FPDmf"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<15'
clases["FPDmf"]['PROFUNDIDAD_EFECTIVA'] = '>50'
clases["FPDmf"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                            'Muy gruesa', 'Fina y media']
clases["FPDmf"]['FERTILIDAD'] = '>1.0'
clases["FPDmf"]['CE_(dS_m)'] = '<4'
clases["FPDmf"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["FPDmf"]['PORC_SAI'] = '<30'
clases["FPDmf"]['PORC_CARBONO ORGANICO'] = '>2.7'

clases["FPP"] = dict()
clases["FPP"]['CLIMA_AMBIENTAL'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                    '16', '17']
clases["FPP"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["FPP"]['PORC_PENDIENTE'] = "<50"
clases["FPP"]['GRADO_EROSION'] = ["Moderado"]
clases["FPP"]['DRENAJE_NATURAL'] = ['Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["FPP"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["FPP"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["FPP"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["FPP"]['PROFUNDIDAD_EFECTIVA'] = '>10'
clases["FPP"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina' , 'Muy fina' , 'Muy gruesa', 'Fina y media']
clases["FPP"]['FERTILIDAD'] = '>0.5'
clases["FPP"]['CE_(dS_m)'] = '<16'
clases["FPP"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["FPP"]['PORC_SAI'] = '<90'
clases["FPP"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["FPR"] = dict()
clases["FPR"]['CLIMA_AMBIENTAL'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                    '16', '17', '18', '19']
clases["FPR"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["FPR"]['PORC_PENDIENTE'] = "<100"
clases["FPR"]['GRADO_EROSION'] = ["Severo"]
clases["FPR"]['DRENAJE_NATURAL'] = ['Excesivo', 'Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["FPR"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["FPR"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["FPR"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["FPR"]['PROFUNDIDAD_EFECTIVA'] = '>10'
clases["FPR"]['H1_CLASE_ESTRUCTURA_1'] = ['Gruesa', 'Media y gruesa', 'Media', 'Muy fina y fina', 'Fina', 'Muy fina',
                                          'Muy gruesa', 'Fina y media']
clases["FPR"]['FERTILIDAD'] = '>0.5'
clases["FPR"]['CE_(dS_m)'] = '<16'
clases["FPR"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '<15'
clases["FPR"]['PORC_SAI'] = '<90'
clases["FPR"]['PORC_CARBONO ORGANICO'] = '>0.2'

clases["CRE"] = dict()
clases["CRE"]['CLIMA_AMBIENTAL'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                    '16', '17', '18', '19']
clases["CRE"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CRE"]['PORC_PENDIENTE'] = "<100"
clases["CRE"]['GRADO_EROSION'] = ["Severo"]
clases["CRE"]['DRENAJE_NATURAL'] = ['Excesivo , Bien drenado', 'Moderado', 'Imperfecto', 'Pobre']
clases["CRE"]['FRECUENCIA_INUNDACION'] = ['Frecuente']
clases["CRE"]['H1_VOLUMEN_POR_CFR_1'] = '<60'
clases["CRE"]['PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA'] = '<50'
clases["CRE"]['PROFUNDIDAD_EFECTIVA'] = '>10'
# clases["CRE"]['H1_CLASE_ESTRUCTURA_1'] =['Gruesa' , 'Media y gruesa' ,'Media' , 'Muy fina' , 'fina', 'Fina' , 'Muy fina' , 'Muy gruesa' , 'Fina y media']
# clases["CRE"]['FERTILIDAD'] = '>0.5'
clases["CRE"]['CE_(dS_m)'] = '>8'
clases["CRE"]['PORC_SAT_SODIO\nSALINIDAD_PSI '] = '>15'
# clases["CRE"]['PORC_SAI'] = '<15'
# clases["CRE"]['PORC_CARBONO ORGANICO'] =


clases["CRH"] = dict()
clases["CRH"]['CLIMA_AMBIENTAL'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                    '16', '17', '18', '19', '20', '21']
clases["CRH"]['DISTRIBUCION_LLUVIAS'] = ['Bimodal', 'Monomodal']
clases["CRH"]['PORC_PENDIENTE'] = "<100"
clases["CRH"]['DRENAJE_NATURAL'] = ['pantanoso']


def mapear_distribucion_lluvias_a_monomodal_o_bimodal(bimodal_o_modal):
    if bimodal_o_modal == 'Monomodal o Bimodal':
        return ['bimodal', 'monomodal']
    return bimodal_o_modal


def conseguir_ACIDEZ_POR_de_sales_y_sodio(sales_y_sodio):
    if sales_y_sodio == 'No hay':
        return "<4"
    if 'S1' in sales_y_sodio:
        return "4-8"
    if 'S2' in sales_y_sodio:
        return "8-16"
    if 'S3' in sales_y_sodio or "S4" in sales_y_sodio:
        return ">16"
    if sales_y_sodio == 'Na (Na > 100cm)':
        return "<4"


def conseguir_porcentaje_de_sodio_de_sales_y_sodio(sales_y_sodio):
    if sales_y_sodio == 'No hay':
        return "<15"
    if "Na" in sales_y_sodio:
        return ">15"
    return "<15"


def mapear_pendiente_a_rango(symbolo):
    return symbolo


def mapear_fertilidad_a_rango(symbolo):
    if symbolo == '0':
        return '0'
    if symbolo.lower() == 'Muy baja'.lower():
        return "0.5-3.5"
    if symbolo.lower() == 'Baja'.lower():
        return "3.6-5.1"
    if symbolo.lower() == 'Media'.lower():
        return "5.2-6.7"
    if symbolo.lower() == 'Alta'.lower():
        return "6.8-8.4"
    if symbolo.lower() == 'Muy alta'.lower():
        return ">8.4"


def mapear_clase_fertilidad_a_rango(fertilidad):
    if fertilidad == 'Muy alta':
        return conseguir_minimo_y_maximo(">8.4")
    if fertilidad == 'Alta':
        return conseguir_minimo_y_maximo("6.8 - 8.4")
    if fertilidad == 'Moderada':
        return conseguir_minimo_y_maximo("5.2 - 6.7")
    if fertilidad == 'Baja':
        return conseguir_minimo_y_maximo("3.6 - 5.1")
    if fertilidad == 'Muy Baja':
        return conseguir_minimo_y_maximo("0.5 - 3.5")


def conseguir_grupo_textual(fila_del_excel):
    if 'Grupo Textual' in fila_del_excel:
        if fila_del_excel['Grupo Textual'] in ['A', 'AF']:
            return "Gruesa"
        if fila_del_excel['Grupo Textual'] in ['FA']:
            return "Media y gruesa"
        if fila_del_excel['Grupo Textual'] in ['F', 'FL', 'L']:
            return "Media"
        if fila_del_excel['Grupo Textual'] in ['FAr', 'FArA', 'FArL']:
            return "Muy fina y fina"
        if fila_del_excel['Grupo Textual'] in ['ArA', 'ArL', 'Ar fina']:
            return "Fina"
        if fila_del_excel['Grupo Textual'] in ['Ar muy fina']:
            return "Muy Fina"


def conseguir_minimo_y_maximo(rango, atributo=None):
    if rango == 'No hay':
        respuesta = dict()
        respuesta['minimo'] = 0
        respuesta['maximo'] = 0
        return respuesta
    minimo_default = 0
    maximo_default = 100
    if atributo is not None:
        minimo_default = minimo_y_maximos_por_atributo[atributo]['minimo']
        maximo_default = minimo_y_maximos_por_atributo[atributo]['maximo']
    if "," in rango:
        rango = rango.replace(",", ".")
    if '%' in rango:
        rango = rango.replace("%", "")
    ### para rangos como <15
    if "<" in rango:
        respuesta = dict()
        respuesta['minimo'] = float(rango.replace("<", ""))
        respuesta['maximo'] = float(rango.replace("<", ""))
        return respuesta
    ### para rangos como >50
    if ">" in rango:
        respuesta = dict()
        respuesta['minimo'] = float(rango.replace(">", ""))
        respuesta['maximo'] = float(rango.replace(">", ""))
        return respuesta
    ## para rangos como 3 -7
    if '-' in rango:
        valores = rango.split("-")
        respuesta = dict()
        respuesta['minimo'] = float(valores[0])
        respuesta['maximo'] = float(valores[1])
    ##para rangos que solo es un numero
    else:
        respuesta = dict()
        respuesta['minimo'] = float(rango)
        respuesta['maximo'] = float(rango)

    return respuesta


def function_para_clasificar(fila_del_excel):
    respuesta = dict()
    Clases_que_son = list()
    clases_que_no_con_razon = dict()
    for clase in clases:
        califica_como_clase = True
        razones_por_que_no = list()
        for atributo in clases[clase]:
            regla = clases[clase][atributo]
            valor_de_atributo = fila_del_excel[atributo]

            '''
            Denominación:
	•	Ligera		== <4		== 1
	•	Modera		== 4 – 8 	== 2
	•	Fuerte		== 8 – 16 	== 3
Sodicidad - %

Suelos sódicos son aquellos que tienen una relación de adsorción de sodio (RAS) mayor de 13. Anteriormente se utilizaba como unidad de media el porciento de saturación de sodio (PSI) y 15% de saturación de sodio para separar los suelos sódicos de los normales. 
No existe una clasificación para determinar las clases de contenido de sodio en el suelo; se ha establecido que un RAS de 13 o mayor, o un contenido de sodio del 15% o mayor afecta el crecimiento normal de los cultivos.
Denominación:
	•	No sódico	== <15		== 1
	•	Sódico		== >15	 	== 2

CE mmhos/cm a 25°C

Denominación:
	•	<4		== 1
	•	4-8		== 2
	•	8-16		== 3
	•	>16		== 4





            '''

            if 'N.D.' == valor_de_atributo.upper() or 'N/A' in valor_de_atributo.upper() or 'Sin dato'.lower() == valor_de_atributo.lower() or valor_de_atributo.strip() == '':
                continue

            if atributo == 'PORC_PENDIENTE':
                valor_de_atributo = mapear_pendiente_a_rango(valor_de_atributo)
            elif atributo == 'DISTRIBUCION_LLUVIAS':
                valor_de_atributo = mapear_distribucion_lluvias_a_monomodal_o_bimodal(valor_de_atributo)
            elif atributo == 'FERTILIDAD':
                valor_de_atributo = mapear_fertilidad_a_rango(valor_de_atributo)
            else:
                valor_de_atributo = fila_del_excel[atributo]

            califica_como_clase = True
            ## El atributo es una lista, y hay que ver si este previo esta en la es
            if type(regla) is list:
                regla = list(map(lambda x: x.lower(), regla))

                if type(valor_de_atributo) is list:
                    is_in_list = False
                    for value in valor_de_atributo:
                        if value.lower() in regla:
                            is_in_list = True
                            break
                    if not is_in_list:
                        razones_por_que_no.append(atributo)
                        califica_como_clase = False

                elif valor_de_atributo.lower() not in regla:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False
            ## El atributo es rango con un maximo, como ['PENDIENTE'] = "<7"
            if "<" in regla:
                maximo = regla
                if "," in maximo:
                    maximo = maximo.replace(",", ".")
                maximo = float(maximo.replace("<", ""))
                valor_de_atributo_min_max = conseguir_minimo_y_maximo(valor_de_atributo)
                if valor_de_atributo_min_max['maximo'] > maximo:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False
            ## El atributo es rango con un minimo, como ['PENDIENTE'] = "<7"
            if ">" in regla:
                minimo = regla
                if "," in minimo:
                    minimo = minimo.replace(",", ".")
                minimo = float(minimo.replace(">", ""))
                valor_de_atributo_min_max = conseguir_minimo_y_maximo(valor_de_atributo)
                if valor_de_atributo_min_max['minimo'] < minimo:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False

        if califica_como_clase:
            # print(fila_del_excel['COD_PERFIL'] + " calificomo"+ ' ' + clase)
            Clases_que_son.append(clase)
        else:
            clases_que_no_con_razon[clase] = razones_por_que_no

            # print("no calificomo" + clase)
    respuesta['clases'] = Clases_que_son
    respuesta['clases_que_con_razones'] = clases_que_no_con_razon

    if len(Clases_que_son) == 0:
        print(fila_del_excel['COD_PERFIL'] + " no tiene classes")
        print(clases_que_no_con_razon)
        listas_de_razones = list()

        for clase in clases_que_no_con_razon:
            razones = clases_que_no_con_razon[clase]
            listas_de_razones.append(razones)
        print(set.intersection(*map(set, listas_de_razones)))
    return respuesta


def leer_csv_de_previas():
    with open('clases.csv', mode='w', encoding='utf-8') as output:
        csvwriter = csv.writer(output, delimiter=';')
        csvwriter.writerow(['COD_PERFIL', 'UCS_F', 'CLASES'])
        with open('20231226 Base Magdalena y Cesar_Información SHAPE.csv', mode='r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            line_count = 0


            for row in csv_reader:
                resultado = function_para_clasificar(row)
                csvwriter.writerow([row['COD_PERFIL'], row['UCS_F'], ",".join(resultado['clases'])])

            print('final')


def correr_pruebas():
    respuesta = function_para_clasificar(prueba)
    print(respuesta)


# correr_pruebas()


def conseguir_previas_de_shapefile(shapefile_path):
    sf = shapefile.Reader("Vocacion/Vocacion.shp", dbf="Vocacion/Vocacion.dbf")
    writer = shapefile.Writer(dbf='new_file4.dbf')

    for field in sf.fields:
        if field[0] == 'DeletionFlag':
            continue
        writer.field(field[0], field[1], field[2])

    for clase in clases:
        writer.field(clase, 'C', '50')

    for record in sf.records():
        new_record = dict(record.as_dict())

        ###por cada vocacion
        for clase in clases:
            new_record[clase] = 'si'

        writer.record(**new_record)

        # resultados = function_para_clasificar(record.as_dict())

        # print(resultados)
    writer.close()

    ##r = shapefile.Reader(dbf='new_file3.dbf')


leer_csv_de_previas()
