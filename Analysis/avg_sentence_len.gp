input    = "../Output/Basic.txt"
cardinal = "#C41E3A"

set timefmt "%Y"
set xdata time
set format x "%Y"
set xtics "1789",252288000 rotate by 45 offset -1.5,-1.5
set bmargin 3
set rmargin 15

set size ratio 0.25

set xrange ["1788":"2018"]

set border 3
set xtics nomirror
set ytics nomirror

set key off
set termoption enhanced

plot input using 1:5 with lines lc rgb cardinal,\
     ""    using 1:5:2 with labels hypertext point pt 7 lc rgb cardinal

pause -1
