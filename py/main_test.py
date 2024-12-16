import importlib

from absl.testing import absltest, parameterized


class AdventTest(parameterized.TestCase):

    @parameterized.parameters(
        {
            "day": "day01",
            "input": "ex0",
            "part_1": "11",
            "part_2": "31",
        },
        {
            "day": "day01",
            "input": "puzzle",
            "part_1": "2166959",
            "part_2": "23741109",
        },
        {
            "day": "day02",
            "input": "ex0",
            "part_1": "2",
            "part_2": "4",
        },
        {
            "day": "day02",
            "input": "puzzle",
            "part_1": "486",
            "part_2": "540",
        },
        {
            "day": "day03",
            "input": "ex0",
            "part_1": "161",
            "part_2": None,
        },
        {
            "day": "day03",
            "input": "ex1",
            "part_1": None,
            "part_2": "48",
        },
        {
            "day": "day03",
            "input": "puzzle",
            "part_1": "174336360",
            "part_2": "88802350",
        },
        {
            "day": "day04",
            "input": "ex0",
            "part_1": "18",
            "part_2": "9",
        },
        {
            "day": "day04",
            "input": "puzzle",
            "part_1": "2517",
            "part_2": "1960",
        },
        {
            "day": "day05",
            "input": "ex0",
            "part_1": "143",
            "part_2": "123",
        },
        {
            "day": "day05",
            "input": "puzzle",
            "part_1": "5948",
            "part_2": "3062",
        },
        {
            "day": "day06",
            "input": "ex0",
            "part_1": "41",
            "part_2": "6",
        },
        {
            "day": "day06",
            "input": "puzzle",
            "part_1": "5086",
            "part_2": None,
        },
        {
            "day": "day07",
            "input": "ex0",
            "part_1": "3749",
            "part_2": "11387",
        },
        {
            "day": "day07",
            "input": "puzzle",
            "part_1": "1298103531759",
            "part_2": "140575048428831",
        },
        {
            "day": "day08",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day08",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day09",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day09",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day10",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day10",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day11",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day11",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day12",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day12",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day13",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day13",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day14",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day14",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day15",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day15",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day16",
            "input": "ex0",
            "part_1": None,
            "part_2": None,
        },
        {
            "day": "day16",
            "input": "puzzle",
            "part_1": None,
            "part_2": None,
        },
    )
    def testAdventResult(self, day, input, part_1, part_2):
        if not part_1 and not part_2:
            return
        module = importlib.import_module(f"py.{day}")
        with open(f"input/{day}_{input}.txt", "r", encoding="utf-8") as f:
            if part_1:
                part_1_answer = str(getattr(module, "part_1")(f))
                self.assertEqual(part_1, part_1_answer)
            f.seek(0)
            if part_2:
                part_2_answer = str(getattr(module, "part_2")(f))
                self.assertEqual(part_2, part_2_answer)


if __name__ == "__main__":
    absltest.main()
