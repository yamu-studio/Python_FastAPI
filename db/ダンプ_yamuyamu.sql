# ************************************************************
# Sequel Ace SQL dump
# バージョン 20062
#
# https://sequel-ace.com/
# https://github.com/Sequel-Ace/Sequel-Ace
#
# ホスト: localhost (MySQL 8.3.0)
# データベース: yamuyamu
# 生成時間: 2024-04-26 02:28:39 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE='NO_AUTO_VALUE_ON_ZERO', SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# テーブルのダンプ channel_infos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `channel_infos`;

CREATE TABLE `channel_infos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `thumbnail_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `back_img_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `janru_cd` int DEFAULT NULL,
  `recent_movie_janru_cds` varchar(999) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `channel_id` int DEFAULT NULL,
  `channel_name` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `channel_infos` WRITE;
/*!40000 ALTER TABLE `channel_infos` DISABLE KEYS */;

INSERT INTO `channel_infos` (`id`, `name`, `description`, `thumbnail_path`, `back_img_path`, `janru_cd`, `recent_movie_janru_cds`, `created_at`, `updated_at`, `channel_id`, `channel_name`)
VALUES
	(1,'チャンネル名１','概要ラン','/channelImg.png','/channelImg.png',1,'1,2,3,2,2,1,2','2000-01-01 00:00:00','2000-01-01 00:00:00',1,'aaa');

/*!40000 ALTER TABLE `channel_infos` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ channel_insights
# ------------------------------------------------------------

DROP TABLE IF EXISTS `channel_insights`;

CREATE TABLE `channel_insights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `view_count` int DEFAULT '0',
  `favorite_count` int DEFAULT '0',
  `comment_count` int DEFAULT '0',
  `movie_count` int DEFAULT NULL,
  `subscriber_count` int DEFAULT NULL,
  `created_at` int DEFAULT NULL,
  `updated_at` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `channel_insights` WRITE;
/*!40000 ALTER TABLE `channel_insights` DISABLE KEYS */;

INSERT INTO `channel_insights` (`id`, `view_count`, `favorite_count`, `comment_count`, `movie_count`, `subscriber_count`, `created_at`, `updated_at`)
VALUES
	(1,1,2,3,4,5,NULL,NULL);

/*!40000 ALTER TABLE `channel_insights` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ channel_masters
# ------------------------------------------------------------

DROP TABLE IF EXISTS `channel_masters`;

CREATE TABLE `channel_masters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `channel_info_id` int DEFAULT NULL,
  `channel_insight_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_channel_info_id` (`channel_info_id`),
  KEY `fk_channel_insight_id` (`channel_insight_id`),
  CONSTRAINT `fk_channel_info_id` FOREIGN KEY (`channel_info_id`) REFERENCES `channel_infos` (`id`),
  CONSTRAINT `fk_channel_insight_id` FOREIGN KEY (`channel_insight_id`) REFERENCES `channel_insights` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `channel_masters` WRITE;
/*!40000 ALTER TABLE `channel_masters` DISABLE KEYS */;

INSERT INTO `channel_masters` (`id`, `created_at`, `is_deleted`, `user_id`, `channel_info_id`, `channel_insight_id`)
VALUES
	(1,'2000-01-01 00:00:00',0,1,1,1);

/*!40000 ALTER TABLE `channel_masters` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ comment_infos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `comment_infos`;

CREATE TABLE `comment_infos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comment` varchar(10000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `comment_infos` WRITE;
/*!40000 ALTER TABLE `comment_infos` DISABLE KEYS */;

INSERT INTO `comment_infos` (`id`, `comment`, `created_at`, `updated_at`)
VALUES
	(1,'あいうえおかきくけこあいうえおかきくけこあいうえおかきくけこあいうえおかきくけこあいうえおかきくけこ','2024-01-01 00:00:00','2024-02-01 00:00:00'),
	(3,'あああああおおおおお','2024-04-21 11:55:26','2024-04-21 11:55:26'),
	(4,'こんにちは！','2024-04-21 11:56:19','2024-04-21 11:56:19');

