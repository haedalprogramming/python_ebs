import { curriculum } from "@/data/curriculum";
import LessonCard from "@/components/LessonCard";

export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      {/* Hero Section */}
      <section className="bg-[#7232d8] py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-4 text-white">
            🐍 EBS 이솦과 함께하는 파이썬
          </h1>
          <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
            초중고 학생을 위한 체계적인 파이썬 프로그래밍 교육
          </p>
          <div className="flex flex-wrap justify-center gap-4 text-sm text-white">
            <span className="bg-white/20 px-4 py-2 rounded-full">
              📚 31차시 커리큘럼
            </span>
            <span className="bg-white/20 px-4 py-2 rounded-full">
              💻 실습 코드 제공
            </span>
            <span className="bg-white/20 px-4 py-2 rounded-full">
              🎯 도전 과제 포함
            </span>
          </div>
        </div>
      </section>

      {/* Curriculum Overview */}
      <section className="py-16 bg-gray-100">
        <div className="container mx-auto px-4">
          <h2 className="text-2xl font-bold text-gray-900 text-center mb-4">
            커리큘럼
          </h2>
          <p className="text-gray-700 text-center mb-12 max-w-2xl mx-auto">
            기초 문법부터 알고리즘까지, 단계별로 파이썬을 마스터하세요
          </p>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
            {curriculum.map(part => (
              <LessonCard key={part.id} part={part} />
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <h2 className="text-2xl font-bold text-gray-900 text-center mb-12">
            학습 특징
          </h2>
          <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div className="text-center">
              <div className="text-4xl mb-4">📖</div>
              <h3 className="font-semibold text-gray-900 mb-2">개념 학습</h3>
              <p className="text-sm text-gray-700">
                각 차시마다 핵심 개념을 코드와 함께 설명합니다
              </p>
            </div>
            <div className="text-center">
              <div className="text-4xl mb-4">🔧</div>
              <h3 className="font-semibold text-gray-900 mb-2">실습 코드</h3>
              <p className="text-sm text-gray-700">
                배운 내용을 바로 적용해보는 실습 예제를 제공합니다
              </p>
            </div>
            <div className="text-center">
              <div className="text-4xl mb-4">🏆</div>
              <h3 className="font-semibold text-gray-900 mb-2">도전 과제</h3>
              <p className="text-sm text-gray-700">
                스스로 문제를 해결하며 실력을 키울 수 있습니다
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-[#4d2c77] py-8">
        <div className="container mx-auto px-4 text-center text-sm">
          <p className="text-white">EBS 이솦과 함께하는 파이썬</p>
        </div>
      </footer>
    </main>
  );
}
