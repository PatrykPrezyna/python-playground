from reactivex import create, of, operators


def fun(observer, scheduler):
    observer.on_next("ein")
    observer.on_next("zwei")
    observer.on_next("drei")


source = of("fun", "fun2", "fun21", "fun222")

composed = source.pipe(
    operators.map(lambda i: len(i)), operators.filter(lambda j: j > 4)
)

composed.subscribe(on_next=lambda a: print("{0}".format(a)))
