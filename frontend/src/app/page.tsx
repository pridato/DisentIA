"use client"

import { useState } from "react"
import { Menu } from "lucide-react"
import { Button } from "../components/ui/button"
import { Card, CardContent } from "../components/ui/card"
import { Sidebar } from "../components/sidebar"
import { TextInput } from "../components/text-input"
import { AnalysisResults } from "../components/analysis-results"
import { mockAnalyze } from "../lib/mock-analysis"
import type { AnalysisResult, HistoryItem } from "../lib/types"
import {COLORS, UI_TEXTS} from "../lib/constants.ts";

export default function DisentIA() {
    const [text, setText] = useState("")
    const [isAnalyzing, setIsAnalyzing] = useState(false)
    const [result, setResult] = useState<AnalysisResult | null>(null)
    const [history, setHistory] = useState<HistoryItem[]>([])
    const [sidebarOpen, setSidebarOpen] = useState(false)

    const handleAnalyze = async () => {
        if (!text.trim()) return

        setIsAnalyzing(true)
        try {
            const analysisResult = await mockAnalyze(text)
            setResult(analysisResult)

            const newHistoryItem: HistoryItem = {
                id: Date.now().toString(),
                text: text.substring(0, 100) + (text.length > 100 ? "..." : ""),
                timestamp: new Date(),
                result: analysisResult,
            }

            setHistory((prev) => [newHistoryItem, ...prev.slice(0, 9)])
        } catch (error) {
            console.error("Error analyzing text:", error)
        } finally {
            setIsAnalyzing(false)
        }
    }

    const handleSelectHistory = (item: HistoryItem) => {
        setText(item.text.replace("...", ""))
        setResult(item.result)
        setSidebarOpen(false)
    }

    return (
        <div className={`min-h-screen ${COLORS.background.primary}`}>
    {/* Sidebar */}
    <Sidebar
        isOpen={sidebarOpen}
    onClose={() => setSidebarOpen(false)}
    history={history}
    onSelectHistory={handleSelectHistory}
    />

    {/* Main Content */}
    <div className="lg:ml-80 min-h-screen">
        {/* Header */}
        <header
    className={`
          sticky top-0 z-30 ${COLORS.background.secondary} 
          border-b ${COLORS.border.light} backdrop-blur-sm bg-white/80
        `}
>
    <div className="flex items-center justify-between p-4">
    <Button variant="ghost" size="icon" className="lg:hidden" onClick={() => setSidebarOpen(true)}>
    <Menu className="w-5 h-5" />
        </Button>

        <div className="hidden lg:block">
    <p className={`${COLORS.text.secondary} text-sm`}>{UI_TEXTS.brand.tagline}</p>
    </div>
    </div>
    </header>

    {/* Main Interface */}
    <main className="p-6 lg:p-12 max-w-4xl mx-auto">
    <div className="space-y-12">
        {/* Input Section */}
        <TextInput text={text} setText={setText} onAnalyze={handleAnalyze} isAnalyzing={isAnalyzing} />

    {/* Results Section */}
    {result ? (
        <div className="space-y-6">
        <div className="text-center">
        <h2 className={`text-2xl font-semibold ${COLORS.text.primary} mb-2`}>Resultados del Análisis</h2>
    <p className={`${COLORS.text.secondary}`}>Análisis completado con inteligencia artificial</p>
    </div>
    <AnalysisResults result={result} />
    </div>
    ) : (
        !isAnalyzing && (
            <Card className={`${COLORS.background.card} border-2 border-dashed ${COLORS.border.medium}`}>
        <CardContent className="pt-12 pb-12">
        <div className={`text-center ${COLORS.text.tertiary}`}>
        <div className="w-16 h-16 mx-auto mb-4 bg-gray-100 rounded-full flex items-center justify-center">
        <span className="text-2xl">🤖</span>
    </div>
    <p className="text-lg font-medium mb-2">Listo para analizar</p>
    <p className="text-sm">
        Los resultados del análisis aparecerán aquí una vez que proceses tu texto
    </p>
    </div>
    </CardContent>
    </Card>
    )
    )}
    </div>
    </main>
    </div>
    </div>
)
}