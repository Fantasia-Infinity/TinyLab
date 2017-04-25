#lang racket

(define (atom? exp)
  (not (pair? exp)))

(define (last? exp)
  (atom? (cdr exp)))

(define (len exp)
  (define (lens exp x)
    (if (atom? exp)
        x
        (lens (cdr exp) (+ x 1))))
 (lens exp 0))

(define (matc? exp1 exp2)
  (if (and (atom? exp1) (atom? exp2))
      #t
      (= (len exp1) (len exp2))))

(define (match? a b)
  (cond[(and (atom? a) (atom? b))
        #t]
       [(and (atom? a) (not (atom? b)))
        #f]
       [(and (not (atom? a)) (atom? b))
        #f]
       [(and (not (atom? a)) (not (atom? b)))
        (and (match? (car a) (car b))
             (match? (cdr a) (cdr b)))]))
  


  

(define a '(1 2 3  (1 2)))
(define b '(2 3 4 ( 5)))

(match? a b)
        









