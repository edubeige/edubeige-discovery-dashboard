from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


def test_existing_domain_copy_is_operator_clear() -> None:
    assert "중복/기존" not in HTML, "ambiguous duplicate/existing-domain label should not be visible"
    assert "우선순위 20" in HTML, "priority badge should read as priority, not like a 20p score"
    assert "<span>P</span><strong>20</strong>" not in HTML, "P/20 vertical badge is ambiguous"
    assert (
        "반복 도메인 주의" in HTML or "기존 도메인 주의" in HTML
    ), "duplicate/existing-domain cards need a specific operator-facing reason"
    assert (
        'chip warn">미검토</span>\n        <span class="chip warn">미검토' not in HTML
    ), "cards should not render duplicate unreviewed chips"


def test_dashboard_controls_contract_still_present() -> None:
    assert 'id="search"' in HTML
    assert 'id="sort"' in HTML
    assert 'id="candidateGrid"' in HTML
    assert "function applySort()" in HTML
    assert "function applyFilters()" in HTML
    assert "data-filter=\"all\"" in HTML
    assert "data-filter=\"warning\"" in HTML
    assert "data-filter=\"existing_domain\"" in HTML
    assert "data-filter=\"duplicate\"" in HTML
    assert "data-card" in HTML


def test_dashboard_remains_read_only_and_path_safe() -> None:
    lower_html = HTML.lower()
    assert "<form" not in lower_html
    assert "fetch(" not in HTML
    assert "xmlhttprequest" not in lower_html
    assert "supabase.from" not in lower_html
    assert "createclient(" not in lower_html
    assert ".insert(" not in lower_html
    assert "approval queue write" not in lower_html
    assert "/Users/hwangdoyeon" not in HTML
    assert "/Volumes/obsidian" not in HTML
    assert "/private/var" not in HTML
