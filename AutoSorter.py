from pathlib import Path 
import shutil

SOURCE= Path.home() /"Desktop"/"TEST DOWNLOAD"
DESTINATION= Path.home()/"Desktop"/"TEST UNIVERSITY"

DRY_RUN= False

COURSE_IDS={
    "49995":"PRINCIPLES OF SOFTWARE ENGINEERING",
    "49028":"ADVANCED PROGRAMMING"
}

def read_note(file):
    try:
        with open(f"{file}:Zone.Identifier",encoding="utf-8",errors="ignore") as f:
            return f.read()
    except OSError:
        return""

def get_course_id(note):
    for line in note.splitlines():
        if line.startswith("ReferrerUrl="):
            url = line.split("=", 1)[1]
            if "course/view.php?id=" in url:
                return url.split("id=")[1].split("&")[0]
    return None

def unique_path(target):
    counter = 1
    new = target
    while new.exists():
        new = target.with_name(f"{target.stem} ({counter}){target.suffix}")
        counter += 1
    return new

def organise():
    for file in SOURCE.iterdir():
        if not file.is_file():
            continue

        note = read_note(file)
        course_id = get_course_id(note)

        if course_id not in COURSE_IDS:
            print(f"SKIP: {file.name}")
            continue

        module = COURSE_IDS[course_id]
        target_dir = DESTINATION / module
        destination = unique_path(target_dir / file.name)

        if DRY_RUN:
            print(f"WOULD MOVE: {file.name} -> {destination}")
        else:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(destination))
            print(f"MOVED: {file.name} -> {destination}")


if __name__ == "__main__":
    organise()

