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
  `PTA_session` text,
  `Problem_Set` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- 创建表2
CREATE TABLE `Student_Info` (
  `stu_id` text NOT NULL,
  `name` text,
  `school` text,
  `subject` text,
  `rank` int(11) DEFAULT NULL,
  `sloved` int(11) DEFAULT NULL,
  `penalty` int(11) DEFAULT NULL,
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
  `strp11` text,
  `strp12` text,
  `strp13` text,
  `strp14` text,
  `strp15` text,
  `strp16` text,
  `strp17` text,
  `strp18` text,
  `strp21` text,
  `strp22` text,
  `cntp11` text,
  `cntp12` text,
  `cntp13` text,
  `cntp14` text,
  `cntp15` text,
  `cntp16` text,
  `cntp17` text,
  `cntp18` text,
  `cntp21` text,
  `cntp22` text,
  `tmep11` text,
  `tmep12` text,
  `tmep13` text,
  `tmep14` text,
  `tmep15` text,
  `tmep16` text,
  `tmep17` text,
  `tmep18` text,
  `tmep21` text,
  `tmep22` text,
  PRIMARY KEY (`stu_id`(255)) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

INSERT INTO Competition_Info (Title) VALUES (`undefined`);