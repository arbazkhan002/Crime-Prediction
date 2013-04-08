CRIME = "LARCENY"

file_to_load = strcat(CRIME," XY")
file_with_limits = "Limits"
output_file = strcat( file_to_load, "_modified_data.dat")
fp_out = fopen(output_file, "w")

data = load(file_to_load)	% frequencies of bins.

format long

limits = load(file_with_limits)	% ranges.
limits(1,2)-limits(1,1)
%xboundaries = [limits(1,1):(limits(1,2)-limits(1,1))/30:limits(1,2)]
%yboundaries = [limits(2,1):(limits(2,2)-limits(2,1))/30:limits(2,2)]

xboundaries = [0.5:1:30.5]
yboundaries = [0.5:1:30.5]

delim = 0
for i = 1:30

	list_i = [i-0.5 i+0.5];

	for towrite_i = list_i
		for j = 1:30

			list_j = [j-0.5, j+0.5];

			if (j==1)
				fprintf(fp_out, "%f\t%f\t%d\n", towrite_i, j-0.5, 0);
			endif

			for towrite_j = list_j
				fprintf(fp_out,"%f\t%f\t%d\n",towrite_i,towrite_j,data(((i-1)*30+j),2));
			endfor
		endfor
		fprintf(fp_out, "\n");
	endfor

endfor
fclose(fp_out)
