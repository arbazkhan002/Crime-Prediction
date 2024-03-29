FILES
----------------
project_report_group10.pdf							:	The project report
dictXY												:	Contains the grid boundaries (region discretized into 900 bins)
Weekday/sample_newdata.csv							:	Sample of 'new_data.csv', the file on which furthur analysis is done
Weekday/script_divide_into_gridfiles.py				:	Given 'new_data', whose sample is given in sample_newdata.csv, does grid-wise division of crimes and stores in the folder 'gridfiles'
Weekday/find_timebounds.py							:	Given 'new_data', find the time bounds of the data.

Weekday/biggest_file.py								:	Given the grid files (in the directory 'gridfiles'), finds the file with the largest size
Weekday/perday.py									:	Given the grid-wise crime files in the directory 'gridfiles', outputs month-wise counts of the total crimes on that particular day. Outputs in output_months_csv in separate folders.
Weekday/gen_nominaltraining_from_outputfolder.py	:	Given the data generated by perday.py above, outputs the data on which learning can be done (weka) in the folder nominal_training_data
Weekday/merge_nominal_training_data.py				:	Merges the data generated above and outputs in nominal_training_data/alldays folder. The resulting files have arff extension and are divided into training and testing data.
Weekday/complete.sh									:	The script that does the above three things
Weekday/weigh_attribute.py							:	Adds instance weight as an attribute in the above generated files to deny any possibility of false accuracy increase (balancing data)

Weekday/16train(test).arff							:	<sample> The sample train&test arff files generated till now
Weekday/AddWeightsFromAtt.java						:	The java file that Takes a arff file and converts it to xrff file after inserting weights (given in the last arff attribute)
Weekday/convert_to_xrff.py							:	The python file that calls the above java executable for all files
Weekday/gen_16train(test).xrff						:	<sample> The xrff files corresponding to 16train(test).arff files that contain information regarding the weight of instances that can be read readily by weka

Weekday/Prediction/*								:	Sample testing and training files for analysis shown in Table4 of the report
Weekday/readme_Alldays_prediction.txt				:	Compiled results for the classification results on above files
Weekday/Weekends_Prediction/*						:	Sample testing and training files for analysis shown in Table5 of the report. Folder name denotes the value of T (number of months taken as attributes)
Weekday/readme_Weekends_prediction.txt				:	Compiled results for the classification results on above files

FOLDERS
----------------
Weekday/Prediction			:	The folder containing the testing and training files generated by the procedure above.
Weekday/Weekends_prediction	:	The folder containing the testing and training files generated only for saturdays and sundays.
octave_weekend				:	The octave file that plots figure7 and figure8
