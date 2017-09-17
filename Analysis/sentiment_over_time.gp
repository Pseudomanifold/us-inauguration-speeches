set border 3
set tics nomirror
set ytics out
set xtics 1789,10 out rotate by 45 offset -1.5,-1.5

set tics font "Fira Sans Bold"

unset key

set xrange [1789:2017]
set yrange [-0.5:0.5]

set terminal svg size 800,400 fname "Crimson,16" enhanced background rgb 'white'

set title "Mean sentiment over time"

set output "/tmp/Mean_sentiment_over_time.svg"

plot "../Output/Mean_sentiments.txt" with filledcurves above y=0 lc rgb '#50C878' notitle,\
       ""                            with filledcurves below y=0 lc rgb '#FF2400' notitle,\
       ""                            with points pt 7 ps 0.5 lc rgb 'black',\
       0                             with lines notitle lc rgb 'black';

set output