/*!40000 ALTER TABLE `comment_infos` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ comment_insights
# ------------------------------------------------------------

DROP TABLE IF EXISTS `comment_insights`;

CREATE TABLE `comment_insights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `view_count` int DEFAULT NULL,
  `good_count` int DEFAULT NULL,
  `bad_count` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `comment_insights` WRITE;
/*!40000 ALTER TABLE `comment_insights` DISABLE KEYS */;

INSERT INTO `comment_insights` (`id`, `view_count`, `good_count`, `bad_count`, `created_at`, `updated_at`)
VALUES
	(1,1,1,1,'2024-01-01 00:00:00','2024-01-01 00:00:00'),
	(3,0,0,0,'2024-04-21 11:55:26','2024-04-21 11:55:26'),
	(4,0,0,0,'2024-04-21 11:56:19','2024-04-21 11:56:19');

/*!40000 ALTER TABLE `comment_insights` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ comment_masters
# ------------------------------------------------------------

DROP TABLE IF EXISTS `comment_masters`;

CREATE TABLE `comment_masters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT '1',
  `movie_id` int DEFAULT NULL,
  `channel_id` int DEFAULT NULL,
  `reply_comment_id` int DEFAULT NULL,
  `comment_info_id` int DEFAULT NULL,
  `comment_insight_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comment_insight_id` (`comment_insight_id`),
  KEY `fk_comment_info_id` (`comment_info_id`),
  KEY `fk_comment_reply_comment_id` (`reply_comment_id`),
  KEY `fk_comment_channel_id` (`channel_id`),
  CONSTRAINT `fk_comment_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `channel_masters` (`id`),
  CONSTRAINT `fk_comment_info_id` FOREIGN KEY (`comment_info_id`) REFERENCES `comment_infos` (`id`),
  CONSTRAINT `fk_comment_insight_id` FOREIGN KEY (`comment_insight_id`) REFERENCES `comment_insights` (`id`),
  CONSTRAINT `fk_comment_reply_comment_id` FOREIGN KEY (`reply_comment_id`) REFERENCES `comment_masters` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `comment_masters` WRITE;
/*!40000 ALTER TABLE `comment_masters` DISABLE KEYS */;

INSERT INTO `comment_masters` (`id`, `created_at`, `is_deleted`, `movie_id`, `channel_id`, `reply_comment_id`, `comment_info_id`, `comment_insight_id`)
VALUES
	(1,'1990-01-01 00:00:00',1,1,1,NULL,1,1),
	(3,'2024-04-21 11:55:26',2,1,1,NULL,3,3),
	(4,'2024-04-21 11:56:19',1,1,1,NULL,4,4);

/*!40000 ALTER TABLE `comment_masters` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ movie_histories
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie_histories`;

CREATE TABLE `movie_histories` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `view_second` int DEFAULT NULL,
  `is_watched` tinyint(1) DEFAULT '0',
  `ip_address` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `movie_id` int DEFAULT NULL,
  `channel_id` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `latest_viewed_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_history_channel_id` (`channel_id`),
  KEY `fk_history_movie_id` (`movie_id`),
  CONSTRAINT `fk_history_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `channel_masters` (`id`),
  CONSTRAINT `fk_history_movie_id` FOREIGN KEY (`movie_id`) REFERENCES `movie_masters` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `movie_histories` WRITE;
/*!40000 ALTER TABLE `movie_histories` DISABLE KEYS */;

INSERT INTO `movie_histories` (`id`, `view_second`, `is_watched`, `ip_address`, `movie_id`, `channel_id`, `created_at`, `latest_viewed_at`)
VALUES
	(4,5,0,'',1,1,'2024-04-22 12:20:22','2024-04-22 12:23:13'),
	(5,1,1,'',2,1,'2024-04-22 12:24:28','2024-04-22 16:41:43');

