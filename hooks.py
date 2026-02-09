import re


DEBUG = False

LAW_CODES = {}


def on_page_markdown(markdown, *, page, config, files):
    counter = 1
    last_number = 0
    file_path = page.file.src_path.replace(f"/{page.file.name}.md", "")

    if DEBUG:
        print(page.file.src_path)

    if ("{reset-law-code}".lower() in markdown.lower()) or (
        ("{law-code}".lower() in markdown.lower())
        # and (file_path not in LAW_CODES.keys())
    ):
        LAW_CODES[file_path] = 1

    def replacer(match):
        nonlocal counter, last_number, file_path

        is_lawcode = file_path in LAW_CODES.keys()

        local_counter = 0
        if is_lawcode:
            local_counter = LAW_CODES[file_path]
        else:
            local_counter = counter

        token = match.group(0)
        result = ""

        if DEBUG:
            print(f"is law code: {is_lawcode}")
            print(f"counter: {counter}")
            print(f"local_counter: {counter}")
            print(f"Law codes: {LAW_CODES}")
            print(f"Current law code: {LAW_CODES.get(file_path)}")

        if token == "{article}":
            result = f"Art. {str(local_counter)}"
            last_number = local_counter
            local_counter += 1
        elif token == "{article-bis}":
            if last_number is None:
                raise ValueError("{article-bis} appeared before any {article}")
            result = f"Art. {last_number}bis"
        elif token == "{article-ter}":
            if last_number is None:
                raise ValueError("{article-ter} appeared before any {article}")
            result = f"Art. {last_number}ter"
        elif token == "{article-quater}":
            if last_number is None:
                raise ValueError("{article-quater} appeared before any {article}")
            result = f"Art. {last_number}quater"
        elif token == "{article-quinquies}":
            if last_number is None:
                raise ValueError("{article-quinquies} appeared before any {article}")
            result = f"Art. {last_number}quinquies"
        elif token == "{article-sexies}":
            if last_number is None:
                raise ValueError("{article-sexies} appeared before any {article}")
            result = f"Art. {last_number}sexies"
        elif token == "{article-septies}":
            if last_number is None:
                raise ValueError("{article-septies} appeared before any {article}")
            result = f"Art. {last_number}septies"
        else:
            result = token  # Should not happen

        if is_lawcode:
            LAW_CODES[file_path] = local_counter
        else:
            counter = local_counter

        return result

    markdown = (
        re.sub(
            r"\{article(?:-bis|-ter|-quater|-quinquies|-sexies|-septies)?\}",
            replacer,
            markdown,
        )
        .replace("{law-code}", "")
        .replace("{reset-law-code}", "")
    )

    # Replace all occurrences of {article} or derivatives
    return markdown
