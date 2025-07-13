// Colores y tema
export const COLORS = {
    background: {
        primary: "bg-gray-50",
        secondary: "bg-white",
        tertiary: "bg-gray-100",
        sidebar: "bg-white",
        card: "bg-white",
    },
    text: {
        primary: "text-gray-900",
        secondary: "text-gray-600",
        tertiary: "text-gray-500",
        accent: "text-blue-600",
        success: "text-green-600",
        warning: "text-amber-600",
        error: "text-red-600",
    },
    border: {
        light: "border-gray-200",
        medium: "border-gray-300",
        focus: "border-blue-500",
    },
    button: {
        primary: "bg-gray-900 hover:bg-gray-800 text-white",
        secondary: "bg-gray-100 hover:bg-gray-200 text-gray-900",
    },
} as const

// Configuración de análisis
export const ANALYSIS_CONFIG = {
    minTextLength: 10,
    maxTextLength: 5000,
    simulationDelay: 1500,
} as const

// Textos de la interfaz
export const UI_TEXTS = {
    brand: {
        name: "DisentIA",
        tagline: "Análisis inteligente de texto",
        description: "Analiza el sentimiento, temas y sesgos de cualquier texto usando IA",
    },
    placeholders: {
        textarea:
            'Escribe o pega aquí el texto que quieres analizar...\n\nPor ejemplo: "El cambio climático es uno de los desafíos más importantes de nuestra época..."',
    },
    buttons: {
        analyze: "Analizar texto",
        analyzing: "Analizando...",
        clear: "Limpiar",
    },
    sections: {
        sentiment: "Análisis de Sentimiento",
        topics: "Temas Principales",
        biases: "Análisis de Sesgo",
        verifiability: "Verificabilidad",
        history: "Historial",
    },
    tabs: {
        complete: "Análisis Completo",
        summary: "Resumen",
    },
} as const

// Configuración de sentimientos
export const SENTIMENT_CONFIG = {
    positive: {
        label: "Positivo",
        emoji: "😊",
        color: "text-green-600",
        bgColor: "bg-green-50",
        borderColor: "border-green-200",
    },
    negative: {
        label: "Negativo",
        emoji: "😔",
        color: "text-red-600",
        bgColor: "bg-red-50",
        borderColor: "border-red-200",
    },
    neutral: {
        label: "Neutral",
        emoji: "😐",
        color: "text-amber-600",
        bgColor: "bg-amber-50",
        borderColor: "border-amber-200",
    },
} as const

// Configuración de verificabilidad
export const VERIFIABILITY_CONFIG = {
    fact: {
        label: "Hecho Verificable",
        color: "bg-green-100 text-green-800 border-green-200",
        icon: "✓",
    },
    opinion: {
        label: "Opinión",
        color: "bg-blue-100 text-blue-800 border-blue-200",
        icon: "💭",
    },
    needs_context: {
        label: "Necesita Contexto",
        color: "bg-amber-100 text-amber-800 border-amber-200",
        icon: "❓",
    },
} as const

// Temas predefinidos
export const TOPICS = [
    "Política",
    "Medio Ambiente",
    "Tecnología",
    "Salud",
    "Economía",
    "Educación",
    "Deportes",
    "Cultura",
    "Ciencia",
    "Sociedad",
] as const

// Tipos de sesgo
export const BIAS_TYPES = [
    "Objetivo",
    "Alarmista",
    "Polarizado",
    "Sensacionalista",
    "Neutral",
    "Emocional",
    "Racional",
    "Parcial",
] as const
