CREATE TABLE IF NOT EXISTS Courses (
    chapter_id VARCHAR NOT NULL DEFAULT 'PC',
    chapter_text VARCHAR DEFAULT ' ',
	chapter_complexity VARCHAR DEFAULT 'easy' CHECK (chapter_complexity IN ('easy', 'medium', 'hard', 'extra')),
	chapter_award INT DEFAULT 42,
    material_arrangement VARCHAR DEFAULT '../chapter/'
);


CREATE TABLE IF NOT EXISTS InterviewTasks (
    task_id VARCHAR NOT NULL DEFAULT 'PIT',
    task_text VARCHAR DEFAULT ' ',
    task_answer_1 VARCHAR DEFAULT " ",
    task_answer_2 VARCHAR DEFAULT " ",
    task_answer_3 VARCHAR DEFAULT " ",
    task_complexity VARCHAR DEFAULT 'easy' CHECK (task_complexity IN ('easy', 'medium', 'hard', 'extra')),
	task_money_award INT DEFAULT 21,
	task_exp_award INT DEFAULT 21
);


CREATE TABLE IF NOT EXISTS Notebooks (
    notebook_id VARCHAR NOT NULL DEFAULT 'PN',
    notebook_text VARCHAR DEFAULT ' ',
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
    user_avatar VARCHAR NOT NULL UNIQUE,
    user_name VARCHAR NOT NULL,
    user_chat_id BIGINT NOT NULL PRIMARY KEY,
    user_chapter_id CHAR(5) DEFAULT 'PC000',
    user_interview_tasks JSONB DEFAULT '{"PIT1": 0, "PIT2": 0, "PIT3": 0, "PIT4": 0, "PIT5": 0, "PIT6": 0, "PIT7": 0, "PIT8": 0, "PIT9": 0, "PIT10": 0, "PIT11": 0, "PIT12": 0, "PIT13": 0, "PIT14": 0, "PIT15": 0, "PIT16": 0, "PIT17": 0, "PIT18": 0, "PIT19": 0, "PIT20": 0}',
    user_notebook_id CHAR(5) DEFAULT 'PN000',
    user_money INT DEFAULT 21,
    user_consumables INT[] DEFAULT ARRAY[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    user_total_tasks INT DEFAULT 0,
    user_maximum_series INT DEFAULT 0,
    user_register_day TIMESTAMP DEFAULT CURRENT_DATE,
    user_level INT DEFAULT 1,
    user_exp INT DEFAULT 0,
    user_status VARCHAR DEFAULT 'novice pythonist',
    user_achievements INT[] DEFAULT ARRAY[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    user_money_rate REAL DEFAULT 1.0,
    user_exp_rate REAL DEFAULT 1.0
);


CREATE TABLE IF NOT EXISTS Suggestions (
    user_name VARCHAR NOT NULL,
    suggestion VARCHAR NOT NULL
);