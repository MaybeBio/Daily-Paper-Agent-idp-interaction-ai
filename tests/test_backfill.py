import backfill


def test_monday_run_dates_returns_only_mondays():
    assert backfill.monday_run_dates("2026-09-01", "2026-09-30") == [
        "2026-09-07", "2026-09-14", "2026-09-21", "2026-09-28",
    ]


def test_monday_run_dates_includes_both_ends():
    assert backfill.monday_run_dates("2026-09-14", "2026-09-14") == ["2026-09-14"]


def test_monday_run_dates_empty_when_range_has_no_monday():
    # 2026-09-15 (Tue) .. 2026-09-18 (Fri)
    assert backfill.monday_run_dates("2026-09-15", "2026-09-18") == []


def test_monday_run_dates_empty_when_until_precedes_since():
    assert backfill.monday_run_dates("2026-09-14", "2026-09-01") == []


def test_monday_run_dates_covers_one_year():
    assert len(backfill.monday_run_dates("2025-09-15", "2026-09-14")) == 53


def test_week_args_uses_a_whole_week_window():
    args = backfill.week_args("2026-09-14", "config.yaml", ".")
    assert args[args.index("--run-date") + 1] == "2026-09-14"
    assert args[args.index("--window-days") + 1] == "7"


def test_week_args_never_asks_for_an_issue():
    args = backfill.week_args("2026-09-14", "config.yaml", ".")
    assert "--issue-body" not in args
    assert "--issue-title" not in args


def test_missing_env_lists_absent_vars(monkeypatch):
    monkeypatch.delenv("ENTREZ_EMAIL", raising=False)
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    assert backfill.missing_env() == ["ENTREZ_EMAIL", "LLM_API_KEY"]


def test_missing_env_ignores_blank_values(monkeypatch):
    monkeypatch.setenv("ENTREZ_EMAIL", "  ")
    monkeypatch.setenv("LLM_API_KEY", "sk-x")
    assert backfill.missing_env() == ["ENTREZ_EMAIL"]
