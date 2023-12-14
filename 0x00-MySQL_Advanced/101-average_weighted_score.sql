-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS u, 
    (SELECT u.id, SUM(score * weight) / SUM(weight) AS w_avg 
    FROM users AS u 
    JOIN corrections as c ON u.id=c.user_id 
    JOIN projects AS P ON c.project_id=P.id 
    GROUP BY u.id)
  AS AW
  SET u.average_score = AW.w_avg 
  WHERE u.id=WA.id;
END;
