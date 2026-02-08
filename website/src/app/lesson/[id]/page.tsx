import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Link from "next/link";
import fs from "fs";
import path from "path";
import { getLessonById, getAllLessons } from "@/data/curriculum";
import Sidebar from "@/components/Sidebar";
import CodeViewer from "@/components/CodeViewer";

interface PageProps {
  params: Promise<{ id: string }>;
}

export async function generateStaticParams() {
  return getAllLessons().map(lesson => ({
    id: String(lesson.id),
  }));
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { id } = await params;
  const result = getLessonById(parseInt(id, 10));

  if (!result) {
    return { title: "차시를 찾을 수 없습니다" };
  }

  const { part, lesson } = result;
  const title = `${lesson.id}차시. ${lesson.title}`;
  const description = `${lesson.description} - ${part.title} | 해달에듀 파이썬`;

  return {
    title,
    description,
    openGraph: {
      title: `${title} | 해달에듀 파이썬`,
      description,
      url: `https://python.haedal.io/lesson/${lesson.id}`,
    },
    alternates: {
      canonical: `https://python.haedal.io/lesson/${lesson.id}`,
    },
  };
}

async function getCodeContents(codes: {[key: string]: string | undefined}): Promise<Record<string, string>> {
  const contents: Record<string, string> = {};
  const codeDir = path.join(process.cwd(), "..", "code");

  for (const [, filename] of Object.entries(codes)) {
    if (filename) {
      try {
        const filePath = path.join(codeDir, filename);
        contents[filename] = fs.readFileSync(filePath, "utf-8");
      } catch {
        contents[filename] = `// 파일을 찾을 수 없습니다: ${filename}`;
      }
    }
  }

  return contents;
}

export default async function LessonPage({ params }: PageProps) {
  const { id } = await params;
  const lessonId = parseInt(id, 10);
  const result = getLessonById(lessonId);

  if (!result) {
    notFound();
  }

  const { part, lesson } = result;
  const codeContents = await getCodeContents(lesson.codes);

  const allLessons = getAllLessons();
  const currentIndex = allLessons.findIndex(l => l.id === lessonId);
  const prevLesson = currentIndex > 0 ? allLessons[currentIndex - 1] : null;
  const nextLesson = currentIndex < allLessons.length - 1 ? allLessons[currentIndex + 1] : null;

  return (
    <div className="flex bg-white">
      <Sidebar />
      <main className="flex-1 min-h-[calc(100vh-64px)] p-8 bg-white">
        <div className="max-w-4xl mx-auto">
          {/* Breadcrumb */}
          <div className="flex items-center gap-2 text-sm mb-6">
            <Link href="/" className="text-gray-600 hover:text-[#7232d8]">홈</Link>
            <span className="text-gray-400">/</span>
            <span className="text-gray-600">{part.title}</span>
            <span className="text-gray-400">/</span>
            <span className="text-gray-900 font-medium">{lesson.id}차시</span>
          </div>

          {/* Title */}
          <div className="mb-8">
            <div className="text-sm text-[#7232d8] font-medium mb-2">
              {part.title}
            </div>
            <h1 className="text-3xl font-bold text-gray-900 mb-3">
              {lesson.id}차시. {lesson.title}
            </h1>
            <p className="text-lg text-gray-700">
              {lesson.description}
            </p>
          </div>

          {/* Code Viewer */}
          <div className="mb-8">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">
              학습 코드
            </h2>
            <CodeViewer codes={lesson.codes} codeContents={codeContents} />
          </div>

          {/* Navigation */}
          <div className="flex justify-between items-center pt-8 border-t border-gray-200">
            {prevLesson ? (
              <Link
                href={`/lesson/${prevLesson.id}`}
                className="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-700 hover:text-[#7232d8] transition-colors"
              >
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                </svg>
                <span>이전: {prevLesson.id}차시. {prevLesson.title}</span>
              </Link>
            ) : (
              <div />
            )}
            {nextLesson ? (
              <Link
                href={`/lesson/${nextLesson.id}`}
                className="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-700 hover:text-[#7232d8] transition-colors"
              >
                <span>다음: {nextLesson.id}차시. {nextLesson.title}</span>
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            ) : (
              <div />
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
