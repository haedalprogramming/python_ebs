"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { curriculum } from "@/data/curriculum";
import { useState } from "react";

export default function Sidebar() {
  const pathname = usePathname();
  const [openParts, setOpenParts] = useState<number[]>([1]);

  const togglePart = (partId: number) => {
    setOpenParts(prev =>
      prev.includes(partId)
        ? prev.filter(id => id !== partId)
        : [...prev, partId]
    );
  };

  const currentLessonId = pathname?.match(/\/lesson\/(\d+)/)?.[1];

  return (
    <aside className="w-72 border-r border-gray-200 bg-white overflow-y-auto h-[calc(100vh-64px)] sticky top-16">
      <nav className="p-4">
        {curriculum.map(part => (
          <div key={part.id} className="mb-2">
            <button
              onClick={() => togglePart(part.id)}
              className="w-full flex items-center justify-between p-3 text-left text-sm font-semibold text-gray-800 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <span className="truncate">{part.title}</span>
              <svg
                className={`w-4 h-4 transition-transform ${
                  openParts.includes(part.id) ? "rotate-180" : ""
                }`}
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            {openParts.includes(part.id) && (
              <ul className="mt-1 ml-2 space-y-1">
                {part.lessons.map(lesson => (
                  <li key={lesson.id}>
                    <Link
                      href={`/lesson/${lesson.id}`}
                      className={`block p-2 pl-4 text-sm rounded-lg transition-colors ${
                        currentLessonId === String(lesson.id)
                          ? "bg-[#ffd506] text-gray-900 font-medium"
                          : "text-gray-700 hover:bg-gray-100"
                      }`}
                    >
                      {lesson.id}차시. {lesson.title}
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </div>
        ))}
      </nav>
    </aside>
  );
}
