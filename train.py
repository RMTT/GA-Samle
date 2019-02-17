from generator import generate_grid
import random
import time
import logging

direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("log.txt", mode="w")
handler.setLevel(logging.INFO)
fmt = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(fmt)
logger.addHandler(handler)
handler = logging.StreamHandler()
handler.setFormatter(fmt)
logger.addHandler(handler)


def train_unit(unit, w, h, proportion, times, actions):
    random.seed(time.time())
    score = 0
    for i in range(times):
        x = y = 0
        grid = generate_grid(w, h, proportion)
        for action in range(actions):
            state = 0
            tx = x
            ty = y
            for j in range(4):
                tx += direction[j][0]
                ty += direction[j][1]
                if tx >= 0 and tx < w and ty >= 0 and ty < h:
                    state = state * 3 + grid[tx][ty]
                else:
                    state = state * 3 + 2
            state = state * 3 + grid[x][y]
            next = unit[state]

            if next == 5:
                if grid[x][y] == 1:
                    score += 10
                else:
                    score -= 1
            elif next == 4:
                pass
            else:
                if next == 6:
                    r = random.randint(0, 3)
                else:
                    r = next
                tx = x + direction[r][0]
                ty = y + direction[r][1]

                if tx >= 0 and tx < w and ty >= 0 and ty < h:
                    x = tx
                    y = ty
                    if grid[x][y] == 0:
                        score -= 1
                else:
                    score -= 5
    return score


def mating(a, b, max_genes, max_gene_type):
    random.seed(time.time())
    p = random.randint(0, max_genes - 1)

    # heredity
    unit = a[:p] + b[p:]

    # mutation
    n = random.randint(1, 1000)
    if n <= 10:
        for i in range(n):
            unit[random.randint(0, max_genes - 1)] = random.randint(0, max_gene_type - 1)

    return unit


def evolution(units, scores, numbers, max_genes, max_gene_type):
    result = []
    n = len(scores)
    min_score = min(scores)
    b = 0
    if min_score < 0:
        for i in range(n):
            scores[i] -= min_score
        b -= min_score - 1

    sum_scores = sum(scores)
    sum_array = [0] + scores

    for i in range(n):
        sum_array[i + 1] += sum_array[i]

    for i in range(numbers):
        A = B = 0
        t = random.randint(0, sum_scores)

        for i in range(n):
            if t >= sum_array[i] and t <= sum_array[i + 1]:
                A = i
                break
        B = A
        while A == B:
            t = random.randint(1, sum_scores)
            for i in range(n):
                if t >= sum_array[i] and t <= sum_array[i + 1]:
                    B = i
                    break
        result.append(mating(units[A], units[B], max_genes, max_gene_type))
    return result


def train_units(units, w, h, proportion, times, actions, max_genes, max_gene_type, generation):
    random.seed(time.time())
    r = []
    logger.info("Start train!")
    for i in range(generation):
        logger.info("generation %d:" % (i + 1))
        scores = []

        logger.info("Start action!")
        for k, unit in enumerate(units):
            s = train_unit(unit, w, h, proportion, times, actions)
            scores.append(s)
            logger.info("score of a unit %d: %f" % (k + 1, s / times))
        logger.info("Action complete")
        logger.info("Start evolution!")
        units = evolution(units, scores, 200, max_genes, max_gene_type)
        logger.info("Evolution complete")
        logger.info("average score of generation %d : %f" % (i + 1, sum(scores) / (times * len(units))))
        fs = open("unit.ga", "w")
        r.append(sum(scores) / (times * len(units)))
        fs.write(str(units))
        fs.close()
    fs = open("average.ga", "w")
    fs.write(str(r))
    fs.close()
