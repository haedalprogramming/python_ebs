"use client";

import Link from "next/link";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-gray-200 bg-white backdrop-blur">
      <div className="container mx-auto flex h-16 items-center justify-between px-4">
        <Link href="/" className="flex items-center gap-2">
          <span className="text-2xl">🐍</span>
          <span className="text-xl font-bold text-gray-900">
            해달에듀 파이썬
          </span>
        </Link>
        <nav className="flex items-center gap-6">
          <Link
            href="/"
            className="text-sm font-medium text-gray-700 hover:text-[#7232d8] transition-colors"
          >
            홈
          </Link>
          <Link
            href="/lesson/1"
            className="text-sm font-medium text-gray-900 bg-[#ffd506] hover:bg-[#e6c005] px-4 py-2 rounded-lg transition-colors"
          >
            시작하기
          </Link>
        </nav>
      </div>
    </header>
  );
}
