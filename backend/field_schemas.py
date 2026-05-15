"""
Esquemas de campos para los módulos FUR Primera Vez, FUR Servicios y FRG.
Basado en el "Diccionario de Campos FUR Y FUR SERVICIOS" (ADRES, normativa Colombia)
y la "Circular Documento para Formularios" (sistema SOAT).

Cada campo define:
  - key: nombre exacto de la columna en la plantilla XLSX
  - label: etiqueta legible en español
  - type: text | number | date | time | select | textarea
  - length: longitud máxima
  - required: True/False
  - options (opcional): lista de {value, label}
  - section: agrupación lógica para el formulario
"""

# Listas de valores reutilizables -------------------------------------------------

TIPO_DOC_VICTIMA = [
    {"value": "CC", "label": "CC - Cédula de ciudadanía"},
    {"value": "CE", "label": "CE - Cédula de extranjería"},
    {"value": "CD", "label": "CD - Carné diplomático"},
    {"value": "PA", "label": "PA - Pasaporte"},
    {"value": "PE", "label": "PE - Permiso especial de permanencia"},
    {"value": "RC", "label": "RC - Registro civil de nacimiento"},
    {"value": "TI", "label": "TI - Tarjeta de identidad"},
    {"value": "CN", "label": "CN - Certificado de nacido vivo"},
    {"value": "DE", "label": "DE - Documento extranjero"},
    {"value": "PT", "label": "PT - Permiso por protección temporal"},
    {"value": "SC", "label": "SC - Salvoconducto"},
    {"value": "AS", "label": "AS - Adulto sin identificar"},
    {"value": "MS", "label": "MS - Menor sin identificar"},
]

TIPO_DOC_PROPIETARIO = [
    {"value": "CC", "label": "CC - Cédula de ciudadanía"},
    {"value": "CE", "label": "CE - Cédula de extranjería"},
    {"value": "CD", "label": "CD - Carné diplomático"},
    {"value": "PA", "label": "PA - Pasaporte"},
    {"value": "PE", "label": "PE - Permiso especial de permanencia"},
    {"value": "DE", "label": "DE - Documento extranjero"},
    {"value": "PT", "label": "PT - Permiso de protección temporal"},
    {"value": "NI", "label": "NI - Número de identificación tributario NIT"},
]

TIPO_DOC_CONDUCTOR = [
    {"value": "TI", "label": "TI - Tarjeta de identidad"},
    {"value": "CC", "label": "CC - Cédula de ciudadanía"},
    {"value": "CE", "label": "CE - Cédula de extranjería"},
    {"value": "CD", "label": "CD - Carné diplomático"},
    {"value": "PA", "label": "PA - Pasaporte"},
    {"value": "PE", "label": "PE - Permiso especial de permanencia"},
    {"value": "DE", "label": "DE - Documento extranjero"},
    {"value": "PT", "label": "PT - Permiso de protección temporal"},
    {"value": "SC", "label": "SC - Salvoconducto"},
    {"value": "AS", "label": "AS - Adulto sin identificación"},
    {"value": "MS", "label": "MS - Menor sin identificación"},
]

TIPO_DOC_PROFESIONAL = [
    {"value": "CC", "label": "CC - Cédula de ciudadanía"},
    {"value": "CE", "label": "CE - Cédula de extranjería"},
    {"value": "CD", "label": "CD - Carné diplomático"},
    {"value": "PA", "label": "PA - Pasaporte"},
    {"value": "PE", "label": "PE - Permiso especial de permanencia"},
    {"value": "DE", "label": "DE - Documento extranjero"},
    {"value": "PT", "label": "PT - Permiso de protección temporal"},
]

