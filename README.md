# Claudify My Club

Claude-ready project templates for small clubs, esports communities, youth groups, local events, and volunteer teams.

The goal: turn messy club work into clear Claude conversations, reusable project folders, and safe publishing checklists — without needing a custom agent platform.

## What this repo gives you

- A practical `CLAUDE.md` operating guide for club projects.
- Reusable templates for briefs, content calendars, consent checks, release packets, and review checklists.
- Five complete example projects you can copy and adapt.
- A tiny stdlib-only scaffold script to start a new Claude-ready project.

## Who it is for

- Clubs that run events and need social posts, recaps, sponsor updates, or member communication.
- Community managers who want Claude to help without losing editorial control.
- Non-technical teams that still want a clean, repeatable folder structure.
- Open-source maintainers building Claude-first workflows for real-world organizations.

## Why Claude helps here

Club work usually fails because context is scattered: dates in calendars, ideas in chats, photos on phones, consent in memory, and posts drafted last minute. Claude works better when each task has a small folder with:

1. a clear brief,
2. trusted source material,
3. constraints,
4. review gates,
5. and a concrete output target.

This repository turns that into copyable project patterns.

## Quick start

```bash
git clone https://github.com/denniskazakis/claudify-my-club.git
cd claudify-my-club
python3 scripts/claudify.py --list
python3 scripts/claudify.py my-first-event --example event-announcement-pack --out ./work
```

Then open the generated folder in Claude Code or the Claude desktop app and say:

```text
Read CLAUDE.md and PROJECT_BRIEF.md. Produce the first draft, then run REVIEW_CHECKLIST.md before final output.
```

## Example projects

| Example | Use it when | Output |
| --- | --- | --- |
| `event-announcement-pack` | You need posts and flyers for an upcoming club event | copy, schedule, asset checklist |
| `tournament-ops-briefing` | You run a small tournament or meetup | ops brief, volunteer tasks, player info |
| `post-event-clip-harvest` | You have raw photos/videos after an event | READY/HOLD/REVIEW sorting and captions |
| `sponsor-proof-report` | You must show sponsors what happened | short proof report with safe media list |
| `window-display-loop` | You need a silent screen/window promo | 30-second loop storyboard and text plan |

## Suggested Claude workflow

1. Copy one example folder.
2. Replace fictional sample data with your real event facts.
3. Keep raw private material out of git.
4. Ask Claude for a first draft.
5. Ask Claude to run the review checklist.
6. Human approves before publishing.

## Safety rules

- Do not publish faces, names, minors, prices, sponsors, or event claims unless the project brief proves they are approved.
- Treat consent and sponsor usage as separate scopes.
- Keep raw photos, voice notes, private calendars, and DMs outside public repositories.
- Claude drafts; humans approve.

## Repository layout

```text
templates/              Reusable Claude-first files
examples/               Five complete example projects
scripts/claudify.py     Copy templates + one example into a new project
tests/                  Stdlib tests for the scaffold script
```

## Roadmap

- Add more examples for sports clubs, music events, school projects, and nonprofit campaigns.
- Add optional JSON schemas for review packets.
- Add a gallery of before/after Claude prompts.
- Add translations for German club workflows.
- Collect real-world feedback from community organizers.

## Contributing

Contributions are welcome: new examples, clearer checklists, translations, and safer review gates are the most useful additions.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).
