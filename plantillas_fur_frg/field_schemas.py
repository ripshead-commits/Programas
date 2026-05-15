"""
Esquemas de campos para los módulos FUR Primera Vez, FUR Servicios y FRG.
Basado en el "Diccionario de Campos FUR Y FUR SERVICIOS" (ADRES) y la
"Circular Documento para Formularios" (SOAT - Colombia).

Cada campo:
  - key: nombre exacto de la columna en la plantilla XLSX
  - label: etiqueta visible en español
  - type: text | number | date | time | select | textarea
  - length: longitud máxima
  - required: True/False
  - options (si aplica): lista de (value, label)
  - section: agrupación lógica
"""

# --------------------------- LISTAS DE VALORES ---------------------------------
TIPO_DOC_VICTIMA = [
    ("CC", "CC - Cédula de ciudadanía"),
    ("CE", "CE - Cédula de extranjería"),
    ("CD", "CD - Carné diplomático"),
    ("PA", "PA - Pasaporte"),
    ("PE", "PE - Permiso especial de permanencia"),
    ("RC", "RC - Registro civil de nacimiento"),
    ("TI", "TI - Tarjeta de identidad"),
    ("CN", "CN - Certificado de nacido vivo"),
    ("DE", "DE - Documento extranjero"),
    ("PT", "PT - Permiso por protección temporal"),
    ("SC", "SC - Salvoconducto"),
    ("AS", "AS - Adulto sin identificar"),
    ("MS", "MS - Menor sin identificar"),
]

TIPO_DOC_PROPIETARIO = [
    ("CC", "CC - Cédula de ciudadanía"),
    ("CE", "CE - Cédula de extranjería"),
    ("CD", "CD - Carné diplomático"),
    ("PA", "PA - Pasaporte"),
    ("PE", "PE - Permiso especial de permanencia"),
    ("DE", "DE - Documento extranjero"),
    ("PT", "PT - Permiso de protección temporal"),
    ("NI", "NI - Número de identificación tributario NIT"),
]

TIPO_DOC_CONDUCTOR = [
    ("TI", "TI - Tarjeta de identidad"),
    ("CC", "CC - Cédula de ciudadanía"),
    ("CE", "CE - Cédula de extranjería"),
    ("CD", "CD - Carné diplomático"),
    ("PA", "PA - Pasaporte"),
    ("PE", "PE - Permiso especial de permanencia"),
    ("DE", "DE - Documento extranjero"),
    ("PT", "PT - Permiso de protección temporal"),
    ("SC", "SC - Salvoconducto"),
    ("AS", "AS - Adulto sin identificación"),
    ("MS", "MS - Menor sin identificación"),
]

TIPO_DOC_PROFESIONAL = [
    ("CC", "CC - Cédula de ciudadanía"),
    ("CE", "CE - Cédula de extranjería"),
    ("CD", "CD - Carné diplomático"),
    ("PA", "PA - Pasaporte"),
    ("PE", "PE - Permiso especial de permanencia"),
    ("DE", "DE - Documento extranjero"),
    ("PT", "PT - Permiso de protección temporal"),
]

TIPO_VEHICULO = [
    ("01", "01 - Automóvil"),
    ("02", "02 - Bus"),
    ("03", "03 - Buseta"),
    ("04", "04 - Camión"),
    ("05", "05 - Camioneta"),
    ("06", "06 - Campero"),
    ("07", "07 - Microbús"),
    ("08", "08 - Tractocamión"),
    ("09", "09 - Transporte escolar"),
    ("10", "10 - Motocicleta"),
    ("14", "14 - Motocarro"),
    ("17", "17 - Moto triciclo"),
    ("19", "19 - Cuatrimoto"),
    ("20", "20 - Moto Extranjera"),
    ("21", "21 - Vehículo Extranjero"),
    ("22", "22 - Volqueta"),
    ("23", "23 - Transporte masivo"),
]

