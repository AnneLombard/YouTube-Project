SELECT * FROM `youtube-project-444210.Database.Top20_2024`;

#Ordering by subscriptions desc and adding a column rank
CREATE OR REPLACE TABLE `youtube-project-444210.Database.Top20_2024` AS
SELECT
  *,
  ROW_NUMBER() OVER (ORDER BY subscribers DESC) AS rank
FROM `youtube-project-444210.Database.Top20_2024`
ORDER BY rank;

#replacing null with 0 because it is a real number from the source
UPDATE `youtube-project-444210.Database.Top20_2024`
SET subscribers_last_30_days = 0
WHERE rank IN (5, 19);

SELECT * FROM `youtube-project-444210.Database.Top20_2024` 
ORDER BY rank;