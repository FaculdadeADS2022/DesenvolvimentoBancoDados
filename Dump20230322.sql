CREATE DATABASE  IF NOT EXISTS `bar_do_neu` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bar_do_neu`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: bar_do_neu
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `movimentacoes`
--

DROP TABLE IF EXISTS `movimentacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimentacoes` (
  `idmovimentacao` int NOT NULL AUTO_INCREMENT,
  `codTipo` int NOT NULL,
  `data` date NOT NULL,
  `Observacao` varchar(100) DEFAULT NULL,
  `Valor` float NOT NULL,
  PRIMARY KEY (`idmovimentacao`),
  KEY `fk_movimentacao_tipomovimentacao_idx` (`codTipo`),
  CONSTRAINT `fk_movimentacao_tipomovimentacao` FOREIGN KEY (`codTipo`) REFERENCES `tipomovimentacao` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimentacoes`
--

LOCK TABLES `movimentacoes` WRITE;
/*!40000 ALTER TABLE `movimentacoes` DISABLE KEYS */;
INSERT INTO `movimentacoes` VALUES (13,1,'2023-03-03','Sanduíche',300.4),(14,1,'2023-03-02','Sanduíche',300.4),(15,1,'2023-03-03','Sanduíche',300.4);
/*!40000 ALTER TABLE `movimentacoes` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `movimentacoes_AFTER_INSERT` AFTER INSERT ON `movimentacoes` FOR EACH ROW BEGIN
	DECLARE nExiste INTEGER;
   DECLARE cTipo char(1);

   SELECT COUNT(*) INTO nExiste
   FROM SALDODIARIO
   WHERE DATA = new.DATA;

   IF (nExiste = 0) THEN
		INSERT INTO SALDODIARIO (data, valor)
							  VAlUES (new.Data, new.Valor);
	ELSE
		SELECT tipo into cTipo
      FROM tipomovimentacao
      where id = new.codTipo;

      IF cTipo = 'S' THEN
			UPDATE SALDODIARIO SET VALOR = VALOR + new.VALOR WHERE DATA = new.DATA;
		ELSE
			UPDATE SALDODIARIO SET VALOR = VALOR - new.VALOR WHERE DATA = new.DATA;
		END IF;

	END IF;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `movimentacoes_AFTER_UPDATE` AFTER UPDATE ON `movimentacoes` FOR EACH ROW BEGIN

	DECLARE iExiste INTEGER;
	DECLARE sTipolancamento CHAR(1);

	SELECT COUNT(*)
	INTO iExiste 
	FROM saldodiario
	WHERE data = new.data;

	SELECT codtipo
	INTO sTipolancamento 
	FROM tipomovimentacao
	WHERE id = new.codtipo;

	if (iExiste = 0) then

	 	if(sTipolancamento = "E") then

	 		INSERT INTO saldodiario(data, valor) 
			VALUES(new.data, new.valor);

	 	else

	 		INSERT INTO saldodiario(data, valor)
			VALUES(new.data, new.valor * (-1));

		end if;

	else

		if(sTipolancamento = "E") then

			UPDATE saldodiario
			SET valor = valor + new.valor
			WHERE data = new.data;

		else

			UPDATE saldodiario
			SET valor = valor - new.valor
			WHERE data = new.data;

		end if;

	end if;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `movimentacoes_AFTER_DELETE` AFTER DELETE ON `movimentacoes` FOR EACH ROW BEGIN
   DECLARE cTipo char(1);

	SELECT tipo into cTipo
	FROM tipomovimentacao
	where id = old.codTipo;

	IF cTipo = 'S' THEN
		UPDATE SALDODIARIO SET VALOR = VALOR - old.VALOR WHERE DATA = old.DATA;
	ELSE
		UPDATE SALDODIARIO SET VALOR = VALOR + old.VALOR WHERE DATA = old.DATA;
	END IF;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `saldodiario`
--

DROP TABLE IF EXISTS `saldodiario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `saldodiario` (
  `data` date NOT NULL,
  `valor` float NOT NULL,
  PRIMARY KEY (`data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `saldodiario`
--

LOCK TABLES `saldodiario` WRITE;
/*!40000 ALTER TABLE `saldodiario` DISABLE KEYS */;
INSERT INTO `saldodiario` VALUES ('2023-03-01',300.4),('2023-03-02',300.4),('2023-03-03',300.4);
/*!40000 ALTER TABLE `saldodiario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipomovimentacao`
--

DROP TABLE IF EXISTS `tipomovimentacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipomovimentacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(45) NOT NULL,
  `tipo` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipomovimentacao`
--

LOCK TABLES `tipomovimentacao` WRITE;
/*!40000 ALTER TABLE `tipomovimentacao` DISABLE KEYS */;
INSERT INTO `tipomovimentacao` VALUES (1,'Receitas','S'),(2,'Despesas','E'),(4,'teste 3','E'),(5,'teste 2','S');
/*!40000 ALTER TABLE `tipomovimentacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'bar_do_neu'
--

--
-- Dumping routines for database 'bar_do_neu'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-22 20:06:44
