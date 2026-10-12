# Contenido del sitio, con la misma estructura y orden que www.urracaasesores.com.
#
# Tipos de bloque:
#   ("h", nivel, texto)      encabezado
#   ("p", texto)             párrafo
#   ("ul", [items])          lista
#   ("pendiente", nota)      párrafo de la web original que queda por pegar
#
# Las imágenes son de Pexels (licencia gratuita) y se cargan por URL desde su CDN.

def pexels(photo_id, w=2000):
    return (f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg"
            f"?auto=compress&cs=tinysrgb&w={w}")


SITE_TITLE = "URRACA ASESORES Y ABOGADOS"

NAV = [
    ("Inicio", "/"),
    ("Urraca Asesores", "/urraca-asesores"),
    ("Urraca Abogados", [
        ("Concursal", "/concursal"),
        ("Gestion de recobro", "/gestion-de-recobro"),
        ("Derecho mercantil", "/derecho-mercantil"),
        ("Derecho bancario", "/derecho-bancario"),
        ("Derecho contractual", "/derecho-contractual"),
        ("Derecho civil", "/derecho-civil"),
        ("Derecho penal", "/derecho-penal"),
        ("Derecho procesal", "/derecho-procesal"),
        ("Derecho inmobiliario", "/derecho-inmobiliario"),
        ("Derecho urbanistico", "/derecho-urbanistico"),
        ("Derecho laboral", "/derecho-laboral"),
        ("Derecho de familia", "/derecho-de-familia"),
    ]),
    ("Contacto", "/contacto"),
]

FOOTER = {
    "Ubicación": ["C. Mayor Principal, 15", "Piso 2D, 34001 Palencia, Spain"],
    "Horario de verano": [
        "JULIO: Lunes a viernes 9:00 a 17:00",
        "AGOSTO: Lunes a viernes 9:00 a 14:00",
        "Sábado y domingo: cerrado",
    ],
    "Contacto": ["(+34) 979 74 43 58", "e-mail: info@urracaasesores.com"],
}

