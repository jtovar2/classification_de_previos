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
prueba['CLASE_DE_C'] = '4'
prueba['CLASE_DE_H'] = '5'
prueba['PENDIENTE'] = 'b'
prueba['EROSION'] = "No hay"
prueba['DRENAJE_NA'] = 'Bien Drenado'
prueba['INUNDABILI'] = 'No hay'
prueba['DURACION'] = '<3'
prueba['FRAGMENTOS'] = '<3'
prueba['PROFUNDIDA'] = '100-150'
prueba['FERTILIDAD'] = 'muy baja'
prueba['Sales y sodio'] = 'No hay'
prueba['SODICIDAD'] = '0-15'


clases = dict()
clases["CTIc"] = dict()
clases["CTIc"]['CLASE_DE_C'] = ['4']
clases["CTIc"]['CLASE_DE_H'] = ['bimodal']
clases["CTIc"]['PENDIENTE'] = "<7"
clases["CTIc"]['EROSION'] = ["No hay"]
clases["CTIc"]['DRENAJE_NA'] = ['Bien Drenado']
clases["CTIc"]['INUNDABILI'] = ['No hay']
clases["CTIc"]['DURACION'] = '<3'
clases["CTIc"]['FRAGMENTOS'] = '<3'
clases["CTIc"]['PROFUNDIDA'] = '>100'
clases["CTIc"]['FERTILIDAD'] = '>6.8'
clases["CTIc"]['ACIDEZ_POR'] = '<4'
clases["CTIc"]['SALINIDAD'] = '<15'
clases["CTIc"]['SODICIDAD'] = '<15'


clases["CTIm"] = dict()
clases["CTIm"]['CLASE_DE_C'] = ['9']
clases["CTIm"]['CLASE_DE_H'] = ['bimodal']
clases["CTIm"]['PENDIENTE'] = "<7"
clases["CTIm"]['EROSION'] = ["no hay"]
clases["CTIm"]['DRENAJE_NA'] = ['bien Drenado']
clases["CTIm"]['INUNDABILI'] = ['no hay']
clases["CTIm"]['DURACION'] = '<3'
clases["CTIm"]['FRAGMENTOS'] = '<3'
clases["CTIm"]['PROFUNDIDA'] = '>100'
clases["CTIm"]['FERTILIDAD'] = '>6.8'
clases["CTIm"]['ACIDEZ_POR'] = '<4'
clases["CTIm"]['SALINIDAD'] = '<15'
clases["CTIm"]['SODICIDAD'] = '<15'


clases["CTIf"] = dict()
clases["CTIf"]['CLASE_DE_C'] = ['13']
clases["CTIf"]['CLASE_DE_H'] = ['bimodal']
clases["CTIf"]['PENDIENTE'] = "<7"
clases["CTIf"]['EROSION'] = ["no hay"]
clases["CTIf"]['DRENAJE_NA'] = ['bien Drenado']
clases["CTIf"]['INUNDABILI'] = ['no hay']
clases["CTIf"]['DURACION'] = '<3'
clases["CTIf"]['FRAGMENTOS'] = '<3'
clases["CTIf"]['PROFUNDIDA'] = '>100'
clases["CTIf"]['FERTILIDAD'] = '>6.8'
clases["CTIf"]['ACIDEZ_POR'] = '<4'
clases["CTIf"]['SALINIDAD'] = '<15'
clases["CTIf"]['SODICIDAD'] = '<15'


