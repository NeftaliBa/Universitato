import xml.etree.ElementTree as ET
import csv

#cargar y parsear el archivo XML
tree = ET.parse('encuesta.xml')
root = tree.getroot()

#Crear una lista para almacenar la informacion
persons = []

#Iterar sobre cada elemento 'person' en el XML
for person in root.findall('row'):
    name = person.find('Identificador_anónimo').text
    promedio = person.find('Promedio_semestre_anterior').text
    fatiga = person.find('A_la_hora_de_contestar_el_test_presentabas_fatiga').text
    enfermedad = person.find('A_la_hora_de_contestar_el_test_presentabas_problemas_de_salud_temporales_como_dolores_de_cabeza_o_enfermedades_pueden_impactar_el_desempeño_en_el_test').text
    testU = person.find('Consideras_que_el_test_no_está_bien_diseñado_para_medir_lo_que_pretende_evaluar_').text
    #age = person.find('age').text
    #email = person.find('email').text

    #agregar la informacion a la lista como un diccionario
    persons.append({'Identificador_anónimo': name,
                    'Promedio_semestre_anterior': promedio,
                    'A_la_hora_de_contestar_el_test_presentabas_fatiga' : fatiga,
                    'A_la_hora_de_contestar_el_test_presentabas_problemas_de_salud_temporales_como_dolores_de_cabeza_o_enfermedades_pueden_impactar_el_desempeño_en_el_test' : enfermedad,
                    'Consideras_que_el_test_no_está_bien_diseñado_para_medir_lo_que_pretende_evaluar_' : testU
                    #'age' : age
                    #'email' : email
                    })

# Encabezados
headers = [
    'Identificador_anónimo', 
    'Promedio_semestre_anterior', 
    'A_la_hora_de_contestar_el_test_presentabas_fatiga', 
    'A_la_hora_de_contestar_el_test_presentabas_problemas_de_salud_temporales_como_dolores_de_cabeza_o_enfermedades_pueden_impactar_el_desempeño_en_el_test', 
    'Consideras_que_el_test_no_está_bien_diseñado_para_medir_lo_que_pretende_evaluar_'
]

# Escribir en un archivo CSV
with open('encuesta.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(persons)