TIPO_VEHICULO = [
    {"value": "01", "label": "01 - Automóvil"},
    {"value": "02", "label": "02 - Bus"},
    {"value": "03", "label": "03 - Buseta"},
    {"value": "04", "label": "04 - Camión"},
    {"value": "05", "label": "05 - Camioneta"},
    {"value": "06", "label": "06 - Campero"},
    {"value": "07", "label": "07 - Microbús"},
    {"value": "08", "label": "08 - Tractocamión"},
    {"value": "09", "label": "09 - Transporte escolar"},
    {"value": "10", "label": "10 - Motocicleta"},
    {"value": "14", "label": "14 - Motocarro"},
    {"value": "17", "label": "17 - Moto triciclo"},
    {"value": "19", "label": "19 - Cuatrimoto"},
    {"value": "20", "label": "20 - Moto Extranjera"},
    {"value": "21", "label": "21 - Vehículo Extranjero"},
    {"value": "22", "label": "22 - Volqueta"},
    {"value": "23", "label": "23 - Transporte masivo"},
]

TIPO_POBLACION_ESPECIAL = [
    {"value": "01", "label": "01 - Población habitante de calle"},
    {"value": "02", "label": "02 - NNAJ en proceso administrativo de restablecimiento de derechos"},
    {"value": "10", "label": "10 - Población infantil vulnerable bajo protección (no ICBF)"},
    {"value": "14", "label": "14 - Población privada de la libertad a cargo de entidades territoriales"},
    {"value": "16", "label": "16 - Adultos mayores de escasos recursos en centros de protección"},
    {"value": "17", "label": "17 - Comunidades indígenas incluida población en centros de armonización"},
    {"value": "22", "label": "22 - Personas en prisión domiciliaria (INPEC) no contributivo/especial"},
    {"value": "25", "label": "25 - Adolescentes y jóvenes a cargo del ICBF (SRPA)"},
    {"value": "00", "label": "00 - No aplica / No pertenece"},
]

NATURALEZA_EVENTO = [
    {"value": "01", "label": "01 - Accidente de tránsito"},
    {"value": "02", "label": "02 - Sismo"},
    {"value": "03", "label": "03 - Maremoto"},
    {"value": "04", "label": "04 - Erupción volcánica"},
    {"value": "05", "label": "05 - Deslizamiento de tierra"},
    {"value": "06", "label": "06 - Inundación"},
    {"value": "07", "label": "07 - Avalancha"},
    {"value": "08", "label": "08 - Incendio natural"},
    {"value": "09", "label": "09 - Explosión terrorista"},
    {"value": "10", "label": "10 - Incendio terrorista"},
    {"value": "11", "label": "11 - Combate"},
    {"value": "12", "label": "12 - Ataques a Municipios"},
    {"value": "13", "label": "13 - Masacre"},
    {"value": "14", "label": "14 - Desplazados"},
    {"value": "15", "label": "15 - Mina antipersonal"},
    {"value": "16", "label": "16 - Huracán"},
    {"value": "17", "label": "17 - Otro"},
    {"value": "25", "label": "25 - Rayo"},
    {"value": "26", "label": "26 - Vendaval"},
    {"value": "27", "label": "27 - Tornado"},
]

CONDICION_VICTIMA = [
    {"value": "01", "label": "01 - Conductor"},
    {"value": "02", "label": "02 - Peatón"},
    {"value": "03", "label": "03 - Ocupante"},
    {"value": "04", "label": "04 - Ciclista"},
]

ZONA_OCURRENCIA = [
    {"value": "01", "label": "01 - Rural"},
    {"value": "02", "label": "02 - Urbana"},
]

ESTADO_ASEGURAMIENTO = [
    {"value": "2", "label": "2 - No asegurado"},
    {"value": "3", "label": "3 - Vehículo fantasma"},
    {"value": "4", "label": "4 - Póliza falsa"},
    {"value": "6", "label": "6 - Cobertura tarifa diferencial Decreto 2497/2022"},
    {"value": "7", "label": "7 - No asegurado: propietario indeterminado o sin información"},
    {"value": "8", "label": "8 - Vehículo sin placa"},
]

SI_NO = [
    {"value": "0", "label": "0 - No"},
    {"value": "1", "label": "1 - Sí"},
]

SI_NO_INV = [
    {"value": "1", "label": "1 - Sí"},
    {"value": "2", "label": "2 - No"},
]

