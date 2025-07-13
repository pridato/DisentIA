export interface AnalysisResult {
    sentiment: {
        type: keyof typeof import("./constants").SENTIMENT_CONFIG
        confidence: number
    }
    topics: Array<{
        name: string
        confidence: number
    }>
    biases: Array<{
        type: string
        percentage: number
    }>
    verifiability: {
        type: keyof typeof import("./constants").VERIFIABILITY_CONFIG
        confidence: number
    }
}

export interface HistoryItem {
    id: string
    text: string
    timestamp: Date
    result: AnalysisResult
}
