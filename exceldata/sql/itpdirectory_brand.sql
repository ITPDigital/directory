-- MySQL dump 10.13  Distrib 5.1.53, for apple-darwin10.6.0 (i386)
--
-- Host: localhost    Database: directory
-- ------------------------------------------------------
-- Server version	5.1.53

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `itpdirectory_brand`
--

DROP TABLE IF EXISTS `itpdirectory_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itpdirectory_brand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itpdirectory_brand`
--

LOCK TABLES `itpdirectory_brand` WRITE;
/*!40000 ALTER TABLE `itpdirectory_brand` DISABLE KEYS */;
INSERT INTO `itpdirectory_brand` VALUES (4,'Apple'),(3,'Acer'),(5,'Aspire'),(6,'Asus'),(7,'BenQ'),(8,'Blackberry'),(9,'Compaq'),(10,'Dell'),(11,'Fujitsu'),(12,'HCL'),(13,'HP'),(14,'HTC'),(15,'IBM'),(16,'iPhone'),(17,'Lanix'),(18,'Lenovo'),(19,'LG'),(20,'Micro-Star International'),(21,'Motorolla'),(22,'MSI'),(23,'Nexus'),(24,'Nokia'),(25,'Panasonic'),(26,'Samsung'),(27,'Sony'),(28,'Toshiba');
/*!40000 ALTER TABLE `itpdirectory_brand` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-07-13 11:11:50
