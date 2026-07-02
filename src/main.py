from generate import generate, generate_page


def main():
    generate("./public", "./static")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