/*!40000 ALTER TABLE `movie_histories` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ movie_infos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie_infos`;

CREATE TABLE `movie_infos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `movie_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `thumbnail_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `janru_cd` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `movie_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `movie_infos` WRITE;
/*!40000 ALTER TABLE `movie_infos` DISABLE KEYS */;

INSERT INTO `movie_infos` (`id`, `title`, `description`, `movie_path`, `thumbnail_path`, `janru_cd`, `created_at`, `updated_at`, `movie_id`)
VALUES
	(1,'タイトル１タイトル１タイトル１タイトル１タイトル１タイトル１タイトル１タイトル１','概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章','/movies/movie_1.mp4','/movies/thumbnail_1.png',1,'1990-01-01 00:00:00','2000-01-01 00:00:00',1),
	(2,'タイトル2タイトル2タイトル2タイトル2タイトル2タイトル2タイトル2タイトル2','概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章','/movies/movie_2.mp4','/movies/thumbnail_2.png',2,'2024-01-01 00:00:00','2024-02-02 00:00:00',2),
	(3,'タイトル3タイトル3タイトル3タイトル3タイトル3タイトル3タイトル3タイトル3','概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章','/movies/movie_1.mp4','/movies/thumbnail_3.png',3,'2023-12-10 00:00:00','2023-12-31 00:00:00',3),
	(4,'タイトル4タイトル4タイトル4タイトル4タイトル4タイトル4タイトル4タイトル4','概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章','/movies/movie_2.mp4','/movies/thumbnail_4.png',0,'2023-01-01 00:00:00','2023-01-01 12:00:00',4),
	(5,'タイトル5タイトル5タイトル5タイトル5タイトル5タイトル5タイトル5タイトル5','概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章','/movies/movie_1.mp4','/movies/thumbnail_5.png',0,'2020-01-23 00:00:00','2023-11-01 00:00:00',5),
	(6,'タイトル6タイトル6タイトル6タイトル6タイトル6タイトル6タイトル6タイトル6','概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章概要欄文章','/movies/movie_2.mp4','/movies/thumbnail_6.png',1,'2000-10-10 00:00:00','2001-01-01 12:34:56',6);

/*!40000 ALTER TABLE `movie_infos` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ movie_insights
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie_insights`;

CREATE TABLE `movie_insights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `view_count` int DEFAULT '0',
  `favorite_count` int DEFAULT '0',
  `comment_count` int DEFAULT '0',
  `good_count` int DEFAULT NULL,
  `bad_count` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `movie_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `movie_insights` WRITE;
/*!40000 ALTER TABLE `movie_insights` DISABLE KEYS */;

INSERT INTO `movie_insights` (`id`, `view_count`, `favorite_count`, `comment_count`, `good_count`, `bad_count`, `created_at`, `updated_at`, `movie_id`)
VALUES
	(1,33000,5,8,300,20,'2024-01-01 00:00:00','2024-01-01 00:00:00',NULL),
	(2,11289019,30,1900,30020,20,'2002-01-01 00:00:00','2002-01-01 00:00:00',NULL),
	(3,827365189,30,45609,928760,20,'2002-01-01 00:00:00','2002-01-01 00:00:00',NULL),
	(4,9810,30,3,49,20,'2002-01-01 00:00:00','2002-01-01 00:00:00',NULL),
	(5,33000,30,29,438,20,'2002-01-01 00:00:00','2002-01-01 00:00:00',NULL),
	(6,11289019,30,32,82361,20,'2002-01-01 00:00:00','2002-01-01 00:00:00',NULL);

