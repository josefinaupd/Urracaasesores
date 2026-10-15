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
        "title": "Urraca Asesores",
        "sections": [
            {"layout": "banner", "image": pexels(6863279), "image_alt": "Impresos fiscales, calculadora y lápices", "heading": "ASESORIA."},
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
        "title": "Concursal",
        "sections": [
            {"layout": "text", "blocks": [
                ("h", 2, "Concursal."),
                ("p", "Urraca Asesores / Urraca Abogados es un despacho de abogados experto en derecho concursal, atesorando una gran experiencia en el asesoramiento a todos los sujetos que se pueden ver envueltos en una situación de concurso de acreedores, ya sea como acreedores o deudores."),
                ("p", "Nuestro equipo multidisciplinar puede asesorar, tanto en las actuaciones que se dan en las fases previas al concurso, como en las que se originan en el propio seno concursal."),
                ("p", "La experiencia contrastada de Urraca Asesores / Urraca Abogados ante un procedimiento concursal y en el asesoramiento a clientes en los diversos sectores empresariales, nos permite abordar estas cuestiones tan delicadas, con naturalidad y desenvolvimiento."),
            ]},
            {"layout": "split", "image": pexels(3943746), "image_alt": "Manos intercambiando billetes de euro", "blocks": [
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
            {"layout": "banner", "image": pexels(16399858), "image_alt": "Monedas de euro sobre fondo negro", "heading": "Gestion  de recobro."},
            {"layout": "text", "blocks": [
                ("p", "La reclamación de deuda procedente de facturas impagadas es la principal actividad de nuestro departamento de Gestión y Recobro. Hoy en día, la gestión de recobro de impagados para reducir el porcentaje de morosidad, se sitúa como una de las principales preocupaciones de las empresas."),
                ("p", "En este sentido, para afrontar con éxito la morosidad, Urraca Asesores / Urraca Abogados cuenta con una extraordinaria estructura organizativa y un amplio equipo especializados en la gestión de recobros, tanto por vía judicial como por vía extrajudicial."),
                ("p", "El equipo de gestión de recobros de Urraca Asesores / Urraca Abogados tiene una dilatada y contrastada experiencia en reclamación de deuda, con todo tipo de clientes y elevados porcentajes de recuperación en todos los casos, por lo que puede hacer frente a las necesidades de cualquier cliente, independientemente del tipo de deuda y del importe que pudiera ser asignado."),
                ("p", "Dentro de un marco de transparencia y respeto, para no dañar nunca la imagen del cliente, nuestro equipo procede a la reclamación de deuda, poniendo en marcha las respuestas adaptadas en adecuación a las necesidades de los clientes."),
                ("p", "Tratamiento personalizado, exclusivo e individual a cada cliente."),
            ]},
            {"layout": "card", "image": pexels(8730987), "image_alt": "Firma de un documento con pluma", "blocks": [
                ("p", "Realizamos nuestros trabajo ofreciendo un tratamiento personalizado, exclusivo e individual a cada cliente, desde el primer día e independientemente del volumen de trabajo encomendado. Estudiamos su caso y le ofrecemos la mejor de las soluciones."),
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
            {"layout": "split", "image": pexels(5669602), "image_alt": "Balanza de la justicia y mazo", "blocks": [
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
            {"layout": "split", "image": pexels(16584983), "image_alt": "Fachada del Banco de España", "blocks": [
                ("h", 2, "Derecho bancario."),
                ("p", "Asesoramiento y planificación en los aspectos legales en operaciones de las entidades financieras. Informes de bastanteos (documentación nacional y extranjera)."),
                ("p", "Supervisión de operaciones de préstamo y de crédito, de préstamos sindicados y en la constitución y ejecución de todo tipo de garantías financieras: garantías a primer requerimiento, fianzas, prendas sobre acciones y otros bienes muebles, hipotecas mobiliarias e inmobiliarias."),
            ]},
        ],
    },

    "derecho-contractual": {
        "title": "Derecho contractual",
        "sections": [
            {"layout": "split", "image": pexels(8069428), "image_alt": "Apretón de manos", "blocks": [
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
            {"layout": "banner", "image": pexels(3450124), "image_alt": "Pareja mayor paseando por una calle", "heading": "Derecho civil."},
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
            {"layout": "split", "image": pexels(3747555), "image_alt": "Libros de derecho", "blocks": [
                ("h", 2, "Derecho penal."),
                ("p", "Urraca Asesores / Urraca Abogados cuenta con gran experiencia en Derecho Penal."),
                ("p", "El profesional de Urraca Asesores / Urraca Abogados (abogado penal) asesora y actúa en todo tipo de procesos relacionados con el derecho penal, en especial:"),
                ("ul", [
                    "Delitos económicos (infracciones penales en el ámbito bancario, robos, apropiaciones indebidas, insolvencias punibles o estafas).",
                    "Delitos contra la Hacienda Pública y contra la Seguridad Social u otras instituciones de carácter público.",
                    "Delitos societarios (administración fraudulenta, adopción de acuerdos abusivos, e infracción de los derechos políticos de los socios).",
                    "Blanqueo de capitales.",
                    "Delitos contra la propiedad industrial o intelectual (derechos de autor, marca, patentes, etc.).",
                    "Delitos contra el honor, la intimidad y el derecho a la propia imagen.",
                    "Delitos informáticos.",
                ]),
                ("p", "Con la reciente reforma del Código Penal en materia de responsabilidad penal de las personas jurídicas se han planteado innumerables dudas acerca de las consecuencias que tal modificación supondrá para los órganos de gobierno de las compañías mercantiles y, en definitiva para las propias entidades."),
                ("p", "Los profesionales que integran el área de Derecho Penal económico poseen un alto grado de “expertise” en la práctica forense en Juzgados y Tribunales, lo que les convierte en los mejores asesores a la hora de dimensionar y de anticiparse a los riesgos que supone semejante cambio legislativo, y para ofrecer soluciones prácticas y resolutivas cuando estos riesgos finalmente se han materializado en la imputación de la persona jurídica."),
            ]},
        ],
    },

    "derecho-procesal": {
        "title": "Derecho procesal",
        "sections": [
            {"layout": "split", "image": pexels(5668473), "image_alt": "Mazo de juez", "image_first": True, "blocks": [
                ("h", 3, "Derecho procesal."),
                ("p", "Nuestro equipo de Derecho Procesal y Arbitraje asesora en diversas materias, tanto a sociedades como a particulares, entre las que destacan por su relevancia, las de naturaleza civil y mercantil."),
                ("p", "Conformado por un equipo de dilatada experiencia profesional en derecho procesal, permite tener una visión global del problema, no ya sólo desde el punto de vista técnico formal, sino desde el sustantivo material de la problemática en cuestión, lo que ayuda a la comunicación y entendimiento con el cliente."),
                ("p", "En Urraca Asesores / Urraca Abogados existen una serie de departamentos que merecen especial atención por el trabajo en materia procesal que desarrollan, como el de reclamación de créditos pecuniarios y no pecuniarios, derivados del incumplimiento de todo tipo de contratos, civiles, mercantiles y administrativos, con una experiencia de más de veinticinco años en la materia, en la que se ha asesorado a grandes y pequeñas empresas y a particulares."),
                ("p", "Asimismo, el departamento de Derecho de Familia, intentando siempre buscar la solución más favorable, pero sobre todo la menos traumática para los cónyuges y la más beneficiosa para los menores."),
                ("p", "El equipo especializado en Derecho de la Edificación que atiende cualquier problema derivado de los vicios constructivos, responsabilidad de los agentes de la construcción y su correspondiente reclamación en los Juzgados, auxiliados por los mejores peritos en la materia."),
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
            {"layout": "split", "image": pexels(35417681), "image_alt": "Calle con edificios de viviendas", "image_first": True, "blocks": [
                ("h", 3, "Derecho inmobiliario."),
                ("p", "Los especialistas de Urraca Asesores / Urraca Abogados prestan asesoramiento de calidad a nuestros clientes en materia de derecho inmobiliario, ya sean administraciones públicas o empresas privadas.Asesoramos a promotores, constructores, administradores de fincas,… Nos encargamos de todos los asuntos referentes, en materia legal, a la compraventa de inmuebles de todo tipo, a los contratos de arrendamiento, promoción, construcción y técnicos."),
                ("p", "Nuestro equipo de abogados presta asistencia letrada en distintas áreas del derecho inmobiliario asesorando en todos los aspectos relacionados con la propiedad inmobiliaria, promoción, construcción, inversión, fiscalidad, financiación y arrendamiento de todo tipo de inmuebles en sus distintas fases:"),
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
            {"layout": "split", "image": pexels(5505125), "image_alt": "Grúa en una obra", "blocks": [
                ("h", 2, "Derecho urbanistico."),
                ("p", "Prestamos asesoramiento a empresas privadas y particulares en todos los aspectos derivados de los procesos urbanísticos, tanto administrativos como civiles, fiscales y registrales."),
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
            {"layout": "banner", "image": pexels(3183150), "image_alt": "Equipo de trabajo en una reunión", "heading": "Derecho laboral."},
            {"layout": "text", "blocks": [
                ("p", "Urraca Asesores / Urraca Abogados cuenta con un equipo de especialistas en derecho laboral que da cobertura a todos y cada uno de los aspectos de esta área de práctica, ofreciendo asesoramiento ante todas aquellas controversias que puedan surgir en materia de derecho laboral."),
                ("p", "Nuestro despacho de abogados presta servicios jurídicos a diferentes colectivos, ya sean empresas privadas, públicas o trabajadores particulares, teniendo en la actualidad decenas de clientes que son asesorados por Urraca Asesores / Urraca Abogados en toda España."),
                ("p", "El derecho laboral abarca todo lo relacionado con el derecho del trabajo o el derecho social. En este sentido acumulamos muchos años de experiencia en la tramitación de asuntos y asistencia legal en materias concretas como:"),
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
            {"layout": "split", "image": pexels(3617568), "image_alt": "Fotografías familiares antiguas", "image_first": True, "blocks": [
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
                ("p", "La utilización de este sitio web está sujeta a las siguientes condiciones de uso. Le rogamos que las lea atentamente. El hecho de acceder a este sitio web y utilizar los materiales contenidos en ella implica que usted ha leído y acepta, sin reserva alguna, estas condiciones."),
                ("h", 4, "3. Condiciones de uso"),
                ("p", "Este sitio web contiene materiales preparados por Urraca Asesores / Urraca Abogados con fines únicamente informativos. El usuario debe tener en cuenta que tales materiales pudieran no reflejar el estado legislativo o jurisprudencial más reciente sobre las cuestiones analizadas. Asimismo, estos materiales pueden ser modificados, desarrollados o actualizados sin notificación previa."),
                ("p", "Los materiales contenidos en este sitio web no pueden ser considerados, en ningún caso, como sustitutivos de asesoramiento legal o de otra naturaleza. El acceso a estos materiales no pretende constituir ni implica relación alguna entre asesor / abogado y cliente, ni cualquier otro tipo de relación de confianza o profesional entre Urraca Asesores / Urraca Abogados y el usuario de este sitio web. Por ello, el usuario no debe actuar sobre la base de la información contenida en la misma, sin recurrir previamente al correspondiente asesoramiento profesional. Asimismo, el usuario no debe enviar a Urraca Asesores / Urraca Abogados ningún tipo de información confidencial sin haberlo consultado previamente con alguno de nuestros asesores / abogados y haber recibido de los mismos autorización para remitir dicha información. Los enlaces o links que contiene este sitio web pueden conducir al usuario a otros sitios y páginas web gestionados por terceros, sobre las que Urraca Asesores / Urraca Abogados no ejerce ningún tipo de control. Urraca Asesores / Urraca Abogados no responde ni de los contenidos ni del estado de dichos sitios y páginas web, y el acceso a las mismas a través de este sitio web tampoco implica que Urraca Asesores / Urraca Abogados recomiende o apruebe sus contenidos."),
                ("h", 4, "4. Limitación de responsabilidad"),
                ("p", "Quien utiliza este sitio web, lo hace por su propia cuenta y riesgo. Urraca Asesores / Urraca Abogados, sus socios, colaboradores, empleados y representantes no se responsabilizan de los errores u omisiones de los que pudieran adolecer los contenidos este sitio web u otros contenidos a los que se pueda acceder a través de la misma. Urraca Asesores / Urraca Abogados, sus socios, colaboradores, empleados y representantes tampoco podrán ser considerados responsables por cualesquiera daños derivados de la utilización de este sitio web, ni por cualquier actuación realizada sobre la base de la información que en ella se facilita. Urraca Asesores / Urraca Abogados no garantiza la ausencia de virus u otros elementos lesivos que pudieran causar daños o alteraciones en el sistema informático, en los documentos electrónicos o en los ficheros del usuario de este sitio web. En consecuencia, Urraca Asesores / Urraca Abogados no responde por los daños y perjuicios que tales elementos pudieran ocasionar al usuario o a terceros."),
                ("h", 4, "5. Propiedad intelectual e industrial"),
                ("p", "Todos los contenidos del Sitio web, entendiendo por estos a título meramente enunciativo los textos, fotografías, gráficos, imágenes, iconos, tecnología, software, links y demás contenidos audiovisuales o sonoros, así como su diseño gráfico y códigos fuente (en adelante, los 'Contenidos'), son propiedad intelectual de Urraca Asesores / Urraca Abogados o de terceros, sin que puedan entenderse cedidos al Usuario ninguno de los derechos de explotación sobre los mismos más allá de lo estrictamente necesario para el correcto uso del Sitio web."),
                ("p", "Las marcas, nombres comerciales o signos distintivos son titularidad de Urraca Asesores / Urraca Abogados o terceros, sin que pueda entenderse que el acceso al Sitio web atribuya ningún derecho sobre las citadas marcas, nombres comerciales y/o signos distintivos."),
                ("p", "El Usuario se obliga a hacer un uso correcto del Sitio web de conformidad con la Ley y el presente Aviso Legal. El Usuario responderá frente a Urraca Asesores / Urraca Abogados o frente a terceros, de cualesquiera daños y perjuicios que pudieran causarse como consecuencia del incumplimiento de dicha obligación."),
                ("p", "Queda expresamente prohibido el uso del Sitio web con fines lesivos de bienes o intereses de Urraca Asesores / Urraca Abogados o de terceros o que de cualquier otra forma sobrecarguen, dañen o inutilicen las redes, servidores y demás equipos informáticos (hardware) o productos y aplicaciones informáticas (software) de Urraca Asesores / Urraca Abogados o de terceros."),
                ("h", 4, "6. Contenidos"),
                ("p", "El Usuario se compromete a utilizar los Contenidos de conformidad con la Ley y el presente Aviso Legal, así como con las demás condiciones, reglamentos e instrucciones que en su caso pudieran ser de aplicación de conformidad con lo dispuesto las presentes condiciones de uso con carácter meramente enunciativo, el Usuario de acuerdo con la legislación vigente deberá abstenerse de:"),
                ("ul", [
                    "Reproducir, copiar, distribuir, poner a disposición, comunicar públicamente, transformar o modificar los Contenidos salvo en los casos autorizados en la ley o expresamente consentidos por Urraca Asesores / Urraca Abogados o por quien ostente la titularidad de los derechos de explotación en su caso. Reproducir o copiar para uso privado los Contenidos que puedan ser considerados como Software o Base de Datos de conformidad con la legislación vigente en materia de propiedad intelectual, así como su comunicación pública o puesta a disposición de terceros cuando estos actos impliquen necesariamente la reproducción por parte del Usuario o de un tercero.",
                    "Extraer y/o reutilizar la totalidad o una parte sustancial de los Contenidos integrantes del Sitio web así como de las bases de datos que Urraca Asesores / Urraca Abogados ponga a disposición de los Usuarios.",
                ]),
                ("h", 4, "7. Introducción de enlaces al Sitio web"),
                ("p", "El Usuario se compromete a utilizar los Contenidos de conformidad con la Ley y el presente Aviso Legal, así como con las demás condiciones, reglamentos e instrucciones que en su caso pudieran ser de aplicación de conformidad con lo dispuesto las presentes condiciones de uso con carácter meramente enunciativo, el Usuario de acuerdo con la legislación vigente deberá abstenerse de:"),
                ("ul", [
                    "El enlace únicamente vinculará con la home page o página principal del Sitio web pero no podrá reproducirla de ninguna forma (inline links, copia de los textos, gráficos, etc.).",
                    "Quedará en todo caso prohibido, de acuerdo con la legislación aplicable y vigente en cada momento, establecer frames o marcos de cualquier tipo que envuelvan al Sitio web o permitan la visualización de los Contenidos a través de direcciones de Internet distintas a las del Sitio web y, en cualquier caso, cuando se visualicen conjuntamente con contenidos ajenos al Sitio web de forma que: (I) produzca, o pueda producir, error, confusión o engaño en los usuarios sobre la verdadera procedencia del servicio o Contenidos; (II) suponga un acto de comparación o imitación desleal; (III) sirva para aprovechar la reputación de la marca y prestigio de Urraca Asesores / Urraca Abogados; o (IV) de cualquier otra forma resulte prohibido por la legislación vigente.",
                    "No se realizarán desde la página que introduce el enlace ningún tipo de manifestación falsa, inexacta o incorrecta sobre Urraca Asesores / Urraca Abogados, sus socios, empleados, clientes o sobre la calidad de los servicios que presta.",
                    "Está prohibida la utilización de cualquier marca denominativa, gráfica o mixta o cualquier otro signo distintivo de Urraca Asesores / Urraca Abogados dentro de la página del remitente salvo en los casos permitidos por la ley o expresamente autorizados por Urraca Asesores / Urraca Abogados y siempre que se permita, en estos casos, un enlace directo con el Sitio web en la forma establecida en esta cláusula.",
                    "La página que establezca el enlace deberá cumplir fielmente con la ley y no podrá en ningún caso disponer o enlazar con contenidos propios o de terceros que: (I) sean ilícitos, nocivos o contrarios a la moral y a las buenas costumbres (pornográficos, violentos, racistas, etc.); (II) induzcan o puedan inducir en el Usuario la falsa concepción de que Urraca Asesores / Urraca Abogados suscribe, respalda, se adhiere o de cualquier manera apoya, las ideas, manifestaciones o expresiones, lícitas o ilícitas, del remitente; (III) resulten inapropiados o no pertinentes con la actividad de Urraca Asesores / Urraca Abogados en atención al lugar, contenidos y temática de la página web del remitente.",
                ]),
                ("h", 4, "8. Exclusión de responsabilidad"),
                ("p", "a) De la Información"),
                ("p", "El acceso al Sitio web no implica la obligación por parte de Urraca Asesores / Urraca Abogados de comprobar la veracidad, exactitud, adecuación, idoneidad, exhaustividad y actualidad de la información suministrada a través del mismo. Los contenidos de esta página son de carácter general y no constituyen, en modo alguno, la prestación de un servicio de asesoramiento legal o fiscal de ningún tipo, por lo que dicha información resulta insuficiente para la toma de decisiones personales o empresariales por parte del Usuario."),
                ("p", "Urraca Asesores / Urraca Abogados no se responsabiliza de los daños producidos en los equipos informáticos de los Usuarios o de terceros durante la prestación del servicio del Sitio web."),
                ("p", "b) De la calidad del servicio"),
                ("p", "El acceso al Sitio web requiere de servicios y suministros de terceros, incluidos el transporte a través de redes de telecomunicaciones cuya fiabilidad, calidad, continuidad y funcionamiento no corresponde a Urraca Asesores / Urraca Abogados. Por consiguiente, los servicios provistos a través del Sitio web pueden ser suspendidos, cancelados o resultar inaccesibles, con carácter previo o simultáneo a la prestación del servicio del Sitio web."),
                ("p", "c) De la disponibilidad del Servicio"),
                ("p", "El acceso al Sitio web requiere de servicios y suministros de terceros, incluidos el transporte a través de redes de telecomunicaciones cuya fiabilidad, calidad, continuidad y funcionamiento no corresponde a Urraca Asesores / Urraca Abogados. Por consiguiente, los servicios provistos a través del Sitio web pueden ser suspendidos, cancelados o resultar inaccesibles, con carácter previo o simultáneo a la prestación del servicio del Sitio web."),
                ("p", "Urraca Asesores / Urraca Abogados no se responsabiliza de los daños o perjuicios de cualquier tipo producidos en el Usuario que traigan causa de fallos o desconexiones en las redes de telecomunicaciones que produzcan la suspensión, cancelación o interrupción del servicio del Sitio web durante la prestación del mismo o con carácter previo."),
                ("p", "d) De los contenidos y servicios enlazados a través del Sitio web"),
                ("p", "El servicio de acceso al Sitio web incluye dispositivos técnicos de enlace que permiten al Usuario acceder a otras páginas y sitio webs de Internet (en adelante, 'Sitios Enlazados'). En estos casos, Urraca Asesores / Urraca Abogados actúa como prestador de servicios de intermediación de conformidad con el artículo 17 de la Ley 32/2002, de 12 de julio, de Servicios de la Sociedad de la Información y el Comercio Electrónico (LSSI) y sólo será responsable de los contenidos y servicios suministrados en los Sitios Enlazados en la medida en que tenga conocimiento efectivo de la ilicitud y no haya desactivado el enlace con la diligencia debida. En el supuesto de que el Usuario considere que existe un Sitio Enlazado con contenidos ilícitos o inadecuados podrá comunicárselo a Urraca Asesores / Urraca Abogados de acuerdo con el procedimiento y los efectos establecidos en la cláusula 6, sin que en ningún caso esta comunicación conlleve la obligación de retirar el correspondiente enlace."),
                ("p", "En ningún caso, la existencia de Sitios Enlazados debe presuponer la existencia de acuerdos con los responsables o titulares de los mismos, ni la recomendación, promoción o identificación de Urraca Asesores / Urraca Abogados con las manifestaciones, contenidos o servicios provistas."),
                ("p", "Urraca Asesores / Urraca Abogados no conoce los contenidos y servicios de los Sitios Enlazados y por tanto no se hace responsable por los daños producidos por la ilicitud, calidad, desactualización, indisponibilidad, error e inutilidad de los contenidos y/o servicios de los Sitios Enlazados ni por cualquier otro daño que no sea directamente imputable a Urraca Asesores / Urraca Abogados."),
                ("h", 4, "9. Protección de datos personales"),
                ("p", "Los datos que pudieran ser recabados a través de esta web serán incorporados a un fichero automatizado de datos de carácter personal del que es responsable Urraca Asesores / Urraca Abogados. Esta entidad tratará los datos de forma confidencial y exclusivamente con la finalidad de gestionar la relación con sus clientes y promocionar las actividades del Despacho. Asimismo, Urraca Asesores / Urraca Abogados cancelará, borrará y/o bloqueará los datos cuando resulten inexactos, incompletos o hayan dejado de ser necesarios o pertinentes para su finalidad, de conformidad con lo previsto en la legislación en materia de protección de datos."),
                ("p", "Al introducir los datos en el correspondiente formulario, el Usuario consiente de forma expresa que sus datos podrán ser utilizados para el envío de comunicaciones comerciales por correo electrónico o por cualquier otro medio."),
                ("p", "El Usuario podrá revocar el consentimiento prestado y ejercer los derechos de acceso, rectificación, cancelación y oposición dirigiéndose a tal efecto a la dirección señalada en la cláusula 1 e indicando de forma visible el concreto derecho que se ejerce."),
                ("p", "Urraca Asesores / Urraca Abogados adopta los niveles de seguridad requeridos en el Real Decreto 1720/2007 de 21 de diciembre. No obstante lo anterior, la seguridad técnica en un medio como Internet no es inexpugnable y pueden existir filtraciones por actuaciones dolosas de terceros."),
                ("p", "Urraca Asesores / Urraca Abogados podrá utilizar cookies durante la prestación del servicio del Sitio web. Las cookies son procedimientos automáticos de recogida de información relativa a las preferencias determinadas por un usuario durante su visita a una determinada página web. Esta información se registra en pequeños archivos que son guardados en los equipos informáticos del usuario correspondiente de forma imperceptible. Cada vez que el usuario vuelve a acceder al sitio web en cuestión estos archivos se activan automáticamente de manera que se configura el sitio web con las preferencias señaladas en anteriores visitas. En definitiva, las cookies son ficheros físicos de información personal alojados en el propio terminal del usuario y asociados inequívocamente a este terminal. Las cookies no pueden leer los archivos cookie creados por otros proveedores."),
                ("p", "El Usuario tiene la posibilidad de configurar su programa navegador de manera que se impida la creación de archivos cookie o se advierta del momento en que esto ocurre. El Sitio web es accesible sin necesidad de que estén activadas las opciones referentes a los archivos cookie, si bien pueden impedir el correcto funcionamiento de mecanismos de seguridad para servicios exclusivos o determinados servicios que requieren de una mayor seguridad. Por norma general, la finalidad de los archivos cookie del Sitio web es la de facilitar la navegación del Usuario."),
                ("h", 4, "10. Comunicación de actividades de carácter ilícito e inadecuado"),
                ("p", "En el caso de que el Usuario o cualquier otro usuario de Internet tuviera conocimiento de que los Sitios Enlazados remiten a páginas cuyos contenidos o servicios son ilícitos, nocivos, denigrantes, violentos o contrarios a la moral podrá ponerse en contacto con Urraca Asesores / Urraca Abogados indicando los siguientes extremos:"),
                ("p", "Datos personales del comunicante: nombre, dirección, número de teléfono y dirección de correo electrónico"),
                ("p", "Descripción de los hechos que revelan el carácter ilícito o inadecuado del Sitio Enlazado"),
                ("p", "En el supuesto de violación de derechos, tales como propiedad intelectual e industrial, los datos personales del titular del derecho infringido cuando sea persona distinta del comunicante. Asimismo deberá aportar el título que acredite la legitimación del titular de los derechos y, en su caso, el de representación para actuar por cuenta del titular cuando sea persona distinta del comunicante, y declaración expresa de que la información contenida en la reclamación es exacta."),
                ("p", "La recepción por parte de Urraca Asesores / Urraca Abogados de la comunicación prevista en esta cláusula no supondrá, según lo dispuesto en la LSSI, el conocimiento efectivo de las actividades y/o contenidos indicados por el comunicante."),
                ("h", 4, "11. Legislación"),
                ("p", "El presente Aviso Legal se rige en todos y cada uno de sus extremos por la ley española."),
            ]},
        ],
    },
}

# "/urraca-abogados-1" era en la web original una copia de "Concursal":
# se mantiene la URL como redirección.
REDIRECTS = {"urraca-abogados-1": "concursal"}

HOME_IMAGE = pexels(7054505)
HOME_IMAGE_ALT = "Mano escribiendo sobre un documento"