# Cada página: slug -> dict(title, layout, image, blocks...)
# layouts:
#   "banner"  imagen a ancho completo con el título encima, contenido debajo
#   "split"   título + contenido a un lado, imagen al otro
PAGES = {
    "urraca-asesores": {
        "title": "General  2",
        "sections": [
            {"layout": "banner", "image": pexels(6863183), "image_alt": "Documentos fiscales", "heading": "ASESORIA."},
            {"layout": "columns", "columns": [
            [
                ("h", 2, "LABORAL"),
                ("p", "Asesoramiento y Gestión Laboral integral de Empresas."),
                ("p", "Confección de Contratos, Nóminas y Seguros Sociales."),
                ("p", "Confecciones de Escritos y Recursos ante las diversas Administraciones."),
                ("p", "Representaciones:"),
                ("ul", [
                    "Ante la Inspección de trabajo",
                    "En conciliación ante el SMAC",
                    "Ante el Juzgado de lo Social",
                ]),
                ("p", "Tramitación de Subvenciones."),
                ("p", "Informes de costes salariales."),
            ],
            [
                ("h", 2, "FISCAL"),
                ("p", "Asesoramiento y Gestión Fiscal de Empresas."),
                ("p", "Planificación Fiscal."),
                ("p", "Inspecciones Fiscales."),
                ("p", "Recursos y Reclamaciones."),
                ("p", "Solicitud de Ingresos Indebidos."),
                ("p", "Fraccionamiento y aplazamiento de pagos."),
                ("p", "Procedimiento de apremio de deudas fiscal y de la Seguridad Social."),
            ],
            [
                ("h", 2, "CONTABLE"),
                ("p", "Asesoramiento y Gestión Contable de Empresas."),
                ("p", "Actualización de Contabilidades."),
                ("p", "Elaboración y legislación de los Libros Oficiales de Contabilidad."),
                ("p", "Depósito de Cuentas Anuales en el Registro mercantil."),
            ],
            ]},
        ],
    },

    "concursal": {
        "title": "General 3",
        "sections": [
            {"layout": "text", "blocks": [
                ("h", 2, "Concursal."),
                ("pendiente", "Concursal · párrafo 1"),
                ("pendiente", "Concursal · párrafo 2"),
                ("pendiente", "Concursal · párrafo 3"),
            ]},
            {"layout": "split", "image": pexels(4386339), "image_alt": "Calculadora y billetes", "blocks": [
                ("h", 3, "Como asesor del deudor."),
                ("ul", [
                    "Asesoramiento en la fase preconcursal para negociación con acreedores, refinanciación, reestructuración, etc….",
                    "Preparación y negociación del convenio anticipado con acreedores.",
                    "Negociación previa con las Administraciones Públicas.",
                    "Expedientes de regulación de empleo.",
                    "Dirección letrada del concursado en la fase común y liquidación",
                    "Impugnación de créditos.",
                    "Defensa de acciones rescisorias.",
                ]),
                ("h", 3, "Como asesor del acreedor."),
                ("ul", [
                    "Negociación del convenio anticipado con el deudor.",
                    "Comunicación y Defensa del crédito de los acreedores.",
                    "Ejecución de garantías reales.",
                    "Acciones de responsabilidad frente a los administradores societarios y concursales.",
                ]),
            ]},
        ],
    },

    "gestion-de-recobro": {
        "title": "Gestion de recobro",
        "sections": [
            {"layout": "banner", "image": pexels(3943716), "image_alt": "Monedas", "heading": "Gestion  de recobro."},
            {"layout": "text", "blocks": [
                ("pendiente", "Gestión de recobro · párrafo 1"),
                ("pendiente", "Gestión de recobro · párrafo 2"),
                ("pendiente", "Gestión de recobro · párrafo 3"),
                ("pendiente", "Gestión de recobro · párrafo 4"),
                ("p", "Tratamiento personalizado, exclusivo e individual a cada cliente."),
            ]},
            {"layout": "card", "image": pexels(7681091), "image_alt": "Firma de documentos", "blocks": [
                ("pendiente", "Gestión de recobro · párrafo introductorio del recuadro"),
                ("ul", [
                    "Asignamos interlocutores exclusivos “Urraca Asesores / Urraca Abogados - Cliente” para lograr una comunicación directa, cercana y eficaz entre las dos partes.",
                    "Exhaustiva evaluación del proyecto y personalización de las acciones.",
                    "Junto con el cliente, toma de decisiones y diseño de estrategia a seguir.",
                    "Asignación exclusiva al proyecto de medios técnicos y humanos en función del volumen de trabajo encomendado, garantizando siempre la respuesta óptima a sus necesidades.",
                    "Establecimiento, con acceso por parte del cliente, de sistemas de seguimiento y medición de los resultados que vayamos obteniendo.",
                ]),
                ("p", "Todos nuestros departamentos al servicio del cliente."),
                ("ul", [
                    "Departamento de Atención al Cliente. Atendido por gestores con alta cualificación en técnicas de recobro con presencia en todas las todas las sedes.",
                    "Departamento de Investigación y Localización. Se ocupa de los expedientes más complejos en los que no es posible localizar al deudor o se necesita buscar sus bienes.",
                    "Departamento Precontencioso. Ligado al departamento jurídico, asume los expedientes que requieren de cualquier acto judicial, previo a la vía judicial en sí: actos de conciliación o similares.",
                ]),
            ]},
        ],
    },

    "derecho-mercantil": {
        "title": "Derecho mercantil",
        "sections": [
            {"layout": "split", "image": pexels(5669602), "image_alt": "Balanza de la justicia", "blocks": [
                ("h", 2, "Derecho mercantil."),
                ("ul", [
                    "Constitución de Sociedades Mercantiles.",
                    "Negociación y formalización de pactos de accionistas.",
                    "Transformaciones de Sociedades Mercantiles.",
                    "Operaciones de Reestructuración Societaria (Fusiones y adquisiciones, escisiones).",
                    "Adquisición de sociedades y empresas, Due Dilligence.",
                    "Operaciones societarias en general (ampliación y disminución de capital, modificaciones estatutarias).",
                    "Asesoramiento a Consejos de Administración, llevanza de Secretarías del Consejo.",
                    "Preparación de Juntas Generales de Accionistas.",
                    "Impugnación de acuerdos sociales, ejercicio de la acción social de responsabilidad de administradores.",
                    "Redacción, negociación y conclusión de contratos de compraventa de acciones y participaciones sociales y de constitución de derechos reales sobre las mismas.",
                    "Procesos de liquidación de sociedades.",
                ]),
            ]},
        ],
    },

    "derecho-bancario": {
        "title": "Derecho bancario",
        "sections": [
            {"layout": "split", "image": pexels(6266283), "image_alt": "Billetes y calculadora", "blocks": [
                ("h", 2, "Derecho bancario."),
                ("pendiente", "Derecho bancario · párrafo 1"),
                ("pendiente", "Derecho bancario · párrafo 2"),
            ]},
        ],
    },

    "derecho-contractual": {
        "title": "Derecho contractual",
        "sections": [
            {"layout": "split", "image": pexels(5673488), "image_alt": "Apretón de manos", "blocks": [
                ("h", 2, "Derecho contractual."),
                ("ul", [
                    "Contratación Mercantil nacional e internacional.",
                    "Ejercicio de acciones judiciales.",
                    "Arbitrajes nacionales e internacionales.",
                ]),
            ]},
        ],
    },

    "derecho-civil": {
        "title": "Derecho civil",
        "sections": [
            {"layout": "banner", "image": pexels(8730047), "image_alt": "Familia", "heading": "Derecho civil."},
            {"layout": "columns", "columns": [
                [("ul", [
                    "Procesos civiles e hipotecarios, declarativos y ejecutivos.",
                    "Arrendamientos Urbanos y Propiedad Horizontal. Elaboración y negociación de contratos de arrendamiento de vivienda y locales de negocio; procedimientos verbales de arrendamientos urbanos, procedimientos de desahucio por precario.",
                    "Comunidad de propietarios. Reclamación judicial de las cuotas de propietarios morosos. Impugnación de los acuerdos adoptados en las juntas de comunidades de propietarios.",
                    "Resolución y rescisión contractual. Reclamaciones de cantidad.",
                    "Protección de los derechos fundamentales de la personas (infracción del derecho al honor, intimidad y propia imagen).",
                    "Derecho sucesorio (declaración de herederos ab intestato, adjudicación y partición del caudal hereditario, informes de testamentaría, impugnación de disposiciones testamentarias).",
                    "Derecho de familia (separación, divorcio, unión de hecho, filiación, liquidación del régimen económico matrimonial).",
                ])],
                [("ul", [
                    "Procedimientos judiciales contenciosos y de mutuo acuerdo.",
                    "Procedimiento judicial de modificación de medinas definitivas.",
                    "Ejecución de resoluciones judiciales, sentencias y laudos arbitrales nacionales y extranjeros",
                    "Condiciones generales de la contratación civil.",
                    "Acciones de responsabilidad contractual y extracontractual.",
                    "Derechos de propiedad intelectual.",
                    "Derecho audiovisual.",
                    "Nuevas tecnologías.",
                    "Contratación relacionada con los derechos de propiedad intelectual.",
                    "Defensa jurídica en procedimientos por infracción de los Derechos de propiedad intelectual.",
                    "Protección de datos personales.",
                    "Defensa jurídica ante resoluciones del Registro civil.",
                    "Expedientes de dominio.",
                    "Redacción de minutas notariales.",
                ])],
            ]},
        ],
    },

    "derecho-penal": {
        "title": "Derecho penal",
        "sections": [
            {"layout": "split", "image": pexels(5668473), "image_alt": "Mazo de juez", "blocks": [
                ("h", 2, "Derecho penal."),
                ("p", "Urraca Asesores / Urraca Abogados cuenta con gran experiencia en Derecho Penal."),
                ("pendiente", "Derecho penal · párrafo 2"),
                ("ul", [
                    "Delitos económicos (infracciones penales en el ámbito bancario, robos, apropiaciones indebidas, insolvencias punibles o estafas).",
                    "Delitos contra la Hacienda Pública y contra la Seguridad Social u otras instituciones de carácter público.",
                    "Delitos societarios (administración fraudulenta, adopción de acuerdos abusivos, e infracción de los derechos políticos de los socios).",
                    "Blanqueo de capitales.",
                    "Delitos contra la propiedad industrial o intelectual (derechos de autor, marca, patentes, etc.).",
                    "Delitos contra el honor, la intimidad y el derecho a la propia imagen.",
                    "Delitos informáticos.",
                ]),
                ("pendiente", "Derecho penal · párrafo 3"),
                ("pendiente", "Derecho penal · párrafo 4"),
            ]},
        ],
    },

    "derecho-procesal": {
        "title": "Derecho procesal",
        "sections": [
            {"layout": "split", "image": pexels(8112199), "image_alt": "Estatua de la justicia", "image_first": True, "blocks": [
                ("h", 3, "Derecho procesal."),
                ("pendiente", "Derecho procesal · párrafo 1"),
                ("pendiente", "Derecho procesal · párrafo 2"),
                ("pendiente", "Derecho procesal · párrafo 3"),
                ("pendiente", "Derecho procesal · párrafo 4"),
                ("pendiente", "Derecho procesal · párrafo 5"),
                ("p", "Nuestros profesionales en derecho procesal le asesorarán en todo tipo de asuntos, especialmente los relacionados con:"),
                ("ul", [
                    "Arbitraje ante Tribunales arbitrales nacionales e internacionales.",
                    "Mediación.",
                    "Acciones de responsabilidad civil.",
                    "Conflictos societarios.",
                    "Responsabilidad de administradores.",
                    "Ejecuciones de títulos judiciales y no judiciales de procedencia nacional e internacional.",
                    "Resolución de Contratos civiles y mercantiles.",
                    "Reclamación de cumplimiento de las obligaciones derivadas de cualquier tipo de contrato.",
                    "Procesos familiares y sucesorios.",
                    "Reclamación de todo tipo de deudas.",
                ]),
            ]},
        ],
    },

    "derecho-inmobiliario": {
        "title": "Derecho inmobiliario",
        "sections": [
            {"layout": "split", "image": pexels(106399), "image_alt": "Vivienda", "image_first": True, "blocks": [
                ("h", 3, "Derecho inmobiliario."),
                ("pendiente", "Derecho inmobiliario · párrafo 1"),
                ("pendiente", "Derecho inmobiliario · párrafo 2"),
                ("ul", [
                    "Promoción inmobiliaria.",
                    "Compraventa de suelo. Opción de compra.",
                    "Servidumbres y derechos reales.",
                    "Permutas de suelo y edificabilidad.",
                    "Redacción y negociación de Contratos.",
                    "Contratos de Promoción, Construcción y Técnicos.",
                    "Promoción delegada, Project management y, en general, contratos vinculados a la promoción inmobiliaria.",
                    "Contratos de obra, llave en mano.",
                    "Contratos con arquitectos, ingenieros y otros agentes que intervienen en el proceso constructivo.",
                    "Elaboración de dictámenes jurídicos.",
                    "Contratos de arrendamiento. Desde la negociación de toda clase de contratos, de todo tipo de inmuebles y locales comerciales (en especial locales comerciales en centros comerciales), pasando por cualquier incidencia durante la vida de los mismos.",
                    "Comunidades de Propietarios y divisiones horizontales.",
                    "Asesoramiento a ciudadanos extranjeros en la adquisición de propiedades en España.",
                    "Derecho de la edificación. Vicios de la construcción y responsabilidad de los agentes de la edificación. Indemnizaciones extracontractuales referidas al derecho de la construcción. Licencias de primera ocupación.",
                ]),
            ]},
        ],
    },

    "derecho-urbanistico": {
        "title": "Derecho urbanistico",
        "sections": [
            {"layout": "split", "image": pexels(2219024), "image_alt": "Obra en construcción", "blocks": [
                ("h", 2, "Derecho urbanistico."),
                ("pendiente", "Derecho urbanístico · párrafo 1"),
                ("p", "Nuestros servicios en este ámbito nos permiten ofrecerle asesoramiento jurídico en:"),
                ("ul", [
                    "Licencias y contratos urbanísticos.",
                    "Negociaciones con la Administración y convenios urbanísticos.",
                    "Estudio del planeamiento en vigor.",
                    "Asistencia jurídica a entidades urbanísticas y urbanizadoras.",
                    "Defensa en procedimientos administrativos y jurisdiccionales.",
                ]),
            ]},
        ],
    },

    "derecho-laboral": {
        "title": "Derecho laboral",
        "sections": [
            {"layout": "text", "blocks": [
                ("h", 2, "Derecho laboral."),
                ("pendiente", "Derecho laboral · párrafo 1"),
                ("pendiente", "Derecho laboral · párrafo 2"),
                ("pendiente", "Derecho laboral · párrafo 3"),
            ]},
            {"layout": "columns", "columns": [
                [("ul", [
                    "Despidos individuales.",
                    "Expedientes de Regulación de Empleo.",
                    "Expedientes de Regulación Temporal de Empleo.",
                    "Memoria para desarrollar los criterios de selección dentro de un Expediente de Regulación de Empleo.",
                    "Modificaciones sustanciales de condiciones laborales de los trabajadores.",
                    "Asesoramiento a representantes legales de los trabajadores: Comités de Empresa o Comisiones Negociadoras.",
                    "Subcontratación en el ámbito laboral. Cesión ilegal de trabajadores y el delito social.",
                    "Contratación laboral en general.",
                    "Recursos Humanos.",
                    "Sistemas retributivos.",
                    "Negociación, planificación y redacción de contratos de trabajo y convenios colectivos.",
                    "Procedimientos sancionatorios.",
                    "Reclamaciones de cantidad y derechos.",
                    "Actuaciones ante la jurisdicción social en todas sus instancias.",
                ])],
                [("ul", [
                    "Tramitación de incapacidades ante el INSS.",
                    "Reclamaciones ante la Tesorería General de la Seguridad Social.",
                    "Trámites relacionados con las Administraciones Generales del Estado, autonómicas y locales.",
                    "Directivos de empresa. Alta Dirección. Contratos, cláusulas, blindajes, competencia, estructura societaria, ceses y despidos de altos directivos.",
                    "Asesoramiento en el día a día empresarial.",
                    "Inspecciones de trabajo.",
                    "Arbitraje, mediación y conciliación.",
                    "Redacción de toda la documentación necesaria para cualquier trámite laboral: demandas, reclamaciones, alegaciones, asistencia a juicios, preparación de documentación para asistencia a juicios, recursos en primera, segunda y tercera instancia procesal.",
                    "Elaboración de planes de reestructuración laboral o contractual de los trabajadores dentro de las empresas.",
                    "Conflictos colectivos.",
                    "Acoso laboral.",
                    "Planes y Fondos de Pensiones.",
                    "Permisos y excedencias.",
                ])],
            ]},
        ],
    },

    "derecho-de-familia": {
        "title": "Derecho de familia",
        "sections": [
            {"layout": "text", "blocks": [("h", 3, "Derecho de familia.")]},
            {"layout": "split", "image": pexels(1648387), "image_alt": "Familia", "image_first": True, "blocks": [
                ("ul", [
                    "Separación, Divorcio y Nulidad Civil.",
                    "Nulidad Eclesiástica.",
                    "Uniones de hecho.",
                    "Custodia compartida.",
                    "Regímenes Económico – Matrimoniales y Acuerdos Prematrimoniales.",
                    "Testamentos y procedimientos sucesorios.",
                    "Filiación, Adopción, Emancipación y Patria Potestad.",
                    "Derecho del Menor, Síndrome de alienación parental.",
                    "Incapacidades, Tutelas y Patrimonio Protegido.",
                    "Derecho Internacional.",
                    "Sustracción Internacional de Menores.",
                    "Otras materias de Derecho de Familia.",
                ]),
            ]},
        ],
    },

    "aviso-legal": {
        "title": "Aviso legal",
        "sections": [
            {"layout": "text", "blocks": [
                ("h", 2, "Aviso legal."),
                ("h", 4, "1. Datos Legales"),
                ("p", "Nombre: Urraca Asesores, SL."),
                ("p", "Domicilio Social: C/ Mayor Principal 15, 2D. 34001 PALENCIA"),
                ("p", "Inscripción en el Registro Mercantil de Palencia"),
                ("p", "CIF: B-34215699"),
                ("p", "Teléfono: 979 74 43 58"),
                ("p", "e-mail: info@urracaasesores.com"),
                ("h", 4, "2. Aceptación"),
                ("pendiente", "Aviso legal · apartado 2"),
                ("h", 4, "3. Condiciones de uso"),
                ("pendiente", "Aviso legal · apartado 3"),
                ("h", 4, "4. Limitación de responsabilidad"),
                ("pendiente", "Aviso legal · apartado 4"),
                ("h", 4, "5. Propiedad intelectual e industrial"),
                ("pendiente", "Aviso legal · apartado 5"),
                ("h", 4, "6. Contenidos"),
                ("pendiente", "Aviso legal · apartado 6"),
                ("h", 4, "7. Introducción de enlaces al Sitio web"),
                ("pendiente", "Aviso legal · apartado 7"),
                ("h", 4, "8. Exclusión de responsabilidad"),
                ("p", "a) De la Información"),
                ("pendiente", "Aviso legal · apartado 8 a)"),
                ("p", "b) De la calidad del servicio"),
                ("pendiente", "Aviso legal · apartado 8 b)"),
                ("p", "c) De la disponibilidad del Servicio"),
                ("pendiente", "Aviso legal · apartado 8 c)"),
                ("p", "d) De los contenidos y servicios enlazados a través del Sitio web"),
                ("pendiente", "Aviso legal · apartado 8 d)"),
                ("h", 4, "9. Protección de datos personales"),
                ("pendiente", "Aviso legal · apartado 9"),
                ("h", 4, "10. Comunicación de actividades de carácter ilícito e inadecuado"),
                ("pendiente", "Aviso legal · apartado 10"),
                ("h", 4, "11. Legislación"),
                ("p", "El presente Aviso Legal se rige en todos y cada uno de sus extremos por la ley española."),
            ]},
        ],
    },
}

# "urraca-abogados-1" es, en la web original, una copia de "concursal".
PAGES["urraca-abogados-1"] = PAGES["concursal"]
