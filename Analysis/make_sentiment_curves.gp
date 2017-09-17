set border 2
set tics nomirror
set ytics out

set tics font "Fira Sans Bold"

unset key
unset xtics

set xrange [ 0:1]
set yrange [-1:1]

set terminal svg size 800,300 fname "Crimson,16" enhanced background rgb 'white'

do for [i=0:116:2] {
  sed  = sprintf("sed '%dq;d' Names.txt", i/2+1)
  title = system(sed)

  set title title

  out = sprintf("/tmp/%s sentiment curve.svg", title)
  set output out

  set key out vert center top
  set key autotitle columnheader

  plot "../Output/Sentiment_curves.txt" index i with filledcurves above y=0 lc rgb '#50C878' notitle,\
       "" index i with filledcurves below y=0 lc rgb '#FF2400' notitle,\
       "" index i+1 with l notitle lc rgb 'black',\
       0 with lines notitle lc rgb 'black'

  set output
}

set output "/tmp/Sentiment_curves_all.svg";

set terminal svg size 800,17700 fname "Crimson,16" enhanced background rgb 'white'
set multiplot layout 59,1

do for [i=0:116:2] {
  sed   = sprintf("sed '%dq;d' Names.txt", i/2+1)
  title = system(sed)

  set title title

  set key out vert center top
  set key autotitle columnheader

  plot "../Output/Sentiment_curves.txt" index i with filledcurves above y=0 lc rgb '#50C878' notitle,\
       "" index i with filledcurves below y=0 lc rgb '#FF2400' notitle,\
       "" index i+1 with l notitle lc rgb 'black',\
       0 with lines notitle lc rgb 'black'
}