TIPO_POBLACION_ESPECIAL = [
    ("00", "00 - No aplica / No pertenece"),
    ("01", "01 - Población habitante de calle"),
    ("02", "02 - NNAJ en proceso de restablecimiento de derechos"),
    ("10", "10 - Población infantil vulnerable bajo protección (no ICBF)"),
    ("14", "14 - Privados de la libertad - entidades territoriales"),
    ("16", "16 - Adultos mayores en centros de protección"),
    ("17", "17 - Comunidades indígenas / centros de armonización"),
    ("22", "22 - Prisión domiciliaria INPEC (no contributivo)"),
    ("25", "25 - Adolescentes y jóvenes ICBF (SRPA)"),
]

NATURALEZA_EVENTO = [
    ("01", "01 - Accidente de tránsito"),
    ("02", "02 - Sismo"),
    ("03", "03 - Maremoto"),
    ("04", "04 - Erupción volcánica"),
    ("05", "05 - Deslizamiento de tierra"),
    ("06", "06 - Inundación"),
    ("07", "07 - Avalancha"),
    ("08", "08 - Incendio natural"),
    ("09", "09 - Explosión terrorista"),
    ("10", "10 - Incendio terrorista"),
    ("11", "11 - Combate"),
    ("12", "12 - Ataques a Municipios"),
    ("13", "13 - Masacre"),
    ("14", "14 - Desplazados"),
    ("15", "15 - Mina antipersonal"),
    ("16", "16 - Huracán"),
    ("17", "17 - Otro"),
    ("25", "25 - Rayo"),
    ("26", "26 - Vendaval"),
    ("27", "27 - Tornado"),
]

CONDICION_VICTIMA = [
    ("01", "01 - Conductor"),
    ("02", "02 - Peatón"),
    ("03", "03 - Ocupante"),
    ("04", "04 - Ciclista"),
]

ZONA_OCURRENCIA = [
    ("01", "01 - Rural"),
    ("02", "02 - Urbana"),
]

ESTADO_ASEGURAMIENTO = [
    ("2", "2 - No asegurado"),
    ("3", "3 - Vehículo fantasma"),
    ("4", "4 - Póliza falsa"),
    ("6", "6 - Cobertura tarifa diferencial Decreto 2497/2022"),
    ("7", "7 - No asegurado: propietario indeterminado"),
    ("8", "8 - Vehículo sin placa"),
]

SI_NO = [("0", "0 - No"), ("1", "1 - Sí")]
SI_NO_INV = [("1", "1 - Sí"), ("2", "2 - No")]
TIPO_TRANSPORTE = [("1", "1 - Transporte básico"), ("2", "2 - Transporte medicalizado")]

ES_ATENCION_INICIAL = [
    ("1", "1 - Atención médica inicial del evento"),
    ("2", "2 - Transporte primario"),
    ("3", "3 - Transporte secundario"),
    ("4", "4 - Continuidad de la atención"),
    ("5", "5 - Atención ambulatoria"),
    ("6", "6 - Atención inicial + transporte primario"),
    ("7", "7 - Atención inicial + transporte secundario"),
    ("8", "8 - Atención inicial + transporte primario + secundario"),
]

TIPO_SERVICIO = [
    ("1", "1 - Medicamentos"),
    ("2", "2 - Procedimientos"),
    ("3", "3 - Transporte primario"),
    ("4", "4 - Transporte secundario"),
    ("5", "5 - Insumos"),
    ("6", "6 - Dispositivos médicos"),
    ("7", "7 - Material de osteosíntesis"),
    ("8", "8 - Procedimiento no incluido"),
]

CREDIT_DEBIT_NOTE = [
    ("CreditNote", "CreditNote - Nota Crédito"),
    ("DebitNote", "DebitNote - Nota Débito"),
]

TIPO_RESPUESTA_GLOSA = [
    ("01", "01 - Aceptación total de la glosa"),
    ("02", "02 - Aceptación parcial de la glosa"),
    ("03", "03 - No aceptación de la glosa"),
]

PERFIL_AUDITOR = [
    ("Medico", "Médico"),
    ("Odontologo", "Odontólogo"),
    ("Enfermero", "Enfermero/a"),
    ("Quimico_Farmaceutico", "Químico Farmacéutico"),
    ("Administrativo", "Administrativo"),
    ("Otro", "Otro"),
]

