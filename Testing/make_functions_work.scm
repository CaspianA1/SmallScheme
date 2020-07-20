; make_functions_work.scm

(define x 5)

; (define increment (lambda (y) (+ x 1)))

; (display (increment 5))

; (define f (lambda (x y) (if (> x y) 25 36)))

; (define result (f 5 2))

; (display (f 1 2))

(define fact (lambda (x) (if (= x 1) 1 (* x (fact (- x 1))))))

(define result (fact))

(display result)