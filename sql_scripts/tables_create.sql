CREATE TABLE IF NOT EXISTS Courses (
    chapter_id VARCHAR NOT NULL DEFAULT 'PC00',
    chapter_text VARCHAR DEFAULT '../chapter/PC00',
	chapter_complexity VARCHAR DEFAULT 'easy' CHECK (chapter_complexity IN ('easy', 'medium', 'hard', 'extra')),
	chapter_award INT DEFAULT 42,
    material_arrangement VARCHAR DEFAULT '../chapter/'
);


CREATE TABLE IF NOT EXISTS InterviewTasks (
    task_id VARCHAR NOT NULL DEFAULT 'PIT00',
    task_text VARCHAR DEFAULT '../interview_tasks/PT00',
    task_complexity VARCHAR DEFAULT 'easy' CHECK (task_complexity IN ('easy', 'medium', 'hard', 'extra')),
	task_award INT DEFAULT 21,
    material_arrangement VARCHAR DEFAULT '../interview_tasks/'
);


CREATE TABLE IF NOT EXISTS Notebooks (
    notebook_id VARCHAR NOT NULL DEFAULT 'PN00',
    notebook_text VARCHAR DEFAULT '../notebooks/PN00',
    notebook_complexity VARCHAR DEFAULT 'easy' CHECK (notebook_complexity IN ('easy', 'medium', 'hard', 'extra')),
    notebook_award INT DEFAULT 21,
    material_arrangement VARCHAR DEFAULT '../notebooks/'
);


CREATE TABLE IF NOT EXISTS Store (
    item_name VARCHAR NOT NULL PRIMARY KEY,
	item_type VARCHAR DEFAULT 'consumable',
    item_description VARCHAR DEFAULT ' ',
    item_price INT DEFAULT 21,
    item_bought_once INT DEFAULT 0
);


CREATE TABLE IF NOT EXISTS Stat (
    total_users INT DEFAULT 0,
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


CREATE TABLE IF NOT EXISTS Users (
    user_name VARCHAR NOT NULL,
    user_chat_id BIGINT NOT NULL PRIMARY KEY,
    user_chapter_id CHAR(4) DEFAULT 'PC00',
    user_task_id CHAR(5) DEFAULT 'PIT00',
    user_notebook_id CHAR(4) DEFAULT 'PN00',
    user_money INT DEFAULT 21,
    user_consumables INT[] DEFAULT ARRAY[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    user_total_tasks INT DEFAULT 0,
    user_maximum_series INT DEFAULT 0,
    user_register_day TIMESTAMP DEFAULT CURRENT_DATE,
    user_level INT DEFAULT 1,
    user_exp INT DEFAULT 0,
    user_status VARCHAR DEFAULT 'novice pythonist',
    user_achievements INT[] DEFAULT ARRAY[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
);


CREATE TABLE IF NOT EXISTS Suggestions (
    user_name VARCHAR NOT NULL,
    suggestion VARCHAR NOT NULL
);