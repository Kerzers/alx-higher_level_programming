-- script that lists all shows contained in hbtn_0d_tvshows.
SELECT t.title, tg.genre_id
FROM tv_shows AS `t`
LEFT JOIN tv_show_genres AS `tg`
ON t.id = tg.show_id
ORDER BY t.title, tg.genre_id;
