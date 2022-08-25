-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2020 at 09:44 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel1`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id_customer` varchar(5) NOT NULL,
  `nama_cs` varchar(25) NOT NULL,
  `alamat_cs` text NOT NULL,
  `no_telp_cs` varchar(13) NOT NULL,
  `email` varchar(30) NOT NULL,
  `username_cs` varchar(25) NOT NULL,
  `password_cs` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id_customer`, `nama_cs`, `alamat_cs`, `no_telp_cs`, `email`, `username_cs`, `password_cs`) VALUES
('1', 'rizky', 'bogor', '083186746843', 'riky@gmail.com', 'riky123', '123'),
('31710', 'Dimas', '08123513432', 'Depok', 'enggal@gmail.com', 'dims', '123'),
('96550', 'fahmi', 'jakbar', '081257543', 'fahmi@gmial.com', 'fahmi12', '123');

-- --------------------------------------------------------

--
-- Table structure for table `harga`
--

CREATE TABLE `harga` (
  `id_harga` int(5) NOT NULL,
  `jenis_kamar` enum('Standar Room (STD)','Superior Room (SUP)','Deluxe Room (DLX)','Junior Suit Room (JRSTE)','Suit Room','Presidental Suit') NOT NULL,
  `harga` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `harga`
--

INSERT INTO `harga` (`id_harga`, `jenis_kamar`, `harga`) VALUES
(1, 'Standar Room (STD)', 100000),
(2, 'Superior Room (SUP)', 150000),
(3, 'Deluxe Room (DLX)', 250000),
(4, 'Junior Suit Room (JRSTE)', 350000),
(5, 'Suit Room', 500000),
(6, 'Presidental Suit', 800000);

-- --------------------------------------------------------

--
-- Table structure for table `kamar`
--

CREATE TABLE `kamar` (
  `id_kamar` varchar(5) NOT NULL,
  `kelas_kamar` enum('Standar Room (STD)','Superior Room (SUP)','Deluxe Room (DLX)','Junior Suit Room (JRSTE)','Suit Room','Presidental Suit') NOT NULL,
  `id_harga` int(5) NOT NULL,
  `status` enum('Tersedia','Terisi','Perbaikan') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `kamar`
--

INSERT INTO `kamar` (`id_kamar`, `kelas_kamar`, `id_harga`, `status`) VALUES
('KM1', 'Deluxe Room (DLX)', 3, 'Terisi'),
('KM2', 'Deluxe Room (DLX)', 3, 'Terisi'),
('KM3', 'Deluxe Room (DLX)', 3, 'Tersedia'),
('KM4', 'Presidental Suit', 6, 'Tersedia'),
('KM5', 'Standar Room (STD)', 1, 'Tersedia'),
('KM6', 'Superior Room (SUP)', 2, 'Tersedia'),
('KM7', 'Junior Suit Room (JRSTE)', 4, 'Tersedia'),
('KM8', 'Suit Room', 5, 'Tersedia');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `no_transaksi` int(5) NOT NULL,
  `id_cs` varchar(5) NOT NULL,
  `id_kamar` varchar(5) NOT NULL,
  `id_resepsionis` varchar(5) NOT NULL,
  `tgl_masuk` date NOT NULL,
  `tgl_keluar` date NOT NULL,
  `wilayah` enum('Jakarta Barat','Jakarta Timur','Jakarta Utara','Jakarta Selatan','Jakarta Pusat') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`no_transaksi`, `id_cs`, `id_kamar`, `id_resepsionis`, `tgl_masuk`, `tgl_keluar`, `wilayah`) VALUES
(1, '4354', 'KM2', '14135', '2020-01-01', '2020-01-08', 'Jakarta Barat'),
(2, '20979', 'KM1', '14135', '2020-01-07', '2020-01-10', 'Jakarta Pusat'),
(5, '123', '123', '123', '0000-00-00', '0000-00-00', 'Jakarta Barat');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_user` int(5) NOT NULL,
  `nama` varchar(25) NOT NULL,
  `alamat` text NOT NULL,
  `no_telp` varchar(13) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `role` enum('Admin','Resepsionis') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id_user`, `nama`, `alamat`, `no_telp`, `username`, `password`, `role`) VALUES
(14135, 'riski', 'bogor', '592450234', 'riski', '123', 'Resepsionis'),
(75986, 'dimas', 'sawangan', '087543256753', 'dimas12', '123', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Indexes for table `harga`
--
ALTER TABLE `harga`
  ADD PRIMARY KEY (`id_harga`);

--
-- Indexes for table `kamar`
--
ALTER TABLE `kamar`
  ADD PRIMARY KEY (`id_kamar`),
  ADD KEY `harga` (`id_harga`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`no_transaksi`),
  ADD UNIQUE KEY `id_cs` (`id_cs`,`id_kamar`,`id_resepsionis`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `harga`
--
ALTER TABLE `harga`
  MODIFY `id_harga` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `no_transaksi` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `kamar`
--
ALTER TABLE `kamar`
  ADD CONSTRAINT `kamar_ibfk_1` FOREIGN KEY (`id_harga`) REFERENCES `harga` (`id_harga`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
