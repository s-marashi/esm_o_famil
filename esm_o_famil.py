def calc_scores(items, ch):
    scores = [0] * len(items)
    item_usage_count = dict()

    for item in items:
        if item not in item_usage_count:
            item_usage_count[item] = 0
        item_usage_count[item] += 1

    for idx, item in enumerate(items):
        if item[0] != ch:
            scores[idx] = 0
            continue
        
        if item_usage_count[item] > 1:
            scores[idx] = 5
        else:
            scores[idx] = 10
    
    return scores

def judge(answers, ch):
    scores = [0] * len(answers)
    
    names = [ans[0] for ans in answers]
    cities = [ans[1] for ans in answers]
    foods = [ans[2] for ans in answers]
    colors = [ans[3] for ans in answers]

    score_names = calc_scores(names, ch)
    score_cities = calc_scores(cities, ch)
    score_foods = calc_scores(foods, ch)
    score_colors = calc_scores(colors, ch)

    for idx in range(len(answers)):
        scores[idx] = score_names[idx] + score_cities[idx] + score_foods[idx] + score_colors[idx]
    
    return scores

def main():
    people_count, ch = input().split()
    people_count = int(people_count)
    answers = []
    for _ in range(people_count):
        answers.append(input().split())
    
    scores = judge(answers, ch)
    print(*scores)

if __name__ == '__main__':
    main()