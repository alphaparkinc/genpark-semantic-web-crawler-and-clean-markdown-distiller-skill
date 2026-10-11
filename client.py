"""Semantic Web Crawler & Clean Markdown Distiller.
100% Python Standard Library.
"""

import re

class CleanMarkdownDistiller:
    """Strips boilerplate tags from raw HTML and distills clean LLM-ready Markdown with citations."""

    @staticmethod
    def distill_html_to_markdown(html: str, source_url: str = "https://example.com") -> dict:
        cleaned = re.sub(r"<(script|style|nav|footer|aside)[^>]*>.*?</\1>", "", html, flags=re.DOTALL | re.IGNORECASE)
        cleaned = re.sub(r"<h1[^>]*>(.*?)</h1>", r"\n# \1\n", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", cleaned, flags=re.IGNORECASE)

        links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', r"[\2](\1)", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"<[^>]+>", " ", cleaned)
        cleaned = re.sub(r"[ \t]+", " ", cleaned)
        cleaned = re.sub(r"\n\s*\n+", "\n\n", cleaned).strip()

        return {
            "source_url": source_url,
            "markdown": cleaned,
            "extracted_links_count": len(links),
            "estimated_tokens": max(1, len(cleaned) // 4)
        }
