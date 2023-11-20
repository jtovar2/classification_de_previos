import csv


minimo_y_maximos_por_atributo = dict()
minimo_y_maximos_por_atributo['Profundidad efectiva (cm)'] = dict()
minimo_y_maximos_por_atributo['Profundidad efectiva (cm)']['minimo'] = 0
minimo_y_maximos_por_atributo['Profundidad efectiva (cm)']['maximo'] = 151

## array based
##  <50


prueba = dict()
prueba['Clase'] = '4'
prueba['Distribución de lluvias'] = '5'
prueba['Pendiente'] = 'b'
prueba['Erosión (Grado)'] = "No hay"
prueba['Drenaje natural'] = 'Bien Drenado'
prueba['Inundaciones/Encharcamientos(Frecuencia)'] = 'No hay'
prueba['Fragmentos roca (% por Vol.) '] = '<3'
prueba['Fragmentos roca (% por Vol.) '] = '<3'
prueba['Profundidad efectiva (cm)'] = '100-150'
prueba['Fertilidad'] = 'muy baja'
prueba['Sales y sodio'] = 'No hay'
prueba['Saturación Al (%)'] = '0-15'


clases = dict()
clases["CTIc"] = dict()
clases["CTIc"]['Clase'] = ['4']
clases["CTIc"]['Distribución de lluvias'] = ['bimodal']
clases["CTIc"]['Pendiente'] = "<7"
clases["CTIc"]['Erosión (Grado)'] = ["No hay"]
clases["CTIc"]['Drenaje natural'] = ['Bien Drenado']
clases["CTIc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['No hay']
clases["CTIc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIc"]['Profundidad efectiva (cm)'] = '>100'
clases["CTIc"]['Fertilidad'] = '>6.8'
clases["CTIc"]['CEmmhos'] = '<4'
clases["CTIc"]['%SNa'] = '<15'
clases["CTIc"]['Saturación Al (%)'] = '<15'


clases["CTIm"] = dict()
clases["CTIm"]['Clase'] = ['9']
clases["CTIm"]['Distribución de lluvias'] = ['bimodal']
clases["CTIm"]['Pendiente'] = "<7"
clases["CTIm"]['Erosión (Grado)'] = ["no hay"]
clases["CTIm"]['Drenaje natural'] = ['bien Drenado']
clases["CTIm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['no hay']
clases["CTIm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIm"]['Profundidad efectiva (cm)'] = '>100'
clases["CTIm"]['Fertilidad'] = '>6.8'
clases["CTIm"]['CEmmhos'] = '<4'
clases["CTIm"]['%SNa'] = '<15'
clases["CTIm"]['Saturación Al (%)'] = '<15'


clases["CTIf"] = dict()
clases["CTIf"]['Clase'] = ['13']
clases["CTIf"]['Distribución de lluvias'] = ['bimodal']
clases["CTIf"]['Pendiente'] = "<7"
clases["CTIf"]['Erosión (Grado)'] = ["no hay"]
clases["CTIf"]['Drenaje natural'] = ['bien Drenado']
clases["CTIf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['no hay']
clases["CTIf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTIf"]['Profundidad efectiva (cm)'] = '>100'
clases["CTIf"]['Fertilidad'] = '>6.8'
clases["CTIf"]['CEmmhos'] = '<4'
clases["CTIf"]['%SNa'] = '<15'
clases["CTIf"]['Saturación Al (%)'] = '<15'


clases["CTSc"] = dict()
clases["CTSc"]['Clase'] = ['3 , 4']
clases["CTSc"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["CTSc"]['Pendiente'] = "<12"
clases["CTSc"]['Erosión (Grado)'] = ["no hay"]
clases["CTSc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CTSc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["CTSc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSc"]['Profundidad efectiva (cm)'] = '>50'
clases["CTSc"]['Fertilidad'] = '>3.6'
clases["CTSc"]['CEmmhos'] = '<4'
clases["CTSc"]['%SNa'] = '<15'
clases["CTSc"]['Saturación Al (%)'] = '<30'


clases["CTSm"] = dict()
clases["CTSm"]['Clase'] = ['8 , 9']
clases["CTSm"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["CTSm"]['Pendiente'] = "<12"
clases["CTSm"]['Erosión (Grado)'] = ["no hay"]
clases["CTSm"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CTSm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["CTSm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSm"]['Profundidad efectiva (cm)'] = '>50'
clases["CTSm"]['Fertilidad'] = '>3.6'
clases["CTSm"]['CEmmhos'] = '<4'
clases["CTSm"]['%SNa'] = '<15'
clases["CTSm"]['Saturación Al (%)'] = '<30'


clases["CTSf"] = dict()
clases["CTSf"]['Clase'] = ['12 , 13']
clases["CTSf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["CTSf"]['Pendiente'] = "<12"
clases["CTSf"]['Erosión (Grado)'] = ["no hay"]
clases["CTSf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CTSf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["CTSf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CTSf"]['Profundidad efectiva (cm)'] = '>50'
clases["CTSf"]['Fertilidad'] = '>3.6'
clases["CTSf"]['CEmmhos'] = '<4'
clases["CTSf"]['%SNa'] = '<15'
clases["CTSf"]['Saturación Al (%)'] = '<30'


clases["CPIc"] = dict()
clases["CPIc"]['Clase'] = ['3 , 4']
clases["CPIc"]['Distribución de lluvias'] = ['bimodal']
clases["CPIc"]['Pendiente'] = "<12"
clases["CPIc"]['Erosión (Grado)'] = ["no hay"]
clases["CPIc"]['Drenaje natural'] = ['bueno , moderado']
clases["CPIc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["CPIc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIc"]['Profundidad efectiva (cm)'] = '>100'
clases["CPIc"]['Fertilidad'] = '>5.2'
clases["CPIc"]['CEmmhos'] = '<4'
clases["CPIc"]['%SNa'] = '<15'
clases["CPIc"]['Saturación Al (%)'] = '<15'



clases["CPIm"] = dict()
clases["CPIm"]['Clase'] = ['3 , 4']
clases["CPIm"]['Distribución de lluvias'] = ['bimodal']
clases["CPIm"]['Pendiente'] = "<12"
clases["CPIm"]['Erosión (Grado)'] = ["no hay"]
clases["CPIm"]['Drenaje natural'] = ['bueno , moderado']
clases["CPIm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["CPIm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIm"]['Profundidad efectiva (cm)'] = '>100'
clases["CPIm"]['Fertilidad'] = '>5.2'
clases["CPIm"]['CEmmhos'] = '<4'
clases["CPIm"]['%SNa'] = '<15'
clases["CPIm"]['Saturación Al (%)'] = '<15'

clases["CPIf"] = dict()
clases["CPIf"]['Clase'] = ['12 , 13']
clases["CPIf"]['Distribución de lluvias'] = ['bimodal']
clases["CPIf"]['Pendiente'] = "<12"
clases["CPIf"]['Erosión (Grado)'] = ["no hay"]
clases["CPIf"]['Drenaje natural'] = ['bueno , moderado']
clases["CPIf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["CPIf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPIf"]['Profundidad efectiva (cm)'] = '>100'
clases["CPIf"]['Fertilidad'] = '>5.2'
clases["CPIf"]['CEmmhos'] = '<4'
clases["CPIf"]['%SNa'] = '<15'
clases["CPIf"]['Saturación Al (%)'] = '<15'


clases["CPSc"] = dict()
clases["CPSc"]['Clase'] = ['3 , 4 , 5']
clases["CPSc"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["CPSc"]['Pendiente'] = "<25"
clases["CPSc"]['Erosión (Grado)'] = ["no hay"]
clases["CPSc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CPSc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["CPSc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["CPSc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPSc"]['Profundidad efectiva (cm)'] = '>50'
clases["CPSc"]['Fertilidad'] = '>3.6'
clases["CPSc"]['CEmmhos'] = '<4'
clases["CPSc"]['%SNa'] = '<15'
clases["CPSc"]['Saturación Al (%)'] = '<30'

clases["CPSm"] = dict()
clases["CPSm"]['Clase'] = ['8 , 9']
clases["CPSm"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["CPSm"]['Pendiente'] = "<25"
clases["CPSm"]['Erosión (Grado)'] = ["no hay"]
clases["CPSm"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CPSm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["CPSm"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["CPSm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPSm"]['Profundidad efectiva (cm)'] = '>50'
clases["CPSm"]['Fertilidad'] = '>3.6'
clases["CPSm"]['CEmmhos'] = '<4'
clases["CPSm"]['%SNa'] = '<15'
clases["CPSm"]['Saturación Al (%)'] = '<30'

clases["CPSf"] = dict()
clases["CPSf"]['Clase'] = ['12 , 13']
clases["CPSf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["CPSf"]['Pendiente'] = "<25"
clases["CPSf"]['Erosión (Grado)'] = ["no hay"]
clases["CPSf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["CPSf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["CPSf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["CPSf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["CPSf"]['Profundidad efectiva (cm)'] = '>50'
clases["CPSf"]['Fertilidad'] = '>3.6'
clases["CPSf"]['CEmmhos'] = '<4'
clases["CPSf"]['%SNa'] = '<15'
clases["CPSf"]['Saturación Al (%)'] = '<30'

clases["PINc"] = dict()
clases["PINc"]['Clase'] = ['4']
clases["PINc"]['Distribución de lluvias'] = ['bimodal']
clases["PINc"]['Pendiente'] = "<7"
clases["PINc"]['Erosión (Grado)'] = ["no hay"]
clases["PINc"]['Drenaje natural'] = ['bueno , moderado']
clases["PINc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["PINc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PINc"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["PINc"]['Profundidad efectiva (cm)'] = '<50'
clases["PINc"]['Fertilidad'] = '>5.2'
clases["PINc"]['CEmmhos'] = '<4'
clases["PINc"]['%SNa'] = '<15'
clases["PINc"]['Saturación Al (%)'] = '<30'


clases["PINm"] = dict()
clases["PINm"]['Clase'] = ['9']
clases["PINm"]['Distribución de lluvias'] = ['bimodal']
clases["PINm"]['Pendiente'] = "<7"
clases["PINm"]['Erosión (Grado)'] = ["no hay"]
clases["PINm"]['Drenaje natural'] = ['bueno , moderado']
clases["PINm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["PINm"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PINm"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["PINm"]['Profundidad efectiva (cm)'] = '<50'
clases["PINm"]['Fertilidad'] = '>5.2'
clases["PINm"]['CEmmhos'] = '<4'
clases["PINm"]['%SNa'] = '<15'
clases["PINm"]['Saturación Al (%)'] = '<30'


clases["PINf"] = dict()
clases["PINf"]['Clase'] = ['13']
clases["PINf"]['Distribución de lluvias'] = ['bimodal']
clases["PINf"]['Pendiente'] = "<7"
clases["PINf"]['Erosión (Grado)'] = ["no hay"]
clases["PINf"]['Drenaje natural'] = ['bueno , moderado']
clases["PINf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["PINf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PINf"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["PINf"]['Profundidad efectiva (cm)'] = '<50'
clases["PINf"]['Fertilidad'] = '>5.2'
clases["PINf"]['CEmmhos'] = '<4'
clases["PINf"]['%SNa'] = '<15'
clases["PINf"]['Saturación Al (%)'] = '<30'

clases["PSIc"] = dict()
clases["PSIc"]['Clase'] = ['3 , 4 , 5']
clases["PSIc"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PSIc"]['Pendiente'] = "<12"
clases["PSIc"]['Erosión (Grado)'] = ["ligera"]
clases["PSIc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["PSIc"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["PSIc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIc"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIc"]['Fertilidad'] = '>3.6'
clases["PSIc"]['CEmmhos'] = '<8'
clases["PSIc"]['%SNa'] = '<15'
clases["PSIc"]['Saturación Al (%)'] = '<30'


clases["PSIc"] = dict()
clases["PSIc"]['Clase'] = ['3 , 4 , 5']
clases["PSIc"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PSIc"]['Pendiente'] = "<12"
clases["PSIc"]['Erosión (Grado)'] = ["ligera"]
clases["PSIc"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["PSIc"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["PSIc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIc"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIc"]['Fertilidad'] = '>3.6'
clases["PSIc"]['CEmmhos'] = '<8'
clases["PSIc"]['%SNa'] = '<15'
clases["PSIc"]['Saturación Al (%)'] = '<30'

clases["PSIm"] = dict()
clases["PSIm"]['Clase'] = ['8 , 9']
clases["PSIm"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PSIm"]['Pendiente'] = "<12"
clases["PSIm"]['Erosión (Grado)'] = ["ligera"]
clases["PSIm"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["PSIm"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["PSIm"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIm"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIm"]['Fertilidad'] = '>3.6'
clases["PSIm"]['CEmmhos'] = '<8'
clases["PSIm"]['%SNa'] = '<15'
clases["PSIm"]['Saturación Al (%)'] = '<30'


clases["PSIf"] = dict()
clases["PSIf"]['Clase'] = ['12 , 13']
clases["PSIf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PSIf"]['Pendiente'] = "<12"
clases["PSIf"]['Erosión (Grado)'] = ["ligera"]
clases["PSIf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["PSIf"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["PSIf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIf"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIf"]['Fertilidad'] = '>3.6'
clases["PSIf"]['CEmmhos'] = '<8'
clases["PSIf"]['%SNa'] = '<15'
clases["PSIf"]['Saturación Al (%)'] = '<30'


clases["PSIf"] = dict()
clases["PSIf"]['Clase'] = ['12 , 13']
clases["PSIf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PSIf"]['Pendiente'] = "<12"
clases["PSIf"]['Erosión (Grado)'] = ["ligera"]
clases["PSIf"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["PSIf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["PSIf"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["PSIf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["PSIf"]['Profundidad efectiva (cm)'] = '<25'
clases["PSIf"]['Fertilidad'] = '>3.6'
clases["PSIf"]['CEmmhos'] = '<8'
clases["PSIf"]['%SNa'] = '<15'
clases["PSIf"]['Saturación Al (%)'] = '<30'


clases["PEXc"] = dict()
clases["PEXc"]['Clase'] = ['2 , 3 , 4 , 5']
clases["PEXc"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PEXc"]['Pendiente'] = "<25"
clases["PEXc"]['Erosión (Grado)'] = ["ligera"]
clases["PEXc"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["PEXc"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["PEXc"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXc"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXc"]['Fertilidad'] = '>0.5'
clases["PEXc"]['CEmmhos'] = '<8'
clases["PEXc"]['%SNa'] = '<15'
clases["PEXc"]['Saturación Al (%)'] = '<60'


clases["PEXm"] = dict()
clases["PEXm"]['Clase'] = ['7 , 8 , 9 , 10']
clases["PEXm"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PEXm"]['Pendiente'] = "<25"
clases["PEXm"]['Erosión (Grado)'] = ["ligera"]
clases["PEXm"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["PEXm"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["PEXm"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXm"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXm"]['Fertilidad'] = '>0.5'
clases["PEXm"]['CEmmhos'] = '<8'
clases["PEXm"]['%SNa'] = '<15'
clases["PEXm"]['Saturación Al (%)'] = '<60'


clases["PEXf"] = dict()
clases["PEXf"]['Clase'] = ['12 , 13 , 14']
clases["PEXf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PEXf"]['Pendiente'] = "<25"
clases["PEXf"]['Erosión (Grado)'] = ["ligera"]
clases["PEXf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["PEXf"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["PEXf"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXf"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXf"]['Fertilidad'] = '>0.5'
clases["PEXf"]['CEmmhos'] = '<8'
clases["PEXf"]['%SNa'] = '<15'
clases["PEXf"]['Saturación Al (%)'] = '<60'

clases["PEXmf"] = dict()
clases["PEXmf"]['Clase'] = ['16 , 17']
clases["PEXmf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["PEXmf"]['Pendiente'] = "<25"
clases["PEXmf"]['Erosión (Grado)'] = ["ligera"]
clases["PEXmf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["PEXmf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["PEXmf"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["PEXmf"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["PEXmf"]['Profundidad efectiva (cm)'] = '>10'
clases["PEXmf"]['Fertilidad'] = '>0.5'
clases["PEXmf"]['CEmmhos'] = '<8'
clases["PEXmf"]['%SNa'] = '<15'
clases["PEXmf"]['Saturación Al (%)'] = '<60'

clases["AGSt"] = dict()
clases["AGSt"]['Clase'] = ['3 , 4 , 8 , 9 , 13 , 14 , 15']
clases["AGSt"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["AGSt"]['Pendiente'] = "<25"
clases["AGSt"]['Erosión (Grado)'] = ["no hay"]
clases["AGSt"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["AGSt"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["AGSt"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["AGSt"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["AGSt"]['Profundidad efectiva (cm)'] = '>25'
clases["AGSt"]['Fertilidad'] = '>0.5'
clases["AGSt"]['CEmmhos'] = '<8'
clases["AGSt"]['%SNa'] = '<15'
clases["AGSt"]['Saturación Al (%)'] = '<60'

clases["AGSp"] = dict()
clases["AGSp"]['Clase'] = ['3 , 4 , 5 , 6 , 8 , 9 , 13 , 14 , 15']
clases["AGSp"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["AGSp"]['Pendiente'] = "<75"
clases["AGSp"]['Erosión (Grado)'] = ["ligera"]
clases["AGSp"]['Drenaje natural'] = ['Excesivo , bueno , moderado']
clases["AGSp"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["AGSp"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["AGSp"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["AGSp"]['Profundidad efectiva (cm)'] = '>25'
clases["AGSp"]['Fertilidad'] = '>0.5'
clases["AGSp"]['CEmmhos'] = '<8'
clases["AGSp"]['%SNa'] = '<15'
clases["AGSp"]['Saturación Al (%)'] = '<60'

clases["ASPt"] = dict()
clases["ASPt"]['Clase'] = ['3 , 4 , 8 , 9 , 13 , 14 , 18']
clases["ASPt"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["ASPt"]['Pendiente'] = "<25"
clases["ASPt"]['Erosión (Grado)'] = ["moderada"]
clases["ASPt"]['Drenaje natural'] = ['bueno , moderado , imperfecto']
clases["ASPt"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocasionales']
clases["ASPt"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["ASPt"]['Fragmentos roca (% por Vol.) '] = '<3'
clases["ASPt"]['Profundidad efectiva (cm)'] = '>25'
clases["ASPt"]['Fertilidad'] = '>0.5'
clases["ASPt"]['CEmmhos'] = '<8'
clases["ASPt"]['%SNa'] = '<15'
clases["ASPt"]['Saturación Al (%)'] = '<60'

clases["ASPp"] = dict()
clases["ASPp"]['Clase'] = ['3 , 4 , 5 , 8 , 9 , 10 , 13 , 14']
clases["ASPp"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["ASPp"]['Pendiente'] = "<50"
clases["ASPp"]['Erosión (Grado)'] = ["moderada"]
clases["ASPp"]['Drenaje natural'] = ['bueno , moderado']
clases["ASPp"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['raras']
clases["ASPp"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["ASPp"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["ASPp"]['Profundidad efectiva (cm)'] = '>50'
clases["ASPp"]['Fertilidad'] = '>0.5'
clases["ASPp"]['CEmmhos'] = '<8'
clases["ASPp"]['%SNa'] = '<15'
clases["ASPp"]['Saturación Al (%)'] = '<60'


clases["SPA"] = dict()
clases["ASPp"]['Clase'] = ['2 , 3 , 4 , 5 , 7 , 8 , 9 , 10 , 12 , 13 , 15 , 17 , 18']
clases["ASPp"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["ASPp"]['Pendiente'] = "<50"
clases["ASPp"]['Erosión (Grado)'] = ["moderada"]
clases["ASPp"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["ASPp"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["ASPp"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["ASPp"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["ASPp"]['Profundidad efectiva (cm)'] = '>25'
clases["ASPp"]['Fertilidad'] = '>0.5'
clases["ASPp"]['CEmmhos'] = '<16'
clases["ASPp"]['%SNa'] = '<15'
clases["ASPp"]['Saturación Al (%)'] = '<90'


clases["FPDc"] = dict()
clases["FPDc"]['Clase'] = ['3 , 4 , 5 , 6']
clases["FPDc"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPDc"]['Pendiente'] = "<25"
clases["FPDc"]['Erosión (Grado)'] = ["ligera"]
clases["FPDc"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDc"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["FPDc"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["FPDc"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDc"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDc"]['Fertilidad'] = '>1.0'
clases["FPDc"]['CEmmhos'] = '<4'
clases["FPDc"]['%SNa'] = '<15'
clases["FPDc"]['Saturación Al (%)'] = '<30'

clases["FPDm"] = dict()
clases["FPDm"]['Clase'] = ['8 , 9 , 10']
clases["FPDm"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPDm"]['Pendiente'] = "<25"
clases["FPDm"]['Erosión (Grado)'] = ["ligera"]
clases["FPDm"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDm"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["FPDm"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["FPDm"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDm"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDm"]['Fertilidad'] = '>1.0'
clases["FPDm"]['CEmmhos'] = '<4'
clases["FPDm"]['%SNa'] = '<15'
clases["FPDm"]['Saturación Al (%)'] = '<30'

clases["FPDf"] = dict()
clases["FPDf"]['Clase'] = ['13 , 14 , 15 , 16']
clases["FPDf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPDf"]['Pendiente'] = "<25"
clases["FPDf"]['Erosión (Grado)'] = ["ligera"]
clases["FPDf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["FPDf"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["FPDf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDf"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDf"]['Fertilidad'] = '>1.0'
clases["FPDf"]['CEmmhos'] = '<4'
clases["FPDf"]['%SNa'] = '<15'
clases["FPDf"]['Saturación Al (%)'] = '<30'

clases["FPDmf"] = dict()
clases["FPDmf"]['Clase'] = ['17 , 18']
clases["FPDmf"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPDmf"]['Pendiente'] = "<12"
clases["FPDmf"]['Erosión (Grado)'] = ["ligera"]
clases["FPDmf"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPDmf"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['ocacionales']
clases["FPDmf"]['Fragmentos roca (% por Vol.) '] = '<35'
clases["FPDmf"]['Fragmentos roca (% por Vol.) '] = '<15'
clases["FPDmf"]['Profundidad efectiva (cm)'] = '>50'
clases["FPDmf"]['Fertilidad'] = '>1.0'
clases["FPDmf"]['CEmmhos'] = '<4'
clases["FPDmf"]['%SNa'] = '<15'
clases["FPDmf"]['Saturación Al (%)'] = '<30'


clases["FPP"] = dict()
clases["FPP"]['Clase'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17']
clases["FPP"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<50"
clases["FPP"]['Erosión (Grado)'] = ["moderada"]
clases["FPP"]['Drenaje natural'] = ['bueno , moderado , imperfecto , pobre']
clases["FPP"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["FPP"]['Profundidad efectiva (cm)'] = '>10'
clases["FPP"]['Fertilidad'] = '>0.5'
clases["FPP"]['CEmmhos'] = '<16'
clases["FPP"]['%SNa'] = '<15'
clases["FPP"]['Saturación Al (%)'] = '<90'


clases["FPP"] = dict()
clases["FPP"]['Clase'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19']
clases["FPP"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<100"
clases["FPP"]['Erosión (Grado)'] = ["severa"]
clases["FPP"]['Drenaje natural'] = ['excesivo , bueno , moderado , imperfecto , pobre']
clases["FPP"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["FPP"]['Profundidad efectiva (cm)'] = '>10'
clases["FPP"]['Fertilidad'] = '>0.5'
clases["FPP"]['CEmmhos'] = '<16'
clases["FPP"]['%SNa'] = '<15'
clases["FPP"]['Saturación Al (%)'] = '<90'

clases["FPP"] = dict()
clases["FPP"]['Clase'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21']
clases["FPP"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<100"
clases["FPP"]['Erosión (Grado)'] = ["severa"]
clases["FPP"]['Drenaje natural'] = ['excesivo , bueno , moderado , imperfecto , pobre']
clases["FPP"]['Inundaciones/Encharcamientos(Frecuencia)'] = ['frecuentes']
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<60'
clases["FPP"]['Fragmentos roca (% por Vol.) '] = '<50'
clases["FPP"]['Profundidad efectiva (cm)'] = '>10'
clases["FPP"]['CEmmhos'] = '<8'
clases["FPP"]['%SNa'] = '>15'
clases["FPP"]['Saturación Al (%)'] = '<90'

clases["FPP"] = dict()
clases["FPP"]['Clase'] = ['1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21']
clases["FPP"]['Distribución de lluvias'] = ['bimodal , monomodal']
clases["FPP"]['Pendiente'] = "<100"
clases["FPP"]['Drenaje natural'] = ['pantanoso']



def mapear_distribucion_lluvias_a_monomodal_o_bimodal(numero):
    numero = int(numero)
    if numero <= 4:
        return "monomodal"
    return "bimodal"


def conseguir_CEmmhos_de_sales_y_sodio(sales_y_sodio):
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
            if atributo == "CEmmhos":
                valor_de_atributo = conseguir_CEmmhos_de_sales_y_sodio(fila_del_excel["Sales y sodio"])
            elif atributo == "%SNa":
                valor_de_atributo = conseguir_porcentaje_de_sodio_de_sales_y_sodio(fila_del_excel["Sales y sodio"])
            else:
                valor_de_atributo = fila_del_excel[atributo]
            if atributo == 'Pendiente':
                valor_de_atributo = mapear_pendiente_a_rango(valor_de_atributo)
            if atributo == 'Distribución de lluvias':
                valor_de_atributo = mapear_distribucion_lluvias_a_monomodal_o_bimodal(valor_de_atributo)
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

correr_pruebas()

