import re


def on_page_markdown(markdown, **kwargs):
    counter = 1
    last_number = None

    def replacer(match):
        nonlocal counter, last_number
        token = match.group(0)
        if token == "{article}":
            result = f"Art. {str(counter)}"
            last_number = counter
            counter += 1
            return result
        elif token == "{article-bis}":
            if last_number is None:
                raise ValueError("{article-bis} appeared before any {article}")
            return f"Art. {last_number}bis"
        elif token == "{article-ter}":
            if last_number is None:
                raise ValueError("{article-ter} appeared before any {article}")
            return f"Art. {last_number}ter"
        elif token == "{article-quater}":
            if last_number is None:
                raise ValueError("{article-quater} appeared before any {article}")
            return f"Art. {last_number}quater"
        elif token == "{article-quinquies}":
            if last_number is None:
                raise ValueError("{article-quinquies} appeared before any {article}")
            return f"Art. {last_number}quinquies"
        elif token == "{article-sexies}":
            if last_number is None:
                raise ValueError("{article-sexies} appeared before any {article}")
            return f"Art. {last_number}sexies"
        elif token == "{article-septies}":
            if last_number is None:
                raise ValueError("{article-septies} appeared before any {article}")
            return f"Art. {last_number}septies"
        else:
            return token  # Should not happen

    # Replace all occurrences of {article} or derivatives
    return re.sub(r"\{article(?:-bis|-ter|-quater|-quinquies|-sexies|-septies)?\}", replacer, markdown)

    