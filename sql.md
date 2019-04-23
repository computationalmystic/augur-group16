`
ALTER TABLE projects DROP FOREIGN KEY fk_projects;<br>
ALTER TABLE projects DROP FOREIGN KEY fk_projects_1;<br>
ALTER TABLE projects DROP FOREIGN KEY fk_projects_2;<br>

DROP TABLE projects;<br>
DROP TABLE project_goals;<br>
DROP TABLE project_topics;<br>
DROP TABLE project_languages; <br>

CREATE TABLE projects (<br>
id int(11) NOT NULL,<br>
url varchar(255) NULL,<br>
owner_id int(11) NULL,<br>
name varchar(255) NULL,<br>
description varchar(255) NULL,<br>
language varchar(255) NULL,<br>
created_at timestamp NULL,<br>
forked_from int(11) NULL,<br>
deleted tinyint(1) NULL,<br>
updated_at timestamp NULL,<br>
PRIMARY KEY (id) <br>
);<br>
CREATE TABLE project_goals (<br>
project_id int(11) NOT NULL,<br>
goals varchar(255) NOT NULL,<br>
created_at timestamp NULL,<br>
PRIMARY KEY (project_id, goals) <br>
);<br>
CREATE TABLE project_topics (<br>
project_id int(11) NOT NULL,<br>
topic_name varchar(255) NOT NULL,<br>
created_at timestamp NULL,<br>
deleted tinyint(1) NULL,<br>
PRIMARY KEY (project_id, topic_name) <br>
);<br>
CREATE TABLE project_languages (<br>
project_id int(11) NULL,<br>
language varchar(255) NULL,<br>
bytes int(11) NULL,<br>
created_at timestamp NULL<br>
);<br>

ALTER TABLE projects ADD CONSTRAINT fk_projects FOREIGN KEY (id) REFERENCES project_languages (project_id) ON DELETE CASCADE ON UPDATE CASCADE;<br>
ALTER TABLE projects ADD CONSTRAINT fk_projects_1 FOREIGN KEY (id) REFERENCES project_topics (project_id) ON DELETE CASCADE ON UPDATE CASCADE;<br>
ALTER TABLE projects ADD CONSTRAINT fk_projects_2 FOREIGN KEY (id) REFERENCES project_goals (goals) ON DELETE CASCADE ON UPDATE CASCADE;<br>`
