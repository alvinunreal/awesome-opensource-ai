# .moltfounders/

This directory defines how AI agents maintain this repository.

Agents participating in the [MoltFounders](https://moltfounders.com) workspace for this repo read these files on every run and follow them exactly. Rules are versioned here like code - propose changes via PR, same as everything else.

## Files

| File | Purpose |
|------|---------|
| `labels.md` | Canonical GitHub label definitions |
| `issue-management.md` | How to triage and handle stale issues/PRs |
| `pr-review.md` | How to review pull requests |
| `research.md` | How to discover and suggest new entries |

## Principles

- **Agents prepare, humans decide.** Agents review, comment, and label. Only the repo maintainer merges.
- **Idempotent by default.** Once an agent has handled an item, it won't touch it again unless the label is removed.
- **Transparent.** Anyone can read exactly how submissions are reviewed by reading this directory.
- **Community-editable.** Want to change how the repo is maintained? Open a PR against these files.

## Branch Protection Note

Changes to `.moltfounders/` should only be merged by the repo maintainer, as they directly affect agent behavior.
