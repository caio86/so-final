import matplotlib.pyplot as plt
import pandas as pd

# Docker
## txt
d_gz_txt_500 = pd.read_csv("./saida-docker/gz-txt_500MB.txt.csv", sep=";")
d_gz_txt_5 = pd.read_csv("./saida-docker/gz-txt_5MB.txt.csv", sep=";")
d_bz_txt_500 = pd.read_csv("./saida-docker/bz-txt_500MB.txt.csv", sep=";")
d_bz_txt_5 = pd.read_csv("./saida-docker/bz-txt_5MB.txt.csv", sep=";")
d_xz_txt_500 = pd.read_csv("./saida-docker/xz-txt_500MB.txt.csv", sep=";")
d_xz_txt_5 = pd.read_csv("./saida-docker/xz-txt_5MB.txt.csv", sep=";")

## png
d_gz_png_500 = pd.read_csv("./saida-docker/gz-png_500MB.png.csv", sep=";")
d_gz_png_5 = pd.read_csv("./saida-docker/gz-png_5MB.png.csv", sep=";")
d_bz_png_500 = pd.read_csv("./saida-docker/bz-png_500MB.png.csv", sep=";")
d_bz_png_5 = pd.read_csv("./saida-docker/bz-png_5MB.png.csv", sep=";")
d_xz_png_500 = pd.read_csv("./saida-docker/xz-png_500MB.png.csv", sep=";")
d_xz_png_5 = pd.read_csv("./saida-docker/xz-png_5MB.png.csv", sep=";")

## mp4
d_gz_mp4_500 = pd.read_csv("./saida-docker/gz-mp4_500MB.mp4.csv", sep=";")
d_gz_mp4_5 = pd.read_csv("./saida-docker/gz-mp4_5MB.mp4.csv", sep=";")
d_bz_mp4_500 = pd.read_csv("./saida-docker/bz-mp4_500MB.mp4.csv", sep=";")
d_bz_mp4_5 = pd.read_csv("./saida-docker/bz-mp4_5MB.mp4.csv", sep=";")
d_xz_mp4_500 = pd.read_csv("./saida-docker/xz-mp4_500MB.mp4.csv", sep=";")
d_xz_mp4_5 = pd.read_csv("./saida-docker/xz-mp4_5MB.mp4.csv", sep=";")

# Podman
## txt
p_gz_txt_500 = pd.read_csv("./saida-podman/gz-txt_500MB.txt.csv", sep=";")
p_gz_txt_5 = pd.read_csv("./saida-podman/gz-txt_5MB.txt.csv", sep=";")
p_bz_txt_500 = pd.read_csv("./saida-podman/bz-txt_500MB.txt.csv", sep=";")
p_bz_txt_5 = pd.read_csv("./saida-podman/bz-txt_5MB.txt.csv", sep=";")
p_xz_txt_500 = pd.read_csv("./saida-podman/xz-txt_500MB.txt.csv", sep=";")
p_xz_txt_5 = pd.read_csv("./saida-podman/xz-txt_5MB.txt.csv", sep=";")

## png
p_gz_png_500 = pd.read_csv("./saida-podman/gz-png_500MB.png.csv", sep=";")
p_gz_png_5 = pd.read_csv("./saida-podman/gz-png_5MB.png.csv", sep=";")
p_bz_png_500 = pd.read_csv("./saida-podman/bz-png_500MB.png.csv", sep=";")
p_bz_png_5 = pd.read_csv("./saida-podman/bz-png_5MB.png.csv", sep=";")
p_xz_png_500 = pd.read_csv("./saida-podman/xz-png_500MB.png.csv", sep=";")
p_xz_png_5 = pd.read_csv("./saida-podman/xz-png_5MB.png.csv", sep=";")

## mp4
p_gz_mp4_500 = pd.read_csv("./saida-podman/gz-mp4_500MB.mp4.csv", sep=";")
p_gz_mp4_5 = pd.read_csv("./saida-podman/gz-mp4_5MB.mp4.csv", sep=";")
p_bz_mp4_500 = pd.read_csv("./saida-podman/bz-mp4_500MB.mp4.csv", sep=";")
p_bz_mp4_5 = pd.read_csv("./saida-podman/bz-mp4_5MB.mp4.csv", sep=";")
p_xz_mp4_500 = pd.read_csv("./saida-podman/xz-mp4_500MB.mp4.csv", sep=";")
p_xz_mp4_5 = pd.read_csv("./saida-podman/xz-mp4_5MB.mp4.csv", sep=";")


def create_graph(
    data_sources: dict[str, list[pd.DataFrame]],
    compactador="XXXXX",
    tipo_arquivo="XXXXX",
):
    metricas = [
        "User time",
        "System time",
        "System input",
        "System output",
        "Swaps",
        "Voluntary context switches",
        "Involuntary context switches",
    ]

    unidades = [
        "Segundos",
        "Segundos",
        "QTD.",
        "QTD.",
        "QTD.",
        "QTD.",
        "QTD.",
    ]

    for idx, metric in enumerate(metricas):
        # Prepare data for plotting
        labels = []
        means = []

        for category in data_sources:
            for _, dataframe in enumerate(data_sources[category]):
                labels.append(category)
                means.append(dataframe[metric].mean())
        # Create the plot
        plt.figure(figsize=(12, 8), dpi=300)

        # Create bars with color coding by compression type
        colors = []
        for label in labels:
            if "docker" in label:
                colors.append("skyblue")
            elif "podman" in label:
                colors.append("salmon")

        bars = plt.bar(labels, means, color=colors, edgecolor="black", linewidth=0.5)

        # Add value labels on top of each bar
        for bar, mean in zip(bars, means):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + max(means) * 0.01,
                f"{mean:.2f}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

        plt.title(
            f"{metric} usando {compactador} em {tipo_arquivo}", fontsize=14, pad=20
        )
        plt.xlabel("Cenários", fontsize=12)
        plt.ylabel(unidades[idx], fontsize=12)
        plt.grid(True, axis="y", alpha=0.3)

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha="right")

        # Adjust layout to prevent clipping of labels
        plt.tight_layout()

        # Add a legend for compression types
        import matplotlib.patches as mpatches

        legend_elements = [
            mpatches.Patch(facecolor="skyblue", edgecolor="black", label="docker"),
            mpatches.Patch(facecolor="salmon", edgecolor="black", label="podman"),
        ]
        plt.legend(handles=legend_elements, loc="best")

        plt.savefig(fname=f"./graph-{metric}.png", bbox_inches="tight")


# Corresponding data for each category
data_sources = {
    "docker-5MB": [d_gz_txt_5],
    "podman-5MB": [p_gz_txt_5],
    "docker-500MB": [d_gz_txt_500],
    "podman-500MB": [p_gz_txt_500],
}

create_graph(data_sources, "gzip2", "txt")
