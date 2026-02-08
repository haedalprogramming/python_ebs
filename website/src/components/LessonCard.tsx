import Link from "next/link";
import { Part } from "@/data/curriculum";

interface LessonCardProps {
  part: Part;
}

const PART_COLORS: Record<number, { bar: string; button: string }> = {
  1: { bar: "bg-[#ffd506]", button: "bg-[#ffd506] hover:bg-[#e6c005]" },
  2: { bar: "bg-[#7232d8]", button: "bg-[#7232d8] hover:bg-[#4d2c77]" },
  3: { bar: "bg-[#50a5dc]", button: "bg-[#50a5dc] hover:opacity-90" },
  4: { bar: "bg-[#d069a9]", button: "bg-[#d069a9] hover:opacity-90" },
  5: { bar: "bg-[#4d2c77]", button: "bg-[#4d2c77] hover:opacity-90" }
};

const PART_ICONS: Record<number, string> = {
  1: "📚",
  2: "🧰",
  3: "🌐",
  4: "📊",
  5: "🧠"
};

export default function LessonCard({ part }: LessonCardProps) {
  const firstLesson = part.lessons[0];
  const lastLesson = part.lessons[part.lessons.length - 1];
  const isReady = part.id === 1;
  const colors = PART_COLORS[part.id];

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
      <div className={`h-2 ${colors.bar}`} />
      <div className="p-6">
        <div className="flex items-center gap-3 mb-3">
          <span className="text-3xl">{PART_ICONS[part.id]}</span>
          <h3 className="text-lg font-bold text-gray-900">{part.title}</h3>
        </div>
        <p className="text-sm text-gray-700 mb-4">{part.description}</p>
        <div className="flex items-center justify-between text-sm text-gray-600 mb-4">
          <span>{firstLesson.id}~{lastLesson.id}차시</span>
          <span>{part.lessons.length}개 강의</span>
        </div>
        {isReady ? (
          <Link
            href={`/lesson/${firstLesson.id}`}
            className={`block w-full text-center py-2.5 rounded-lg text-gray-900 font-medium ${colors.button} transition-all`}
          >
            학습 시작하기
          </Link>
        ) : (
          <div className="block w-full text-center py-2.5 rounded-lg text-gray-500 font-medium bg-gray-200 cursor-not-allowed">
            준비중
          </div>
        )}
      </div>
    </div>
  );
}
