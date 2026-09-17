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


def test_week_failures_reads_platforms_from_the_summary_line():
    log = "[pubmed] FAILED: RemoteDisconnected\nWarning: 1 platform(s) failed: ['pubmed']\n"
    assert backfill.week_failures(log) == ["pubmed"]


def test_week_failures_handles_several_platforms():
    log = "Warning: 2 platform(s) failed: ['arxiv', 'pubmed']\n"
    assert backfill.week_failures(log) == ["arxiv", "pubmed"]


def test_week_failures_empty_on_a_clean_run():
    assert backfill.week_failures("[pubmed] 12 records (archived 12)\n") == []


def test_week_failures_ignores_per_paper_agent_failures():
    # [agent] FAILED lines mean one paper's LLM call died, not that a platform
    # went down — the week is still complete.
    log = "[agent] pubmed/42723155 FAILED: 429 rate limited\n"
    assert backfill.week_failures(log) == []


def test_retry_commands_pin_each_week_to_itself():
    assert backfill.retry_commands(["2026-03-02", "2026-09-14"]) == [
        "python scripts/backfill.py --since 2026-03-02 --until 2026-03-02",
        "python scripts/backfill.py --since 2026-09-14 --until 2026-09-14",
    ]


# Verbatim shape of a real 503 week: the interpolated httpx error wraps onto a
# second line, so the "returning Crossref-only results." tail is NOT on the line
# that starts with the platform tag.
_DEGRADED_NOTICE = (
    "[biorxiv] Europe PMC search failed (Server error '503 Service Temporarily Unavailable' for url "
    "'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3APPR&cursorMark=%2A'\n"
    "For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503); "
    "returning Crossref-only results.\n"
)
_DEGRADED_LOG = _DEGRADED_NOTICE + "[biorxiv] 2 records (archived 2)\n"


def test_week_degradations_detects_crossref_only_fallback():
    assert backfill.week_degradations(_DEGRADED_LOG) == ["biorxiv"]


def test_week_degradations_dedupes_a_repeated_notice():
    # The medrxiv run reuses BioRxivFetcher, whose notice is hardcoded "[biorxiv]",
    # so one Europe PMC outage prints the same line twice.
    assert backfill.week_degradations(_DEGRADED_LOG * 2) == ["biorxiv"]


def test_week_degradations_empty_on_a_clean_run():
    assert backfill.week_degradations("[biorxiv] 2 records (archived 2)\n") == []


def test_week_degradations_ignores_an_outright_platform_failure():
    log = "[biorxiv] FAILED: connection refused\nWarning: 1 platform(s) failed: ['biorxiv']\n"
    assert backfill.week_degradations(log) == []
