from flask import Flask, render_template
from utils.logger import setup_logger
from utils.file_generator import generate_log_file
from services.log_parser import parse_logs
from services.analyzer import analyze_logs
from services.visualizer import generate_error_chart
from config import LOG_FILE_PATH
import logging
import os
import webbrowser

app = Flask(__name__)

# Setup application logging
setup_logger()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze")
def analyze():
    try:
        # Ensure required directories exist
        os.makedirs("logs", exist_ok=True)
        os.makedirs("static/charts", exist_ok=True)

        # Step 1: Generate log file if not present
        if not os.path.exists(LOG_FILE_PATH):
            generate_log_file(LOG_FILE_PATH)

        logging.info("Log analysis started")

        # Step 2: Parse logs
        parsed_data, total_requests = parse_logs(LOG_FILE_PATH)

        # Step 3: Analyze logs safely
        analysis = analyze_logs(parsed_data)

        total_errors = analysis.get("total_errors", 0)
        error_counts = analysis.get("error_counts", {})
        top_ips = analysis.get("top_ips", {})

        # Step 4: Generate chart only if errors exist
        chart_path = None
        if error_counts:
            chart_path = "static/charts/error_distribution.png"
            generate_error_chart(error_counts, chart_path)

        logging.info("Log analysis completed successfully")

        # Step 5: Render report
        return render_template(
            "report.html",
            total_requests=total_requests,
            total_errors=total_errors,
            error_counts=error_counts,
            top_ips=top_ips,
            chart=chart_path
        )

    except Exception as e:
        logging.error(f"Application crashed: {str(e)}")

        return render_template(
            "report.html",
            total_requests=0,
            total_errors=0,
            error_counts={},
            top_ips={},
            chart=None,
            error_message="An error occurred while processing logs. Please check logs."
        )


if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"

    print("\n" + "=" * 60)
    print("🚀 Log File Analyzer Flask App Started")
    print("🌐 Open this URL in your browser:")
    print(f"👉 {url}")
    print("=" * 60 + "\n")

    # Automatically open browser
    webbrowser.open(url)

    app.run(debug=True)
