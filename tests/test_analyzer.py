from services.analyzer import analyze_logs

def test_analyze_logs():
    data = [
        {"ip": "1.1.1.1", "status": "404"},
        {"ip": "1.1.1.1", "status": "500"},
        {"ip": "2.2.2.2", "status": "404"}
    ]

    result = analyze_logs(data)
    assert result["total_errors"] == 3
    assert result["error_counts"]["404"] == 2
