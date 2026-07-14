names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

student_scores = dict(zip(names, scores))

ranked_students = sorted(student_scores.items(), key=lambda x: x[1], reverse=True)

for rank, (name, score) in enumerate(ranked_students, start=1):
    print(f"Rank {rank}: {name} scored {score}")