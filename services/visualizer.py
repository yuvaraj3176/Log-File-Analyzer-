import matplotlib.pyplot as plt

def generate_error_chart(error_counts, output_path):
    plt.figure()
    plt.bar(error_counts.keys(), error_counts.values())
    plt.xlabel("Error Code")
    plt.ylabel("Count")
    plt.title("HTTP Error Distribution")
    plt.savefig(output_path)
    plt.close()
