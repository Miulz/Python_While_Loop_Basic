# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки.
# Незадоволителна е всяка оценка, която е по-малка или равна на 4.

bad_grades_limit = int(input()) # limita na broq loshi ocenki
bad_grades_count = 0 # broqt na loshi ocenki
problem_count = 0 # broqt na zadachi
grades_sum = 0 # sumirane na ocenkite
last_problem_name = ""


while bad_grades_count < bad_grades_limit:
    problem_name = input()  # nova zadacha
    if problem_name == "Enough":
        break

    problem_count += 1
    last_problem_name = problem_name
    current_grade = int(input())
    grades_sum += current_grade

    if current_grade <= 4:
        bad_grades_count += 1

if bad_grades_count >= bad_grades_limit:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    print(f"Average score: {grades_sum / problem_count:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem_name}")