TIPO_TRANSPORTE = [
    {"value": "1", "label": "1 - Transporte básico"},
    {"value": "2", "label": "2 - Transporte medicalizado"},
]

ES_ATENCION_INICIAL = [
    {"value": "1", "label": "1 - Atención médica inicial del evento"},
    {"value": "2", "label": "2 - Transporte primario"},
    {"value": "3", "label": "3 - Transporte secundario"},
    {"value": "4", "label": "4 - Continuidad de la atención"},
    {"value": "5", "label": "5 - Atención ambulatoria"},
    {"value": "6", "label": "6 - Atención inicial + transporte primario"},
    {"value": "7", "label": "7 - Atención inicial + transporte secundario"},
    {"value": "8", "label": "8 - Atención inicial + transporte primario + secundario"},
]

TIPO_SERVICIO = [
    {"value": "1", "label": "1 - Medicamentos"},
    {"value": "2", "label": "2 - Procedimientos"},
    {"value": "3", "label": "3 - Transporte primario"},
    {"value": "4", "label": "4 - Transporte secundario"},
    {"value": "5", "label": "5 - Insumos"},
    {"value": "6", "label": "6 - Dispositivos médicos"},
    {"value": "7", "label": "7 - Material de osteosíntesis"},
    {"value": "8", "label": "8 - Procedimiento no incluido"},
]

CREDIT_DEBIT_NOTE = [
    {"value": "CreditNote", "label": "CreditNote - Nota Crédito"},
    {"value": "DebitNote", "label": "DebitNote - Nota Débito"},
]

TIPO_RESPUESTA_GLOSA = [
    {"value": "01", "label": "01 - Aceptación total de la glosa"},
    {"value": "02", "label": "02 - Aceptación parcial de la glosa"},
    {"value": "03", "label": "03 - No aceptación de la glosa"},
]

PERFIL_AUDITOR = [
    {"value": "Medico", "label": "Médico"},
    {"value": "Odontologo", "label": "Odontólogo"},
    {"value": "Enfermero", "label": "Enfermero/a"},
    {"value": "Quimico_Farmaceutico", "label": "Químico Farmacéutico"},
    {"value": "Administrativo", "label": "Administrativo"},
    {"value": "Otro", "label": "Otro"},
]

# Secciones reutilizables ---------------------------------------------------------
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


def f(key, label, type_="text", length=None, required=True, options=None, section=None, placeholder=None, help_=None):
    d = {"key": key, "label": label, "type": type_, "required": required, "section": section}
    if length is not None:
        d["length"] = length
    if options is not None:
        d["options"] = options
    if placeholder is not None:
        d["placeholder"] = placeholder
    if help_ is not None:
        d["help"] = help_
    return d


