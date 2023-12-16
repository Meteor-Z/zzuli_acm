-- 使用 PTA_Data 数据库
USE PTA_Data;

-- 设置数据库配置
SET GLOBAL innodb_large_prefix=on;
SET GLOBAL innodb_file_format=Barracuda;
SET GLOBAL innodb_file_format_max=Barracuda;

-- 创建表1
CREATE TABLE `Competition_Info` (
  `Start_time` text,
  `End_time` text,
  `Title` text,
  `standard1` int(11) DEFAULT NULL,
  `standard2` int(11) DEFAULT NULL,
  `standard3` int(11) DEFAULT NULL,
  `PTA_session` text,
  `Problem_Set` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- 创建表2
CREATE TABLE `Student_Info` (
  `stu_id` text NOT NULL,
  `name` text,
  `class` text,
  `team_id` text,
  `team` text,
  `rank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `p11` int(11) DEFAULT NULL,
  `p12` int(11) DEFAULT NULL,
  `p13` int(11) DEFAULT NULL,
  `p14` int(11) DEFAULT NULL,
  `p15` int(11) DEFAULT NULL,
  `p16` int(11) DEFAULT NULL,
  `p17` int(11) DEFAULT NULL,
  `p18` int(11) DEFAULT NULL,
  `p21` int(11) DEFAULT NULL,
  `p22` int(11) DEFAULT NULL,
  `p23` int(11) DEFAULT NULL,
  `p24` int(11) DEFAULT NULL,
  `p31` int(11) DEFAULT NULL,
  `p32` int(11) DEFAULT NULL,
  `p33` int(11) DEFAULT NULL,
  `part1` int(11) DEFAULT NULL,
  `part2` int(11) DEFAULT NULL,
  `part3` int(11) DEFAULT NULL,
  PRIMARY KEY (`stu_id`(255)) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- 创建表3
CREATE TABLE `Team_Info` (
  `TeamID` text NOT NULL,
  `TeamName` text,
  `Class` text,
  `score` int(11) DEFAULT NULL,
  `part1` int(11) DEFAULT NULL,
  `part2` int(11) DEFAULT NULL,
  `part3` int(11) DEFAULT NULL,
  `sum1` int(11) DEFAULT NULL,
  `sum2` int(11) DEFAULT NULL,
  `sum3` int(11) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`TeamID`(255)) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

INSERT INTO Competition_Info (standard1,standard2,standard3) VALUES (800,400,450);