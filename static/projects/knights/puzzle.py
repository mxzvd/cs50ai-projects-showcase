from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    # A is either a kinght or a knave.
    Not(And(AKnight, AKnave)), Or(AKnight, AKnave),

    # If A is a knight then his statement must hold true.
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    # Each of A, B are either a kinght or a knave.
    Not(And(AKnight, AKnave)), Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)), Or(BKnight, BKnave),

    # If A is a knight then his statement must hold true.
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave then his statement must be false.
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    # Each of A, B are either a kinght or a knave.
    Not(And(AKnight, AKnave)), Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)), Or(BKnight, BKnave),

    # If A is a knight they, A's words are true, meaning they both have to be knights.
    Implication(AKnight, BKnight),
    # If A is a knave they, A's words are false, meaning B has to be a knight.
    Implication(AKnave, BKnight),

    # If B is a knight they, B's words are true, meaning A has to be a knave.
    Implication(BKnight, AKnave),
    # If B is a kanve they, B's words are false, meaning A has to be a knave as well.
    Implication(BKnave, AKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

     # Each of A, B, C are either a kinght or a knave.
    Not(And(AKnight, AKnave)), Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)), Or(BKnight, BKnave),
    Not(And(CKnight, CKnave)), Or(CKnight, CKnave),

    # If A is a knight he told B the truth, so B must be telling us the truth.
    Implication(And(BKnight, AKnight), AKnave),
    # If A is a knave he told B a lie, so B is telling us A's lie.
    Implication(And(BKnight, AKnave), AKnight),

    # B claims C is a knave, meaning if B is a knight then C must be a knave, otherwise C is a knight.
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # C claims A is a knight, meaning if C is a knight then A is a knight as well, otherwise A is a knave.
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
