# Contributing

Thanks for improving Claudify My Club.

## Good contributions

- New example project folders under `examples/`.
- Better safety checklists for consent, minors, sponsor use, or accessibility.
- More practical Claude prompts for club work.
- Translations and localization.
- Small stdlib-only improvements to `scripts/claudify.py`.

## Rules

- Do not commit private event data, personal data, images of real people, tokens, cookies, API keys, or private calendar exports.
- Use fictional sample data unless you have explicit permission.
- Keep examples easy to copy.
- Prefer plain Markdown over complex tooling.
- Claude-specific instructions are welcome; do not require paid third-party services.

## Local checks

```bash
python3 -m unittest discover -s tests
python3 -m py_compile scripts/claudify.py
```
