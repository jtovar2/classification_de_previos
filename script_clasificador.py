import csv
import shapefile


print('ejemplooo')
minimo_y_maximos_por_atributo = dict()
minimo_y_maximos_por_atributo['Profundidad efectiva (cm)'] = dict()
minimo_y_maximos_por_atributo['Profundidad efectiva (cm)']['minimo'] = 0
minimo_y_maximos_por_atributo['Profundidad efectiva (cm)']['maximo'] = 151

## array based
##  <50


prueba = dict()
#prueba['CLASE_DE_C'] = '4'
#prueba['CLASE_DE_H'] = '5'
prueba['Pendiente'] = 'b'
prueba['Erosion\n(Grado)'] = "No hay"
prueba['Drenaje natural'] = 'Bien Drenado'
prueba['Inundaciones/Encharcamientos\n(Frecuencia)'] = 'No hay'
prueba['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
prueba['Fragmentos roca (% por Vol.) '] = '<3'
prueba['Profundidad efectiva (cm)'] = '100-150'
prueba['Fertilidad'] = 'muy baja'
prueba['Sales y sodio'] = 'No hay'
#prueba['SODICIDAD'] = '0-15'


clases = dict()
clases["CTIc"] = dict()
#clases["CTIc"]['CLASE_DE_C'] = ['4']
#clases["CTIc"]['CLASE_DE_H'] = ['bimodal']
clases["CTIc"]['Pendiente'] = "<7"
clases["CTIc"]['Erosion\n(Grado)'] = ["No hay"]
clases["CTIc"]['Drenaje natural'] = ['Bien Drenado']
clases["CTIc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['No hay']
clases["CTIc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CTIc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIc"]['Profundidad efectiva (cm)'] = '>100'
clases["CTIc"]['Fertilidad'] = '>6.8'
clases["CTIc"]['ACIDEZ_POR'] = '<4'
#clases["CTIc"]['SALINIDAD'] = '<15'
#clases["CTIc"]['SODICIDAD'] = '<15'


clases["CTIm"] = dict()
#clases["CTIm"]['CLASE_DE_C'] = ['9']
#clases["CTIm"]['CLASE_DE_H'] = ['bimodal']
clases["CTIm"]['Pendiente'] = "<7"
clases["CTIm"]['Erosion\n(Grado)'] = ["no hay"]
clases["CTIm"]['Drenaje natural'] = ['bien Drenado']
clases["CTIm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['no hay']
clases["CTIm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CTIm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIm"]['Profundidad efectiva (cm)'] = '>100'
clases["CTIm"]['Fertilidad'] = '>6.8'
clases["CTIm"]['ACIDEZ_POR'] = '<4'
#clases["CTIm"]['SALINIDAD'] = '<15'
#clases["CTIm"]['SODICIDAD'] = '<15'


clases["CTIf"] = dict()
#clases["CTIf"]['CLASE_DE_C'] = ['13']
#clases["CTIf"]['CLASE_DE_H'] = ['bimodal']
clases["CTIf"]['Pendiente'] = "<7"
clases["CTIf"]['Erosion\n(Grado)'] = ["no hay"]
clases["CTIf"]['Drenaje natural'] = ['bien Drenado']
clases["CTIf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['no hay']
clases["CTIf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CTIf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIf"]['Profundidad efectiva (cm)'] = '>100'
clases["CTIf"]['Fertilidad'] = '>6.8'
clases["CTIf"]['ACIDEZ_POR'] = '<4'
#clases["CTIf"]['SALINIDAD'] = '<15'
#clases["CTIf"]['SODICIDAD'] = '<15'


clases["CTSc"] = dict()
#clases["CTSc"]['CLASE_DE_C'] = ['3 , 4']
#clases["CTSc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CTSc"]['Pendiente'] = "<12"
clases["CTSc"]['Erosion\n(Grado)'] = ["no hay"]
clases["CTSc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CTSc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["CTSc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CTSc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSc"]['Profundidad efectiva (cm)'] = '>50'
clases["CTSc"]['Fertilidad'] = '>3.6'
clases["CTSc"]['ACIDEZ_POR'] = '<4'
#clases["CTSc"]['SALINIDAD'] = '<15'
#clases["CTSc"]['SODICIDAD'] = '<30'


clases["CTSm"] = dict()
#clases["CTSm"]['CLASE_DE_C'] = ['8 , 9']
#clases["CTSm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CTSm"]['Pendiente'] = "<12"
clases["CTSm"]['Erosion\n(Grado)'] = ["no hay"]
clases["CTSm"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CTSm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["CTSm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CTSm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSm"]['Profundidad efectiva (cm)'] = '>50'
clases["CTSm"]['Fertilidad'] = '>3.6'
clases["CTSm"]['ACIDEZ_POR'] = '<4'
#clases["CTSm"]['SALINIDAD'] = '<15'
#clases["CTSm"]['SODICIDAD'] = '<30'


clases["CTSf"] = dict()
#clases["CTSf"]['CLASE_DE_C'] = ['12 , 13']
#clases["CTSf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CTSf"]['Pendiente'] = "<12"
clases["CTSf"]['Erosion\n(Grado)'] = ["no hay"]
clases["CTSf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CTSf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["CTSf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CTSf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSf"]['Profundidad efectiva (cm)'] = '>50'
clases["CTSf"]['Fertilidad'] = '>3.6'
clases["CTSf"]['ACIDEZ_POR'] = '<4'
#clases["CTSf"]['SALINIDAD'] = '<15'
#clases["CTSf"]['SODICIDAD'] = '<30'


clases["CPIc"] = dict()
#clases["CPIc"]['CLASE_DE_C'] = ['3 , 4']
#clases["CPIc"]['CLASE_DE_H'] = ['bimodal']
clases["CPIc"]['Pendiente'] = "<12"
clases["CPIc"]['Erosion\n(Grado)'] = ["no hay"]
clases["CPIc"]['Drenaje natural'] = ['bueno , moderado']
clases["CPIc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["CPIc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CPIc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIc"]['Profundidad efectiva (cm)'] = '>100'
clases["CPIc"]['Fertilidad'] = '>5.2'
clases["CPIc"]['ACIDEZ_POR'] = '<4'
#clases["CPIc"]['SALINIDAD'] = '<15'
#clases["CPIc"]['SODICIDAD'] = '<15'



clases["CPIm"] = dict()
#clases["CPIm"]['CLASE_DE_C'] = ['3 , 4']
#clases["CPIm"]['CLASE_DE_H'] = ['bimodal']
clases["CPIm"]['Pendiente'] = "<12"
clases["CPIm"]['Erosion\n(Grado)'] = ["no hay"]
clases["CPIm"]['Drenaje natural'] = ['bueno , moderado']
clases["CPIm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["CPIm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CPIm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIm"]['Profundidad efectiva (cm)'] = '>100'
clases["CPIm"]['Fertilidad'] = '>5.2'
clases["CPIm"]['ACIDEZ_POR'] = '<4'
#clases["CPIm"]['SALINIDAD'] = '<15'
#clases["CPIm"]['SODICIDAD'] = '<15'

clases["CPIf"] = dict()
#clases["CPIf"]['CLASE_DE_C'] = ['12 , 13']
#clases["CPIf"]['CLASE_DE_H'] = ['bimodal']
clases["CPIf"]['Pendiente'] = "<12"
clases["CPIf"]['Erosion\n(Grado)'] = ["no hay"]
clases["CPIf"]['Drenaje natural'] = ['bueno , moderado']
clases["CPIf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["CPIf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<3'
clases["CPIf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIf"]['Profundidad efectiva (cm)'] = '>100'
clases["CPIf"]['Fertilidad'] = '>5.2'
clases["CPIf"]['ACIDEZ_POR'] = '<4'
#clases["CPIf"]['SALINIDAD'] = '<15'
#clases["CPIf"]['SODICIDAD'] = '<15'


clases["CPSc"] = dict()
#clases["CPSc"]['CLASE_DE_C'] = ['3 , 4 , 5']
#clases["CPSc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CPSc"]['Pendiente'] = "<25"
clases["CPSc"]['Erosion\n(Grado)'] = ["no hay"]
clases["CPSc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CPSc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["CPSc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["CPSc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPSc"]['Profundidad efectiva (cm)'] = '>50'
clases["CPSc"]['Fertilidad'] = '>3.6'
clases["CPSc"]['ACIDEZ_POR'] = '<4'
#clases["CPSc"]['SALINIDAD'] = '<15'
#clases["CPSc"]['SODICIDAD'] = '<30'

clases["CPSm"] = dict()
#clases["CPSm"]['CLASE_DE_C'] = ['8 , 9']
#clases["CPSm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CPSm"]['Pendiente'] = "<25"
clases["CPSm"]['Erosion\n(Grado)'] = ["no hay"]
clases["CPSm"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CPSm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["CPSm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["CPSm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPSm"]['Profundidad efectiva (cm)'] = '>50'
clases["CPSm"]['Fertilidad'] = '>3.6'
clases["CPSm"]['ACIDEZ_POR'] = '<4'
#clases["CPSm"]['SALINIDAD'] = '<15'
#clases["CPSm"]['SODICIDAD'] = '<30'

clases["CPSf"] = dict()
#clases["CPSf"]['CLASE_DE_C'] = ['12 , 13']
#clases["CPSf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CPSf"]['Pendiente'] = "<25"
clases["CPSf"]['Erosion\n(Grado)'] = ["no hay"]
clases["CPSf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CPSf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["CPSf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["CPSf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPSf"]['Profundidad efectiva (cm)'] = '>50'
clases["CPSf"]['Fertilidad'] = '>3.6'
clases["CPSf"]['ACIDEZ_POR'] = '<4'
#clases["CPSf"]['SALINIDAD'] = '<15'
#clases["CPSf"]['SODICIDAD'] = '<30'

clases["PINc"] = dict()
#clases["PINc"]['CLASE_DE_C'] = ['4']
#clases["PINc"]['CLASE_DE_H'] = ['bimodal']
clases["PINc"]['Pendiente'] = "<7"
clases["PINc"]['Erosion\n(Grado)'] = ["no hay"]
clases["PINc"]['Drenaje natural'] = ['bueno , moderado']
clases["PINc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["PINc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["PINc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["PINc"]['Profundidad efectiva (cm)'] = '<50'
clases["PINc"]['Fertilidad'] = '>5.2'
clases["PINc"]['ACIDEZ_POR'] = '<4'
#clases["PINc"]['SALINIDAD'] = '<15'
#clases["PINc"]['SODICIDAD'] = '<30'


clases["PINm"] = dict()
#clases["PINm"]['CLASE_DE_C'] = ['9']
#clases["PINm"]['CLASE_DE_H'] = ['bimodal']
clases["PINm"]['Pendiente'] = "<7"
clases["PINm"]['Erosion\n(Grado)'] = ["no hay"]
clases["PINm"]['Drenaje natural'] = ['bueno , moderado']
clases["PINm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["PINm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["PINm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["PINm"]['Profundidad efectiva (cm)'] = '<50'
clases["PINm"]['Fertilidad'] = '>5.2'
clases["PINm"]['ACIDEZ_POR'] = '<4'
#clases["PINm"]['SALINIDAD'] = '<15'
#clases["PINm"]['SODICIDAD'] = '<30'


clases["PINf"] = dict()
#clases["PINf"]['CLASE_DE_C'] = ['13']
#clases["PINf"]['CLASE_DE_H'] = ['bimodal']
clases["PINf"]['Pendiente'] = "<7"
clases["PINf"]['Erosion\n(Grado)'] = ["no hay"]
clases["PINf"]['Drenaje natural'] = ['bueno , moderado']
clases["PINf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["PINf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["PINf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["PINf"]['Profundidad efectiva (cm)'] = '<50'
clases["PINf"]['Fertilidad'] = '>5.2'
clases["PINf"]['ACIDEZ_POR'] = '<4'
#clases["PINf"]['SALINIDAD'] = '<15'
#clases["PINf"]['SODICIDAD'] = '<30'

clases["PSIc"] = dict()
#clases["PSIc"]['CLASE_DE_C'] = ['3 , 4 , 5']
#clases["PSIc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIc"]['Pendiente'] = "<12"
clases["PSIc"]['Erosion\n(Grado)'] = ["ligera"]
clases["PSIc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["PSIc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["PSIc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIc"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIc"]['Fertilidad'] = '>3.6'
clases["PSIc"]['ACIDEZ_POR'] = '<8'
#clases["PSIc"]['SALINIDAD'] = '<15'
#clases["PSIc"]['SODICIDAD'] = '<30'


clases["PSIc"] = dict()
#clases["PSIc"]['CLASE_DE_C'] = ['3 , 4 , 5']
#clases["PSIc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIc"]['Pendiente'] = "<12"
clases["PSIc"]['Erosion\n(Grado)'] = ["ligera"]
clases["PSIc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["PSIc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["PSIc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIc"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIc"]['Fertilidad'] = '>3.6'
clases["PSIc"]['ACIDEZ_POR'] = '<8'
#clases["PSIc"]['SALINIDAD'] = '<15'
#clases["PSIc"]['SODICIDAD'] = '<30'

clases["PSIm"] = dict()
#clases["PSIm"]['CLASE_DE_C'] = ['8 , 9']
#clases["PSIm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIm"]['Pendiente'] = "<12"
clases["PSIm"]['Erosion\n(Grado)'] = ["ligera"]
clases["PSIm"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["PSIm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["PSIm"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIm"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIm"]['Fertilidad'] = '>3.6'
clases["PSIm"]['ACIDEZ_POR'] = '<8'
#clases["PSIm"]['SALINIDAD'] = '<15'
#clases["PSIm"]['SODICIDAD'] = '<30'


clases["PSIf"] = dict()
#clases["PSIf"]['CLASE_DE_C'] = ['12 , 13']
#clases["PSIf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIf"]['Pendiente'] = "<12"
clases["PSIf"]['Erosion\n(Grado)'] = ["ligera"]
clases["PSIf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["PSIf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["PSIf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIf"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIf"]['Fertilidad'] = '>3.6'
clases["PSIf"]['ACIDEZ_POR'] = '<8'
#clases["PSIf"]['SALINIDAD'] = '<15'
#clases["PSIf"]['SODICIDAD'] = '<30'


clases["PSIf"] = dict()
#clases["PSIf"]['CLASE_DE_C'] = ['12 , 13']
#clases["PSIf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIf"]['Pendiente'] = "<12"
clases["PSIf"]['Erosion\n(Grado)'] = ["ligera"]
clases["PSIf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["PSIf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["PSIf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIf"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIf"]['Fertilidad'] = '>3.6'
clases["PSIf"]['ACIDEZ_POR'] = '<8'
#clases["PSIf"]['SALINIDAD'] = '<15'
#clases["PSIf"]['SODICIDAD'] = '<30'


clases["PEXc"] = dict()
#clases["PEXc"]['CLASE_DE_C'] = ['2 , 3 , 4 , 5']
#clases["PEXc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXc"]['Pendiente'] = "<25"
clases["PEXc"]['Erosion\n(Grado)'] = ["ligera"]
clases["PEXc"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["PEXc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["PEXc"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXc"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXc"]['Fertilidad'] = '>0.5'
clases["PEXc"]['ACIDEZ_POR'] = '<8'
#clases["PEXc"]['SALINIDAD'] = '<15'
#clases["PEXc"]['SODICIDAD'] = '<60'


clases["PEXm"] = dict()
#clases["PEXm"]['CLASE_DE_C'] = ['7 , 8 , 9 , 10']
#clases["PEXm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXm"]['Pendiente'] = "<25"
clases["PEXm"]['Erosion\n(Grado)'] = ["ligera"]
clases["PEXm"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["PEXm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["PEXm"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXm"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXm"]['Fertilidad'] = '>0.5'
clases["PEXm"]['ACIDEZ_POR'] = '<8'
#clases["PEXm"]['SALINIDAD'] = '<15'
#clases["PEXm"]['SODICIDAD'] = '<60'


clases["PEXf"] = dict()
#clases["PEXf"]['CLASE_DE_C'] = ['12 , 13 , 14']
#clases["PEXf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXf"]['Pendiente'] = "<25"
clases["PEXf"]['Erosion\n(Grado)'] = ["ligera"]
clases["PEXf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["PEXf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["PEXf"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXf"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXf"]['Fertilidad'] = '>0.5'
clases["PEXf"]['ACIDEZ_POR'] = '<8'
#clases["PEXf"]['SALINIDAD'] = '<15'
#clases["PEXf"]['SODICIDAD'] = '<60'

clases["PEXmf"] = dict()
#clases["PEXmf"]['CLASE_DE_C'] = ['16 , 17']
#clases["PEXmf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXmf"]['Pendiente'] = "<25"
clases["PEXmf"]['Erosion\n(Grado)'] = ["ligera"]
clases["PEXmf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXmf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["PEXmf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["PEXmf"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXmf"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXmf"]['Fertilidad'] = '>0.5'
clases["PEXmf"]['ACIDEZ_POR'] = '<8'
#clases["PEXmf"]['SALINIDAD'] = '<15'
#clases["PEXmf"]['SODICIDAD'] = '<60'

clases["AGSt"] = dict()
#clases["AGSt"]['CLASE_DE_C'] = ['3 , 4 , 8 , 9 , 13 , 14 , 15']
#clases["AGSt"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["AGSt"]['Pendiente'] = "<25"
clases["AGSt"]['Erosion\n(Grado)'] = ["no hay"]
clases["AGSt"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["AGSt"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["AGSt"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["AGSt"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["AGSt"]['Profundidad efectiva (cm)'] = '>25'
clases["AGSt"]['Fertilidad'] = '>0.5'
clases["AGSt"]['ACIDEZ_POR'] = '<8'
#clases["AGSt"]['SALINIDAD'] = '<15'
#clases["AGSt"]['SODICIDAD'] = '<60'

clases["AGSp"] = dict()
#clases["AGSp"]['CLASE_DE_C'] = ['3 , 4 , 5 , 6 , 8 , 9 , 13 , 14 , 15']
#clases["AGSp"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["AGSp"]['Pendiente'] = "<75"
clases["AGSp"]['Erosion\n(Grado)'] = ["ligera"]
clases["AGSp"]['Drenaje natural'] = ['Excesivo , bueno , moderado']
clases["AGSp"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["AGSp"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["AGSp"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["AGSp"]['Profundidad efectiva (cm)'] = '>25'
clases["AGSp"]['Fertilidad'] = '>0.5'
clases["AGSp"]['ACIDEZ_POR'] = '<8'
#clases["AGSp"]['SALINIDAD'] = '<15'
#clases["AGSp"]['SODICIDAD'] = '<60'

clases["ASPt"] = dict()
#clases["ASPt"]['CLASE_DE_C'] = ['3 , 4 , 8 , 9 , 13 , 14 , 18']
#clases["ASPt"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["ASPt"]['Pendiente'] = "<25"
clases["ASPt"]['Erosion\n(Grado)'] = ["moderada"]
clases["ASPt"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["ASPt"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocasionales']
clases["ASPt"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<15'
clases["ASPt"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["ASPt"]['Profundidad efectiva (cm)'] = '>25'
clases["ASPt"]['Fertilidad'] = '>0.5'
clases["ASPt"]['ACIDEZ_POR'] = '<8'
#clases["ASPt"]['SALINIDAD'] = '<15'
#clases["ASPt"]['SODICIDAD'] = '<60'

clases["ASPp"] = dict()
#clases["ASPp"]['CLASE_DE_C'] = ['3 , 4 , 5 , 8 , 9 , 10 , 13 , 14']
#clases["ASPp"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["ASPp"]['Pendiente'] = "<50"
clases["ASPp"]['Erosion\n(Grado)'] = ["moderada"]
clases["ASPp"]['Drenaje natural'] = ['bueno , moderado']
clases["ASPp"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['raras']
clases["ASPp"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["ASPp"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["ASPp"]['Profundidad efectiva (cm)'] = '>50'
clases["ASPp"]['Fertilidad'] = '>0.5'
clases["ASPp"]['ACIDEZ_POR'] = '<8'
#clases["ASPp"]['SALINIDAD'] = '<15'
#clases["ASPp"]['SODICIDAD'] = '<60'


clases["SPA"] = dict()
#clases["ASPp"]['CLASE_DE_C'] = ['2 , 3 , 4 , 5 , 7 , 8 , 9 , 10 , 12 , 13 , 15 , 17 , 18']
#clases["ASPp"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["SPA"]['Pendiente'] = "<50"
clases["SPA"]['Erosion\n(Grado)'] = ["moderada"]
clases["SPA"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["SPA"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["SPA"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["SPA"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["SPA"]['Profundidad efectiva (cm)'] = '>25'
clases["SPA"]['Fertilidad'] = '>0.5'
clases["SPA"]['ACIDEZ_POR'] = '<16'
#clases["ASPp"]['SALINIDAD'] = '<15'
#clases["ASPp"]['SODICIDAD'] = '<90'


clases["FPDc"] = dict()
#clases["FPDc"]['CLASE_DE_C'] = ['3 , 4 , 5 , 6']
#clases["FPDc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDc"]['Pendiente'] = "<25"
clases["FPDc"]['Erosion\n(Grado)'] = ["ligera"]
clases["FPDc"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDc"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["FPDc"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["FPDc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDc"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDc"]['Fertilidad'] = '>1.0'
clases["FPDc"]['ACIDEZ_POR'] = '<4'
#clases["FPDc"]['SALINIDAD'] = '<15'
#clases["FPDc"]['SODICIDAD'] = '<30'

clases["FPDm"] = dict()
#clases["FPDm"]['CLASE_DE_C'] = ['8 , 9 , 10']
#clases["FPDm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDm"]['Pendiente'] = "<25"
clases["FPDm"]['Erosion\n(Grado)'] = ["ligera"]
clases["FPDm"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDm"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["FPDm"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["FPDm"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDm"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDm"]['Fertilidad'] = '>1.0'
clases["FPDm"]['ACIDEZ_POR'] = '<4'
#clases["FPDm"]['SALINIDAD'] = '<15'
#clases["FPDm"]['SODICIDAD'] = '<30'

clases["FPDf"] = dict()
#clases["FPDf"]['CLASE_DE_C'] = ['13 , 14 , 15 , 16']
#clases["FPDf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDf"]['Pendiente'] = "<25"
clases["FPDf"]['Erosion\n(Grado)'] = ["ligera"]
clases["FPDf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["FPDf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["FPDf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDf"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDf"]['Fertilidad'] = '>1.0'
clases["FPDf"]['ACIDEZ_POR'] = '<4'
#clases["FPDf"]['SALINIDAD'] = '<15'
#clases["FPDf"]['SODICIDAD'] = '<30'

clases["FPDmf"] = dict()
#clases["FPDmf"]['CLASE_DE_C'] = ['17 , 18']
#clases["FPDmf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDmf"]['Pendiente'] = "<12"
clases["FPDmf"]['Erosion\n(Grado)'] = ["ligera"]
clases["FPDmf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDmf"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['ocacionales']
clases["FPDmf"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<35'
clases["FPDmf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDmf"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDmf"]['Fertilidad'] = '>1.0'
clases["FPDmf"]['ACIDEZ_POR'] = '<4'
#clases["FPDmf"]['SALINIDAD'] = '<15'
#clases["FPDmf"]['SODICIDAD'] = '<30'


clases["FPP"] = dict()
#clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17']
#clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<50"
clases["FPP"]['Erosion\n(Grado)'] = ["moderada"]
clases["FPP"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPP"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["FPP"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["FPP"]['Profundidad efectiva (cm)'] = '>10'
clases["FPP"]['Fertilidad'] = '>0.5'
clases["FPP"]['ACIDEZ_POR'] = '<16'
#clases["FPP"]['SALINIDAD'] = '<15'
#clases["FPP"]['SODICIDAD'] = '<90'


clases["FPP"] = dict()
#clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19']
#clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<100"
clases["FPP"]['Erosion\n(Grado)'] = ["severa"]
clases["FPP"]['Drenaje natural'] = ['excesivo , bueno , moderado , imperfecto , pobre']
clases["FPP"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["FPP"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["FPP"]['Profundidad efectiva (cm)'] = '>10'
clases["FPP"]['Fertilidad'] = '>0.5'
clases["FPP"]['ACIDEZ_POR'] = '<16'
#clases["FPP"]['SALINIDAD'] = '<15'
#clases["FPP"]['SODICIDAD'] = '<90'

clases["FPP"] = dict()
#clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21']
#clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<100"
clases["FPP"]['Erosion\n(Grado)'] = ["severa"]
clases["FPP"]['Drenaje natural'] = ['excesivo , bueno , moderado , imperfecto , pobre']
clases["FPP"]['Inundaciones/Encharcamientos\n(Frecuencia)'] = ['frecuentes']
clases["FPP"]['Inundaciones/Encharcamientos\n(Duracion)'] = '<60'
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["FPP"]['Profundidad efectiva (cm)'] = '>10'
clases["FPP"]['ACIDEZ_POR'] = '<8'
#clases["FPP"]['SALINIDAD'] = '>15'
#clases["FPP"]['SODICIDAD'] = '<90'

clases["FPP"] = dict()
#clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21']
#clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<100"
clases["FPP"]['Drenaje natural'] = ['pantanoso']



def mapear_distribucion_lluvias_a_monomodal_o_bimodal(numero):
    numero = int(numero)
    if numero <= 4:
        return "monomodal"
    return "bimodal"


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
    if symbolo == 'a':
        return "0-3"
    if symbolo == 'b':
        return "3-7"
    if symbolo == 'c':
        return "7-12"
    if symbolo == 'd':
        return "12-25"
    if symbolo == 'e':
        return "25-50"
    if symbolo == 'f':
        return "50-75"
    if symbolo == 'g':
        return ">75"
def mapear_fertilidad_a_rango(symbolo):
    symbolo=symbolo.lower()
    if symbolo == 'baja':
        return "3.6-5.1"
    if symbolo == 'muy baja':
        return "0.5-3.5"
    if symbolo == 'media':
        return "5.2-6.7"
    if symbolo == 'alta':
        return "6.8-8.4"
    if symbolo == 'muy alta':
        return ">8.4"


def mapear_clase_fertilidad_a_rango(fertilidad):
    if fertilidad == 'Media':
        return conseguir_minimo_y_maximo("5.2 - 6.7")
    if fertilidad == 'Muy alta':
        return conseguir_minimo_y_maximo(">8.4")
    if fertilidad == 'Alta':
        return conseguir_minimo_y_maximo("6.8 - 8.4")
    if fertilidad == 'Baja':
        return conseguir_minimo_y_maximo("3.6 - 5.1")
    if fertilidad == 'Muy Baja':
        return conseguir_minimo_y_maximo("0.5 - 3.5")

def conseguir_grupo_textual(fila_del_excel):
    if 'Grupo Textual' in fila_del_excel:
        if fila_del_excel['Grupo Textual'] in ['A', 'AF']:
            return "Gruesas"
        if fila_del_excel['Grupo Textual'] in ['FA']:
            return "Moderadamente Gruesas"
        if fila_del_excel['Grupo Textual'] in ['F', 'FL', 'L']:
            return "Medias"
        if fila_del_excel['Grupo Textual'] in ['FAr', 'FArA', 'FArL']:
            return "Moderadamente finas"
        if fila_del_excel['Grupo Textual'] in ['ArA', 'ArL', 'Ar fina']:
            return "Finas"
        if fila_del_excel['Grupo Textual'] in ['Ar muy fina']:
            return "Muy Finas"
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

    ### para rangos como <15
    if "<" in rango:
        respuesta = dict()
        respuesta['minimo'] = minimo_default
        respuesta['maximo'] = float(rango.replace("<", ""))
        return respuesta
    ### para rangos como >50
    if ">" in rango:
        respuesta = dict()
        respuesta['minimo'] = float(rango.replace(">", ""))
        respuesta['maximo'] = maximo_default
        return respuesta
    valores = rango.split("-")
    respuesta = dict()
    respuesta['minimo'] = float(valores[0])
    respuesta['maximo'] = float(valores[1])
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
            valor_de_atributo = None
            if atributo == "ACIDEZ_POR":
                valor_de_atributo = conseguir_ACIDEZ_POR_de_sales_y_sodio(fila_del_excel["Sales y sodio"])
            elif atributo == "SALINIDAD":
                valor_de_atributo = conseguir_porcentaje_de_sodio_de_sales_y_sodio(fila_del_excel["Sales y sodio"])
            else:
                valor_de_atributo = fila_del_excel[atributo]
            if atributo == 'Pendiente':
                valor_de_atributo = mapear_pendiente_a_rango(valor_de_atributo)
            #if atributo == 'CLASE_DE_H':
                #valor_de_atributo = mapear_distribucion_lluvias_a_monomodal_o_bimodal(valor_de_atributo)
            if atributo == 'Fertilidad':
                valor_de_atributo = mapear_fertilidad_a_rango(valor_de_atributo)
            ## El atributo es una lista, y hay que ver si este previo esta en la es
            if type(regla) is list:
                regla = list(map(lambda x: x.lower(), regla))
                if valor_de_atributo.lower() not in regla:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False
            ## El atributo es rango con un maximo, como ['Pendiente'] = "<7"
            if "<" in regla:
                maximo = regla
                if "," in maximo:
                    maximo = maximo.replace(",", ".")
                maximo = float(maximo.replace("<", ""))
                valor_de_atributo = conseguir_minimo_y_maximo( valor_de_atributo)
                if valor_de_atributo['maximo'] > maximo:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False
            ## El atributo es rango con un minimo, como ['Pendiente'] = "<7"
            if ">" in regla:
                minimo = regla
                if "," in minimo:
                    minimo = minimo.replace(",", ".")
                minimo = float(minimo.replace(">", ""))
                valor_de_atributo = conseguir_minimo_y_maximo( valor_de_atributo)
                if valor_de_atributo['minimo'] > minimo:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False

        if califica_como_clase:
            #print("calificomo" + clase)
            Clases_que_son.append(clase)
        else:
            clases_que_no_con_razon[clase] = razones_por_que_no
            #print("no calificomo" + clase)
    respuesta['clases'] = Clases_que_son
    respuesta['clases_que_no_con_razones'] = clases_que_no_con_razon
    return respuesta

def leer_csv_de_previas():
    with open('clases.csv', mode='w', encoding='utf-8') as output:
        csvwriter = csv.writer(output, delimiter=';')
        csvwriter.writerow(['Codigo Perfil', 'Clases','Clases Que No'])

        with open('excel.csv', mode='r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                resultado = function_para_clasificar(row)
                if len(resultado) > 0:
                    print("clases de este previo")
                    print(resultado)
                    csvwriter.writerow([row['Codigo Perfil'], ",".join( resultado['clases']), ','.join(resultado['clases_que_no_con_razones'].keys())])


            print('final')

def correr_pruebas():


    respuesta = function_para_clasificar(prueba)
    print(respuesta)

#correr_pruebas()


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
        new_record = dict( record.as_dict())

        ###por cada vocacion
        for clase in clases:
            new_record[clase] = 'si'


        writer.record(**new_record)

        #resultados = function_para_clasificar(record.as_dict())


        #print(resultados)
    writer.close()

    ##r = shapefile.Reader(dbf='new_file3.dbf')



leer_csv_de_previas()