# --------------------------- SECCIONES ----------------------------------------
S_PRESTADOR = "Datos del Prestador"
S_VICTIMA = "Datos de la Víctima"
S_EVENTO = "Datos del Sitio donde Ocurrió el Evento"
S_VEHICULO = "Datos del Vehículo"
S_PROPIETARIO = "Datos del Propietario"
S_CONDUCTOR = "Datos del Conductor"
S_ATENCION = "Datos de Atención de la Víctima"
S_REMISION = "Datos de Remisión"
S_TRANSPORTE = "Datos Transporte y Movilización"
S_SERVICIO = "Datos del Servicio"
S_RECLAMACION = "Datos de la Reclamación"
S_GLOSA = "Datos de la Glosa"
S_AUDITOR = "Datos del Auditor"


def f(key, label, type_="text", length=None, required=True, options=None, section=None):
    return {
        "key": key,
        "label": label,
        "type": type_,
        "length": length,
        "required": required,
        "options": options,
        "section": section,
    }


# --------------------------- FUR PRIMERA VEZ ----------------------------------
FUR_FIELDS = [
    f("NIT_PRESTADOR", "NIT del Prestador", "number", 10, True, section=S_PRESTADOR),
    f("NUM_FACTURA", "Número de Factura", "text", 20, True, section=S_PRESTADOR),
    f("Tipo_documento_identidad_victima", "Tipo de documento de la víctima", "select", 2, True, TIPO_DOC_VICTIMA, S_VICTIMA),
    f("Numero_documento_identidad_victima", "Número de documento de la víctima", "text", 20, True, section=S_VICTIMA),
    f("Tipo_de_poblacion_especial", "Tipo de población especial", "select", 2, True, TIPO_POBLACION_ESPECIAL, S_VICTIMA),
    f("Primer_nombre_victima", "Primer nombre de la víctima", "text", 30, True, section=S_VICTIMA),
    f("Segundo_nombre_victima", "Segundo nombre de la víctima", "text", 30, False, section=S_VICTIMA),
    f("Primer_apellido_victima", "Primer apellido de la víctima", "text", 30, True, section=S_VICTIMA),
    f("Segundo_apellido_victima", "Segundo apellido de la víctima", "text", 30, False, section=S_VICTIMA),
    f("Direccion_residencia_victima", "Dirección de residencia de la víctima", "text", 100, False, section=S_VICTIMA),
    f("Codigo_municipio_residencia_victima", "Código DIVIPOLA municipio residencia víctima", "number", 5, False, section=S_VICTIMA),
    f("Telefono_victima", "Teléfono de la víctima", "number", 10, False, section=S_VICTIMA),
    f("Naturaleza_del_evento", "Naturaleza del evento", "select", 2, True, NATURALEZA_EVENTO, S_EVENTO),
    f("Descripcion_del_otro_evento", "Descripción del otro evento (si aplica)", "text", 40, False, section=S_EVENTO),
    f("Condicion_victima", "Condición de la víctima", "select", 2, True, CONDICION_VICTIMA, S_EVENTO),
    f("Fecha_de_ocurrencia_evento", "Fecha de ocurrencia del evento", "date", 10, True, section=S_EVENTO),
    f("Zona_de_ocurrencia_evento", "Zona de ocurrencia", "select", 2, True, ZONA_OCURRENCIA, S_EVENTO),
    f("Codigo_municipio_ocurrencia_evento", "Código DIVIPOLA municipio ocurrencia", "number", 5, True, section=S_EVENTO),
    f("Direccion_de_ocurrencia_evento", "Dirección de ocurrencia del evento", "text", 100, True, section=S_EVENTO),
    f("Descripcion_corta_de_lo_ocurrido_en_el_evento", "Descripción corta de lo ocurrido", "textarea", 1000, True, section=S_EVENTO),
    f("Estado_de_aseguramiento", "Estado de aseguramiento", "select", 1, True, ESTADO_ASEGURAMIENTO, S_EVENTO),
    f("Placa_vehiculo", "Placa del vehículo", "text", 10, True, section=S_VEHICULO),
    f("Tipo_de_Vehiculo", "Tipo de vehículo", "select", 2, True, TIPO_VEHICULO, S_VEHICULO),
    f("Codigo_de_la_aseguradora", "Código de la aseguradora", "text", 6, True, section=S_VEHICULO),
    f("Numero_de_poliza_SOAT", "Número de póliza SOAT", "text", 20, True, section=S_VEHICULO),
    f("Fecha_de_inicio_de_vigencia_de_la_poliza", "Fecha inicio vigencia de la póliza", "date", 10, True, section=S_VEHICULO),
    f("Fecha_final_de_vigencia_de_la_poliza", "Fecha final vigencia de la póliza", "date", 10, True, section=S_VEHICULO),
    f("Numero_de_radicado_SIRAS", "Número de radicado SIRAS", "text", 20, True, section=S_VEHICULO),
    f("Cobro_por_agotamiento_tope_Aseguradora", "Cobro por agotamiento tope Aseguradora", "select", 1, True, SI_NO, S_VEHICULO),
    f("Tipo_de_documento_de_identidad_del_propietario", "Tipo de documento del propietario", "select", 2, True, TIPO_DOC_PROPIETARIO, S_PROPIETARIO),
    f("Numero_de_documento_de_identidad_del_propietario", "Número de documento del propietario", "text", 20, True, section=S_PROPIETARIO),
    f("Primer_nombre_del_propietario_o_razon_social", "Primer nombre o razón social del propietario", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_nombre_del_propietario", "Segundo nombre del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Primer_apellido_del_propietario", "Primer apellido del propietario", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_apellido_del_propietario", "Segundo apellido del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Direccion_de_residencia_del_propietario", "Dirección de residencia del propietario", "text", 100, True, section=S_PROPIETARIO),
    f("Telefono_de_residencia_del_propietario", "Teléfono del propietario", "number", 10, True, section=S_PROPIETARIO),
    f("Codigo_del_municipio_de_residencia_del_propietario", "Código DIVIPOLA municipio propietario", "number", 5, True, section=S_PROPIETARIO),
    f("Tipo_de_documento_de_identidad_del_conductor", "Tipo de documento del conductor", "select", 2, True, TIPO_DOC_CONDUCTOR, S_CONDUCTOR),
    f("Numero_de_documento_de_identidad_del_conductor", "Número de documento del conductor", "text", 20, True, section=S_CONDUCTOR),
    f("Primer_nombre_del_conductor", "Primer nombre del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_nombre_del_conductor", "Segundo nombre del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Primer_apellido_del_conductor", "Primer apellido del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_apellido_del_conductor", "Segundo apellido del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Codigo_del_municipio_de_residencia_del_conductor", "Código DIVIPOLA municipio conductor", "number", 5, True, section=S_CONDUCTOR),
    f("Direccion_de_residencia_del_conductor", "Dirección de residencia del conductor", "text", 100, True, section=S_CONDUCTOR),
    f("Telefono_de_residencia_del_conductor", "Teléfono del conductor", "number", 10, True, section=S_CONDUCTOR),
    f("Uso_material_de_osteosintesis_en_la_atencion", "Uso de material de osteosíntesis", "select", 1, True, SI_NO_INV, S_ATENCION),
    f("Es_atencion_inicial_paciente_remitido_o_control", "Tipo de atención", "select", 1, True, ES_ATENCION_INICIAL, S_ATENCION),
    f("Placa_ambulancia_que_realiza_el_traslado_secundario", "Placa ambulancia traslado secundario", "text", 7, True, section=S_REMISION),
    f("Tipo_de_servicio_del_transporte_secundario", "Tipo servicio transporte secundario", "select", 1, True, TIPO_TRANSPORTE, S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_remite", "Código habilitación prestador que remite", "number", 12, True, section=S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_recibe", "Código habilitación prestador que recibe", "number", 12, True, section=S_REMISION),
    f("TIPO_de_documento_Profesional_que_recibe", "Tipo doc. profesional que recibe", "select", 2, True, TIPO_DOC_PROFESIONAL, S_REMISION),
    f("Numero_de_documento_Profesional_que_recibe", "Número doc. profesional que recibe", "text", 20, True, section=S_REMISION),
    f("Fecha_de_aceptacion", "Fecha de aceptación", "date", 10, True, section=S_REMISION),
    f("Hora_aceptacion", "Hora de aceptación (HH:MM)", "time", 5, True, section=S_REMISION),
    f("Tipo_de_servicio_del_transporte", "Tipo servicio transporte primario", "select", 1, True, TIPO_TRANSPORTE, S_TRANSPORTE),
    f("Placa_ambulancia_que_realiza_el_traslado", "Placa ambulancia traslado primario", "text", 7, True, section=S_TRANSPORTE),
    f("Codigo_de_habilitacion_del_prestador_que_recibe_transporte_primario", "Cód. habilitación prestador recibe (transp. primario)", "number", 12, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_desde_el_sitio_del_evento_Direccion", "Dirección desde donde se transporta a la víctima", "text", 100, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_hasta_el_fin_del_recorrido_direccion_IPS", "Dirección IPS donde termina el recorrido", "text", 100, True, section=S_TRANSPORTE),
]

