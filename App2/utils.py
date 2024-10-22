from .models import Student1

def calculate_average_marks(total_students: int, total_marks_sum: float):
    return (total_marks_sum / total_students) if total_students > 0 else 0


def get_subjectwise_failed(cutoff_marks):
    failedin_maths=Student1.objects.filter(maths__lt=cutoff_marks)
    failedin_chemistry=Student1.objects.filter(chemistry__lt=cutoff_marks)
    failedin_physics=Student1.objects.filter(physics__lt=cutoff_marks)
    return {
            'failedin_maths':failedin_maths,
            'failedin_chemistry':failedin_chemistry,
            'failedin_physics':failedin_physics,
    } 

# def calculate_teacher_pass_percentage(teacher_name):
#     total_students = Student1.objects.filter(classteacher=teacher_name).count()
#             # Count passed students for the teacher (total_marks > 150)
#     passed_students_count = Student1.objects.filter(classteacher=teacher_name, total_marks__gt=150).count()

#     if total_students > 0:
#                 # Calculate pass percentage
#         pass_percentage = (passed_students_count / total_students) * 100
#         return round(pass_percentage,2)
#     return 0
def calculate_teacher_pass_percentage(teacher_id):
    # Count the total number of students for the given teacher
    total_students = Student1.objects.filter(teacher_id=teacher_id).count()
    
    # Count passed students for the teacher (total_marks > 150)
    passed_students_count = Student1.objects.filter(teacher_id=teacher_id, total_marks__gt=150).count()

    if total_students > 0:
        # Calculate pass percentage
        pass_percentage = (passed_students_count / total_students) * 100
        return round(pass_percentage, 2)
    
    return 0
