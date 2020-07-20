(define seq '(1 2 3))

(define fun
	(lambda (x y) (+ x y)))

(define result (reduce fun seq))

(display (reduce fun seq))