import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://python.haedal.io"),
  title: {
    default: "해달에듀 파이썬 | EBS 이솦과 함께하는 파이썬",
    template: "%s | 해달에듀 파이썬",
  },
  description:
    "초중고 학생을 위한 체계적인 파이썬 프로그래밍 교육. 기초 문법부터 알고리즘까지 31차시 커리큘럼으로 배우는 파이썬.",
  keywords: [
    "파이썬",
    "Python",
    "프로그래밍 교육",
    "코딩 교육",
    "EBS",
    "이솦",
    "초등 코딩",
    "중등 코딩",
    "고등 코딩",
    "해달에듀",
    "알고리즘",
    "자료구조",
  ],
  openGraph: {
    type: "website",
    locale: "ko_KR",
    siteName: "해달에듀 파이썬",
    title: "해달에듀 파이썬 | EBS 이솦과 함께하는 파이썬",
    description:
      "초중고 학생을 위한 체계적인 파이썬 프로그래밍 교육. 기초 문법부터 알고리즘까지 31차시 커리큘럼.",
    url: "https://python.haedal.io",
  },
  twitter: {
    card: "summary",
    title: "해달에듀 파이썬 | EBS 이솦과 함께하는 파이썬",
    description:
      "초중고 학생을 위한 체계적인 파이썬 프로그래밍 교육. 31차시 커리큘럼으로 배우는 파이썬.",
  },
  robots: {
    index: true,
    follow: true,
  },
  alternates: {
    canonical: "https://python.haedal.io",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-gray-50`}
      >
        <Header />
        {children}
      </body>
    </html>
  );
}
