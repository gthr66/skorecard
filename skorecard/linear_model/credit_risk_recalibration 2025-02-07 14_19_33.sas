/* Credit Risk Model Recalibration in SAS */

/* Step 1: Logistic Regression Model Training */
proc logistic data=historical_credit_data descending;
    model Default(event='1') = Income Age DebtToIncome CreditScore / lackfit;
    output out=predictions p=PD_hat;
run;

/* Step 2: Score New Data Using the Model */
proc logistic inmodel=historical_model;
    score data=current_credit_data out=scored_data priorevent='1';
run;

/* Step 3: Recalibrate PD Estimates */
proc logistic data=scored_data descending;
    model Actual_Default(event='1') = PD_hat / lackfit;
    output out=recalibrated_data p=PD_recalibrated;
run;

/* Step 4: Compare the Calibration */
proc means data=recalibrated_data mean std min max;
    var PD_hat PD_recalibrated;
run;

proc sgplot data=recalibrated_data;
    scatter x=PD_hat y=PD_recalibrated / markerattrs=(symbol=circlefilled color=blue);
    lineparm x=0 y=0 slope=1 / lineattrs=(pattern=solid color=red);
    xaxis label="Original PD Estimates";
    yaxis label="Recalibrated PD Estimates";
run;
