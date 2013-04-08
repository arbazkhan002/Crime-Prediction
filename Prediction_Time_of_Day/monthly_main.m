% initial template code. Template code used to build other code files for different parameters like no_of_months, hourly data etc.
monthly_data = csvread('monthly_train.csv');
% format of monthly_train.csv:
% grid_no,hour,year_month,sum_last_3_month,last_mont,2_last_month,3_last_month,nieghborhood_3_month,this_month
monthly_data = sortrows(monthly_data,[1 3]);
filenametemplate = 'monthly_hourly_t3/Result%3.3d.csv';

% to get the number of Coldspots and Hotspots for all hours from 0 to 23
for i=0:23
    H(i+1) = nnz(monthly_data(monthly_data(:,2)==i,9));
    C(i+1) = length(monthly_data(monthly_data(:,2)==i,9))-H(i+1);
end

% to get the ratio of C by H for hours varying from 0 to 23
for i=1:length(C)
   out(i)=C(i)/H(i); 
end

% normalize the monthly data by multiplying the total count with C/H
norm_monthly_data = monthly_data;
for i=1:length(monthly_data)
   norm_monthly_data(i,9) = norm_monthly_data(i,9)*out(norm_monthly_data(i,2)+1);
end

k = 1;
for i=1:900
    filename = sprintf(filenametemplate,i);
    monthly_i = monthly_data(monthly_data(:,1)==i,:);
    if ~isempty(monthly_i ~= 0) && length(monthly_i) > 20
        Length = length(monthly_i);
        p = floor(Length*0.75);
        if p==0
            p=1;
        end
        training = [monthly_i(1:p,2), monthly_i(1:p,5:end)];
        testing = [monthly_i(p:end,2),monthly_i(p:end,5:end)];
        Class = knnclassify(testing(:,1:5),training(:,1:5),training(:,6),10);
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
        title('Comparison between Number of Crime predicted and actual');
        fig = figure(gcf);
        saveas(fig,sprintf('Results/result%03d',i),'jpg');
        close(fig);

    end
end
Accuracy = Accuracy(Accuracy(:,1)~=0,:);
dlmwrite('accuracy_monthly_t3.csv',Accuracy);
% monthly_620 = norm_monthly_data(norm_monthly_data(:,1)==620,:);
% training_620 = [monthly_620(1:2100,2),monthly_620(1:2100,5:end)];
% testing_620 = [monthly_620(2101:2700,2),monthly_620(2101:2700,5:end)];
% Prediction = knnclassify(testing_620(:,1:5),training_620(:,1:5),training_620(:,6),3);
% Results = [testing_620(:,6),Prediction];
% 
% code to calculate the optimized value of k for minimium SSE
% for k=1:100
%     monthly_620 = norm_monthly_data(norm_monthly_data(:,1)==620,:);
%     length(monthly_620)
%     training_620 = [monthly_620(1:2000,2),monthly_620(1:2000,5:end)];
%     testing_620 = [monthly_620(2001:2700,2),monthly_620(2001:2700,5:end)];
%     Prediction = knnclassify(testing_620(:,1:5),training_620(:,1:5),training_620(:,6),k);
%     Results = [testing_620(:,6),Prediction];
%     yy1=smooth(Results(:,1));
%     yy2=smooth(Results(:,2));
%     yy=[yy1,yy2];
%     % plot(yy,'DisplayName','yy','YDataSource','yy');figure(gcf)
%     % plot(Results,'DisplayName','Results','YDataSource','Results');figure(gcf)
%     mean_absolute_error(k) = (sumabs(yy1-yy2))/length(yy1-yy2); 
% %     mean_absolute_error
% end
% mean_absolute_error'
% SSE = (mean_absolute_error.*mean_absolute_error)'
% 
% code by dang
% day_data = csvread('training_data\622train.csv');
% thursday_prediction = knnclassify(day_data(81:end,1:4),day_data(1:80,1:4),day_data(1:80,5));
% thursday_results = [day_data(81:end,5),thursday_prediction];
% plot(thursday_results,'DisplayName','thursday_results','YDataSource','thursday_results');figure(gcf)


filenametemplate = 'monthly_nothourly_t3/Result%3.3d.csv';
for i=1:900
    filename = sprintf(filenametemplate,i);
    data_i = data(data(:,1)==i,:);
    % format of data: grid_no, year_month, sum_last_3_months, last_month, second_last_month, third_last_month, neighborhood_avg_3_months, this_month
    if ~isempty(data_i ~= 0) && length(data_i(:,1)) > 10
        dlmwrite(filename,data_i)
        Length = length(data_i);
        p = floor(Length*0.75);
        if p==0
            p=1;
        end
        training = [data_i(1:p,2), data_i(1:p,4:end)];
        testing = [data_i(p:end,2),data_i(p:end,4:end)];
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