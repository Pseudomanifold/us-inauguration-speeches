unset border
unset tics
unset key

base=10
scale(string,size) = sprintf("{/=%d %s}", size+base,string)

set xtics scale 0 out

set yrange [-0.5:4]

do for [i=0:57] {
  plot "Topics_gnuplot.txt" using 1:(4-$2):(scale(stringcolumn(4),$5*10+10)):xticlabel(3) index i with labels
}

pause -1
