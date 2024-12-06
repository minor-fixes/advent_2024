class Rule:
    def __init__(self, before, after):
        self.key = frozenset([before, after])
        self.first = before

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Rules:
    def __init__(self, rules_text):
        self.rules = dict()
        for rule_text in rules_text.split():
            before, after = rule_text.split("|")
            rule = Rule(int(before), int(after))
            self.rules[rule] = rule

    def conforms(self, update):
        for i in range(len(update)):
            for j in range(i+1, len(update)):
                rule = self.rules.get(Rule(update[i], update[j]), None)
                if rule and update[i] != rule.first:
                    return False
        return True

    def fix_one(self, update):
        for i in range(len(update)):
            for j in range(i+1, len(update)):
                rule = self.rules.get(Rule(update[i], update[j]), None)
                if rule and update[i] != rule.first:
                    update[i], update[j] = update[j], update[i]
        return update



def mid(l):
    return l[len(l) // 2]


def part_1(f):
    rules_text, updates_text = f.read().split("\n\n")
    rules = Rules(rules_text)
    updates = [[int(i) for i in u.split(",")] for u in updates_text.split()]

    midpoints = [mid(u) for u in updates if rules.conforms(u)]
    return sum(midpoints)

def part_2(f):
    rules_text, updates_text = f.read().split("\n\n")
    rules = Rules(rules_text)
    updates = [[int(i) for i in u.split(",")] for u in updates_text.split()]

    nonconforming = [u for u in updates if not rules.conforms(u)]
    fixed = list()
    for n in nonconforming:
        while not rules.conforms(n):
            n = rules.fix_one(n)
        fixed.append(n)
    return sum(mid(f) for f in fixed)
