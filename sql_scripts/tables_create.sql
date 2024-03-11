CREATE TABLE IF NOT EXISTS Courses (
    chapter_name VARCHAR NOT NULL DEFAULT 'PC00',
    chapter_text VARCHAR DEFAULT '../chapter/PC00',
	chapter_complexity VARCHAR DEFAULT 'easy' CHECK (chapter_complexity IN ('easy', 'medium', 'hard', 'extra')),
	chapter_award INT DEFAULT 42,
    material_arrangement VARCHAR DEFAULT '../chapter/'
);


CREATE TABLE IF NOT EXISTS InterviewTasks (
    task_name VARCHAR NOT NULL DEFAULT 'PIT00',
    task_text VARCHAR DEFAULT '../interview_tasks/PT00',
    task_complexity VARCHAR DEFAULT 'easy' CHECK (task_complexity IN ('easy', 'medium', 'hard', 'extra')),
	task_award INT DEFAULT 21,
    material_arrangement VARCHAR DEFAULT '../interview_tasks/'
);


CREATE TABLE Notebooks (
    notebook_name VARCHAR NOT NULL DEFAULT 'PN00',
    notebook_text VARCHAR DEFAULT '../notebooks/PN00',
    notebook_complexity VARCHAR DEFAULT 'easy' CHECK (notebook_complexity IN ('easy', 'medium', 'hard', 'extra')),
    notebook_award INT DEFAULT 21,
    material_arrangement VARCHAR DEFAULT '../notebooks/'
);


CREATE TABLE IF NOT EXISTS Store (
    name VARCHAR NOT NULL PRIMARY KEY,
	type VARCHAR DEFAULT 'consumable',
    description VARCHAR DEFAULT ' ',
    price INT DEFAULT 21,
    bought_once INT DEFAULT 0
);


CREATE TABLE IF NOT EXISTS Stat (
    total_users INT NOT NULL DEFAULT 0,
    correct_answer_stat FLOAT DEFAULT 0,
    total_solved_common INT DEFAULT 0,
    total_solved_hard INT DEFAULT 0,
    total_chapters_covered INT DEFAULT 0,
    total_notebooks_covered INT DEFAULT 0,
    total_interview_tasks INT DEFAULT 0,
    total_boosters_used INT DEFAULT 0,
    total_achievements_obtained INT DEFAULT 0,
    total_consumables_used INT DEFAULT 0,
    total_chibis_bought INT DEFAULT 0,
    total_donations FLOAT DEFAULT 0
);


CREATE TABLE Users (
    user_chat_id SERIAL PRIMARY KEY,
    step_id CHAR(4) DEFAULT 'PC00',
    money INT DEFAULT 21,
    consumables INT[] DEFAULT ARRAY[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    total_tasks INT DEFAULT 0,
    maximum_series INT DEFAULT 0,
    register_day TIMESTAMP DEFAULT CURRENT_DATE,
    level INT DEFAULT 1,
    status VARCHAR DEFAULT 'novice pythonist',
    achievements INT[] DEFAULT ARRAY[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
);