# --------------------------- FUR SERVICIOS ------------------------------------
SER_FIELDS = [
    f("NUM_FACTURA", "Número de Factura", "text", 20, True, section=S_PRESTADOR),
    f("NIT_PRESTADOR", "NIT del Prestador", "number", 10, True, section=S_PRESTADOR),
    f("Tipo_de_servicio", "Tipo de servicio", "select", 1, True, TIPO_SERVICIO, S_SERVICIO),
    f("Codigo_general_del_procedimiento_quirurgico", "Código general procedimiento quirúrgico", "number", 6, False, section=S_SERVICIO),
    f("Consecutivo_procedimiento_quirurgico", "Consecutivo procedimiento quirúrgico", "number", 2, False, section=S_SERVICIO),
    f("Codigo_del_servicio", "Código del servicio", "text", 20, True, section=S_SERVICIO),
    f("Codificacion_CUPS", "Codificación CUPS", "text", 6, True, section=S_SERVICIO),
    f("Descripcion_del_servicio_o_elemento_reclamado", "Descripción del servicio o elemento reclamado", "textarea", 200, True, section=S_SERVICIO),
    f("Cantidad_de_servicios", "Cantidad de servicios", "number", 15, True, section=S_SERVICIO),
    f("Valor_unitario_facturado", "Valor unitario facturado", "number", 15, True, section=S_SERVICIO),
    f("Valor_unitario_reclamado", "Valor unitario reclamado", "number", 15, True, section=S_SERVICIO),
    f("Valor_total_facturado", "Valor total facturado", "number", 15, True, section=S_SERVICIO),
    f("Valor_total_reclamado", "Valor total reclamado", "number", 15, True, section=S_SERVICIO),
]

