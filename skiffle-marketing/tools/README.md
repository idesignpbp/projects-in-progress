# Skiffle site build tools

## `build_prd.py` — regenerate the PRD page

`/prd` is the **only** page on the site sourced from Slack. It is generated
from the **"PRD [v1.1]"** canvas in the `#skiffle` channel, not hand-edited.

### Re-sync workflow
1. Edit the PRD in Slack (content + tables, with Slack's default formatting).
2. Re-pull the canvas markdown into [`prd_source.md`](./prd_source.md) — this
   step uses the Slack connector (read canvas `F0BJ7S5UT6Y`, save its
   `markdown_content`). It is done via Claude Code, not by hand.
3. Regenerate the page:
   ```bash
   pip install markdown        # one-time dependency
   python3 tools/build_prd.py  # rewrites prd/index.html
   ```
4. Commit `prd_source.md` + `prd/index.html` and push.

### Notes
- **Do not hand-edit `prd/index.html`** — a re-sync overwrites it. Content
  changes go in Slack; page styling/layout lives in the `TEMPLATE` string in
  `build_prd.py`.
- The generator produces: styled tables (with horizontal scroll), color-coded
  status badges (LOCKED / DECIDED / OPEN / FIX / VERIFIED / …), and a sticky
  sidebar table of contents built from the `##` headings.
- **Images**: images embedded in the Slack canvas do not survive the markdown
  export cleanly and may need to be handled separately.

The home page (`/`) and `/current-app` are **not** Slack-sourced and are edited
directly (Current App images come from the Kickoff FigJam).
