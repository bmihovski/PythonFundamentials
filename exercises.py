"""
Exercises are fun … Especially when they represent a problem from your exercises.
Implement a class Exercise, which has a topic (string), a course_name (string), a judge_contest_link (string),
and problems (collection of strings).
You will receive several input lines containing information about a single exercise in the following format:
{topic} -> {course_name} -> {judge_contest_link} -> {problem1}, {problem2}. . .
You need to store every exercise in a Collection of Exercises. When you receive the command "go go go",
you end the input sequence.
You must print every exercise, in the following format:
"Exercises: {topic}
 Problems for exercises and homework for the "{course_name}" course @ SoftUni.
 Check your solutions here: {judge_contest_link}
 1. {problem1}
 2. {problem2}
 . . ."

Examples:
    Input
ObjectsAndSimpleClasses -> ProgrammingFundamentalsExtended -> https://judge.softuni.bg/Contests/439 -> Exercises,
OptimizedBankingSystem, Animals, Websites, Boxes, BoxIntersection, Messages
go go go
Output
Exercises: ObjectsAndSimpleClasses
Problems for exercises and homework for the "ProgrammingFundamentalsExtended" course @ SoftUni.
Check your solutions here: https://judge.softuni.bg/Contests/439
1. Exercises
2. OptimizedBankingSystem
3. Animals
4. Websites
5. Boxes
6. BoxIntersection
7. Messages
"""


class Exercises:
    def __init__(self, topic, course, judge_link, problems):
        """
        Instantiates course constructor
        :param topic: (Str) Course topic
        :param course: (Str) Course name
        :param judge_link: (Str) Code test system url
        :param problems: (List) Problems to be solved
        """
        self.topic = topic
        self.course = course
        self.judge_link = judge_link
        self.problems = problems

    def __str__(self):
        """
        Constructs structure ready for sdtout printing
        :return: (Str) Exercises structured data to be print
        """
        info = (
            f'Exercises: {self.topic}\n'
            f'Problems for exercises and homework for the "{self.course}" course @ SoftUni.\n'
            f'Check your solutions here: {self.judge_link}\n')
        problems_constr = [f'{index + 1}. {problem}' for index, problem in enumerate(self.problems)]

        info += '\n'.join(problems_constr)

        return info


problems_to_solve = list()

while True:
    inputs_text = input().split(' -> ')
    if 'go go go' in inputs_text:
        break
    info = inputs_text[:-1]
    problems_separated = inputs_text[-1].split(', ')
    problems_to_solve.append(Exercises(*info, problems_separated))

[print(exercise) for exercise in problems_to_solve]