/*!40000 ALTER TABLE `movie_insights` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ movie_masters
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie_masters`;

CREATE TABLE `movie_masters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `time_longth` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `channel_id` int DEFAULT NULL,
  `movie_info_id` int DEFAULT NULL,
  `movie_insight_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_movie_insight_id` (`movie_insight_id`),
  KEY `fk_movie_info_id` (`movie_info_id`),
  KEY `fk_channel_id` (`channel_id`),
  CONSTRAINT `fk_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `channel_masters` (`id`),
  CONSTRAINT `fk_movie_info_id` FOREIGN KEY (`movie_info_id`) REFERENCES `movie_infos` (`id`),
  CONSTRAINT `fk_movie_insight_id` FOREIGN KEY (`movie_insight_id`) REFERENCES `movie_insights` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `movie_masters` WRITE;
/*!40000 ALTER TABLE `movie_masters` DISABLE KEYS */;

INSERT INTO `movie_masters` (`id`, `movie_id`, `time_longth`, `created_at`, `is_deleted`, `channel_id`, `movie_info_id`, `movie_insight_id`)
VALUES
	(1,'1',180,'2024-04-20 00:00:00',1,1,1,1),
	(2,'aaa',240,'2024-01-01 00:00:00',1,1,2,2),
	(3,'abcde',31,'2024-04-26 09:50:00',1,1,3,3),
	(4,'123abc',3601,'2023-01-01 00:00:00',1,1,4,4),
	(5,'5',33000,'2020-01-23 00:00:00',1,1,5,5),
	(6,'6',440,'2000-10-10 00:00:00',1,1,6,6);

/*!40000 ALTER TABLE `movie_masters` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ subscribe_channels
# ------------------------------------------------------------

DROP TABLE IF EXISTS `subscribe_channels`;

CREATE TABLE `subscribe_channels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int NOT NULL,
  `channel_id` int NOT NULL,
  `created_at` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_subsc_channel_id` (`channel_id`),
  KEY `fk_subsc_movie_id` (`movie_id`),
  CONSTRAINT `fk_subsc_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `channel_masters` (`id`),
  CONSTRAINT `fk_subsc_movie_id` FOREIGN KEY (`movie_id`) REFERENCES `movie_masters` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `subscribe_channels` WRITE;
/*!40000 ALTER TABLE `subscribe_channels` DISABLE KEYS */;

INSERT INTO `subscribe_channels` (`id`, `movie_id`, `channel_id`, `created_at`)
VALUES
	(1,1,1,'2024-01-01 00:00:00');

/*!40000 ALTER TABLE `subscribe_channels` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ user_auths
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_auths`;

CREATE TABLE `user_auths` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `token` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `latest_login_at` timestamp NULL DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `user_auths` WRITE;
/*!40000 ALTER TABLE `user_auths` DISABLE KEYS */;

INSERT INTO `user_auths` (`id`, `email`, `password`, `token`, `created_at`, `latest_login_at`, `user_id`)
VALUES
	(1,'ex@gmail.c','pass1','aaa','1990-01-01 00:00:00','1990-02-01 00:00:00',1);

/*!40000 ALTER TABLE `user_auths` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ user_infos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_infos`;

CREATE TABLE `user_infos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `user_infos` WRITE;
/*!40000 ALTER TABLE `user_infos` DISABLE KEYS */;

INSERT INTO `user_infos` (`id`, `name`, `created_at`, `user_id`)
VALUES
	(1,'お名前','1990-01-01 00:00:00',1);

/*!40000 ALTER TABLE `user_infos` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ user_masters
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_masters`;

CREATE TABLE `user_masters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `user_masters` WRITE;
/*!40000 ALTER TABLE `user_masters` DISABLE KEYS */;

INSERT INTO `user_masters` (`id`, `user_id`, `created_at`, `is_deleted`)
VALUES
	(1,'abc','1990-01-01 00:00:00',0);

/*!40000 ALTER TABLE `user_masters` ENABLE KEYS */;
UNLOCK TABLES;


# テーブルのダンプ youtube_channel_auths
# ------------------------------------------------------------

DROP TABLE IF EXISTS `youtube_channel_auths`;

CREATE TABLE `youtube_channel_auths` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `token` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `latest_login_at` timestamp NULL DEFAULT NULL,
  `channel_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
