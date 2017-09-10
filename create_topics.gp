unset border
unset tics
unset key

base=12
scale(string,size) = sprintf("{/=%d %s}", size+base,string)

set tics font "Fira Sans Bold"
unset ytics
set xtics scale 0 out

set yrange [-0.5:4]

set terminal svg size 20000,400 fname "Crimson" enhanced
set output "/tmp/Complete.svg"
set multiplot layout 1,59 margins 0.0,1.00,0.1,0.90 spacing 0
do for [i=0:58] {

  #out = sprintf("/tmp/%02d.svg", i)
  #set output out

  plot "Topics_gnuplot.txt" using 1:(4-$2):(scale(stringcolumn(4),$5*10+10)):xticlabel(3) index i with labels

}

unset multiplot

set terminal svg size 200,400 fname "Crimson" enhanced
do for [i=0:58] {

  out = sprintf("/tmp/%02d.svg", i)
  set output out

  plot "Topics_gnuplot.txt" using 1:(4-$2):(scale(stringcolumn(4),$5*10+10)):xticlabel(3) index i with labels

  set output
}

set terminal svg size 1000,200 fname "Crimson" enhanced
set output "/tmp/Last_eight.svg"
set multiplot layout 1,8 margins 0,1,0.2,0.9 spacing 0

do for [i=51:58] {
  plot "Topics_gnuplot.txt" using 1:(4-$2):(scale(stringcolumn(4),$5*10+10)):xticlabel(3) index i with labels
}
