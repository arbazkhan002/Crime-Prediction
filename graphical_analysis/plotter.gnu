unset origin
unset label
set term postscript eps enhanced color
set ticslevel 0
set nohidden3d
set size 4.0, 4.0
unset key

################## change the following variables ##############################################################
XLABEL = "X"
YLABEL = "Y"
CRIME = "LARCENY"
set cbrange [0:10000]		# that defines the colouring range- depends on the max value of frequency in graph.
set view 60,40,0.5			# Angle with z-axis, angle with x-axis, magnification.
DATAINPUT = CRIME." XY_modified_data.dat"
set out CRIME."_stats.ps"
################################################################################################################

set label "X and Y coordinates merged into bins" font "Helvetica,22" at screen 1.75, screen 0.93
set multiplot
set label "XY Frequency Bar Chart for Crime: ".CRIME font "Helvetica,26" at screen 1.6, screen 2.5

set origin 0,-0.1		# DO NOT TOUCH THIS
set pm3d
set ticslevel 0
set palette defined (0 "gray", 1 "blue", 2 "red", 4 "black")
unset colorbox
unset surface
set xlabel
set xlabel XLABEL font "Helvetica,30"
set ylabel
set ylabel YLABEL font "Helvetica,22"
set xtics offset 0.5,-0.5
set ytics offset -0.5,-0.5

set xrange [0:31]
set yrange [0:31]
set xtics 1,1,30
set ytics 1,1,30
set ztics 0,500,10000
set zrange [0:10000]
set label "Observed Crime Frequency" font "Helvetica,26" at screen 1.1, screen 1.6 rotate by 90
splot DATAINPUT with lines

unset multiplot
