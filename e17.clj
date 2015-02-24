(ns projecteuler.17)

;;
;; SHOULD HAVE USED CORE.MATCH
;;

(def n->e
  {1 "one"
   2 "two"
   3 "three"
   4 "four"
   5 "five"
   6 "six"
   7 "seven"
   8 "eight"
   9 "nine"
   10 "ten"
   11 "eleven"
   12 "twelve"
   13 "thirteen"
   14 "fourteen"
   15 "fifteen"
   16 "sixteen"
   17 "seventeen"
   18 "eighteen"
   19 "nineteen"
   20 "twenty"
   30 "thirty"
   40 "forty"
   50 "fifty"
   60 "sixty"
   70 "seventy"
   80 "eighty"
   90 "ninety"
   100 "hundred"
   1000 "thousand"})

(defn convert-two-digit [n]
  (let [digits (str n)
        read-char (comp read-string str)]
    (if (or (= \1 (first digits))
            (= \0 (second digits)))
      (n->e n)
      (str (n->e (* 10 (read-char (first digits))))
           (n->e (read-char (second digits)))))))

(comment
  (convert-two-digit 10)
  (convert-two-digit 50)
  (convert-two-digit 11)
  (convert-two-digit 21)
  (convert-two-digit 42)
  )

(defn convert-three-digit [n]
  (let [digits (str n)]
    (if (= \0 (second digits) (last digits))
      (str (n->e ((comp read-string str) (first digits))) "hundred")
      (let [read-char (comp read-string str)
            x (if (= \0 (second digits))
                (n->e (read-char (last digits)))
                (convert-two-digit (read-string (clojure.string/join "" (rest digits)))))]
        (str (n->e (read-char (first digits)))
             (n->e 100)
             "and"
             x)))))

(comment
  (convert-three-digit 200)
  (convert-three-digit 230)
  (convert-three-digit 100)
  (convert-three-digit 101))

(defn convert-num
  [n]
  (let [num-digits (count (str n))]
    (case num-digits
      0 nil
      1 (n->e n)
      2 (convert-two-digit n)
      3 (convert-three-digit n))))

(convert-num 1)
(convert-num 10)
(convert-num 100)
(assert (= 23 (count (convert-num 342))))

(def answer
  (+ (count "onethousand")
     (reduce +
       (map count
        (for [n (range 1 1000)]
          (convert-num n))))))

