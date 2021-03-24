range = 0:30; % Requests arrive between Minutes
ProbDensityFn = poisspdf(range, 15); % λ = 8 (centers the distrobution)

figure
bar(range, ProbDensityFn, 1); % Bar width = 1
xlabel('Time between Requests (s)');
ylabel('Probability');
title('Request Distrobution');

