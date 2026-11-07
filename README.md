# The Blueprint

A Field Guide to Building Organisations of People and Agents.

## Local development

```sh
npm install
npm run build          # site only, output in build/site/
make build-full        # site + PDF + EPUB (Docker)
```

Preview with `cd build/site && python3 -m http.server 8000`.

## Repo layout

- `docs/modules/ROOT/pages/`: chapters (AsciiDoc)
- `docs/modules/ROOT/nav.adoc`: navigation
- `lib/`: Antora extensions (llms.txt generator, footnotes heading)
- `supplemental-ui/`: theme overrides
- `scripts/`: checks (`copyright-overlap.py`)

## Publishing

`.github/workflows/publish.yml` publishes to GitHub Pages on push to `main`. It is set to manual-only (`workflow_dispatch`) until the book is ready to go public.

## Keeping it fresh (answer-engine optimisation)

Answer engines favour pages that are current, answer the question up front, and agree with each other. Every quarter:

1. Re-check the research the chapters cite and update figures that have moved. Add new evidence where the field has shifted.
2. Bump `:page-date-modified:` on every page you change. It drives the visible "Last updated" line, the JSON-LD `dateModified` and the sitemap `<lastmod>`.
3. Add a dated entry to `docs/modules/ROOT/pages/updates.adoc` (What's New).
4. Check each changed chapter's `[.in-short]` answer and `:page-search-title:` still match the body.
5. Run the prompt panel: ask the tracked questions in ChatGPT, Perplexity, Google AI Mode, Gemini and Claude, and note whether the book is cited.

Page conventions for search and AI engines:

- `:page-search-title:` sets the HTML `<title>` (and `og:title`) to the question a reader would type. The visible chapter title stays as written.
- `[.in-short]` is a 40–60 word, self-contained answer placed directly under the `[.lead]`.
- Key-concept pages (`what-is-*.adoc`) set `:page-schema: term` with `:page-term-name:` and `:page-term-definition:`, which become a schema.org `DefinedTerm`.
- The Person, Book and WebSite JSON-LD nodes in `supplemental-ui/partials/head-meta.hbs` have stable `@id`s; update `sameAs` there when author profiles change.
