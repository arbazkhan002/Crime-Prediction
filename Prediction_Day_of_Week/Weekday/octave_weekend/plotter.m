a=[.5625,0.833,.75,1,.34,0.667;.40625,.833,.8125,1,.375,.667;.6875,.833,.84375,1,.21875,.833;.8125,.833,.90625,1,.468,.833;.8125,.667,.781,.833,.3125,.5;.78125,.5,.84375,.833,.46875,.833;.8125,.5,.71875,.833,.34375,.167];

b=[3,4,5,6,7,8,9]

accu_nb=a(:,1)*100
accu_log=a(:,3)*100
accu_mp=a(:,5)*100
rec_nb=a(:,2)
rec_log=a(:,4)
rec_mp=a(:,6)

h = plot(b,accu_nb,b,accu_log,b,accu_mp);
title('Accuracy for different classifiers with varying T',"fontsize",20)
xlabel("T - number of months taken as attributes","fontsize",20)
ylabel("Accuracy","fontsize",20)
set(h,"linewidth",5)
axis([3,9,0,110])
set(gca,'fontsize',16)
legend("Naive Bayes","Logistics","Multi-level Perceptron")
print('Accuracy.png','-dpng')

h = plot(b,rec_nb,b,rec_log,b,rec_mp);
title('Recall for different classifiers with varying T',"fontsize",20)
xlabel("T - number of months taken as attributes","fontsize",20)
ylabel("Recall","fontsize",20)
set(h,"linewidth",5)
axis([3,9,0.0,1.10])
set(gca,'fontsize',16)
legend("Naive Bayes","Logistics","Multi-level Perceptron")
print('Recall.png','-dpng')
