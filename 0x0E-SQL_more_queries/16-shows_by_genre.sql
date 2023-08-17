-- script that lists all shows contained in hbtn_0d_tvshows.
SELECT t.title, tvg.name
FROM tv_shows AS `t`
LEFT JOIN tv_show_genres AS `tg`
ON t.id = tg.show_id
	LEFT JOIN tv_genres AS tvg
	ON tg.genre_id = tvg.id
ORDER BY t.title, tvg.name;
