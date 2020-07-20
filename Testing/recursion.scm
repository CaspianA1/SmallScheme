(define factorial
  (lambda (x)
    (if
      (eq? x 0) 1
      (* x (factorial (- x 1))))))

(define f
   (lambda (x)
     (if (eq? x 2) x
       (f (- x 1)))) 
         )
