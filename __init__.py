"""Monid plugin — bundles the official Monid skill.

Monid (https://monid.ai) is "OpenRouter for agent tools": one interface to
discover and run 2,000+ data endpoints across 72+ providers — web search and
scraping, people/company enrichment, social platforms, market data, and
media generation. Discovery and inspection are free; only running an
endpoint spends workspace balance.

The skill registers as ``monid:monid`` and is loaded explicitly with
``skill_view("monid:monid")``. It drives either the ``monid`` CLI (works
with the built-in terminal tool, no Hermes configuration needed) or the
hosted Monid MCP server (``mcp_servers.monid`` with ``auth: oauth``).
"""

from pathlib import Path

_SKILL_MD = Path(__file__).parent / "skills" / "monid" / "SKILL.md"


def register(ctx):
    ctx.register_skill(
        "monid",
        _SKILL_MD,
        description=(
            "Discover and run 2,000+ data endpoints (web scraping, people/"
            "company enrichment, social media, search, media generation) "
            "through Monid. Load before writing a scraper, calling a "
            "third-party API directly, or declaring data inaccessible."
        ),
    )
