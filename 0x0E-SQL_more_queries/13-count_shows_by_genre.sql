-- Lists all genres contained in hbtn_0d_tvshows and how many shows belong to
-- them.
-- Select and display content.
SELECT `tv_genres`.`name`, COUNT(`tv_show_genres`.`genre_id`) AS `number_shows`
       FROM `tv_genres`, `tv_show_genres`
       WHERE `tv_show_genres`.`genre_id`=`tv_genres`.`id`
       GROUP BY `tv_genres`.`name`
       ORDER BY `number_shows` DESC;
