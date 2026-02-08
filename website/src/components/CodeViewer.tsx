"use client";

import { useState } from "react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";
import { CodeFiles } from "@/data/curriculum";

interface CodeViewerProps {
  codes: CodeFiles;
  codeContents: Record<string, string>;
}

const TAB_LABELS: Record<keyof CodeFiles, string> = {
  concept: "개념 학습",
  practiceA: "실습 A",
  practiceB: "실습 B",
  challenge: "도전 과제",
  answer: "정답"
};

export default function CodeViewer({ codes, codeContents }: CodeViewerProps) {
  const availableTabs = Object.keys(codes).filter(
    key => codes[key as keyof CodeFiles]
  ) as (keyof CodeFiles)[];

  const [activeTab, setActiveTab] = useState<keyof CodeFiles>(
    availableTabs[0] || "concept"
  );
  const [showAnswer, setShowAnswer] = useState(false);
  const [copied, setCopied] = useState(false);

  if (availableTabs.length === 0) {
    return (
      <div className="bg-gray-100 rounded-lg p-8 text-center text-gray-600">
        이 차시에는 코드 예제가 없습니다.
      </div>
    );
  }

  const currentCode = codeContents[codes[activeTab] || ""] || "";

  const handleCopy = async () => {
    await navigator.clipboard.writeText(currentCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const isAnswerTab = activeTab === "answer";

  return (
    <div className="rounded-lg overflow-hidden border border-gray-200">
      {/* Tabs */}
      <div className="flex border-b border-gray-200 bg-gray-50 overflow-x-auto">
        {availableTabs.map(tab => (
          <button
            key={tab}
            onClick={() => {
              setActiveTab(tab);
              if (tab === "answer") setShowAnswer(false);
            }}
            className={`px-4 py-3 text-sm font-medium whitespace-nowrap transition-colors ${
              activeTab === tab
                ? "bg-white text-[#7232d8] border-b-2 border-[#ffd506]"
                : "text-gray-600 hover:text-gray-900 hover:bg-gray-100"
            }`}
          >
            {TAB_LABELS[tab]}
          </button>
        ))}
      </div>

      {/* Code Content */}
      <div className="relative">
        {/* Copy Button */}
        <button
          onClick={handleCopy}
          className="absolute top-3 right-3 z-10 px-3 py-1.5 text-xs font-medium text-white bg-gray-700 hover:bg-gray-600 rounded transition-colors"
        >
          {copied ? "복사됨!" : "복사"}
        </button>

        {isAnswerTab && !showAnswer ? (
          <div className="bg-gray-800 p-12 text-center">
            <p className="text-gray-300 mb-4">정답을 확인하시겠습니까?</p>
            <button
              onClick={() => setShowAnswer(true)}
              className="px-6 py-2 bg-[#ffd506] hover:bg-[#e6c005] text-gray-900 rounded-lg font-medium transition-colors"
            >
              정답 보기
            </button>
          </div>
        ) : (
          <SyntaxHighlighter
            language="python"
            style={oneDark}
            showLineNumbers
            customStyle={{
              margin: 0,
              padding: "1rem",
              fontSize: "0.875rem",
              lineHeight: "1.5"
            }}
          >
            {currentCode}
          </SyntaxHighlighter>
        )}
      </div>

      {/* File Name */}
      <div className="px-4 py-2 bg-gray-100 border-t border-gray-200">
        <span className="text-xs text-gray-600">
          📄 {codes[activeTab]}
        </span>
      </div>
    </div>
  );
}
