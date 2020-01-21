#
# Wiki Vote In Degree. G(7115, 103689). 1321 (0.1857) nodes with in-deg > avg deg (29.1), 617 (0.0867) with >2*avg.deg (Tue Jan 21 18:29:38 2020)
#

set title "Wiki Vote In Degree. G(7115, 103689). 1321 (0.1857) nodes with in-deg > avg deg (29.1), 617 (0.0867) with >2*avg.deg"
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
set output 'inDeg.wiki_vote.png'
plot 	"inDeg.wiki_vote.tab" using 1:2 title "" with linespoints pt 6
