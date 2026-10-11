def check_winners(scores: list[int], student_score: int) -> None:
    """
    Печатает, вошёл ли участник олимпиады в тройку лидеров.

    Предполагается, что все участники набрали разное количество баллов.

    Parameters:
        scores: неотсортированный список оценок студентов
        student_score: оценка студента.
    """

    top3 = sorted(scores, reverse=True)[:3]
    if student_score in top3:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")
