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
