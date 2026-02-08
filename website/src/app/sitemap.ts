import type { MetadataRoute } from "next";
import { getAllLessons } from "@/data/curriculum";

export default function sitemap(): MetadataRoute.Sitemap {
  const lessons = getAllLessons().map((lesson) => ({
    url: `https://python.haedal.io/lesson/${lesson.id}`,
    lastModified: new Date(),
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  return [
    {
      url: "https://python.haedal.io",
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 1.0,
    },
    ...lessons,
  ];
}