# --------------------------- FRG ----------------------------------------------
FRG_FIELDS = [
    f("NIT_PRESTADOR", "NIT del Prestador", "number", 10, True, section=S_PRESTADOR),
    f("NUM_FACTURA_ANTERIOR", "Número de factura anterior", "text", 20, True, section=S_RECLAMACION),
    f("NUM_FACTURA", "Número de factura (nueva)", "text", 20, True, section=S_RECLAMACION),
    f("NUMERO_RADICACION", "Número de radicación", "text", 20, True, section=S_RECLAMACION),
    f("CreditNote_o_DebitNote", "Tipo de nota (Credit/Debit)", "select", 20, True, CREDIT_DEBIT_NOTE, S_RECLAMACION),
    f("Valor_reclamado", "Valor reclamado", "number", 15, True, section=S_RECLAMACION),
    f("Direccion_residencia_victima", "Dirección de residencia de la víctima", "text", 100, False, section=S_VICTIMA),
    f("Telefono_victima", "Teléfono de la víctima", "number", 10, False, section=S_VICTIMA),
    f("Condicion_victima", "Condición de la víctima", "select", 2, True, CONDICION_VICTIMA, S_VICTIMA),
    f("Fecha_de_ocurrencia_evento", "Fecha de ocurrencia", "date", 10, True, section=S_EVENTO),
    f("Zona_de_ocurrencia_evento", "Zona de ocurrencia", "select", 2, True, ZONA_OCURRENCIA, S_EVENTO),
    f("Codigo_municipio_ocurrencia_evento", "Código DIVIPOLA municipio ocurrencia", "number", 5, True, section=S_EVENTO),
    f("Direccion_de_ocurrencia_evento", "Dirección de ocurrencia", "text", 100, True, section=S_EVENTO),
    f("Descripcion_corta_de_lo_ocurrido_en_el_evento", "Descripción corta de lo ocurrido", "textarea", 1000, True, section=S_EVENTO),
    f("Estado_de_aseguramiento", "Estado de aseguramiento", "select", 1, True, ESTADO_ASEGURAMIENTO, S_EVENTO),
    f("Placa_vehiculo", "Placa del vehículo", "text", 10, True, section=S_VEHICULO),
    f("Tipo_de_Vehiculo", "Tipo de vehículo", "select", 2, True, TIPO_VEHICULO, S_VEHICULO),
    f("Codigo_de_la_aseguradora", "Código de la aseguradora", "text", 6, True, section=S_VEHICULO),
    f("Numero_de_poliza_SOAT", "Número de póliza SOAT", "text", 20, True, section=S_VEHICULO),
    f("Fecha_de_inicio_de_vigencia_de_la_poliza", "Fecha inicio vigencia póliza", "date", 10, True, section=S_VEHICULO),
    f("Fecha_final_de_vigencia_de_la_poliza", "Fecha final vigencia póliza", "date", 10, True, section=S_VEHICULO),
    f("Numero_de_radicado_SIRAS", "Número de radicado SIRAS", "text", 20, True, section=S_VEHICULO),
    f("Cobro_por_agotamiento_tope_Aseguradora", "Cobro por agotamiento tope", "select", 1, True, SI_NO, S_VEHICULO),
    f("Tipo_de_documento_de_identidad_del_propietario", "Tipo doc. del propietario", "select", 2, True, TIPO_DOC_PROPIETARIO, S_PROPIETARIO),
    f("Numero_de_documento_de_identidad_del_propietario", "Número doc. propietario", "text", 20, True, section=S_PROPIETARIO),
    f("Primer_nombre_del_propietario_o_razon_social", "Primer nombre o razón social", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_nombre_del_propietario", "Segundo nombre del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Primer_apellido_del_propietario", "Primer apellido del propietario", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_apellido_del_propietario", "Segundo apellido del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Direccion_de_residencia_del_propietario", "Dirección residencia propietario", "text", 100, True, section=S_PROPIETARIO),
    f("Telefono_de_residencia_del_propietario", "Teléfono del propietario", "number", 10, True, section=S_PROPIETARIO),
    f("Codigo_del_municipio_de_residencia_del_propietario", "Código DIVIPOLA municipio propietario", "number", 5, True, section=S_PROPIETARIO),
    f("Tipo_de_documento_de_identidad_del_conductor", "Tipo doc. del conductor", "select", 2, True, TIPO_DOC_CONDUCTOR, S_CONDUCTOR),
    f("Numero_de_documento_de_identidad_del_conductor", "Número doc. conductor", "text", 20, True, section=S_CONDUCTOR),
    f("Primer_nombre_del_conductor", "Primer nombre del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_nombre_del_conductor", "Segundo nombre del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Primer_apellido_del_conductor", "Primer apellido del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_apellido_del_conductor", "Segundo apellido del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Codigo_del_municipio_de_residencia_del_conductor", "Código DIVIPOLA municipio conductor", "number", 5, True, section=S_CONDUCTOR),
    f("Direccion_de_residencia_del_conductor", "Dirección residencia conductor", "text", 100, True, section=S_CONDUCTOR),
    f("Telefono_de_residencia_del_conductor", "Teléfono del conductor", "number", 10, True, section=S_CONDUCTOR),
    f("Uso_material_de_osteosintesis_en_la_atencion", "Uso material osteosíntesis", "select", 1, True, SI_NO_INV, S_ATENCION),
    f("Es_atencion_inicial_paciente_remitido_o_control", "Tipo de atención", "select", 1, True, ES_ATENCION_INICIAL, S_ATENCION),
    f("Placa_ambulancia_que_realiza_la_remision", "Placa ambulancia que realiza la remisión", "text", 7, True, section=S_REMISION),
    f("Placa_ambulancia_que_realiza_el_traslado_secundario", "Placa ambulancia traslado secundario", "text", 7, True, section=S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_remite", "Cód. habilitación prestador que remite", "number", 12, True, section=S_REMISION),
    f("TIPO_de_documento_Profesional_que_recibe", "Tipo doc. profesional que recibe", "select", 2, True, TIPO_DOC_PROFESIONAL, S_REMISION),
    f("Numero_de_documento_Profesional_que_recibe", "Número doc. profesional que recibe", "text", 20, True, section=S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_recibe", "Cód. habilitación prestador que recibe", "number", 12, True, section=S_REMISION),
    f("Fecha_de_aceptacion", "Fecha de aceptación", "date", 10, True, section=S_REMISION),
    f("Hora_aceptacion", "Hora de aceptación (HH:MM)", "time", 5, True, section=S_REMISION),
    f("Placa_ambulancia_que_realiza_el_traslado", "Placa ambulancia traslado primario", "text", 7, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_desde_el_sitio_del_evento_Direccion", "Dirección desde donde se transporta", "text", 100, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_hasta_el_fin_del_recorrido_direccion_IPS", "Dirección IPS final", "text", 100, True, section=S_TRANSPORTE),
    f("ID_interno_Glosa", "ID interno de la glosa", "text", 20, True, section=S_GLOSA),
    f("itemID_servicio_o_tecnologia_objetado", "Item del servicio o tecnología objetado", "text", 200, True, section=S_GLOSA),
    f("Codigo_glosa", "Código de la glosa", "text", 10, True, section=S_GLOSA),
    f("Tipo_respuesta_a_glosa", "Tipo de respuesta a la glosa", "select", 2, True, TIPO_RESPUESTA_GLOSA, S_GLOSA),
    f("Respuesta_a_glosa", "Respuesta a la glosa", "textarea", 1000, True, section=S_GLOSA),
    f("Cantidad_aceptada", "Cantidad aceptada", "number", 15, True, section=S_GLOSA),
    f("Valor_aceptado", "Valor aceptado", "number", 15, True, section=S_GLOSA),
    f("Primer_nombre_primer_apellido_auditor", "Primer nombre y primer apellido del auditor", "text", 60, True, section=S_AUDITOR),
    f("Perfil_auditor", "Perfil del auditor", "select", 30, True, PERFIL_AUDITOR, S_AUDITOR),
]


MODULES = {
    "fur": {
        "id": "fur",
        "name": "FUR Primera Vez",
        "description": "Formulario Único de Reclamación - Primera Vez",
        "template_filename": "Plantilla_FUR_Primera_Vez.xlsx",
        "download_filename": "Plantilla_FUR_Primera_Vez_Diligenciada.xlsx",
        "fields": FUR_FIELDS,
        "color": "#2C5E4E",
        "color_hover": "#234B3E",
    },
    "ser": {
        "id": "ser",
        "name": "FUR Servicios",
        "description": "Formulario Único de Reclamación - Detalle de Servicios",
        "template_filename": "Plantilla_SER.xlsx",
        "download_filename": "Plantilla_SER_Diligenciada.xlsx",
        "fields": SER_FIELDS,
        "color": "#B8862E",
        "color_hover": "#9A7026",
    },
    "frg": {
        "id": "frg",
        "name": "FRG - Respuesta a Glosa",
        "description": "Formulario Único de Reclamación - Respuesta a Glosa",
        "template_filename": "Plantilla_FRG.xlsx",
        "download_filename": "Plantilla_FRG_Diligenciada.xlsx",
        "fields": FRG_FIELDS,
        "color": "#E27D5F",
        "color_hover": "#C66547",
    },
}


def get_module(module_id):
    return MODULES.get(module_id.lower())


def list_modules():
    return [
        {"id": m["id"], "name": m["name"], "description": m["description"],
         "field_count": len(m["fields"]), "color": m["color"], "color_hover": m["color_hover"]}
        for m in MODULES.values()
    ]


def get_sections(module_id):
    """Devuelve [{'name': str, 'fields': [field,...]}] preservando orden."""
    module = get_module(module_id)
    if not module:
        return []
    sections = []
    seen = {}
    for field in module["fields"]:
        sec = field.get("section") or "General"
        if sec not in seen:
            seen[sec] = len(sections)
            sections.append({"name": sec, "fields": []})
        sections[seen[sec]]["fields"].append(field)
    return sections
