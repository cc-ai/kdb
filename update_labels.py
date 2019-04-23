import os
from urllib.request import urlopen
from pathlib import Path

from bs4 import BeautifulSoup

# This file is used to sync labels from kdb/issues/labels with their
# mentions as shields in md documents, such as in domains/Readme.md


def reset(shields):
    """Put all "visited" values of shields to False

    Args:
        shields (dict): each dict in shields is a dict with a boolean key "visited"
    """
    for s in shields.values():
        s["visited"] = False


def update_shields(labels_path, shields_path):
    """Write shields as md image reference to be copied at the end of a file
    for instance :
        [bug]: https://img.shields.io/badge/bug-d73a4a.svg
    As parsing is fairly simple, it is done line by line in order to
    use as few dependencies as possible. PyYAML would do fine otherwise

    Args:
        labels_path (pathlib.Path): where to read the labels as yml
        shields_path (pathlib.Path): where to write the shields as txt
    """
    if labels_path.exists():
        # read file
        with labels_path.open() as f:
            lines = f.readlines()
        shields = []
        names = []
        # skip first line
        i = 1
        while i < len(lines):
            l = lines[i]
            # begining of a label
            if "  - name" in l:
                name = l.split("name:")[-1].strip().replace('"', "")
                color = lines[i + 1].split("color:")[-1].strip().replace('"', "")
                shields.append(
                    f"https://img.shields.io/badge/{name}-{color}.svg".replace(
                        " ", "%20"
                    )
                )
                names.append(name)
                # find next label
                i += 2 if i < len(lines) - 1 and "  - name" not in lines[i + 2] else 1
            else:
                # skip line
                i += 1
        # format shield strings
        shields_lines = sorted(f"[{n}]: {s}" for n, s in zip(names, shields))
        # write to file
        with open(shields_path, "w") as f:
            f.write("\n".join(shields_lines))


def parse_item(item):
    """Get label dict from parse HTML item from BeautifulSoup
    Example output:
    {
        "color": "ffffff",
        "description": "",
        "name": "bug"
    }

    Args:
        item (BeautifulSoup.element): .label-link element from the github labels page
    
    Returns:
        dict: label dict formatted to be then used in yml
    """
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
    """Get yml format for label

    Args:
        label (dict): dictionnary if labels with keys color, name and description
        as strings, possibly empty

    Returns:
        str: yml formatted dict, as a yml list item
    """
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

    # Constants
    labels_url = "https://github.com/cc-ai/kdb/issues/labels"
    yml_path = Path() / "workflow" / "labels.yml"
    shield_path = Path() / "workflow" / "shields.txt"
    labels_class = ".label-link"
    split_marker = "]: https://img.shields.io/badge/"

    # Fetching kdb's issue labels
    html = urlopen(labels_url).read()
    # Parsing HTML
    bs = BeautifulSoup(html, "lxml")

    print("Fetched and parsed", labels_url)

    # extracting labels from .label-link elements
    items = bs.select(labels_class)
    labels = map(parse_item, items)

    # formatting to yml
    yml_text = "labels:\n"
    yml_text += "\n".join(map(get_label_yml, labels))

    # writing to target file
    with yml_path.open("w") as f:
        f.write(yml_text)

    print("Wrote new labels to", str(yml_path))

    # write shields according to labels fetched
    update_shields(yml_path, shield_path)

    with shield_path.open("r") as f:
        shields = f.readlines()

    # parse updated shields
    shields = {
        s.split(split_marker)[0][1:]: {"text": s.strip(), "visited": False}
        for s in shields
    }

    # Updating shields in all md files
    candidates = Path().glob("**/*.md")
    for cand in candidates:
        text = cand.open("r").read()
        # there is a shield image used in this candidate md file
        if split_marker in text:
            print("Updating", str(cand))
            lines = text.split("\n")
            # lines of new file with updated shields
            new_lines = []

            for i, l in enumerate(lines):
                if split_marker in l:
                    # this line is a shield reference
                    name = l.split(split_marker)[0][1:]
                    if name in shields:
                        # shield still exist but may have an outdated color
                        new_lines.append(shields[name]["text"])
                        shields[name]["visited"] = True
                        if shields[name]["text"] != l:
                            # color indeed has changed
                            print("Updating line", i, ":", l)
                else:
                    # no shield, use unaltered line
                    new_lines.append(l)

            for shield in shields.values():
                # add not listed shields to the end of file,
                # if someone wants to use it at some point
                if not shield["visited"]:
                    new_lines.append(shield["text"])
                    print("Adding", shield["text"])
            # write updated file
            with cand.open("w") as f:
                f.writelines("\n".join(new_lines))
            print()
        # put shields back to visited: False
        reset(shields)