# ============================== FUR PRIMERA VEZ ==================================
FUR_FIELDS = [
    # Prestador
    f("NIT_PRESTADOR", "NIT del Prestador", "number", 10, True, section=S_PRESTADOR),
    f("NUM_FACTURA", "Número de Factura", "text", 20, True, section=S_PRESTADOR),
    # Víctima
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
    # Evento
    f("Naturaleza_del_evento", "Naturaleza del evento", "select", 2, True, NATURALEZA_EVENTO, S_EVENTO),
    f("Descripcion_del_otro_evento", "Descripción del otro evento (si aplica)", "text", 40, False, section=S_EVENTO),
    f("Condicion_victima", "Condición de la víctima", "select", 2, True, CONDICION_VICTIMA, S_EVENTO),
    f("Fecha_de_ocurrencia_evento", "Fecha de ocurrencia del evento", "date", 10, True, section=S_EVENTO),
    f("Zona_de_ocurrencia_evento", "Zona de ocurrencia", "select", 2, True, ZONA_OCURRENCIA, S_EVENTO),
    f("Codigo_municipio_ocurrencia_evento", "Código DIVIPOLA municipio ocurrencia", "number", 5, True, section=S_EVENTO),
    f("Direccion_de_ocurrencia_evento", "Dirección de ocurrencia del evento", "text", 100, True, section=S_EVENTO),
    f("Descripcion_corta_de_lo_ocurrido_en_el_evento", "Descripción corta de lo ocurrido", "textarea", 1000, True, section=S_EVENTO),
    f("Estado_de_aseguramiento", "Estado de aseguramiento", "select", 1, True, ESTADO_ASEGURAMIENTO, S_EVENTO),
    # Vehículo
    f("Placa_vehiculo", "Placa del vehículo", "text", 10, True, section=S_VEHICULO),
    f("Tipo_de_Vehiculo", "Tipo de vehículo", "select", 2, True, TIPO_VEHICULO, S_VEHICULO),
    f("Codigo_de_la_aseguradora", "Código de la aseguradora", "text", 6, True, section=S_VEHICULO),
    f("Numero_de_poliza_SOAT", "Número de póliza SOAT", "text", 20, True, section=S_VEHICULO),
    f("Fecha_de_inicio_de_vigencia_de_la_poliza", "Fecha inicio vigencia de la póliza", "date", 10, True, section=S_VEHICULO),
    f("Fecha_final_de_vigencia_de_la_poliza", "Fecha final vigencia de la póliza", "date", 10, True, section=S_VEHICULO),
    f("Numero_de_radicado_SIRAS", "Número de radicado SIRAS", "text", 20, True, section=S_VEHICULO),
    f("Cobro_por_agotamiento_tope_Aseguradora", "Cobro por agotamiento tope Aseguradora", "select", 1, True, SI_NO, S_VEHICULO),
    # Propietario
    f("Tipo_de_documento_de_identidad_del_propietario", "Tipo de documento del propietario", "select", 2, True, TIPO_DOC_PROPIETARIO, S_PROPIETARIO),
    f("Numero_de_documento_de_identidad_del_propietario", "Número de documento del propietario", "text", 20, True, section=S_PROPIETARIO),
    f("Primer_nombre_del_propietario_o_razon_social", "Primer nombre o razón social del propietario", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_nombre_del_propietario", "Segundo nombre del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Primer_apellido_del_propietario", "Primer apellido del propietario", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_apellido_del_propietario", "Segundo apellido del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Direccion_de_residencia_del_propietario", "Dirección de residencia del propietario", "text", 100, True, section=S_PROPIETARIO),
    f("Telefono_de_residencia_del_propietario", "Teléfono del propietario", "number", 10, True, section=S_PROPIETARIO),
    f("Codigo_del_municipio_de_residencia_del_propietario", "Código DIVIPOLA municipio residencia propietario", "number", 5, True, section=S_PROPIETARIO),
    # Conductor
    f("Tipo_de_documento_de_identidad_del_conductor", "Tipo de documento del conductor", "select", 2, True, TIPO_DOC_CONDUCTOR, S_CONDUCTOR),
    f("Numero_de_documento_de_identidad_del_conductor", "Número de documento del conductor", "text", 20, True, section=S_CONDUCTOR),
    f("Primer_nombre_del_conductor", "Primer nombre del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_nombre_del_conductor", "Segundo nombre del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Primer_apellido_del_conductor", "Primer apellido del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_apellido_del_conductor", "Segundo apellido del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Codigo_del_municipio_de_residencia_del_conductor", "Código DIVIPOLA municipio residencia conductor", "number", 5, True, section=S_CONDUCTOR),
    f("Direccion_de_residencia_del_conductor", "Dirección de residencia del conductor", "text", 100, True, section=S_CONDUCTOR),
    f("Telefono_de_residencia_del_conductor", "Teléfono del conductor", "number", 10, True, section=S_CONDUCTOR),
    # Atención
    f("Uso_material_de_osteosintesis_en_la_atencion", "Uso de material de osteosíntesis", "select", 1, True, SI_NO_INV, S_ATENCION),
    f("Es_atencion_inicial_paciente_remitido_o_control", "Tipo de atención", "select", 1, True, ES_ATENCION_INICIAL, S_ATENCION),
    # Remisión / Transporte secundario
    f("Placa_ambulancia_que_realiza_el_traslado_secundario", "Placa ambulancia traslado secundario", "text", 7, True, section=S_REMISION),
    f("Tipo_de_servicio_del_transporte_secundario", "Tipo de servicio transporte secundario", "select", 1, True, TIPO_TRANSPORTE, S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_remite", "Código habilitación prestador que remite", "number", 12, True, section=S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_recibe", "Código habilitación prestador que recibe", "number", 12, True, section=S_REMISION),
    f("TIPO_de_documento_Profesional_que_recibe", "Tipo doc. del profesional que recibe", "select", 2, True, TIPO_DOC_PROFESIONAL, S_REMISION),
    f("Numero_de_documento_Profesional_que_recibe", "Número doc. del profesional que recibe", "text", 20, True, section=S_REMISION),
    f("Fecha_de_aceptacion", "Fecha de aceptación", "date", 10, True, section=S_REMISION),
    f("Hora_aceptacion", "Hora de aceptación (HH:MM)", "time", 5, True, section=S_REMISION),
    # Transporte primario
    f("Tipo_de_servicio_del_transporte", "Tipo de servicio del transporte primario", "select", 1, True, TIPO_TRANSPORTE, S_TRANSPORTE),
    f("Placa_ambulancia_que_realiza_el_traslado", "Placa ambulancia traslado primario", "text", 7, True, section=S_TRANSPORTE),
    f("Codigo_de_habilitacion_del_prestador_que_recibe_transporte_primario", "Código habilitación prestador que recibe (transp. primario)", "number", 12, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_desde_el_sitio_del_evento_Direccion", "Dirección desde donde se transporta a la víctima", "text", 100, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_hasta_el_fin_del_recorrido_direccion_IPS", "Dirección IPS donde termina el recorrido", "text", 100, True, section=S_TRANSPORTE),
]

