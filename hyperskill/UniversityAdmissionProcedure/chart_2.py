exam_result = [float(input()) for _ in range(3)]
average = sum(exam_result) / len(exam_result)
print(average)
if average >= 60:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")