import pandas as pd


def getC1_4():
    d_gz_txt_500 = pd.read_csv("./saida-docker/gz-txt_500MB.txt.csv", sep=";")
    d_gz_txt_5 = pd.read_csv("./saida-docker/gz-txt_5MB.txt.csv", sep=";")
    p_gz_txt_500 = pd.read_csv("./saida-podman/gz-txt_500MB.txt.csv", sep=";")
    p_gz_txt_5 = pd.read_csv("./saida-podman/gz-txt_5MB.txt.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_gz_txt_5],
        "podman-5MB": [p_gz_txt_5],
        "docker-500MB": [d_gz_txt_500],
        "podman-500MB": [p_gz_txt_500],
    }

    return data_sources, "gzip", "txt"


def getC5_8():
    d_gz_png_500 = pd.read_csv("./saida-docker/gz-png_500MB.png.csv", sep=";")
    d_gz_png_5 = pd.read_csv("./saida-docker/gz-png_5MB.png.csv", sep=";")
    p_gz_png_500 = pd.read_csv("./saida-podman/gz-png_500MB.png.csv", sep=";")
    p_gz_png_5 = pd.read_csv("./saida-podman/gz-png_5MB.png.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_gz_png_5],
        "podman-5MB": [p_gz_png_5],
        "docker-500MB": [d_gz_png_500],
        "podman-500MB": [p_gz_png_500],
    }

    return data_sources, "gzip", "png"


def getC9_12():
    d_gz_mp4_500 = pd.read_csv("./saida-docker/gz-mp4_500MB.mp4.csv", sep=";")
    d_gz_mp4_5 = pd.read_csv("./saida-docker/gz-mp4_5MB.mp4.csv", sep=";")
    p_gz_mp4_500 = pd.read_csv("./saida-podman/gz-mp4_500MB.mp4.csv", sep=";")
    p_gz_mp4_5 = pd.read_csv("./saida-podman/gz-mp4_5MB.mp4.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_gz_mp4_5],
        "podman-5MB": [p_gz_mp4_5],
        "docker-500MB": [d_gz_mp4_500],
        "podman-500MB": [p_gz_mp4_500],
    }

    return data_sources, "gzip", "mp4"


def getC13_16():
    d_bz_txt_500 = pd.read_csv("./saida-docker/bz-txt_500MB.txt.csv", sep=";")
    d_bz_txt_5 = pd.read_csv("./saida-docker/bz-txt_5MB.txt.csv", sep=";")
    p_bz_txt_500 = pd.read_csv("./saida-podman/bz-txt_500MB.txt.csv", sep=";")
    p_bz_txt_5 = pd.read_csv("./saida-podman/bz-txt_5MB.txt.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_bz_txt_5],
        "podman-5MB": [p_bz_txt_5],
        "docker-500MB": [d_bz_txt_500],
        "podman-500MB": [p_bz_txt_500],
    }

    return data_sources, "bzip2", "txt"


def getC17_20():
    d_bz_png_500 = pd.read_csv("./saida-docker/bz-png_500MB.png.csv", sep=";")
    d_bz_png_5 = pd.read_csv("./saida-docker/bz-png_5MB.png.csv", sep=";")
    p_bz_png_500 = pd.read_csv("./saida-podman/bz-png_500MB.png.csv", sep=";")
    p_bz_png_5 = pd.read_csv("./saida-podman/bz-png_5MB.png.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_bz_png_5],
        "podman-5MB": [p_bz_png_5],
        "docker-500MB": [d_bz_png_500],
        "podman-500MB": [p_bz_png_500],
    }

    return data_sources, "bzip2", "png"


def getC21_24():
    d_bz_mp4_500 = pd.read_csv("./saida-docker/bz-mp4_500MB.mp4.csv", sep=";")
    d_bz_mp4_5 = pd.read_csv("./saida-docker/bz-mp4_5MB.mp4.csv", sep=";")
    p_bz_mp4_500 = pd.read_csv("./saida-podman/bz-mp4_500MB.mp4.csv", sep=";")
    p_bz_mp4_5 = pd.read_csv("./saida-podman/bz-mp4_5MB.mp4.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_bz_mp4_5],
        "podman-5MB": [p_bz_mp4_5],
        "docker-500MB": [d_bz_mp4_500],
        "podman-500mb": [p_bz_mp4_500],
    }

    return data_sources, "bzip2", "mp4"


