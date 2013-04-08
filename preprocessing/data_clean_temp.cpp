#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main()
{
	static const char input_file[] = "sfpd_incident_all.csv";
	//~ static const char input_file[] = "sample";
	FILE* fp_in = fopen(input_file,"r");
	static const char output_file[] = "clean_data_temp.csv";
	FILE* fp_out = fopen(output_file,"w");

	int quote_flag=0;				// if 1, we are in quotes.
	int comma_count=0;				// denotes the number of commas we have already seen in the given line.
	int c=5;						// that stores character.
	int comma_replacement = '-';	// ONLY SINGLE CHARACTER. The character that takes place of comma if in quotes.
	int space_replacement = ' ';	// can be changed to eliminate spaces.
	int separate_block_flag = 0;			// if 1, then we are at the 'LOCATION' part. To separate block number from the address.

	while((c = fgetc(fp_in))!=EOF)
	{
		if (c=='\n')
		{
			fputc(c, fp_out);
			comma_count = 0;
			separate_block_flag = 0;
			continue;
		}
		if (c==',')
		{
			if (quote_flag==1)
				fputc(comma_replacement, fp_out);			// commas in quotes are replaced by comma_replacement
			else
			{
				fputc(',', fp_out);
				comma_count+=1;
				if (comma_count==8)
					separate_block_flag = 1;
			}
			continue;
		}
		if ((c=='"')||(c=='\''))
		{
			quote_flag = (quote_flag+1)%2;
			//~ fputc(c, fp_out);
			continue;
		}
		if ((comma_count == 4)&&(c=='/'))
		{
			fputc(',', fp_out);
			continue;
		}
		if ((comma_count == 5)&&(c==':'))
		{
			fputc(',', fp_out);
			continue;
		}
		if (c==' ')
		{
			if (separate_block_flag == 1)
			{
				//~ fputc(',', fp_out);
				comma_count += 1;				// making the count to 10 so that X and Y coordinates face count as 10.
				separate_block_flag = 0;
			}
			fputc(space_replacement, fp_out);
			continue;
		}
		
		// if nothing else, just put in file.
		fputc(c, fp_out);
	}

	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
