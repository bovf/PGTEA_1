assessment_bel = int(input())
assessment_mat = int(input())
assessment_fiz = int(input())
assessment_him = int(input())
assessment_bio = int(input())
success = (assessment_bio + assessment_him + assessment_fiz + assessment_mat + assessment_bel) / 5

print(success)

if success >= 5.50:
    print("Good job")
elif success < 5.50:
    print("try again")