clases["CTSc"] = dict()
clases["CTSc"]['CLASE_DE_C'] = ['3 , 4']
clases["CTSc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CTSc"]['PENDIENTE'] = "<12"
clases["CTSc"]['EROSION'] = ["no hay"]
clases["CTSc"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["CTSc"]['INUNDABILI'] = ['ocasionales']
clases["CTSc"]['DURACION'] = '<3'
clases["CTSc"]['FRAGMENTOS'] = '<3'
clases["CTSc"]['PROFUNDIDA'] = '>50'
clases["CTSc"]['FERTILIDAD'] = '>3.6'
clases["CTSc"]['ACIDEZ_POR'] = '<4'
clases["CTSc"]['SALINIDAD'] = '<15'
clases["CTSc"]['SODICIDAD'] = '<30'


clases["CTSm"] = dict()
clases["CTSm"]['CLASE_DE_C'] = ['8 , 9']
clases["CTSm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CTSm"]['PENDIENTE'] = "<12"
clases["CTSm"]['EROSION'] = ["no hay"]
clases["CTSm"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["CTSm"]['INUNDABILI'] = ['ocasionales']
clases["CTSm"]['DURACION'] = '<3'
clases["CTSm"]['FRAGMENTOS'] = '<3'
clases["CTSm"]['PROFUNDIDA'] = '>50'
clases["CTSm"]['FERTILIDAD'] = '>3.6'
clases["CTSm"]['ACIDEZ_POR'] = '<4'
clases["CTSm"]['SALINIDAD'] = '<15'
clases["CTSm"]['SODICIDAD'] = '<30'


clases["CTSf"] = dict()
clases["CTSf"]['CLASE_DE_C'] = ['12 , 13']
clases["CTSf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CTSf"]['PENDIENTE'] = "<12"
clases["CTSf"]['EROSION'] = ["no hay"]
clases["CTSf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["CTSf"]['INUNDABILI'] = ['ocasionales']
clases["CTSf"]['DURACION'] = '<3'
clases["CTSf"]['FRAGMENTOS'] = '<3'
clases["CTSf"]['PROFUNDIDA'] = '>50'
clases["CTSf"]['FERTILIDAD'] = '>3.6'
clases["CTSf"]['ACIDEZ_POR'] = '<4'
clases["CTSf"]['SALINIDAD'] = '<15'
clases["CTSf"]['SODICIDAD'] = '<30'


clases["CPIc"] = dict()
clases["CPIc"]['CLASE_DE_C'] = ['3 , 4']
clases["CPIc"]['CLASE_DE_H'] = ['bimodal']
clases["CPIc"]['PENDIENTE'] = "<12"
clases["CPIc"]['EROSION'] = ["no hay"]
clases["CPIc"]['DRENAJE_NA'] = ['bueno , moderado']
clases["CPIc"]['INUNDABILI'] = ['raras']
clases["CPIc"]['DURACION'] = '<3'
clases["CPIc"]['FRAGMENTOS'] = '<3'
clases["CPIc"]['PROFUNDIDA'] = '>100'
clases["CPIc"]['FERTILIDAD'] = '>5.2'
clases["CPIc"]['ACIDEZ_POR'] = '<4'
clases["CPIc"]['SALINIDAD'] = '<15'
clases["CPIc"]['SODICIDAD'] = '<15'



clases["CPIm"] = dict()
clases["CPIm"]['CLASE_DE_C'] = ['3 , 4']
clases["CPIm"]['CLASE_DE_H'] = ['bimodal']
clases["CPIm"]['PENDIENTE'] = "<12"
clases["CPIm"]['EROSION'] = ["no hay"]
clases["CPIm"]['DRENAJE_NA'] = ['bueno , moderado']
clases["CPIm"]['INUNDABILI'] = ['raras']
clases["CPIm"]['DURACION'] = '<3'
clases["CPIm"]['FRAGMENTOS'] = '<3'
clases["CPIm"]['PROFUNDIDA'] = '>100'
clases["CPIm"]['FERTILIDAD'] = '>5.2'
clases["CPIm"]['ACIDEZ_POR'] = '<4'
clases["CPIm"]['SALINIDAD'] = '<15'
clases["CPIm"]['SODICIDAD'] = '<15'

clases["CPIf"] = dict()
clases["CPIf"]['CLASE_DE_C'] = ['12 , 13']
clases["CPIf"]['CLASE_DE_H'] = ['bimodal']
clases["CPIf"]['PENDIENTE'] = "<12"
clases["CPIf"]['EROSION'] = ["no hay"]
clases["CPIf"]['DRENAJE_NA'] = ['bueno , moderado']
clases["CPIf"]['INUNDABILI'] = ['raras']
clases["CPIf"]['DURACION'] = '<3'
clases["CPIf"]['FRAGMENTOS'] = '<3'
clases["CPIf"]['PROFUNDIDA'] = '>100'
clases["CPIf"]['FERTILIDAD'] = '>5.2'
clases["CPIf"]['ACIDEZ_POR'] = '<4'
clases["CPIf"]['SALINIDAD'] = '<15'
clases["CPIf"]['SODICIDAD'] = '<15'


clases["CPSc"] = dict()
clases["CPSc"]['CLASE_DE_C'] = ['3 , 4 , 5']
clases["CPSc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CPSc"]['PENDIENTE'] = "<25"
clases["CPSc"]['EROSION'] = ["no hay"]
clases["CPSc"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["CPSc"]['INUNDABILI'] = ['ocacionales']
clases["CPSc"]['DURACION'] = '<15'
clases["CPSc"]['FRAGMENTOS'] = '<3'
clases["CPSc"]['PROFUNDIDA'] = '>50'
clases["CPSc"]['FERTILIDAD'] = '>3.6'
clases["CPSc"]['ACIDEZ_POR'] = '<4'
clases["CPSc"]['SALINIDAD'] = '<15'
clases["CPSc"]['SODICIDAD'] = '<30'

clases["CPSm"] = dict()
clases["CPSm"]['CLASE_DE_C'] = ['8 , 9']
clases["CPSm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CPSm"]['PENDIENTE'] = "<25"
clases["CPSm"]['EROSION'] = ["no hay"]
clases["CPSm"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["CPSm"]['INUNDABILI'] = ['ocacionales']
clases["CPSm"]['DURACION'] = '<15'
clases["CPSm"]['FRAGMENTOS'] = '<3'
clases["CPSm"]['PROFUNDIDA'] = '>50'
clases["CPSm"]['FERTILIDAD'] = '>3.6'
clases["CPSm"]['ACIDEZ_POR'] = '<4'
clases["CPSm"]['SALINIDAD'] = '<15'
clases["CPSm"]['SODICIDAD'] = '<30'

clases["CPSf"] = dict()
clases["CPSf"]['CLASE_DE_C'] = ['12 , 13']
clases["CPSf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["CPSf"]['PENDIENTE'] = "<25"
clases["CPSf"]['EROSION'] = ["no hay"]
clases["CPSf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["CPSf"]['INUNDABILI'] = ['ocacionales']
clases["CPSf"]['DURACION'] = '<15'
clases["CPSf"]['FRAGMENTOS'] = '<3'
clases["CPSf"]['PROFUNDIDA'] = '>50'
clases["CPSf"]['FERTILIDAD'] = '>3.6'
clases["CPSf"]['ACIDEZ_POR'] = '<4'
clases["CPSf"]['SALINIDAD'] = '<15'
clases["CPSf"]['SODICIDAD'] = '<30'

clases["PINc"] = dict()
clases["PINc"]['CLASE_DE_C'] = ['4']
clases["PINc"]['CLASE_DE_H'] = ['bimodal']
clases["PINc"]['PENDIENTE'] = "<7"
clases["PINc"]['EROSION'] = ["no hay"]
clases["PINc"]['DRENAJE_NA'] = ['bueno , moderado']
clases["PINc"]['INUNDABILI'] = ['raras']
clases["PINc"]['DURACION'] = '<15'
clases["PINc"]['FRAGMENTOS'] = '<3'
clases["PINc"]['PROFUNDIDA'] = '<50'
clases["PINc"]['FERTILIDAD'] = '>5.2'
clases["PINc"]['ACIDEZ_POR'] = '<4'
clases["PINc"]['SALINIDAD'] = '<15'
clases["PINc"]['SODICIDAD'] = '<30'


clases["PINm"] = dict()
clases["PINm"]['CLASE_DE_C'] = ['9']
clases["PINm"]['CLASE_DE_H'] = ['bimodal']
clases["PINm"]['PENDIENTE'] = "<7"
clases["PINm"]['EROSION'] = ["no hay"]
clases["PINm"]['DRENAJE_NA'] = ['bueno , moderado']
clases["PINm"]['INUNDABILI'] = ['raras']
clases["PINm"]['DURACION'] = '<15'
clases["PINm"]['FRAGMENTOS'] = '<3'
clases["PINm"]['PROFUNDIDA'] = '<50'
clases["PINm"]['FERTILIDAD'] = '>5.2'
clases["PINm"]['ACIDEZ_POR'] = '<4'
clases["PINm"]['SALINIDAD'] = '<15'
clases["PINm"]['SODICIDAD'] = '<30'


clases["PINf"] = dict()
clases["PINf"]['CLASE_DE_C'] = ['13']
clases["PINf"]['CLASE_DE_H'] = ['bimodal']
clases["PINf"]['PENDIENTE'] = "<7"
clases["PINf"]['EROSION'] = ["no hay"]
clases["PINf"]['DRENAJE_NA'] = ['bueno , moderado']
clases["PINf"]['INUNDABILI'] = ['raras']
clases["PINf"]['DURACION'] = '<15'
clases["PINf"]['FRAGMENTOS'] = '<3'
clases["PINf"]['PROFUNDIDA'] = '<50'
clases["PINf"]['FERTILIDAD'] = '>5.2'
clases["PINf"]['ACIDEZ_POR'] = '<4'
clases["PINf"]['SALINIDAD'] = '<15'
clases["PINf"]['SODICIDAD'] = '<30'

clases["PSIc"] = dict()
clases["PSIc"]['CLASE_DE_C'] = ['3 , 4 , 5']
clases["PSIc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIc"]['PENDIENTE'] = "<12"
clases["PSIc"]['EROSION'] = ["ligera"]
clases["PSIc"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["PSIc"]['INUNDABILI'] = ['ocasionales']
clases["PSIc"]['DURACION'] = '<35'
clases["PSIc"]['FRAGMENTOS'] = '<15'
clases["PSIc"]['PROFUNDIDA'] = '<25'
clases["PSIc"]['FERTILIDAD'] = '>3.6'
clases["PSIc"]['ACIDEZ_POR'] = '<8'
clases["PSIc"]['SALINIDAD'] = '<15'
clases["PSIc"]['SODICIDAD'] = '<30'


clases["PSIc"] = dict()
clases["PSIc"]['CLASE_DE_C'] = ['3 , 4 , 5']
clases["PSIc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIc"]['PENDIENTE'] = "<12"
clases["PSIc"]['EROSION'] = ["ligera"]
clases["PSIc"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["PSIc"]['INUNDABILI'] = ['ocasionales']
clases["PSIc"]['DURACION'] = '<35'
clases["PSIc"]['FRAGMENTOS'] = '<15'
clases["PSIc"]['PROFUNDIDA'] = '<25'
clases["PSIc"]['FERTILIDAD'] = '>3.6'
clases["PSIc"]['ACIDEZ_POR'] = '<8'
clases["PSIc"]['SALINIDAD'] = '<15'
clases["PSIc"]['SODICIDAD'] = '<30'

clases["PSIm"] = dict()
clases["PSIm"]['CLASE_DE_C'] = ['8 , 9']
clases["PSIm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIm"]['PENDIENTE'] = "<12"
clases["PSIm"]['EROSION'] = ["ligera"]
clases["PSIm"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["PSIm"]['INUNDABILI'] = ['ocasionales']
clases["PSIm"]['DURACION'] = '<35'
clases["PSIm"]['FRAGMENTOS'] = '<15'
clases["PSIm"]['PROFUNDIDA'] = '<25'
clases["PSIm"]['FERTILIDAD'] = '>3.6'
clases["PSIm"]['ACIDEZ_POR'] = '<8'
clases["PSIm"]['SALINIDAD'] = '<15'
clases["PSIm"]['SODICIDAD'] = '<30'


clases["PSIf"] = dict()
clases["PSIf"]['CLASE_DE_C'] = ['12 , 13']
clases["PSIf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIf"]['PENDIENTE'] = "<12"
clases["PSIf"]['EROSION'] = ["ligera"]
clases["PSIf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["PSIf"]['INUNDABILI'] = ['ocasionales']
clases["PSIf"]['DURACION'] = '<35'
clases["PSIf"]['FRAGMENTOS'] = '<15'
clases["PSIf"]['PROFUNDIDA'] = '<25'
clases["PSIf"]['FERTILIDAD'] = '>3.6'
clases["PSIf"]['ACIDEZ_POR'] = '<8'
clases["PSIf"]['SALINIDAD'] = '<15'
clases["PSIf"]['SODICIDAD'] = '<30'


clases["PSIf"] = dict()
clases["PSIf"]['CLASE_DE_C'] = ['12 , 13']
clases["PSIf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PSIf"]['PENDIENTE'] = "<12"
clases["PSIf"]['EROSION'] = ["ligera"]
clases["PSIf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["PSIf"]['INUNDABILI'] = ['ocasionales']
clases["PSIf"]['DURACION'] = '<35'
clases["PSIf"]['FRAGMENTOS'] = '<15'
clases["PSIf"]['PROFUNDIDA'] = '<25'
clases["PSIf"]['FERTILIDAD'] = '>3.6'
clases["PSIf"]['ACIDEZ_POR'] = '<8'
clases["PSIf"]['SALINIDAD'] = '<15'
clases["PSIf"]['SODICIDAD'] = '<30'


clases["PEXc"] = dict()
clases["PEXc"]['CLASE_DE_C'] = ['2 , 3 , 4 , 5']
clases["PEXc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXc"]['PENDIENTE'] = "<25"
clases["PEXc"]['EROSION'] = ["ligera"]
clases["PEXc"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXc"]['INUNDABILI'] = ['frecuentes']
clases["PEXc"]['DURACION'] = '<60'
clases["PEXc"]['FRAGMENTOS'] = '<50'
clases["PEXc"]['PROFUNDIDA'] = '>10'
clases["PEXc"]['FERTILIDAD'] = '>0.5'
clases["PEXc"]['ACIDEZ_POR'] = '<8'
clases["PEXc"]['SALINIDAD'] = '<15'
clases["PEXc"]['SODICIDAD'] = '<60'


clases["PEXm"] = dict()
clases["PEXm"]['CLASE_DE_C'] = ['7 , 8 , 9 , 10']
clases["PEXm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXm"]['PENDIENTE'] = "<25"
clases["PEXm"]['EROSION'] = ["ligera"]
clases["PEXm"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXm"]['INUNDABILI'] = ['frecuentes']
clases["PEXm"]['DURACION'] = '<60'
clases["PEXm"]['FRAGMENTOS'] = '<50'
clases["PEXm"]['PROFUNDIDA'] = '>10'
clases["PEXm"]['FERTILIDAD'] = '>0.5'
clases["PEXm"]['ACIDEZ_POR'] = '<8'
clases["PEXm"]['SALINIDAD'] = '<15'
clases["PEXm"]['SODICIDAD'] = '<60'


clases["PEXf"] = dict()
clases["PEXf"]['CLASE_DE_C'] = ['12 , 13 , 14']
clases["PEXf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXf"]['PENDIENTE'] = "<25"
clases["PEXf"]['EROSION'] = ["ligera"]
clases["PEXf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXf"]['INUNDABILI'] = ['frecuentes']
clases["PEXf"]['DURACION'] = '<60'
clases["PEXf"]['FRAGMENTOS'] = '<50'
clases["PEXf"]['PROFUNDIDA'] = '>10'
clases["PEXf"]['FERTILIDAD'] = '>0.5'
clases["PEXf"]['ACIDEZ_POR'] = '<8'
clases["PEXf"]['SALINIDAD'] = '<15'
clases["PEXf"]['SODICIDAD'] = '<60'

clases["PEXmf"] = dict()
clases["PEXmf"]['CLASE_DE_C'] = ['16 , 17']
clases["PEXmf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["PEXmf"]['PENDIENTE'] = "<25"
clases["PEXmf"]['EROSION'] = ["ligera"]
clases["PEXmf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXmf"]['INUNDABILI'] = ['frecuentes']
clases["PEXmf"]['DURACION'] = '<60'
clases["PEXmf"]['FRAGMENTOS'] = '<50'
clases["PEXmf"]['PROFUNDIDA'] = '>10'
clases["PEXmf"]['FERTILIDAD'] = '>0.5'
clases["PEXmf"]['ACIDEZ_POR'] = '<8'
clases["PEXmf"]['SALINIDAD'] = '<15'
clases["PEXmf"]['SODICIDAD'] = '<60'

clases["AGSt"] = dict()
clases["AGSt"]['CLASE_DE_C'] = ['3 , 4 , 8 , 9 , 13 , 14 , 15']
clases["AGSt"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["AGSt"]['PENDIENTE'] = "<25"
clases["AGSt"]['EROSION'] = ["no hay"]
clases["AGSt"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["AGSt"]['INUNDABILI'] = ['ocacionales']
clases["AGSt"]['DURACION'] = '<15'
clases["AGSt"]['FRAGMENTOS'] = '<3'
clases["AGSt"]['PROFUNDIDA'] = '>25'
clases["AGSt"]['FERTILIDAD'] = '>0.5'
clases["AGSt"]['ACIDEZ_POR'] = '<8'
clases["AGSt"]['SALINIDAD'] = '<15'
clases["AGSt"]['SODICIDAD'] = '<60'

clases["AGSp"] = dict()
clases["AGSp"]['CLASE_DE_C'] = ['3 , 4 , 5 , 6 , 8 , 9 , 13 , 14 , 15']
clases["AGSp"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["AGSp"]['PENDIENTE'] = "<75"
clases["AGSp"]['EROSION'] = ["ligera"]
clases["AGSp"]['DRENAJE_NA'] = ['Excesivo , bueno , moderado']
clases["AGSp"]['INUNDABILI'] = ['raras']
clases["AGSp"]['DURACION'] = '<15'
clases["AGSp"]['FRAGMENTOS'] = '<3'
clases["AGSp"]['PROFUNDIDA'] = '>25'
clases["AGSp"]['FERTILIDAD'] = '>0.5'
clases["AGSp"]['ACIDEZ_POR'] = '<8'
clases["AGSp"]['SALINIDAD'] = '<15'
clases["AGSp"]['SODICIDAD'] = '<60'

clases["ASPt"] = dict()
clases["ASPt"]['CLASE_DE_C'] = ['3 , 4 , 8 , 9 , 13 , 14 , 18']
clases["ASPt"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["ASPt"]['PENDIENTE'] = "<25"
clases["ASPt"]['EROSION'] = ["moderada"]
clases["ASPt"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto']
clases["ASPt"]['INUNDABILI'] = ['ocasionales']
clases["ASPt"]['DURACION'] = '<15'
clases["ASPt"]['FRAGMENTOS'] = '<3'
clases["ASPt"]['PROFUNDIDA'] = '>25'
clases["ASPt"]['FERTILIDAD'] = '>0.5'
clases["ASPt"]['ACIDEZ_POR'] = '<8'
clases["ASPt"]['SALINIDAD'] = '<15'
clases["ASPt"]['SODICIDAD'] = '<60'

clases["ASPp"] = dict()
clases["ASPp"]['CLASE_DE_C'] = ['3 , 4 , 5 , 8 , 9 , 10 , 13 , 14']
clases["ASPp"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["ASPp"]['PENDIENTE'] = "<50"
clases["ASPp"]['EROSION'] = ["moderada"]
clases["ASPp"]['DRENAJE_NA'] = ['bueno , moderado']
clases["ASPp"]['INUNDABILI'] = ['raras']
clases["ASPp"]['DURACION'] = '<35'
clases["ASPp"]['FRAGMENTOS'] = '<15'
clases["ASPp"]['PROFUNDIDA'] = '>50'
clases["ASPp"]['FERTILIDAD'] = '>0.5'
clases["ASPp"]['ACIDEZ_POR'] = '<8'
clases["ASPp"]['SALINIDAD'] = '<15'
clases["ASPp"]['SODICIDAD'] = '<60'


clases["SPA"] = dict()
clases["ASPp"]['CLASE_DE_C'] = ['2 , 3 , 4 , 5 , 7 , 8 , 9 , 10 , 12 , 13 , 15 , 17 , 18']
clases["ASPp"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["ASPp"]['PENDIENTE'] = "<50"
clases["ASPp"]['EROSION'] = ["moderada"]
clases["ASPp"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["ASPp"]['INUNDABILI'] = ['frecuentes']
clases["ASPp"]['DURACION'] = '<60'
clases["ASPp"]['FRAGMENTOS'] = '<50'
clases["ASPp"]['PROFUNDIDA'] = '>25'
clases["ASPp"]['FERTILIDAD'] = '>0.5'
clases["ASPp"]['ACIDEZ_POR'] = '<16'
clases["ASPp"]['SALINIDAD'] = '<15'
clases["ASPp"]['SODICIDAD'] = '<90'


clases["FPDc"] = dict()
clases["FPDc"]['CLASE_DE_C'] = ['3 , 4 , 5 , 6']
clases["FPDc"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDc"]['PENDIENTE'] = "<25"
clases["FPDc"]['EROSION'] = ["ligera"]
clases["FPDc"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDc"]['INUNDABILI'] = ['ocacionales']
clases["FPDc"]['DURACION'] = '<35'
clases["FPDc"]['FRAGMENTOS'] = '<15'
clases["FPDc"]['PROFUNDIDA'] = '>50'
clases["FPDc"]['FERTILIDAD'] = '>1.0'
clases["FPDc"]['ACIDEZ_POR'] = '<4'
clases["FPDc"]['SALINIDAD'] = '<15'
clases["FPDc"]['SODICIDAD'] = '<30'

clases["FPDm"] = dict()
clases["FPDm"]['CLASE_DE_C'] = ['8 , 9 , 10']
clases["FPDm"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDm"]['PENDIENTE'] = "<25"
clases["FPDm"]['EROSION'] = ["ligera"]
clases["FPDm"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDm"]['INUNDABILI'] = ['ocacionales']
clases["FPDm"]['DURACION'] = '<35'
clases["FPDm"]['FRAGMENTOS'] = '<15'
clases["FPDm"]['PROFUNDIDA'] = '>50'
clases["FPDm"]['FERTILIDAD'] = '>1.0'
clases["FPDm"]['ACIDEZ_POR'] = '<4'
clases["FPDm"]['SALINIDAD'] = '<15'
clases["FPDm"]['SODICIDAD'] = '<30'

clases["FPDf"] = dict()
clases["FPDf"]['CLASE_DE_C'] = ['13 , 14 , 15 , 16']
clases["FPDf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDf"]['PENDIENTE'] = "<25"
clases["FPDf"]['EROSION'] = ["ligera"]
clases["FPDf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDf"]['INUNDABILI'] = ['ocacionales']
clases["FPDf"]['DURACION'] = '<35'
clases["FPDf"]['FRAGMENTOS'] = '<15'
clases["FPDf"]['PROFUNDIDA'] = '>50'
clases["FPDf"]['FERTILIDAD'] = '>1.0'
clases["FPDf"]['ACIDEZ_POR'] = '<4'
clases["FPDf"]['SALINIDAD'] = '<15'
clases["FPDf"]['SODICIDAD'] = '<30'

clases["FPDmf"] = dict()
clases["FPDmf"]['CLASE_DE_C'] = ['17 , 18']
clases["FPDmf"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPDmf"]['PENDIENTE'] = "<12"
clases["FPDmf"]['EROSION'] = ["ligera"]
clases["FPDmf"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDmf"]['INUNDABILI'] = ['ocacionales']
clases["FPDmf"]['DURACION'] = '<35'
clases["FPDmf"]['FRAGMENTOS'] = '<15'
clases["FPDmf"]['PROFUNDIDA'] = '>50'
clases["FPDmf"]['FERTILIDAD'] = '>1.0'
clases["FPDmf"]['ACIDEZ_POR'] = '<4'
clases["FPDmf"]['SALINIDAD'] = '<15'
clases["FPDmf"]['SODICIDAD'] = '<30'


clases["FPP"] = dict()
clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17']
clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['PENDIENTE'] = "<50"
clases["FPP"]['EROSION'] = ["moderada"]
clases["FPP"]['DRENAJE_NA'] = ['bueno , moderado , imperfecto , pobre']
clases["FPP"]['INUNDABILI'] = ['frecuentes']
clases["FPP"]['DURACION'] = '<60'
clases["FPP"]['FRAGMENTOS'] = '<50'
clases["FPP"]['PROFUNDIDA'] = '>10'
clases["FPP"]['FERTILIDAD'] = '>0.5'
clases["FPP"]['ACIDEZ_POR'] = '<16'
clases["FPP"]['SALINIDAD'] = '<15'
clases["FPP"]['SODICIDAD'] = '<90'


clases["FPP"] = dict()
clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19']
clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['PENDIENTE'] = "<100"
clases["FPP"]['EROSION'] = ["severa"]
clases["FPP"]['DRENAJE_NA'] = ['excesivo , bueno , moderado , imperfecto , pobre']
clases["FPP"]['INUNDABILI'] = ['frecuentes']
clases["FPP"]['DURACION'] = '<60'
clases["FPP"]['FRAGMENTOS'] = '<50'
clases["FPP"]['PROFUNDIDA'] = '>10'
clases["FPP"]['FERTILIDAD'] = '>0.5'
clases["FPP"]['ACIDEZ_POR'] = '<16'
clases["FPP"]['SALINIDAD'] = '<15'
clases["FPP"]['SODICIDAD'] = '<90'

clases["FPP"] = dict()
clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21']
clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['PENDIENTE'] = "<100"
clases["FPP"]['EROSION'] = ["severa"]
clases["FPP"]['DRENAJE_NA'] = ['excesivo , bueno , moderado , imperfecto , pobre']
clases["FPP"]['INUNDABILI'] = ['frecuentes']
clases["FPP"]['DURACION'] = '<60'
clases["FPP"]['FRAGMENTOS'] = '<50'
clases["FPP"]['PROFUNDIDA'] = '>10'
clases["FPP"]['ACIDEZ_POR'] = '<8'
clases["FPP"]['SALINIDAD'] = '>15'
clases["FPP"]['SODICIDAD'] = '<90'

clases["FPP"] = dict()
clases["FPP"]['CLASE_DE_C'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21']
clases["FPP"]['CLASE_DE_H'] = ['bimodal , monomodal']
clases["FPP"]['PENDIENTE'] = "<100"
clases["FPP"]['DRENAJE_NA'] = ['pantanoso']



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
            if atributo == 'PENDIENTE':
                valor_de_atributo = mapear_pendiente_a_rango(valor_de_atributo)
            if atributo == 'CLASE_DE_H':
                valor_de_atributo = mapear_distribucion_lluvias_a_monomodal_o_bimodal(valor_de_atributo)
            if atributo == 'FERTILIDAD':
                valor_de_atributo = mapear_fertilidad_a_rango(valor_de_atributo)
            ## El atributo es una lista, y hay que ver si este previo esta en la es
            if type(regla) is list:
                regla = list(map(lambda x: x.lower(), regla))
                if valor_de_atributo.lower() not in regla:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False
            ## El atributo es rango con un maximo, como ['PENDIENTE'] = "<7"
            if "<" in regla:
                maximo = regla
                if "," in maximo:
                    maximo = maximo.replace(",", ".")
                maximo = float(maximo.replace("<", ""))
                valor_de_atributo = conseguir_minimo_y_maximo( valor_de_atributo)
                if valor_de_atributo['maximo'] > maximo:
                    razones_por_que_no.append(atributo)
                    califica_como_clase = False
            ## El atributo es rango con un minimo, como ['PENDIENTE'] = "<7"
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
            print("calificomo" + clase)
            Clases_que_son.append(clase)
        else:
            clases_que_no_con_razon[clase] = razones_por_que_no
            print("no calificomo" + clase)
    respuesta['clases'] = Clases_que_son
    respuesta['clases_que_con_razones'] = clases_que_no_con_razon
    return respuesta

def leer_csv_de_previas():
    with open('IGAC.txt', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            resultado = function_para_clasificar(row)
            if len(resultado) > 0:
                print("clases de este previo")
                print(resultado)


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



conseguir_previas_de_shapefile("Ejemplo.shp")