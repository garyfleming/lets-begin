import re

background_img_pattern = re.compile("^!\[\]\((.*)\)")

with open('lets-begin-marp.md', 'w') as output:
    with open("lets-begin.md") as file:
        for line in file:
            if line.startswith("^ "):
                output.write("<!-- "+line.replace('^ ', '').rstrip()+" -->\n")
            if background_img_pattern.match(line):
                output.write(line)
            else:
                output.write(line)