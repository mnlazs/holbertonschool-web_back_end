-- Task : 0. We are all unique! - creates a table users
-- script can be executed on any database
SELECT DISTINT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
