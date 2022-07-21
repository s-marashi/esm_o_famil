from dataclasses import dataclass

@dataclass
class Person:
    name: str
    city: str
    food: str
    color: str
    score: dict[str, int]


class Judge:
    def __init__(self, people, ch):
        self.people = people
        self.ch = ch

    def __calc_scores(self, items):
        ch = self.ch
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


    def run(self):
        scores = [0] * len(self.people)
    
        names = [person.name for person in self.people]
        cities = [person.city for person in self.people]
        foods = [person.food for person in self.people]
        colors = [person.color for person in self.people]

        score_names = self.__calc_scores(names)
        score_cities = self.__calc_scores(cities)
        score_foods = self.__calc_scores(foods)
        score_colors = self.__calc_scores(colors)

        for idx, person in enumerate(self.people):
            person.score = {
                'name': score_names[idx],
                'city': score_cities[idx],
                'food': score_foods[idx],
                'color': score_colors[idx]
            }

            scores[idx] = sum(person.score.values())

        return scores

def main():
    people_count, ch = input().split()
    people_count = int(people_count)
    people = []
    for _ in range(people_count):
        row = input().split()
        people.append(Person(*row, None))
    
    judge = Judge(people, ch)
    print(*judge.run())

if __name__ == '__main__':
    main()