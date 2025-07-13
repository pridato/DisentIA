import type { AnalysisResult } from "./types"
import { TOPICS, BIAS_TYPES, ANALYSIS_CONFIG } from "./constants"

export const mockAnalyze = async (inputText: string): Promise<AnalysisResult> => {
    await new Promise((resolve) => setTimeout(resolve, ANALYSIS_CONFIG.simulationDelay))

    const sentimentTypes = ["positive", "neutral", "negative"] as const
    const verifiabilityTypes = ["fact", "opinion", "needs_context"] as const

    return {
        sentiment: {
            type: sentimentTypes[Math.floor(Math.random() * sentimentTypes.length)],
            confidence: Math.floor(Math.random() * 30) + 70,
        },
        topics: TOPICS.map((topic) => ({
            name: topic,
            confidence: Math.floor(Math.random() * 60) + 20,
        }))
            .sort((a, b) => b.confidence - a.confidence)
            .slice(0, 5),
        biases: BIAS_TYPES.map((bias) => ({
            type: bias,
            percentage: Math.floor(Math.random() * 40) + 10,
        }))
            .sort((a, b) => b.percentage - a.percentage)
            .slice(0, 5),
        verifiability: {
            type: verifiabilityTypes[Math.floor(Math.random() * verifiabilityTypes.length)],
            confidence: Math.floor(Math.random() * 30) + 70,
        },
    }
}
