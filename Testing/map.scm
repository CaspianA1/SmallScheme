(define incr
  (lambda (x)
	(+ x 1)))

(define nums '(1 2 3 4 5))

(define bigger-nums (map incr nums))

(display bigger-nums)