# ============================== FUR SERVICIOS ====================================
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

# ============================== FRG (RESPUESTA A GLOSA) ==========================
FRG_FIELDS = [
    # Reclamación
    f("NIT_PRESTADOR", "NIT del Prestador", "number", 10, True, section=S_PRESTADOR),
    f("NUM_FACTURA_ANTERIOR", "Número de factura anterior", "text", 20, True, section=S_RECLAMACION),
    f("NUM_FACTURA", "Número de factura (nueva)", "text", 20, True, section=S_RECLAMACION),
    f("NUMERO_RADICACION", "Número de radicación", "text", 20, True, section=S_RECLAMACION),
    f("CreditNote_o_DebitNote", "Tipo de nota (Credit/Debit)", "select", 20, True, CREDIT_DEBIT_NOTE, S_RECLAMACION),
    f("Valor_reclamado", "Valor reclamado", "number", 15, True, section=S_RECLAMACION),
    # Víctima
    f("Direccion_residencia_victima", "Dirección de residencia de la víctima", "text", 100, False, section=S_VICTIMA),
    f("Telefono_victima", "Teléfono de la víctima", "number", 10, False, section=S_VICTIMA),
    f("Condicion_victima", "Condición de la víctima", "select", 2, True, CONDICION_VICTIMA, S_VICTIMA),
    # Evento
    f("Fecha_de_ocurrencia_evento", "Fecha de ocurrencia", "date", 10, True, section=S_EVENTO),
    f("Zona_de_ocurrencia_evento", "Zona de ocurrencia", "select", 2, True, ZONA_OCURRENCIA, S_EVENTO),
    f("Codigo_municipio_ocurrencia_evento", "Código DIVIPOLA municipio ocurrencia", "number", 5, True, section=S_EVENTO),
    f("Direccion_de_ocurrencia_evento", "Dirección de ocurrencia", "text", 100, True, section=S_EVENTO),
    f("Descripcion_corta_de_lo_ocurrido_en_el_evento", "Descripción corta de lo ocurrido", "textarea", 1000, True, section=S_EVENTO),
    f("Estado_de_aseguramiento", "Estado de aseguramiento", "select", 1, True, ESTADO_ASEGURAMIENTO, S_EVENTO),
    # Vehículo
    f("Placa_vehiculo", "Placa del vehículo", "text", 10, True, section=S_VEHICULO),
    f("Tipo_de_Vehiculo", "Tipo de vehículo", "select", 2, True, TIPO_VEHICULO, S_VEHICULO),
    f("Codigo_de_la_aseguradora", "Código de la aseguradora", "text", 6, True, section=S_VEHICULO),
    f("Numero_de_poliza_SOAT", "Número de póliza SOAT", "text", 20, True, section=S_VEHICULO),
    f("Fecha_de_inicio_de_vigencia_de_la_poliza", "Fecha inicio vigencia póliza", "date", 10, True, section=S_VEHICULO),
    f("Fecha_final_de_vigencia_de_la_poliza", "Fecha final vigencia póliza", "date", 10, True, section=S_VEHICULO),
    f("Numero_de_radicado_SIRAS", "Número de radicado SIRAS", "text", 20, True, section=S_VEHICULO),
    f("Cobro_por_agotamiento_tope_Aseguradora", "Cobro por agotamiento tope", "select", 1, True, SI_NO, S_VEHICULO),
    # Propietario
    f("Tipo_de_documento_de_identidad_del_propietario", "Tipo doc. del propietario", "select", 2, True, TIPO_DOC_PROPIETARIO, S_PROPIETARIO),
    f("Numero_de_documento_de_identidad_del_propietario", "Número doc. propietario", "text", 20, True, section=S_PROPIETARIO),
    f("Primer_nombre_del_propietario_o_razon_social", "Primer nombre o razón social", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_nombre_del_propietario", "Segundo nombre del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Primer_apellido_del_propietario", "Primer apellido del propietario", "text", 30, True, section=S_PROPIETARIO),
    f("Segundo_apellido_del_propietario", "Segundo apellido del propietario", "text", 30, False, section=S_PROPIETARIO),
    f("Direccion_de_residencia_del_propietario", "Dirección residencia propietario", "text", 100, True, section=S_PROPIETARIO),
    f("Telefono_de_residencia_del_propietario", "Teléfono del propietario", "number", 10, True, section=S_PROPIETARIO),
    f("Codigo_del_municipio_de_residencia_del_propietario", "Código DIVIPOLA municipio propietario", "number", 5, True, section=S_PROPIETARIO),
    # Conductor
    f("Tipo_de_documento_de_identidad_del_conductor", "Tipo doc. del conductor", "select", 2, True, TIPO_DOC_CONDUCTOR, S_CONDUCTOR),
    f("Numero_de_documento_de_identidad_del_conductor", "Número doc. conductor", "text", 20, True, section=S_CONDUCTOR),
    f("Primer_nombre_del_conductor", "Primer nombre del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_nombre_del_conductor", "Segundo nombre del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Primer_apellido_del_conductor", "Primer apellido del conductor", "text", 30, True, section=S_CONDUCTOR),
    f("Segundo_apellido_del_conductor", "Segundo apellido del conductor", "text", 30, False, section=S_CONDUCTOR),
    f("Codigo_del_municipio_de_residencia_del_conductor", "Código DIVIPOLA municipio conductor", "number", 5, True, section=S_CONDUCTOR),
    f("Direccion_de_residencia_del_conductor", "Dirección residencia conductor", "text", 100, True, section=S_CONDUCTOR),
    f("Telefono_de_residencia_del_conductor", "Teléfono del conductor", "number", 10, True, section=S_CONDUCTOR),
    # Atención
    f("Uso_material_de_osteosintesis_en_la_atencion", "Uso material osteosíntesis", "select", 1, True, SI_NO_INV, S_ATENCION),
    f("Es_atencion_inicial_paciente_remitido_o_control", "Tipo de atención", "select", 1, True, ES_ATENCION_INICIAL, S_ATENCION),
    # Remisión
    f("Placa_ambulancia_que_realiza_la_remision", "Placa ambulancia que realiza la remisión", "text", 7, True, section=S_REMISION),
    f("Placa_ambulancia_que_realiza_el_traslado_secundario", "Placa ambulancia traslado secundario", "text", 7, True, section=S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_remite", "Código habilitación prestador que remite", "number", 12, True, section=S_REMISION),
    f("TIPO_de_documento_Profesional_que_recibe", "Tipo doc. profesional que recibe", "select", 2, True, TIPO_DOC_PROFESIONAL, S_REMISION),
    f("Numero_de_documento_Profesional_que_recibe", "Número doc. profesional que recibe", "text", 20, True, section=S_REMISION),
    f("Codigo_de_habilitacion_del_prestador_que_recibe", "Código habilitación prestador que recibe", "number", 12, True, section=S_REMISION),
    f("Fecha_de_aceptacion", "Fecha de aceptación", "date", 10, True, section=S_REMISION),
    f("Hora_aceptacion", "Hora de aceptación (HH:MM)", "time", 5, True, section=S_REMISION),
    # Transporte
    f("Placa_ambulancia_que_realiza_el_traslado", "Placa ambulancia traslado primario", "text", 7, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_desde_el_sitio_del_evento_Direccion", "Dirección desde donde se transporta", "text", 100, True, section=S_TRANSPORTE),
    f("Transporte_de_la_victima_hasta_el_fin_del_recorrido_direccion_IPS", "Dirección IPS final", "text", 100, True, section=S_TRANSPORTE),
    # Glosa
    f("ID_interno_Glosa", "ID interno de la glosa", "text", 20, True, section=S_GLOSA),
    f("itemID_servicio_o_tecnologia_objetado", "Item del servicio o tecnología objetado", "text", 200, True, section=S_GLOSA),
    f("Codigo_glosa", "Código de la glosa", "text", 10, True, section=S_GLOSA),
    f("Tipo_respuesta_a_glosa", "Tipo de respuesta a la glosa", "select", 2, True, TIPO_RESPUESTA_GLOSA, S_GLOSA),
    f("Respuesta_a_glosa", "Respuesta a la glosa", "textarea", 1000, True, section=S_GLOSA),
    f("Cantidad_aceptada", "Cantidad aceptada", "number", 15, True, section=S_GLOSA),
    f("Valor_aceptado", "Valor aceptado", "number", 15, True, section=S_GLOSA),
    # Auditor
    f("Primer_nombre_primer_apellido_auditor", "Primer nombre y primer apellido del auditor", "text", 60, True, section=S_AUDITOR),
    f("Perfil_auditor", "Perfil del auditor", "select", 30, True, PERFIL_AUDITOR, S_AUDITOR),
]


MODULES = {
    "fur": {
        "id": "fur",
        "name": "FUR Primera Vez",
        "description": "Formulario Único de Reclamación - Primera Vez (SOAT/ADRES)",
        "template_filename": "Plantilla_FUR_Primera_Vez.xlsx",
        "download_filename": "Plantilla_FUR_Primera_Vez_Diligenciada.xlsx",
        "fields": FUR_FIELDS,
    },
    "ser": {
        "id": "ser",
        "name": "FUR Servicios",
        "description": "Formulario Único de Reclamación - Detalle de Servicios",
        "template_filename": "Plantilla_SER.xlsx",
        "download_filename": "Plantilla_SER_Diligenciada.xlsx",
        "fields": SER_FIELDS,
    },
    "frg": {
        "id": "frg",
        "name": "FRG - Respuesta a Glosa",
        "description": "Formulario Único de Reclamación - Respuesta a Glosa",
        "template_filename": "Plantilla_FRG.xlsx",
        "download_filename": "Plantilla_FRG_Diligenciada.xlsx",
        "fields": FRG_FIELDS,
    },
}


def get_module(module_id: str):
    return MODULES.get(module_id.lower())


def list_modules():
    return [
        {
            "id": m["id"],
            "name": m["name"],
            "description": m["description"],
            "field_count": len(m["fields"]),
        }
        for m in MODULES.values()
    ]
