(def lattice-paths
  (memoize
    (fn
      [n m]
      (if (or (= 0 n) (= 0 m))
        1
        (+ (lattice-paths (dec n) m)
           (lattice-paths n (dec m)))))))

(println (time (lattice-paths 20 20)))