def getC25_28():
    d_xz_txt_500 = pd.read_csv("./saida-docker/xz-txt_500MB.txt.csv", sep=";")
    d_xz_txt_5 = pd.read_csv("./saida-docker/xz-txt_5MB.txt.csv", sep=";")
    p_xz_txt_500 = pd.read_csv("./saida-podman/xz-txt_500MB.txt.csv", sep=";")
    p_xz_txt_5 = pd.read_csv("./saida-podman/xz-txt_5MB.txt.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_xz_txt_5],
        "podman-5MB": [p_xz_txt_5],
        "docker-500MB": [d_xz_txt_500],
        "podman-500mb": [p_xz_txt_500],
    }

    return data_sources, "xz", "txt"


def getC29_32():
    d_xz_png_500 = pd.read_csv("./saida-docker/xz-png_500MB.png.csv", sep=";")
    d_xz_png_5 = pd.read_csv("./saida-docker/xz-png_5MB.png.csv", sep=";")
    p_xz_png_500 = pd.read_csv("./saida-podman/xz-png_500MB.png.csv", sep=";")
    p_xz_png_5 = pd.read_csv("./saida-podman/xz-png_5MB.png.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_xz_png_5],
        "podman-5MB": [p_xz_png_5],
        "docker-500MB": [d_xz_png_500],
        "podman-500mb": [p_xz_png_500],
    }

    return data_sources, "xz", "png"


def getC33_36():
    d_xz_mp4_500 = pd.read_csv("./saida-docker/xz-mp4_500MB.mp4.csv", sep=";")
    d_xz_mp4_5 = pd.read_csv("./saida-docker/xz-mp4_5MB.mp4.csv", sep=";")
    p_xz_mp4_500 = pd.read_csv("./saida-podman/xz-mp4_500MB.mp4.csv", sep=";")
    p_xz_mp4_5 = pd.read_csv("./saida-podman/xz-mp4_5MB.mp4.csv", sep=";")

    data_sources = {
        "docker-5MB": [d_xz_mp4_5],
        "podman-5MB": [p_xz_mp4_5],
        "docker-500MB": [d_xz_mp4_500],
        "podman-500mb": [p_xz_mp4_500],
    }

    return data_sources, "xz", "mp4"


def GTFO():
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

    data_sources = {
        "d_gz_txt_5": [d_gz_txt_5],
        "d_gz_png_5": [d_gz_png_5],
        "d_gz_mp4_5": [d_gz_mp4_5],
        "d_bz_txt_5": [d_bz_txt_5],
        "d_bz_png_5": [d_bz_png_5],
        "d_bz_mp4_5": [d_bz_mp4_5],
        "d_xz_txt_5": [d_xz_txt_5],
        "d_xz_png_5": [d_xz_png_5],
        "d_xz_mp4_5": [d_xz_mp4_5],
        "p_gz_txt_5": [p_gz_txt_5],
        "p_gz_png_5": [p_gz_png_5],
        "p_gz_mp4_5": [p_gz_mp4_5],
        "p_bz_txt_5": [p_bz_txt_5],
        "p_bz_png_5": [p_bz_png_5],
        "p_bz_mp4_5": [p_bz_mp4_5],
        "p_xz_txt_5": [p_xz_txt_5],
        "p_xz_png_5": [p_xz_png_5],
        "p_xz_mp4_5": [p_xz_mp4_5],
        "d_gz_txt_500": [d_gz_txt_500],
        "d_gz_png_500": [d_gz_png_500],
        "d_gz_mp4_500": [d_gz_mp4_500],
        "d_bz_txt_500": [d_bz_txt_500],
        "d_bz_png_500": [d_bz_png_500],
        "d_bz_mp4_500": [d_bz_mp4_500],
        "d_xz_txt_500": [d_xz_txt_500],
        "d_xz_png_500": [d_xz_png_500],
        "d_xz_mp4_500": [d_xz_mp4_500],
        "p_gz_txt_500": [p_gz_txt_500],
        "p_gz_png_500": [p_gz_png_500],
        "p_gz_mp4_500": [p_gz_mp4_500],
        "p_bz_txt_500": [p_bz_txt_500],
        "p_bz_png_500": [p_bz_png_500],
        "p_bz_mp4_500": [p_bz_mp4_500],
        "p_xz_txt_500": [p_xz_txt_500],
        "p_xz_png_500": [p_xz_png_500],
        "p_xz_mp4_500": [p_xz_mp4_500],
    }

    return data_sources, "?!?!?!?", "?!?!?!?"
