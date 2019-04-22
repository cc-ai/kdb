import os
from urllib.request import urlopen
from pathlib import Path

from bs4 import BeautifulSoup


def reset(shields):
    for s in shields.values():
        s["visited"] = False


def update_shields(labels_path, shields_path):
    if labels_path.exists():
        with labels_path.open() as f:
            lines = f.readlines()
        shields = []
        names = []
        i = 1
        while i < len(lines):
            l = lines[i]
            if "  - name" in l:
                name = l.split("name:")[-1].strip().replace('"', "")
                color = lines[i + 1].split("color:")[-1].strip().replace('"', "")
                shields.append(
                    f"https://img.shields.io/badge/{name}-{color}.svg".replace(
                        " ", "%20"
                    )
                )
                names.append(name)
                i += 2
            else:
                i += 1
        shields_lines = sorted(list(f"[{n}]: {s}" for n, s in zip(names, shields)))

        with open(shields_path, "w") as f:
            f.write("\n".join(shields_lines))


def parse_item(item):
    return {
        "description": item.get("title", ""),
        "name": item.find("span").get_text(),
        "color": [
            col.split("background-color: ")[1].replace("#", "")
            for col in item.get_attribute_list("style")[0].split(";")
            if "background-color" in col
        ][0],
    }


def get_label_yml(label):
    text = f'  - name: "{label["name"]}"\n'
    text += f'    color: "{label["color"]}"\n'
    text += f'    description: "{label["description"]}"\n'
    return text


if __name__ == "__main__":

    # Running this file from the root of the repository will:
    # 1 - fetch all labels from the `labels_url` page
    # 2 - write them into a yml file in workflow/
    # 3 - update shields markdowns in workflow/shields.txt
    # 4 - update all shields links in all markdown files which use them

    labels_url = "https://github.com/cc-ai/kdb/issues/labels"
    yml_path = Path() / "workflow" / "labels.yml"
    shield_path = Path() / "workflow" / "shields.txt"
    shield_py = "workflow/generate_shields.py"
    labels_class = ".label-link"
    split_marker = "]: https://img.shields.io/badge/"

    html = urlopen(labels_url).read()
    bs = BeautifulSoup(html, "lxml")

    print("Fetched and parsed", labels_url)

    items = bs.select(labels_class)
    labels = map(parse_item, items)

    yml_text = "labels:\n"
    yml_text += "\n".join(map(get_label_yml, labels))

    with yml_path.open("w") as f:
        f.write(yml_text)

    print("Wrote new labels to", str(yml_path))

    update_shields(yml_path, shield_path)

    with shield_path.open("r") as f:
        shields = f.readlines()
    shields = {
        s.split(split_marker)[0][1:]: {"text": s.strip(), "visited": False}
        for s in shields
    }

    candidates = Path().glob("**/*.md")
    for cand in candidates:
        text = cand.open("r").read()
        if "![][" in text:
            print("Updating", str(cand))
            lines = text.split("\n")
            new_lines = []

            for i, l in enumerate(lines):
                if split_marker in l:
                    name = l.split(split_marker)[0][1:]
                    if name in shields:
                        new_lines.append(shields[name]["text"])
                        shields[name]["visited"] = True
                        print("Updating line", i, ":", l)
                else:
                    new_lines.append(l)

            for shield in shields.values():
                if not shield["visited"]:
                    new_lines.append(shield["text"])
            with cand.open("w") as f:
                f.writelines("\n".join(new_lines))
        reset(shields)
