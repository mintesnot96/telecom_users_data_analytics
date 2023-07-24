CREATE TABLE IF NOT EXISTS `teleco_users` 
(
    `user_id` BigINT NOT NULL AUTO_INCREMENT,
    `engagement_score` INT,
    `experience_score` INT,
    `satisfaction_score` INT,
    PRIMARY KEY (`user_id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci