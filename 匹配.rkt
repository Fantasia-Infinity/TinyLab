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

(define (anymatch? a b)
  (cond[(match? a b)
        b]
       [(anymatch? a (car b))]))





(define c '(define a '(1 2 3  (1 2))))
(define d '(define b '(2 3 4 (f 5))))
(define a '(1 2 3  (1 2)))


(match? c d)


(define (listrefh list n)
  (if (= n 1)
      list
      (listrefh (cdr list) (- n 1))))
(define (listrefq list n)
  (if (= n 1)
      null
      (cons (car list) (listrefq (cdr list) (- n 1)))))


(define (randomexc a b)
  (let((n (random 1 (len b))))
    (append (listrefq a n) (listrefh b n))))

(define x (list 0 0 0 0 0 0 0 0))
(define y (list 1 1 1 1 1 1 1 1))

(define q '(+ (+ 1 2) (* 3 4)))
(define p '(- 1 (+ 1 2 3 4 5)))

















