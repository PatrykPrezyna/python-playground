import reactivex
from reactivex import operators as ops
from reactivex import of


rx = of("pat", "ryk", "sew", "er", "er")
rx2 = reactivex.from_(range(7))
xx = rx.pipe(ops.filter(lambda a: a == "er"), ops.map(lambda a: "test")).subscribe(
    print
)
print("_________")
xx2 = rx2.pipe(ops.map(lambda a: a * 2)).subscribe(print)


xs = reactivex.from_marbles("1-2-3-#-")
ys = reactivex.from_marbles("1-2-3-4-x-5")
xs.pipe(ops.merge(ys)).subscribe(on_error=print())
