# Project: Finance Tracker

A terminal app to record income/expenses, organize categories, set monthly budgets, and get summaries. Data survives between runs.

## Scope

**Core**

1. Record transactions: amount, type (income/expense), category, date, optional note.
2. View/filter by date range, category, type, amount range.
3. Edit and delete transactions.
4. Categories user-manageable, with sensible defaults on first run.
5. Monthly budgets per category: limit, used, remaining, over-limit warnings.
6. Reports: monthly summary, spending by category, income vs. expense totals.
7. Persistence to disk, loaded on startup; first run works smoothly.
8. Import/export CSV, including messy/invalid rows.
9. Real CLI commands/options, not just a `while True` menu (menu may be a stretch).

**Out of scope**
No GUI/web/DB server; no accounts/auth; no multi-currency; no third-party frameworks beyond stdlib + test framework; no async/networking/cloud sync.

## Rules

* Bad input never crashes; handle wrong amounts, impossible dates, unknown categories, corrupted files gracefully.
* Separation of concerns: interaction doesn’t know storage; storage doesn’t know display.
* Business rules live in one place.
* Money handled correctly—research first.
* No global state.
* Tests required for core logic.
* Git from day one with meaningful commits.

## Milestones

|Phase|Goal|Done when|
|-|-|-|
|0. Design first (1–2 days)|Write main things, responsibilities, folder layout. No code.|Can explain design in 5 min.|
|1. Core domain|Model transactions/categories with validation/rules. No files/CLI.|Can create/validate/manipulate in shell; tests pass.|
|2. Persistence|Safe save/load; handle missing, empty, corrupted.|Reopen keeps data; broken file doesn’t crash.|
|3. Budgets/reports|Add budget tracking and summaries.|Reports match hand calculations.|
|4. CLI|User commands and clean errors.|Stranger can use from `--help` alone.|
|5. Import/export|CSV in/out with row-level error reporting.|50 rows with 3 bad imports 47 and clearly reports 3.|
|6. Polish|Logging, config/settings, README.|Comfortable showing repo to interviewer.|

## Skills forced

Modularity/structure; OOP in practice; custom exceptions/error strategy; file I/O and safe writes; testing as design; project thinking; documentation.

## Stretch (after core)

Recurring transactions; tags/search notes; simple terminal charts; undo last action; package for single-command install/run.

## Common traps

CLI first and everything grows from it; one giant file/class; features before previous milestone is tested; copying a tutorial structure; perfecting design before coding (first design will be wrong—that’s the lesson).

## How to work

At each phase end ask: *“If I change how X works, how many files must I touch?”* More than one or two means boundaries need work. That question is the core skill.
