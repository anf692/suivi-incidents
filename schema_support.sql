-- MySQL dump 10.13  Distrib 8.0.45, for Linux (x86_64)
--
-- Host: localhost    Database: suivi_incident
-- ------------------------------------------------------
-- Server version	8.0.45-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `historiques`
--

DROP TABLE IF EXISTS `historiques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historiques` (
  `id_action` int NOT NULL AUTO_INCREMENT,
  `action` varchar(100) NOT NULL,
  `date_action` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `id_user` int NOT NULL,
  `id_ticket` int NOT NULL,
  PRIMARY KEY (`id_action`),
  KEY `fk_action_user` (`id_user`),
  KEY `fk_action_ticket` (`id_ticket`),
  CONSTRAINT `fk_action_ticket` FOREIGN KEY (`id_ticket`) REFERENCES `tickets` (`id_ticket`),
  CONSTRAINT `fk_action_user` FOREIGN KEY (`id_user`) REFERENCES `utilisateurs` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historiques`
--

LOCK TABLES `historiques` WRITE;
/*!40000 ALTER TABLE `historiques` DISABLE KEYS */;
INSERT INTO `historiques` VALUES (1,'Création du ticket','2026-02-12 16:03:39',1,1),(2,'Création du ticket','2026-02-12 16:06:59',1,2),(3,'Création du ticket','2026-02-12 16:07:54',2,3),(4,'Création du ticket','2026-02-13 10:05:23',1,4);
/*!40000 ALTER TABLE `historiques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statuts`
--

DROP TABLE IF EXISTS `statuts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statuts` (
  `id_statut` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(50) NOT NULL,
  PRIMARY KEY (`id_statut`),
  UNIQUE KEY `libelle` (`libelle`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statuts`
--

LOCK TABLES `statuts` WRITE;
/*!40000 ALTER TABLE `statuts` DISABLE KEYS */;
INSERT INTO `statuts` VALUES (1,'En attente'),(2,'En cours'),(3,'Résolu');
/*!40000 ALTER TABLE `statuts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `id_ticket` int NOT NULL AUTO_INCREMENT,
  `titre` varchar(150) NOT NULL,
  `description` text NOT NULL,
  `urgence` enum('Faible','Moyenne','Haute') NOT NULL,
  `date_creation` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `id_user` int NOT NULL,
  `id_statut` int NOT NULL,
  PRIMARY KEY (`id_ticket`),
  KEY `fk_ticket_user` (`id_user`),
  KEY `fk_ticket_statut` (`id_statut`),
  CONSTRAINT `fk_ticket_statut` FOREIGN KEY (`id_statut`) REFERENCES `statuts` (`id_statut`),
  CONSTRAINT `fk_ticket_user` FOREIGN KEY (`id_user`) REFERENCES `utilisateurs` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES (1,'Chargeur','chargeur de couleur noir','Moyenne','2026-02-12 16:03:39',1,1),(2,'Casque','casque bleu blanc','Faible','2026-02-12 16:06:59',1,1),(3,'ecran','ecran sombre','Haute','2026-02-12 16:07:54',2,1),(4,'123','sadcsfsd','Faible','2026-02-13 10:05:23',1,1);
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateurs` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `role` enum('user','admin') DEFAULT 'user',
  `date_creation` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateurs`
--

LOCK TABLES `utilisateurs` WRITE;
/*!40000 ALTER TABLE `utilisateurs` DISABLE KEYS */;
INSERT INTO `utilisateurs` VALUES (1,'fall','a@gmail.com','$2b$12$pw1zPtkKP0g3lFlK99XW7.CycDbpFp/RNKyt9tRj7bvDhcoXcmq6a','user','2026-02-12 15:44:42'),(2,'mamour','m@gmail.com','$2b$12$yaSJbs7lsah5qd6ideUoBe4AYCBq4iSz3nJtCIwfyFjy4s7aM8h.e','user','2026-02-12 16:07:18'),(3,'admin','admin@gmail.com','$2b$12$yM7.6LYU1qpJ2LF9cXo/rOBQrBS9oe4IMEmWMK9BtAoNwVYg7ubQe','admin','2026-02-12 16:08:19'),(4,'Bineta','b@gmail.com','$2b$12$wMs4/QSiGeoZJLJtViMB1u37QIzcvLbjrX9zaAkqNpm8T7UgDneKa','user','2026-02-13 10:17:57'),(5,'Souleymane','s@gmail.com','$2b$12$NSrW5E/3/AMSRdWMuVhrveOd3IisbSirKQFaswP0/Fj/7Jm7oF1yq','user','2026-02-13 10:35:38');
/*!40000 ALTER TABLE `utilisateurs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-13 10:49:11
