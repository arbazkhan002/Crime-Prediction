monthly_data = csvread('monthly_train_not_hourly.csv');
% format of this data:
% grid_no,year_month,sum_3_month,last_month,2_last_month,3_lastmonth,neighborhood_avg,this_month
monthly_data = sortrows(monthly_data,[1 3]);

% to get the number of Coldspots and Hotspots for all hours from 0 to 23
for i=1:900
    H(i) = nnz(monthly_data(monthly_data(:,1)==i,8));
    C(i) = length(monthly_data(monthly_data(:,1)==i,8))-H(i);
end
C=C';
H=H';
% to get the ratio of C by H for hours varying from 0 to 23
for i=1:900
    if H(i) == 0 || C(i) == 0
        out(i) = 1;
    else
        if C(i)>H(i)
            out(i) = C(i)/H(i); 
        else
            out(i) = 1;
        end
    end
end

% normalize the monthly data by multiplying the total count with C/H
norm_monthly_data = monthly_data;
for i=1:length(monthly_data)
   norm_monthly_data(i,8) = norm_monthly_data(i,8)*out(norm_monthly_data(i,1));
end

filenametemplate = 'monthly_nothourly_t3/Result%3.3d.csv';
for i=1:900
    filename = sprintf(filenametemplate,i);
    monthly_i = norm_monthly_data(norm_monthly_data(:,1)==i,:);
    % format of data: grid_no, year_month, sum_last_3_months, last_month, second_last_month, third_last_month, neighborhood_avg_3_months, this_month
    if ~isempty(monthly_i ~= 0) && length(monthly_i(:,1)) > 10
        dlmwrite(filename,monthly_i)
        Length = length(monthly_i);
        p = floor(Length*0.75);
        if p==0
            p=1;
        end
        training = [monthly_i(1:p,2), monthly_i(1:p,4:end)];
        testing = [monthly_i(p:end,2),monthly_i(p:end,4:end)];
        Class = knnclassify(testing(:,1:5),training(:,1:5),training(:,6));
        Results = [testing(:,6),Class];
        TP=0;
        TN=0;
        FP=0;
        FN=0;
        for m=1:length(Results)
            if Results(m,1) == 0
                if Results(m,2)==0
                    TN=TN+1;
                else
                    FP=FP+1;
                end
            else
                if Results(m,2)==0
                    FN = FN+1;
                else
                    TP = TP+1;
                end
            end
        end
        Accuracy(i,1:6) = [i,TP,TN,FP,FN,sumabs(Results(:,1)-Results(:,2))/length(Results)];
        plot(Results,'DisplayName','Results','YDataSource','Results');figure(gcf)
        dlmwrite(filename,Results);
        yy1=smooth(Results(:,1));
        yy2=smooth(Results(:,2));
        yy=[yy1,yy2];
%         fig = figure('visible','off');
        plot(yy,'DisplayName','yy','YDataSource','yy');
%         xlabel('');
        ylabel('Total Number of Crimes');
        title('Comparison between Number of Crime predicted and actual when t=3 and not hourly');
        fig = figure(gcf);
        saveas(fig,sprintf('monthly_nothourly_t3/result%03d',i),'jpg');
        close(fig);
    end
end

Accuracy = Accuracy(Accuracy(:,1)~=0,:);
dlmwrite('accuracy_monthly_t3.csv',Accuracy);