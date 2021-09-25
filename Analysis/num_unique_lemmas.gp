input    = "../Output/Basic.txt"
cardinal = "#C41E3A"

set timefmt "%Y"
set xdata time
set format x "%Y"
set xtics "1789",252288000 rotate by 45 offset -1.5,-1.5
set bmargin 2
set tmargin 0
set rmargin 1

set terminal svg size 800,300 dynamic enhanced fname 'Fira Sans' fsize 10 mousing name "hypertext_1" jsdir "/"
set size ratio 0.25
set xlabel "Time" offset 0,-0.5
set ylabel "Number of unique lemmas"
set title "Inaugural speeches of U.S. presidents" font "Fira Sans Bold"

set xrange ["1788":"2018"]

set border 3
set xtics nomirror
set ytics nomirror

set key off
set termoption enhanced

set output "num_unique_lemmas.svg"

plot input using 1:7 with lines lc rgb cardinal,\
     ""    using 1:7:2 with labels hypertext point pt 7 lc rgb cardinal

set output
