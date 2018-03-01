				SQL More Queries

0. 0-privileges.sql - Lists all privileges of MySQL users user_0d_1 and user_0d_2.

1. 1-create_user.sql - Creates the user user_0d_1 with full privileges and the password user_0d_1_pwd.

2. 2-create_read_user.sql - Creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege and password set to user_0d_2_pwd.

3. 3-force_name.sql - Creates the table force_name with id and name rows.

4. 4-never_empty.sql - Creates the table id_not_null with default id 1 and name row.

5. 5-unique_id.sql - Creates the table unique_id with default value 1. id must be unique.

6. 6-states.sql - Creates the database hbtn_0d_usa and the table states in it. States will have a unique integer id, not null, auto-generated, as a primary key. Name row cannot be null.

7. 7-cities.sql - Creates the databsae hbtn_0d_usa and the table cities in it. City has a unique id, auto-generated, not-null, and as a primary key. Table contains a state_id int, not null, and as a foreign key to the id of the states table.

8. 8-cities_of_california_subquery.sql - Lists all the cities of California that can be found in the database hbtn_0d_usa. The states table contains only one record where name = California. Sorted in ascending order by cities.id.

9. 9-cities_by_state_join.sql - Lists all cities contained in the database hbtn_0d_usa. Displays: cities.id - cities.name - states.name. Sorted in ascending order by cities.id

10. 10-genre_id_by_show.sql - Import the database dump from hbtn_0d_tvshows. Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

11. 11-genre_id_all_shows.sql - Lists all shows contained in the database hbtn_0d_tvshows. Displays: tv_shows.title - tv_show_genres.genre_id. Sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. If a show doesn’t have a genre, displays NULL.

12. 12-no_genre.sql - Lists all shows contained in hbtn_0d_tvshows without a genre linked.
