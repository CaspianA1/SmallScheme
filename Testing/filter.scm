(define smaller-than-two
  (lambda (x)
	(< x 2)))

(define seq '(3 4 5 2 1))

(define filtered-result (filter smaller-than-two seq))

(display filtered-result)
