-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 04/11/2024 às 02:05
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `cadastro_colaborador`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `colaborador`
--

CREATE TABLE `colaborador` (
  `codigo` int(11) DEFAULT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `categoria` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `colaborador`
--

INSERT INTO `colaborador` (`codigo`, `nome`, `email`, `telefone`, `categoria`) VALUES
(3, 'Henrique', 'henrique@gmail.com.br', '6700001234', NULL),
(4, 'João Guilherme', 'joaoguisamp@gmail.com.br', '6701012345', NULL),
(5, 'Carlos Eduardo', 'carlosedudu@gmail.com', '6720203487', NULL),
(6, 'Maria Eduarda', 'mariadudu123@gmail.com', '67912783347', NULL),
(6, 'Lorena', 'lore@gmail.com', '6784322210', 'Administrador'),
(7, 'Thiago', 'thgcgx126790@gmail.com', '67911111111', 'Terceirizada'),
(8, 'Beatriz', 'bia22@gmail.com', '67922224444', 'Terceirizada'),
(9, 'Gerson', 'gersindelas123@gmail.com', '4521450018', 'Administrador'),
(10, 'Geovana', 'gegeovana@gmail.com', '1202547325', 'Colaborador');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
