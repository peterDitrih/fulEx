CREATE SEQUENCE user_id_seq START 1;

CREATE TABLE "user"
(
    id    bigint DEFAULT nextval('user_id_seq'),
    login character varying(255) NOT NULL,
    name  character varying(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE stats
(
    user_id    bigint NOT NULL,
    repo_id    bigint,
    "date"     date,
    stargazers int    NOT NULL,
    forks      int    NOT NULL,
    watchers   int    NOT NULL,
    PRIMARY KEY (repo_id, "date"),
    FOREIGN KEY (user_id) REFERENCES "user" (id)
);

