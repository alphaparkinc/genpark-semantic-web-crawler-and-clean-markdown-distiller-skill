"""Example usage for Semantic Web Crawler & Clean Markdown Distiller."""
from client import CleanMarkdownDistiller

if __name__ == "__main__":
    sample_html = "<html><nav>Skip</nav><h1>Agent Guide</h1><p>Visit <a href='https://example.org'>Docs</a></p></html>"
    res = CleanMarkdownDistiller.distill_html_to_markdown(sample_html)
    print(res["markdown"])
