# Monid — Hermes plugin

**OpenRouter, but for agent tools.** One interface, and your Hermes agent can
discover and run **2,000+ endpoints across 72+ providers**: web search and
scraping, people and company enrichment, social platforms, reviews and market
data, and video, image and voice generation. Discovery and inspection are
free; only executing an endpoint spends workspace balance, and every result
reports its own cost.

This plugin bundles the official [Monid skill](skills/monid/SKILL.md), which
teaches the agent to search the catalog, read an endpoint's schema before
calling it, control cost, and report what each run cost.

## Install

```
hermes plugins install monid
```

(Installs from the [Hermes plugin catalog](https://github.com/NousResearch/hermes-agent/tree/main/plugin-catalog),
pinned to an exact reviewed commit of this repository.)

The agent loads the skill explicitly:

```
skill_view("monid:monid")
```

## Transports

The skill drives one of two transports for the same capabilities:

| Transport | Setup | Notes |
|---|---|---|
| **CLI** (default) | None in Hermes — the agent installs `@monid-ai/cli` via its terminal and walks the user through creating an API key at https://app.monid.ai/access/api-keys | Can write large results to files (`-o`), protecting the context window |
| **MCP** (optional) | Add the hosted server to `~/.hermes/config.yaml`, then `hermes mcp login monid` (OAuth — no API key) | Structured `monid_*` tools in the schema |

MCP configuration:

```yaml
mcp_servers:
  monid:
    url: https://mcp.monid.ai/v1
    auth: oauth
```

`auth: oauth` is required — the hosted server authenticates with OAuth 2.1
(PKCE), and Hermes handles discovery, token exchange, and refresh.

## What's in this repo

```
plugin.yaml               Hermes native plugin manifest
__init__.py               register(ctx) — registers the bundled skill as monid:monid
skills/monid/SKILL.md     The Monid skill, adapted for Hermes (see below)
```

No executable tools, no hooks, no environment variables. The plugin is a
manifest, one `register()` call, and one markdown file.

## Skill provenance and sync

`skills/monid/SKILL.md` is a copy of the canonical Monid skill (maintained in
[monid-ai/plugins](https://github.com/monid-ai/plugins) /
[monid-ai/cli](https://github.com/monid-ai/cli)) with exactly two
Hermes-specific edits. When syncing a new canonical version, re-apply them by
hand:

1. **§1.1** — replace the generic "how to connect" instructions with the
   Hermes ones: CLI works out of the box (the agent always has a terminal);
   MCP is configured via `mcp_servers.monid` with `auth: oauth` +
   `hermes mcp login monid`.
2. **§12 troubleshooting** — the `401 (MCP)` row points at
   `hermes mcp login monid` instead of "reconnect in your client".

The skill must never instruct the agent to fetch or overwrite its own file:
updates reach Hermes users only through a commit here plus a SHA-bump PR to
the Hermes plugin catalog, followed by `hermes plugins update monid`. That is
the catalog's trust model (exact commit pins, human-reviewed), and this repo
must stay compliant with it.

## Releasing to the Hermes catalog

1. Commit the change here (skill sync, manifest bump — keep
   `plugin.yaml: version` moving with meaningful releases).
2. Validate against a Hermes checkout:
   `hermes plugins doctor . --ci && hermes plugins validate .`
3. Open a PR to `NousResearch/hermes-agent` updating the `sha:` (and
   `version:`) in `plugin-catalog/monid.yaml` to the new 40-hex commit.

## Links

- Dashboard — https://app.monid.ai
- API keys — https://app.monid.ai/access/api-keys
- Tool catalog — https://monid.ai/tools
- Connector layer (add your API to Monid) — https://github.com/monid-ai/monid
- CLI — https://github.com/monid-ai/cli
- Multi-agent distribution — https://github.com/monid-ai/plugins

## License

MIT — see [LICENSE](LICENSE).
