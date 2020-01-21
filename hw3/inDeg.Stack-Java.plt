#
# Stack-Java In Degree. G(188406, 415174). 12245 (0.0650) nodes with in-deg > avg deg (4.4), 6917 (0.0367) with >2*avg.deg (Tue Jan 21 18:29:31 2020)
#

set title "Stack-Java In Degree. G(188406, 415174). 12245 (0.0650) nodes with in-deg > avg deg (4.4), 6917 (0.0367) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.Stack-Java.png'
plot 	"inDeg.Stack-Java.tab" using 1:2 title "" with linespoints pt 6
