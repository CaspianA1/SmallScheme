(define nln (lambda () (display "\n")))

(define x 5)
(display x)

(nln)

(define l '(1 2 3))
(define sec-elem (car (cdr l)))
(display sec-elem)

(nln)

(define increment
	(lambda 
		(x)
		(+ x 1)))

; this does not work in my interpreter: (display "hi bob!")
; strings need to be taken care of in a better way
; also, printing newlines needs to be done better


(define a-num (+ 8 (* 5 3)))
(display (increment a-num))

(nln)