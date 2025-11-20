student = {
    "name": "Lan",
    "score": {
        "math": 9,
        "english": 8,
        "history": 7
    }
}

print(f"Điểm môn tiếng anh của {student['name']} là: {student['score']['english']}")

average_score = sum(student['score'].values()) / len(student['score'])
print(f"Điểm trung bình của {student['name']} là: {average_score}")