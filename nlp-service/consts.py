EXTRA_STOPWORDS = {"esto", "eso", "así", "también", "muy", "entonces", "además", "quizás", "igual", "incluso", "solo",
                   "pues", "claro", "bueno", "ok", "vale", "aunque", "ciertamente", "obviamente", "seguro", "sí", "no",
                   "jamás", "siempre", "nunca", "ya", "todavía", "casi", "realmente", "simplemente", "definitivamente"}

TOPIC_LABELS = [
    "política", "economía", "salud", "tecnología", "educación",
    "medio ambiente", "ciencia", "cultura", "deportes", "justicia",
    "religión", "género", "migración", "empleo", "seguridad",
    "infraestructura", "comunicaciones", "finanzas", "defensa", "vivienda"
]

BIAS_LABELS = [
    "objetivo", "subjetivo", "alarmista", "neutral", "tendencioso",
    "emocional", "informativo", "manipulador", "partidista", "equilibrado",
    "extremo", "polarizado", "provocador", "desinformativo", "argumentativo",
    "sarcástico", "crítico", "sensacionalista", "ambiguo", "persuasivo"
]

VERIFY_LABELS = [
    "verificable", "opinión", "necesita contexto", "inverificable", "ambigua",
    "afirmación empírica", "hecho histórico", "proyección", "hipótesis", "dato cuantitativo",
    "fuente citada", "no respaldada", "análisis técnico", "experiencia personal",
    "repetición de rumor", "hecho contrastado", "referencia indirecta", "conspiración",
    "estimación", "exageración"
]