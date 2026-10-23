# RUTHISH GitHub contribution pattern

This public repository contains a scheduled workflow that maps a 5×7 pixel font spelling **RUTHISH** onto selected dates of the GitHub contribution calendar.

## Schedule

- Start date: **2026-11-01**
- Daily check: **09:00 Asia/Kolkata** (03:30 UTC)
- Last planned pixel date: **2027-08-14**
- Planned active pixels: **108**
- Pixel date mapping: [pixel_dates.csv](pixel_dates.csv)
- Date calculator: [scripts/draw_contributions.py](scripts/draw_contributions.py)
- Workflow: [.github/workflows/ruthish-contributions.yml](.github/workflows/ruthish-contributions.yml)

## How it works

The scheduled GitHub Actions workflow checks the current date in Asia/Kolkata. On one of the selected dates, it appends a dated record to `contribution-log.md` and commits that change using the GitHub noreply email associated with this account. On other dates, it exits without committing. It starts making changes on November 1, 2026.

**Keep this GitHub account dedicated to the pattern during the design period.** Do your regular coding, repository updates, and other commits on your separate work account. Do not manually push commits to this pattern account or repository on empty dates, because any other eligible contribution on those dates can create unwanted green squares. The automation itself does not create a commit on an empty pattern date.

The manual `workflow_dispatch` option defaults to **dry run**, so it previews the result without committing. To manually make a commit on an active date, select the workflow's **Run workflow** option and set `dry_run` to false.

## Notes and limitations

- This project creates automated, dated repository activity to form a visual pattern. It should not be represented as substantive day-to-day software development.
- GitHub decides whether a commit qualifies for the contribution graph and the shade of green shown. A desired shade cannot be forced.
- The automation is designed to leave every planned empty date without a commit from this repository. This cannot prevent green squares caused by other eligible activity on the same account, so keep this account dedicated and avoid other contributions during the pattern period.
- Contribution attribution may depend on the commit email being associated with your account, repository default-branch status, and GitHub profile settings.
- Scheduled runs may be delayed by GitHub Actions. Missed dates are not automatically backfilled.
- To display anonymized private contribution activity, use the private contribution display setting on your profile. This repository is public, so its contents and workflow are visible to everyone.

## Test the date calculator locally

Run these commands with Python 3.10 or later:

```bash
python scripts/draw_contributions.py --date 2026-11-01 --dry-run
python scripts/draw_contributions.py --date 2026-11-09 --dry-run
```

The first date is an active pixel date. November 9, 2026 is not an active pixel date.
