#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd


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
        stds = []

        for category in data_sources:
            for _, dataframe in enumerate(data_sources[category]):
                labels.append(category)
                means.append(dataframe[metric].mean())
                stds.append(dataframe[metric].std())
        # Create the plot
        plt.figure(figsize=(12, 8), dpi=300)

        # Create bars with color coding by compression type
        colors = []
        for label in labels:
            if "docker" in label:
                colors.append("skyblue")
            elif "podman" in label:
                colors.append("salmon")

        bars = plt.bar(
            labels,
            means,
            color=colors,
            edgecolor="black",
            linewidth=0.8,
            yerr=stds,
            capsize=5,
            alpha=0.8,
            error_kw={"elinewidth": 1.5},
        )

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


# # Corresponding data for each category
# data_sources = {
#     "docker-5MB": [d_gz_txt_5],
#     "podman-5MB": [p_gz_txt_5],
#     "docker-500MB": [d_gz_txt_500],
#     "podman-500MB": [p_gz_txt_500],
# }
#
# create_graph(data_sources, "gzip2", "txt")
