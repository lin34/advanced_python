try:
    f = open('corrupt_file.txt')
    #var = bad_var#will fail because bad_var was never initialized
    if f.name == 'corrupt_file.txt':
        raise Exception#goes to line 9 where we handle the exception
except FileNotFoundError as e:
    print('Sorry file doesnt exist')
    print(e)
except Exception as e:
    print("somthing went wrong")
    print(e)
else:
    #runs if we don't throw an exception
    print(f.read())
    f.close()
finally:
    #will always execute after a try
    print("Executing finally...")