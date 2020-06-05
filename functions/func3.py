def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

course = ["Math", "Art"]
info = {'name':'Aadesh', 'age':22}

student_info(*course,**info)