FILENAME = "computer_obaachan"
FIN = "../../francocurotto.github.io/jp_lyrics/" + FILENAME + ".md"
FOUT = "../content/projects/jp_lyrics/" + FILENAME + ".shtml"
TITLE = FILENAME.replace("_", " ").title()
PREAMBLE = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<title>Franco's Website</title>
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<link rel=\"stylesheet\" href=\"/style.css\">
</head>

<body>
<!--#include virtual=\"/templates/header.html\" -->

<main>
<h2>{TITLE}</h2>
<div class=\"lyrics\">"""

ENDING = """</div>
</main>

<!--#include virtual=\"/templates/footer.html\" -->
</body>"""

with open(FIN, "r") as fin, open(FOUT, "w") as fout:
    # add preamble to fout
    fout.write(PREAMBLE)
    # add lyrics
    for line in fin:
        line = line.strip()
        # ignore parts
        if line.startswith("---"):
            continue
        elif line.startswith("site:"):
            continue
        elif line.startswith("title:"):
            continue
        elif line == ".":
            continue
        # case lyrics
        else:
            # case english
            if line.startswith("**"):
                line = line.replace("**", "")
                line = "<strong>" + line + "</strong>"
            # add line to file
            fout.write(line+"\n")
    # add ending to fout
    fout.write(ENDING)
