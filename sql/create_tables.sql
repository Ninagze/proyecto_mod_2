USE spotify_db;

CREATE TABLE artists (
    artist_id VARCHAR(250) PRIMARY KEY,
    artist_name VARCHAR(255),
    genres TEXT,
    followers INT,
    popularity INT
);

CREATE TABLE tracks (
    track_id VARCHAR(250) PRIMARY KEY,
    track_name VARCHAR(255),
    artist_id VARCHAR(250),
    release_year INT,
    popularity INT,
    danceability FLOAT,
    energy FLOAT,
    valence FLOAT,
    acousticness FLOAT,
    duration_ms INT,
    tempo FLOAT,
    FOREIGN KEY (artist_id)
    REFERENCES artists(artist_id)
);
