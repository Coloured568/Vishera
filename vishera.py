isRun = 1
version = "V1.0"
name = "Vishera"

def vishera_run(*args):
    def run(code):
        code()  # Call the function passed to run()

    if isinstance(args[0], tuple):  # If the first argument is a tuple
        for func in args[0]:
            run(func)
    else:
        run(args[0])  # Otherwise, just call the single function

    output(f"Vishera Engine {version}")

def onUpdate(*args):
    global isRun
    while isRun == 1:
        if isinstance(args[0], tuple): # if using multiple functions, use "((func1, func2))"
            for func in args[0]:
                func()  # Call each function in the tuple
        else:
            args[0]()  # If a single function is passed, call it

# yes im learning gpt to help me learn python lol

# you can obviously still use print(), but if you want your branding everywhere like me, modify line 3!
def output(string):
    print(f"[{name}] " + string)

def header(string):
    print(string)


