-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 15, 2018 at 09:58 PM
-- Server version: 10.1.33-MariaDB
-- PHP Version: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tinder3`
--
CREATE DATABASE IF NOT EXISTS `tinder3` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `tinder3`;

-- --------------------------------------------------------

--
-- Table structure for table `proposals`
--

CREATE TABLE `proposals` (
  `proposal_id` int(11) NOT NULL,
  `romeo_id` int(11) NOT NULL,
  `juliet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `proposals`
--

INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES
(1, 3, 7),
(2, 7, 3),
(3, 1, 5),
(8, 5, 1),
(9, 3, 4),
(10, 4, 3),
(11, 9, 8),
(12, 12, 6),
(13, 13, 4),
(14, 4, 13),
(15, 12, 4),
(16, 4, 12);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `city` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `gender`, `age`, `city`) VALUES
(1, 'Eshani Ghosh', 'eshani34@gmail.com', 'esha', 'Female', 23, 'Kolkata'),
(2, 'Rahul', 'rahul@gmail.com', '12po5', 'Male', 30, 'Kolkata'),
(3, 'Ritu ', 'ritu@gmail.com', '3456', 'Female', 23, 'Delhi'),
(4, 'salman khan', 'salman@gmail.com', '6789', 'Male', 50, 'Mumbai'),
(5, 'Sayantan ', 'sayantan@gmail.com', 'bubu', 'Male', 21, 'Farakka'),
(6, 'Sukanya', 'sukanya@gmail.com', '1234', 'Female', 20, 'Kolkata'),
(7, 'Diptodip ', 'dipto@gmail.com', '2345', 'Male', 21, 'Darjeeling'),
(8, 'Tiya', 'tiya@gmail.com', '1234', 'Female', 20, 'kolkata'),
(9, 'Raj', 'raj@gmail.com', '8976', 'Male', 25, 'Goa'),
(10, 'simran', 'simran@gmail.com', '6789', 'Female', 24, 'Delhi'),
(11, 'Tina', 'tina@gmail.com', '5678', 'Female', 32, 'Goa'),
(12, 'kalpana', 'kalpana@gmail.com', '123', 'Female', 45, 'Bakura');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `proposals`
--
ALTER TABLE `proposals`
  ADD PRIMARY KEY (`proposal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `proposals`
--
ALTER TABLE `proposals`
  MODIFY `proposal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
