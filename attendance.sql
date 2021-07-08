-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 01, 2021 at 04:43 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `uid` int(20) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`uid`, `username`, `password`, `fname`, `lname`) VALUES
(1, 'admin', 'admin123', 'Admin', 'Administrator'),
(3, 'dipakc', 'dipakc', 'dipak', 'chavhan'),
(4, 'dipakc1', 'dipakc1', 'dipak1', 'c1'),
(5, 'dipakc2', 'dipakc2', 'dipak2', 'c2'),
(6, 'dipakc3', 'dipakc3', 'dipak3', 'c3'),
(8, 'sample', 'sample123', 'Sample', 'Sample'),
(9, 'dipakc4', 'dipakc4', 'dipak4', 'c4');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `eno` int(11) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `mname` varchar(20) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `dept` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(25) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `mob` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`eno`, `fname`, `mname`, `lname`, `dept`, `position`, `username`, `password`, `gender`, `mob`, `address`, `city`, `email`) VALUES
(1, 'Deepak', 'R', 'Chavhan', 'Computer', 'Developer', 'dipak', 'dipak123', 'male', '1234567890', 'abc city,xyz road', 'nowhere', 'xyz@gmail.com'),
(2, 'Tejas', '', 'Borole', 'Computer', 'DBA', 'tejas', 'tejas123', 'male', '1234567890', 'abc city,xyz road', 'nowhere', 'xyz@gmail.com'),
(3, 'Lubdha', '', 'Bonde', 'Computer', 'Front end Designer', 'lubdha', 'lubdha123', 'female', '1234567890', 'abc city,xyz road', 'nowhere', 'xyz@gmail.com'),
(4, 'Pratiksh', '', 'Bharule', 'Computer', 'Tester', 'pratiksha', 'pratiksha123', 'female', '1234567890', 'abc city,xyz road', 'nowhere', 'xyz@gmail.com'),
(5, 'Aishwrya', '', 'Junagade', 'Computer', 'Front end Designer', 'aishwrya', 'aishwrya', 'female', '1234567890', 'abc city,xyz road', 'nowhere', 'xyz@gmail.com'),
(6, 'mohan', 'r', 'chavhan', 'computer', 'engineer', 'mohan', 'mohanseth', 'male', '1234567890', 'abc city,xyz road', 'nowhere', 'xyz@gmail.com'),
(10, 'krishnakant', 'p', 'adhiya', 'computer', 'Prof', 'kpadhiya	', 'kpadhiya', 'male', '1234567890', 'abc city,xyz road', 'nowhere', 'xyz@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `emp_attendance`
--

CREATE TABLE `emp_attendance` (
  `tid` int(30) NOT NULL,
  `eid` int(30) NOT NULL,
  `ename` varchar(70) NOT NULL,
  `status` varchar(20) NOT NULL,
  `date` varchar(50) NOT NULL,
  `timein` varchar(50) NOT NULL,
  `timeout` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `emp_attendance`
--

INSERT INTO `emp_attendance` (`tid`, `eid`, `ename`, `status`, `date`, `timein`, `timeout`) VALUES
(5, 5, 'Aishwrya', 'absent', '2021-05-25', '19:13:25.701250', '18:20:03.127604'),
(6, 6, 'Mohan', 'absent', '2021-05-25', '19:13:51.892626', '18:20:03.127604'),
(9, 9, 'Krishnakant p', 'present', '2021-05-25', '19:15:36.067908', '18:20:03.127604'),
(16, 1, 'Dipak', 'present', '2021-05-28', '22:16:01.580221', ' 18:20:03.127604'),
(20, 1, 'DeepakRChavhan', 'Present', '2021-05-29', '21:42:05.440560', ' 18:20:03.127604'),
(21, 1, 'DeepakRChavhan', 'Present', '2021-05-30', '18:00:34.509366', ' 18:20:03.127604'),
(23, 4, 'Pratiksha ', 'present', '2021-05-30', '21:57:17.424991', ' 18:20:03.127604'),
(25, 2, 'Tejas', 'present', '2021-05-30', '19:10:18.538179', ' 18:20:03.127604'),
(26, 1, 'DeepakRChavhan', 'Present', '2021-06-01', '22:14:06.666867', ' 18:20:03.127604'),
(27, 6, 'Mohan', 'absent', '2021-06-04', '19:13:51', '18:20:03'),
(28, 2, 'TejasBorole', 'Present', '2021-06-05', '18:39:53.995577', ' 18:20:03.127604'),
(29, 3, 'lubdha', 'present', '2021-06-05', '18:42:11.488255', ' 18:20:03.127604'),
(30, 5, 'AishwryaJunagade', 'Present', '2021-06-09', '16:40:16.918134', ' 18:20:03.127604'),
(31, 1, 'DeepakRChavhan', 'Present', '2021-06-13', '17:23:06.583329', ' 18:20:03.127604'),
(32, 2, 'TejasBorole', 'Present', '2021-06-13', '17:23:45.877746', ' 18:20:03.127604'),
(33, 6, 'mohanrchavhan', 'Present', '2021-06-13', '17:27:11.897722', ' 18:20:03.127604'),
(36, 2, 'TejasBorole', 'Present', '2021-06-30', '13:34:04', '18:20:03'),
(37, 1, 'DeepakRChavhan', 'Present', '2021-06-30', '18:31:37.881583', '18:32:12.409606'),
(38, 3, 'LubdhaBonde', 'Present', '2021-06-30', '18:33:38.611911', '18:33:44.616298'),
(39, 4, 'Pratiksha	', 'present', '2021-05-25', '19:12:59', '18:20:03'),
(40, 3, 'LubdhaBonde', 'Present', '2021-06-13', '17:27:13.327009', '18:20:03.127604'),
(41, 4, 'Pratiksha	', 'present', '2021-06-30', '20:53:13.327009', '20:55:13.327009'),
(42, 6, 'mohanrchavhan', 'Present', '2021-06-30', '20:56:36.185004', '20:57:14.606324'),
(43, 5, 'AishwryaJunagade', 'Present', '2021-06-30', '22:28:45.090622', '22:33:28.740828'),
(44, 1, 'DeepakRChavhan', 'Present', '2021-07-01', '13:27:44.951342', '13:33:44.951342');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`eno`);

--
-- Indexes for table `emp_attendance`
--
ALTER TABLE `emp_attendance`
  ADD PRIMARY KEY (`tid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `uid` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `eno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `emp_attendance`
--
ALTER TABLE `emp_attendance`
  MODIFY `tid` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
