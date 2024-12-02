import importlib

from absl import app, flags
from absl import logging as log

FLAGS = flags.FLAGS
flags.DEFINE_integer("day", None, "day number to run")
flags.DEFINE_string("input", "puzzle", "input/example data name")

flags.mark_flags_as_required(["day"])


def main(argv):
    del argv

    try:
        day = importlib.import_module(f"py.day{FLAGS.day:02}")
    except ImportError:
        log.fatal(
            "Failed to import solution for day %d (does //py:day%02d.py exist?)",
            FLAGS.day,
            FLAGS.day,
        )

    with open(f"input/day{FLAGS.day:02}_{FLAGS.input}.txt", "r", encoding="utf-8") as f:
        part_1_answer = getattr(day, "part_1", lambda _: None)(f)
        f.seek(0)
        part_2_answer = getattr(day, "part_2", lambda _: None)(f)

    if part_1_answer is not None:
        log.info("Part 1: %s", part_1_answer)
    else:
        log.warning("Part 1 not implemented (no part_2 function)")
    if part_2_answer is not None:
        log.info("Part 2: %s", part_2_answer)
    else:
        log.warning("Part 2 not implemented (no part_2 function)")


if __name__ == "__main__":
    app.run(main)
