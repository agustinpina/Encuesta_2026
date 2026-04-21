# Metodología de la encuesta

## Objetivo

Identificar qué tareas del trabajo diario de los veterinarios acuícolas chilenos consumen más tiempo, cuáles consideran de bajo valor profesional, y cuáles serían candidatas a delegarse a herramientas de IA generativa. Los resultados alimentarán un whitepaper abierto para MEVEA y COLMEVET.

## Diseño

Encuesta autoadministrada en línea (Tally), distribuida por conveniencia a través de redes profesionales (MEVEA, COLMEVET, LinkedIn). Sin muestreo probabilístico.

**Duración estimada:** 8–10 minutos.

**Estructura del formulario (6 partes + cierre):**

| Parte | Contenido |
|---|---|
| Perfil | Experiencia, rol, región, tamaño de empresa |
| Tu semana en horas | Carga horaria por tarea (12 categorías) |
| Valor y fricción | Tareas de bajo valor profesional, frustrantes, uso actual de IA |
| IA en tu práctica | Reservas, tareas no delegables |
| Pausa | Pregunta abierta creativa (reducir fatiga de encuesta) |
| Impacto económico | % jornada en tareas de bajo valor, tramo de renta, WTP de la empresa |
| Cierre narrativo | Descripción de un día representativo |
| Seguimiento (opcional) | Consentimiento + contacto para entrevista de 20 min |

## Criterio de inclusión

Médicos veterinarios con actividad profesional activa en acuicultura chilena (salmonicultura, mitilicultura, etc.) al momento de responder.

## Idiomas

- **Español (Chile):** versión primaria, formulario `q4EQX9`.
- **Inglés:** versión secundaria para pares internacionales (Noruega, Escocia, Canadá, Japón, Australia). Formulario a publicar. Las preguntas de región y moneda se adaptan.

## Anonimidad y tratamiento de datos

- No se recolectan nombre, RUT ni ningún identificador directo.
- El campo de contacto (email / WhatsApp) se almacena separado del resto de respuestas en Tally y no se cruza con los datos analíticos.
- Los CSVs exportados de Tally no se versionan en este repositorio (`data/raw/` está en `.gitignore`).
- Los datos procesados/anonimizados en `data/processed/` sí se versionan para reproducibilidad.

## Limitaciones

- **Muestra no probabilística:** los resultados no son estadísticamente generalizables al universo de veterinarios acuícolas chilenos.
- **Sesgo de autoselección:** participan quienes tienen interés en el tema o exposición a las redes de distribución.
- **Autoreporte:** las horas semanales por tarea son estimaciones subjetivas, no mediciones objetivas.
- **Heterogeneidad de roles:** la encuesta cubre desde veterinarios de terreno hasta académicos; las comparaciones entre grupos deben interpretarse con cautela.

## Consideraciones éticas

Esta encuesta no constituye investigación biomédica en seres humanos bajo la definición de la Resolución 8430/1993 ni requiere aprobación de comité de ética institucional. Sin embargo, se adhiere a los principios de:

- Participación voluntaria e informada.
- Anonimidad de las respuestas.
- Transparencia en el uso de los datos (whitepaper abierto).
- Posibilidad de omitir cualquier pregunta sin consecuencias.

## Contacto

Agustín Piña · Médico Veterinario, Universidad de Chile  
LinkedIn: [agustinpina](https://www.linkedin.com/in/agustinpina)
