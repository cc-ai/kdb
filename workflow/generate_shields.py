from pathlib import Path

if __name__ == "__main__":
    labels_path = Path() / "labels.yml"
    if labels_path.exists():
        with labels_path.open() as f:
            lines = f.readlines()
        shields = []
        names = []
        i = 1
        while i < len(lines):
            l = lines[i]
            if "  - name" in l:
                name = l.split("name:")[-1].strip()
                color = lines[i + 1].split("color:")[-1].strip()
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

        with open(Path() / "shields.txt", "w") as f:
            f.write("\n".join(shields_lines))
