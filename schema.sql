drop table if exists groups;
create table groups (
  id integer primary key autoincrement,
  group_name text not null
);

drop table if exists participants;
create table participants (
  id integer primary key autoincrement,
  name text not null,
  group_id integer not null
)