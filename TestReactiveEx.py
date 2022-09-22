from reactivex import create


def function(a, b):
    a.on_next("Patryk")
    a.on_next("Christian")
    a.on_error("Helmut")
    a.on_completed()


source = create(function)

source.subscribe(
    on_next=lambda i: print("Hi {0}".format(i)), on_completed=print("Goodbye")
)
