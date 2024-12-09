def outter_function():
    var1=30

    def inner_function():
        var2=90
        print(var1)

    def inner_function2():
        print(var1)

        inner_function()
        inner_function2()


outter_function()


