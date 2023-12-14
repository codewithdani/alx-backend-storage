-- script creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.

drop procedure IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN p_user_id INT
)
BEGIN
	UPDATE users
   	SET average_score=(SELECT AVG(score) FROM corrections
			     WHERE corrections.user_id=p_user_id)
	WHERE id=p_user_id;

END;$$
DELIMITER ;
