-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Feb 09, 2023 alle 23:58
-- Versione del server: 10.4.27-MariaDB
-- Versione PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `poc_swe`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `captcha`
--

CREATE TABLE `captcha` (
  `id` varchar(165) NOT NULL,
  `class_target` varchar(50) NOT NULL,
  `solution` varchar(9) NOT NULL,
  `moment` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `captcha_image`
--

CREATE TABLE `captcha_image` (
  `captcha` varchar(165) NOT NULL,
  `image` varchar(15) NOT NULL,
  `position` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `image`
--

CREATE TABLE `image` (
  `id` varchar(15) NOT NULL,
  `class` varchar(50) NOT NULL,
  `reliability` int(11) NOT NULL,
  `path` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `user`
--

CREATE TABLE `user` (
  `username` varchar(50) NOT NULL,
  `pw` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `captcha`
--
ALTER TABLE `captcha`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `captcha_image`
--
ALTER TABLE `captcha_image`
  ADD PRIMARY KEY (`captcha`,`image`),
  ADD KEY `image` (`image`);

--
-- Indici per le tabelle `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `captcha_image`
--
ALTER TABLE `captcha_image`
  ADD CONSTRAINT `captcha_image_ibfk_1` FOREIGN KEY (`captcha`) REFERENCES `captcha` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `captcha_image_ibfk_2` FOREIGN KEY (`image`) REFERENCES `image` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

INSERT INTO `user` (`username`, `pw`) VALUES ('User', 'Password');

INSERT INTO `image` (`id`, `class`, `reliability`, `path`) VALUES 
('dRs6GoGCoXs', 'laptop', '50', '../assets/dRs6GoGCoXs.jpg'), 
('8krX0HkXw8c', 'laptop', '100', '../assets/8krX0HkXw8c.jpg'),
 ('tpuAo8gVs58', 'laptop', '50', '../assets/tpuAo8gVs58.jpg'), 
 ('i5UV2HpITYA', 'laptop', '100', '../assets/i5UV2HpITYA.jpg'), 
 ('DoGVHBMlbSw', 'laptop', '100', '../assets/DoGVHBMlbSw.jpg'),
 ('vjMgqUkS8q8', 'laptop', '100', '../assets/vjMgqUkS8q8.jpg'),
 ('RaYjMmmaSCA', 'laptop', '100', '../assets/RaYjMmmaSCA.jpg'),
 ('ejhjSZKTeeg', 'laptop', '100', '../assets/ejhjSZKTeeg.jpg'),
 ('ocAuPlfZXEc', 'laptop', '100', '../assets/ocAuPlfZXEc.jpg'),
 ('n8Qb1ZAkK88', 'laptop', '100', '../assets/n8Qb1ZAkK88.jpg'),
 ('gvptKmonylk', 'laptop', '50', '../assets/gvptKmonylk.jpg'), 
 ('ITTqjS3UpoY', 'laptop', '50', '../assets/ITTqjS3UpoY.jpg'), 
 ('8FCNO3t7fso', 'laptop', '100', '../assets/8FCNO3t7fso.jpg'),
 ('03wFmOPaTMA', 'laptop', '50', '../assets/03wFmOPaTMA.jpg'), 
 ('0z7dmskP70E', 'laptop', '50', '../assets/0z7dmskP70E.jpg'), 
 ('zPdBxFAidzY', 'laptop', '50', '../assets/zPdBxFAidzY.jpg'), 
 ('zFOm6KzA-7g', 'laptop', '50', '../assets/zFOm6KzA-7g.jpg'), 
 ('wJpl8D38Tq8', 'laptop', '100', '../assets/wJpl8D38Tq8.jpg'),
 ('v_bri4iVuiM', 'laptop', '50', '../assets/v_bri4iVuiM.jpg'), 
 ('5fNmWej4tAA', 'laptop', '50', '../assets/5fNmWej4tAA.jpg'), 
 ('IKzmglo7JLk', 'libri', '100', '../assets/IKzmglo7JLk.jpg'), 
 ('_OZCl4XcpRw', 'libri', '50', '../assets/_OZCl4XcpRw.jpg'), 
 ('_dAnK9GJvdY', 'libri', '50', '../assets/_dAnK9GJvdY.jpg'), 
 ('i6pKVDldgVA', 'libri', '100', '../assets/i6pKVDldgVA.jpg'),
 ('Oaqk7qqNh_c', 'libri', '50', '../assets/Oaqk7qqNh_c.jpg'), 
 ('KSaLhgex8F0', 'libri', '50', '../assets/KSaLhgex8F0.jpg'), 
 ('UtRyYXcbK6A', 'libri', '100', '../assets/UtRyYXcbK6A.jpg'), 
 ('nGrfKmtwv24', 'libri', '50', '../assets/nGrfKmtwv24.jpg'), 
 ('zvKx6ixUhWQ', 'libri', '50', '../assets/zvKx6ixUhWQ.jpg'), 
 ('pFnvc1Cu6zI', 'libri', '100', '../assets/pFnvc1Cu6zI.jpg'),
 ('Pxbiv0GpV8g', 'libri', '100', '../assets/Pxbiv0GpV8g.jpg'),
 ('qmlGWIaIgpo', 'libri', '50', '../assets/qmlGWIaIgpo.jpg'), 
 ('tVugl_rtvHA', 'libri', '50', '../assets/tVugl_rtvHA.jpg'), 
 ('rSgE6NtntZo', 'libri', '100', '../assets/rSgE6NtntZo.jpg'),
 ('SNHsMunOPME', 'libri', '50', '../assets/SNHsMunOPME.jpg'), 
 ('GoFeJMsxAVM', 'libri', '50', '../assets/GoFeJMsxAVM.jpg'), 
 ('g827ZOCwt30', 'libri', '100', '../assets/g827ZOCwt30.jpg'),
 ('55btQzyDiO8', 'libri', '100', '../assets/55btQzyDiO8.jpg'),
 ('H1IRUS1vEFA', 'libri', '100', '../assets/H1IRUS1vEFA.jpg'),
 ('8ePZbdxnpi0', 'libri', '100', '../assets/8ePZbdxnpi0.jpg'),
 ('1lfRx3GSeQI', 'macchine', '100', '../assets/1lfRx3GSeQI.jpg'), 
 ('qm1C36SOynk', 'macchine', '100', '../assets/qm1C36SOynk.jpg'), 
 ('_4sWbzH5fp8', 'macchine', '50', '../assets/_4sWbzH5fp8.jpg'), 
 ('QD-8l-8_uJg', 'macchine', '50', '../assets/QD-8l-8_uJg.jpg'), 
 ('R_tEh-jjGcI', 'macchine', '100', '../assets/R_tEh-jjGcI.jpg'),
 ('thtUUYPdxWY', 'macchine', '100', '../assets/thtUUYPdxWY.jpg'), 
 ('U06nswCc4l4', 'macchine', '50', '../assets/U06nswCc4l4.jpg'), 
 ('u6BPMXgURuI', 'macchine', '50', '../assets/u6BPMXgURuI.jpg'), 
 ('-_bALOvNBe0', 'macchine', '100', '../assets/-_bALOvNBe0.jpg'),
 ('10tOJa4APL8', 'macchine', '100', '../assets/10tOJa4APL8.jpg'), 
 ('05Q_XPF_YKs', 'macchine', '50', '../assets/05Q_XPF_YKs.jpg'), 
 ('fZmhlIEWVdA', 'macchine', '50', '../assets/fZmhlIEWVdA.jpg'), 
 ('G15HRVNAkMQ', 'macchine', '100', '../assets/G15HRVNAkMQ.jpg'),
 ('heFTscwGDCA', 'macchine', '50', '../assets/heFTscwGDCA.jpg'),
 ('iflRMZelx0M', 'macchine', '50', '../assets/iflRMZelx0M.jpg'), 
 ('h5XcT5T0ST8', 'macchine', '100', '../assets/h5XcT5T0ST8.jpg'),
 ('gts_Eh4g1lk', 'macchine', '50', '../assets/gts_Eh4g1lk.jpg'), 
 ('LlqJyjr5U_o', 'macchine', '50', '../assets/LlqJyjr5U_o.jpg'), 
 ('m3m-lnR90uM', 'macchine', '100', '../assets/m3m-lnR90uM.jpg'),
 ('j0YPbvXu4t0', 'macchine', '100', '../assets/j0YPbvXu4t0.jpg'),
 ('RcEWuCd3dK4', 'ombrelli', '50', '../assets/RcEWuCd3dK4.jpg'), 
 ('MVYsbIAgV68', 'ombrelli', '100', '../assets/MVYsbIAgV68.jpg'),
 ('1Qmej0ahHo4', 'ombrelli', '100', '../assets/1Qmej0ahHo4.jpg'),
 ('XgNJasHTQH0', 'ombrelli', '50', '../assets/XgNJasHTQH0.jpg'), 
 ('-79iS8xF6ro', 'ombrelli', '50', '../assets/-79iS8xF6ro.jpg'), 
 ('iKjU9yHTEg0', 'ombrelli', '100', '../assets/iKjU9yHTEg0.jpg'),
 ('e8e4YY65sOk', 'ombrelli', '50', '../assets/e8e4YY65sOk.jpg'), 
 ('00yDgACVeMA', 'ombrelli', '50', '../assets/00yDgACVeMA.jpg'), 
 ('VxC0DMdCh4E', 'ombrelli', '50', '../assets/VxC0DMdCh4E.jpg'), 
 ('Dx-b6Hl4DXM', 'ombrelli', '100', '../assets/Dx-b6Hl4DXM.jpg'),
 ('GpMStAydX-s', 'ombrelli', '50', '../assets/GpMStAydX-s.jpg'), 
 ('dP5ZnIE4A40', 'ombrelli', '100', '../assets/dP5ZnIE4A40.jpg'),
 ('ltAlHd4dBqY', 'ombrelli', '100', '../assets/ltAlHd4dBqY.jpg'),
 ('D5cxQ5ZvxkY', 'ombrelli', '100', '../assets/D5cxQ5ZvxkY.jpg'),
 ('szaFlE_NeH8', 'ombrelli', '100', '../assets/szaFlE_NeH8.jpg'), 
 ('lRAcIwJ6TXM', 'ombrelli', '50', '../assets/lRAcIwJ6TXM.jpg'), 
 ('CNuhMkVBtSA', 'ombrelli', '50', '../assets/CNuhMkVBtSA.jpg'),
 ('bljj8PxJF74', 'ombrelli', '100', '../assets/bljj8PxJF74.jpg'),
 ('lCZlwYjf3CI', 'ombrelli', '50', '../assets/lCZlwYjf3CI.jpg'), 
 ('6F38-0YjsE0', 'ombrelli', '100', '../assets/6F38-0YjsE0.jpg');

