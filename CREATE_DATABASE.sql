CREATE DATABASE OSS_DB;

\c oss_db

CREATE TABLE EXAM_LEVEL_MST (
  exam_level_id text not null,
  exam_level text not null,
  primary key (exam_level_id)
);
INSERT INTO EXAM_LEVEL_MST VALUES ('silver', 'Silver');
INSERT INTO EXAM_LEVEL_MST VALUES ('gold', 'Gold');

CREATE TABLE QUESTION_GROUP_MST (
  exam_level_id text not null,
  question_group_id text not null,
  question_group text not null,
  primary key (exam_level_id, question_group_id)
);
-- question_group_mst_pkey

CREATE TABLE QUESTIONS (
  exam_level_id text not null,
  question_group_id text not null,
  question_id text not null,
  question text not null,
  commentary text not null,
  answer text not null,
  url text not null,
  primary key (exam_level_id, question_group_id, question_id)
);
-- questions_pkey

CREATE TABLE CHOICES (
  exam_level_id text not null,
  question_group_id text not null,
  question_id text not null,
  choice_num integer not null,
  choice_string text not null,
  primary key (exam_level_id, question_group_id, question_id, choice_num)
);
-- choices_pkey

