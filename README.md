# El trabajo sucio del veterinario acuícola chileno

> Open survey & whitepaper — AI-delegable tasks in Chilean aquaculture veterinary practice

Esta encuesta busca mapear qué tareas consumen el tiempo y la energía de los veterinarios acuícolas en Chile, y cuáles de ellas podrían —o no— delegarse a herramientas de IA. Los resultados se publicarán como whitepaper abierto, compartido con MEVEA y COLMEVET.

## Estado actual

**Recolectando respuestas.** El análisis y el whitepaper se publicarán una vez alcanzada una muestra representativa.

## Participar

| Idioma | Enlace |
|---|---|
| Español (Chile) | [tally.so/r/q4EQX9](https://tally.so/r/q4EQX9) |
| English | _próximamente_ |

La encuesta toma 8–10 minutos, es anónima y no recolecta datos identificatorios.

## Estructura del repo

```
survey/          formularios en markdown + metodología
data/raw/        CSVs exportados de Tally (no versionados — ver .gitignore)
data/processed/  datasets limpios/anonimizados
analysis/        notebooks exploratorios y scripts de descarga
whitepaper/      borrador del paper final
```

## Reproducir el análisis

```bash
# instalar uv si no lo tienes
curl -LsSf https://astral.sh/uv/install.sh | sh

# instalar dependencias
uv sync

# abrir Jupyter
uv run jupyter lab
```

Copia `.env.example` a `.env` y añade tu `TALLY_API_KEY` para usar `analysis/scripts/fetch_tally.py`.

## Citar este trabajo

```
Piña, A. (2026). El trabajo sucio del veterinario acuícola chileno:
tareas delegables a IA. Whitepaper abierto. Universidad de Chile.
https://github.com/agustinpina/Encuesta_2026
```

## Licencia

MIT © 2026 Agustín Piña. El contenido de la encuesta y el whitepaper son de libre uso con atribución.
