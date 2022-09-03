def color_format(
    text: str,
    styled: str = "italics", fg: str = "blue", bg: str = "black",
    no_bg: bool = False
) -> str:
    styled_text = directive + style[styled]
    fg_text = directive + colour[fg]
    bg_text = directive + background[bg]
    clean_code = directive + style['clean']
    return \
        styled_text + fg_text + bg_text + text + \
        clean_code if no_bg else styled_text +\
        fg_text + text + clean_code


if __name__ == "__main__":
    print(color_format("This is default blue text"))
    print(color_format("This is red text", fg="red"))
    print(color_format("▓", fg="white"))
