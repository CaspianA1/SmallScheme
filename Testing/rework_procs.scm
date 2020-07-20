; (define x 20)
;(define y 15)
;(define z 25)


;(define comp (lambda (x) (if (> x y) z 36)))

;(define incr (lambda (x) (+ x 1)))

;(display (incr 5))
;(display (comp 13))

(define factorial (lambda (x) (if (= x 1) 1 (* x (factorial (- x 1))))))

; (define result (factorial 197)); 197 is the biggest number that works

(display (factorial 5))


; (display (factorial 5))

; (define factorial (lambda (x) (if (= x 1) 1 (* f (factorial (- x 1))))))

; (display (factorial 10))