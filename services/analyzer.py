import pandas as pd

def analyze_logs(parsed_data):
    if not parsed_data:
        return {
            "total_errors": 0,
            "error_counts": {},
            "top_ips": {}
        }

    df = pd.DataFrame(parsed_data)

    # ✅ Ensure required columns exist
    required_columns = {"status", "ip"}
    if not required_columns.issubset(df.columns):
        return {
            "total_errors": 0,
            "error_counts": {},
            "top_ips": {}
        }

    # Convert status to string (extra safety)
    df["status"] = df["status"].astype(str)

    error_df = df[df["status"] != "200"]

    error_counts = error_df["status"].value_counts().to_dict()
    top_ips = error_df["ip"].value_counts().head(5).to_dict()

    return {
        "total_errors": len(error_df),
        "error_counts": error_counts,
        "top_ips": top_ips
    }
