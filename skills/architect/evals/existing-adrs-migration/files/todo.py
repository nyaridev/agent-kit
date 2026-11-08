import argparse
import json
from pathlib import Path

DB = Path("todos.json")


def load():
    return json.loads(DB.read_text()) if DB.exists() else []


def save(todos):
    DB.write_text(json.dumps(todos, indent=2))


def add(text):
    todos = load()
    todos.append({"text": text, "done": False})
    save(todos)
    return len(todos)


def done(index):
    todos = load()
    todos[index - 1]["done"] = True
    save(todos)


def main(argv=None):
    p = argparse.ArgumentParser(prog="todo")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    a = sub.add_parser("add")
    a.add_argument("text")
    d = sub.add_parser("done")
    d.add_argument("index", type=int)
    args = p.parse_args(argv)
    if args.cmd == "add":
        print(f"added #{add(args.text)}")
    elif args.cmd == "done":
        done(args.index)
        print("ok")
    else:
        for i, t in enumerate(load(), 1):
            print(f"{i}. [{'x' if t['done'] else ' '}] {t['text']}")


if __name__ == "__main__":
    main()
